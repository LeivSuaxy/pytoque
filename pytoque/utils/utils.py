def get_url(date) -> str:
    return f"https://tasas.eltoque.com/v1/trmi?date_from={date}%2000%3A00%3A01&date_to={date}%2023%3A59%3A01"

def filter_data(data: dict, filters: list) -> dict:
    if not data or not filters:
        raise Exception('Please provide data and filters')

    return_data: dict = {}

    for _ in filters:
        return_data[_] = data.get(_)

    return return_data