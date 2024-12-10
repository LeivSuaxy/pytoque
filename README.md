# PyToque Class

Class with methods to make requests to the ElToque API (Cuba).

## How to use
Primero necesitaras solicitar un token personal desde el sitio de ElToque. 

### Explanation
https://eltoque.com/eltoque-abre-acceso-a-su-api-de-las-tasas-de-cambio

### Form to obtain token
https://tasas-token.eltoque.com/

Open your virtual environment and install dependencies

_Create Virtual Environment_
```python
python -m venv .venv   
```
If you use Linux remember to use python3

<br/>

_Activate Virtual Environment_
### Linux
```bash
source .venv/bin/activate
```

### Windows
```bash
.venv\Scripts\activate
```

_Install Dependencies_
```python
pip install -r requirements.txt
```

_Import the PyToque class and initialize it by sending the api_key obtained on the official ElToque site as a parameter._

**Warning** Remember to be careful with the privacy of your personal token.

```python
from pytoque.pytoque.core import PyToque

toque = PyToque(api_key=API_KEY)
```

## Docs

### get_today() -> dict
Returns the exchange rates for the current date.

#### Additional Params

- filters: List of strings with exchange rate abbreviations

Available filters: ['ECU', 'TRX', 'USDT_TRC20', 'BTC', 'BNB', 'USD', 'MLC']

#### Exceptions
- Exception('Incorrect Filters') If filters are not available
- Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}') In case the API returns another
status code, check the eltoque api documentation to see more.
- RequestException() In case a failure occurs in the request


### get_date(date: str) -> dict
Date parameter in format (YYYY-MM-DD)

Returns the exchange rates of the given date.

#### Additional Params

- filters: List of strings with exchange rate abbreviations

Available filters: ['ECU', 'TRX', 'USDT_TRC20', 'BTC', 'BNB', 'USD', 'MLC']

#### Exceptions
- Exception('Incorrect Filters') If filters are not available
- Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}') In case the API returns another
status code, check the eltoque api documentation to see more.
- RequestException() In case a failure occurs in the request
- Exception('Please provide a date in format "YYYY-MM-DD"') In case a bad date format is sent


