from tryexcept_decorator import tryexcept
import requests
from requests import HTTPError
import json

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

if __name__ == "__main__":
    main()