# This file is used to test the email sending functionality.

import unittest
from Occupancy_Tracker.email_sender import EmailSender


class TestSendEmail(unittest.TestCase):
    """
    This class unit tests send Email class.
    """
    def test_send_email(self):
        self.assertEqual(EmailSender.email_send(), True)


if __name__ == '__main__':
    unittest.main()
