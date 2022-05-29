# I refuse to give out my mobile number...

from cgitb import text


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_text_message(mobile_number, text_message):
        print(text_message)