import datetime

def validate_date(date_str: str) -> bool:
    """
    Validate if the given string is a valid date in the format YYYY-MM-DD.

    :param date_str: Date string to validate.
    :return: True if the date string is valid, False otherwise.
    """

    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_filters(filters: list) -> bool:
    """
    Validate if the given list of filters contains only correct filter values.

    :param filters: List of filters to validate.
    :return: True if all filters are correct, False otherwise.
    """

    correct_filters = ['ECU', 'TRX', 'USDT_TRC20', 'BTC', 'BNB', 'USD', 'MLC']

    for _ in filters:
        if _ not in correct_filters:
            return False

    return True

