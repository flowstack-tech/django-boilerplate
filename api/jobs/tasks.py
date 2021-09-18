from celery import Task
from config import celery_app

from ..common.exceptions import OtpNotSentException
from ..common.sms_client import TwilioClient


class BaseTask(Task):
    abstract = True

    autoretry_for = (Exception,)
    retry_backoff = True
    retry_kwargs = {'max_retries': 3}
    retry_backoff_max = 30
    retry_jitter = False


@celery_app.task(name='send_login_otp', queue='sms', base=BaseTask)
def send_otp(phone, otp):
    """Send the generated otp to a particular phone.

    Args:
        phone: string
        otp: string

    Raises:
        OtpNotSentException
    """
    sms_text = f'<#> Your Studyroom OTP is: {otp}'
    sms_client = TwilioClient()
    _, status = sms_client.send_sms(phone, sms_text)
    if status != 'accepted':
        raise OtpNotSentException
