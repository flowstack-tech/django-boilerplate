from config.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_MS_SID
from twilio.rest import Client


class TwilioClient(object):
    """Client that sends messages using Twilio."""

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        self.messaging_service_sid = TWILIO_MS_SID

    def send_sms(self, destination, text):
        """Encode the message and send.

        Args:
            destination: phone no of user, string
            text: sms text, string

        Returns:
             Message Data, Message Status
        """
        try:
            destination = destination.encode('utf-8')
            text = text.decode('utf-8').encode('utf-8')
        except: # noqa
            text = text.encode('utf-8')

        message = self.client.messages.create(body=text,
                                              to=destination,
                                              messaging_service_sid=self.messaging_service_sid)

        status = message.status

        return message.sid, status
