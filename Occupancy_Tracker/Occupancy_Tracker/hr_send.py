import os
from datetime import datetime
from pathlib import Path

from constants import START_TIME_HR, END_TIME_HR, HOURLY_CSV
from send_receive_messages import SendReceiveMessages


class Hour_email_send:
    def __init__(self):
        self.start_time = START_TIME_HR
        self.end_time = END_TIME_HR
        self.csv_file = None
        self.todays_date = datetime.now()

    def initialize_log_file(self):
        if not self.csv_file:
            self.csv_file = open(os.path.join(Path(__file__).parent, HOURLY_CSV), mode="a")
        # set the file pointer to end of the file
        if self.csv_file.seek(0, os.SEEK_END) == 0:
            self.csv_file.write("Hour,Total Count\n")

    def close_log_file(self):
        # check if the log file object exists, if it does, then close it
        if not self.csv_file:
            self.csv_file.close()

    def log_total_num(self):
        if (self.start_time <= self.todays_date.hour <= self.end_time):
            if not self.csv_file:
                self.initialize_log_file()
            Num_of_people = SendReceiveMessages().get_total_face_detected_count()
            info = "{}, {}\n".format(self.todays_date.hour, Num_of_people)
            self.csv_file.write(info)
            self.csv_file.flush()
            self.close_log_file()


if __name__ == "__main__":
    Hour_email_send().log_total_num()
