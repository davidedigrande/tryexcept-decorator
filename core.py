import inspect
import logging
from logging import Logger
from typing import Any, Callable, Union


def tryexcept(    
    handled_callable:               Callable,
    handled_callable_args:          tuple = (),
    handled_callable_kwargs:        dict = {},

    except_handler                  :Callable = lambda: None,
    except_handler_args             :tuple = (),
    except_handler_kwargs           :dict = {},

    exception_type                  :Union[Exception, tuple[Exception]] = Exception,
    exception_log                   :bool=True
):

    logger:Logger = logging.getLogger()
    try_value:Any = None
    except_value:Any = None
    exc:Exception = None

    try:

        try_value = handled_callable(
            *handled_callable_args,
            **handled_callable_kwargs
            )

        return try_value

    except exception_type as exc:

        if inspect.signature(except_handler).parameters.get("f_exc").__getattribute__("_annotation") is Exception:
            except_handler_kwargs["f_exc"] = exc

        if inspect.signature(except_handler).parameters.get("f_locals").__getattribute__("_annotation") is dict:
            except_handler_kwargs["f_locals"] = inspect.trace()[-2][0].f_locals

        if inspect.signature(except_handler).parameters.get("f_name").__getattribute__("_annotation") is str:
            except_handler_kwargs["f_name"] = handled_callable.__name__
            
        except_value = except_handler(
            *except_handler_args,
            **except_handler_kwargs
            )

        return except_value