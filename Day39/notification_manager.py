# I refuse to give out my mobile number...

from data_manager import DataManager

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_text_message(mobile_number, text_message):
        print(text_message)

    def send_email(message_text):
        user_emails_list = DataManager.get_user_emails()

        for email_address in user_emails_list:
            print('sending email {} to {}'.format(message_text, email_address))

