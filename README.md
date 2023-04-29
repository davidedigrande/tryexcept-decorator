# TryExcept decorator

The TryExcept Decorator is a configurable Python decorator that wraps a function around a try-except statement.
It allows you to write cleaner code in your functions where an exception may happen and you want to handle it even in complex ways.

Installation
To install the handle_exceptions decorator, simply run the following command:

```pip install tryexcept-decorator```

# Usage

To use the tryexcept decorator, simply apply it to any function that may raise an exception.

Here's an example:

https://github.com/davidedigrande/tryexcept-decorator/blob/b36b2ff221119411df1472eaa31f7c75a9fc5446/main.py#L1-L30

Output:
```
Available local variables in the callee namespace at the moment of exception: 
 {
 "url": "http://example.com/nonexistentpage.html",
 "response": "<Response [404]>"
}
The exception raised was of type <class 'requests.exceptions.HTTPError'>
Custom exception handler error message: An error occurred! See exception below.
{'exc': HTTPError('404 Client Error: Not Found for url: http://example.com/nonexistentpage.html'), 'url': 'http://example.com/nonexistentpage.html', 'response': <Response [404]>, 'message': 'An error occurred! See exception below.'}

```

Or you can override default properties on the fly by passing parameters directly to the decorator:

```
@tryexcept(
        except_handler=my_custom_exception_handling_function,
        except_handler_kwargs=my_custom_exception_handling_function_arguments,
        exception_type=(ProxyError, SSLError),
)
def get_data(url):
    # Fetch data from the API
    response = requests.get(url)
    # Raise an exception if the response is not successful
    response.raise_for_status()
    # Return the response data
    return response.json()
```

Note: this will not modify the decorator instance, just this specific execution.

Then you can use it as normal:

```
result = get_data()

print(result)

```


In this example, the get_data() function uses the requests library to fetch data from a hypothetical API. The handle_exceptions decorator is applied to the get_data() function to handle any exceptions that might occur during the API request.

If an exception is raised, the decorator catches it and returns an error message to the user in a dictionary format. If no exception is raised, the decorator simply returns the response data in JSON format. This allows the application to gracefully handle any exceptions that might occur during the API request, without crashing or disrupting the user experience.

Contributing
If you'd like to contribute to the handle_exceptions decorator, feel free to submit a pull request on the GitHub repository.

PyPI
You can find the handle_exceptions decorator on PyPI: https://pypi.org/project/tryexcept_decorator/
