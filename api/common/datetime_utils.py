from datetime import datetime

import pytz


def get_utc_now():
    """Get current datetime in UTC.

    Returns:
        Datetime
    """
    return datetime.utcnow().replace(tzinfo=pytz.UTC)
