import datetime

def validate_date(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_filters(filters: list) -> bool:
    correct_filters = ['ECU', 'TRX', 'USDT_TRC20', 'BTC', 'BNB', 'USD', 'MLC']

    for _ in filters:
        if _ not in correct_filters:
            return False

    return True

