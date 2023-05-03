# TryExcept Decorator
The TryExcept Decorator is a configurable Python decorator that wraps a function around a try-except statement.
It allows you to write cleaner code in your functions where an exception may happen and you want to handle it even in complex ways.

## Installation
```cmd
pip install tryexcept-decorator
```

# Usage
To use the tryexcept decorator, simply apply it to any function that may raise an exception.

```python
import json

import requests
from requests import HTTPError

from tryexcept_decorator import tryexcept


def my_custom_exception_handling_function(f_exc:Exception, f_locals:dict, f_name:str, message:str):
    print(f"Custom exception handler error message: {message}")
    print(f"Custom exception handler was called by the '{f_name}' function.")
    print(f"Available local variables in the callee namespace at the moment of exception: \n {json.dumps(obj=f_locals, indent=1, default=str)}")
    print(f"The exception raised was of type {type(f_exc)}")
    return {"exc":f_exc, **f_locals, "message":message}

mytryexc = tryexcept(
    exception_type=HTTPError,
    except_handler=my_custom_exception_handling_function,
    except_handler_kwargs={"message": "There was an error!"})

@mytryexc
def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    result = get_data(url = "http://example.com/nonexistentpage.html")
    print(result)

```

Output:
```cmd
Available local variables in the callee namespace at the moment of exception: 
 {
 "url": "http://example.com/nonexistentpage.html",
 "response": "<Response [404]>"
}
The exception raised was of type <class 'requests.exceptions.HTTPError'>
Custom exception handler error message: An error occurred! See exception below.
{'exc': HTTPError('404 Client Error: Not Found for url: http://example.com/nonexistentpage.html'), 'url': 'http://example.com/nonexistentpage.html', 'response': <Response [404]>, 'message': 'An error occurred! See exception below.'}
```

In this example, the get_data() function uses the requests library to fetch data from a hypothetical API. The handle_exceptions decorator is applied to the get_data() function to handle any exceptions that might occur during the API request.

If an exception is raised, the decorator catches it and returns an error message to the user in a dictionary format. If no exception is raised, the decorator simply returns the response data in JSON format. This allows the application to gracefully handle any exceptions that might occur during the API request, without crashing or disrupting the user experience.

## Contributing
Contributions are welcome! Please create a pull request with your changes.