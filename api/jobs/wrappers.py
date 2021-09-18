from .config import BASE_RETRY_POLICY
from .tasks import send_otp


def create_send_otp_task(phone, otp):
    """Wraps the send_otp task.

    Args:
        phone: string
        otp: string
    """
    send_otp.apply_async((phone, otp), retry=True, retry_policy=BASE_RETRY_POLICY)
