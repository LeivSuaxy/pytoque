def get_url(date) -> str:
    """
    Generate the URL for the API request based on the given date.

    :param date: Date in format "YYYY-MM-DD".
    :return: URL string for the API request.
    """

    return f"https://tasas.eltoque.com/v1/trmi?date_from={date}%2000%3A00%3A01&date_to={date}%2023%3A59%3A01"

def filter_data(data: dict, filters: list) -> dict:
    """
    Filter the data based on the provided filters.

    :param data: Dictionary containing the data to be filtered.
    :param filters: List of filters to apply to the data.
    :return: Dictionary containing the filtered data.
    :raises Exception: If data or filters are not provided.
    """

    if not data or not filters:
        raise Exception('Please provide data and filters')

    return_data: dict = {}

    for _ in filters:
        return_data[_] = data.get(_)

    return return_data