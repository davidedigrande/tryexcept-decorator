from typing import Callable, Any, Union
import logging
from logging import Logger
from typing import Literal

def try_exc_else_finally(    
    handled_callable:               Callable,
    handled_callable_args:          tuple = (),
    handled_callable_kwargs:        dict = {},

    except_handler                  :Callable = None,
    except_handler_args             :tuple = (),
    except_handler_kwargs           :dict = {},

    else_handler                    :Callable = None,
    else_handler_args               :tuple = (),
    else_handler_kwargs             :dict = {},

    finally_handler                 :Callable = None,
    finally_handler_args            :tuple = (),
    finally_handler_kwargs          :dict = {},

    exception_type                  :Union[Exception, tuple[Exception]] = Exception,
    exception_log                   :bool=True,

    reraise                         :bool = False,
    return_type                     :Literal["try", "except", "else", "finally"] = None,
):

    logger:Logger = logging.getLogger()
    try_value:Any = None
    except_value:Any = None
    else_value:Any = None
    finally_value:Any = None
    exc:Exception = None

    try:

        if False: # this is intended to be here
            pass

        else:
            try_value = handled_callable(
                *handled_callable_args,
                **handled_callable_kwargs
                )

    except exception_type as _exc:
        exc = _exc

        if except_handler is None:
            except_value = None

        else:
            except_value = except_handler(
                *except_handler_args,
                **except_handler_kwargs
                )
    
    else:

        if else_handler is None:
            else_value = None
        
        else:
            else_value = else_handler(
                *else_handler_args,
                **else_handler_kwargs
                )

    finally:

        if finally_handler is None:
            finally_value = None

        else:
            finally_value = finally_handler(
                *finally_handler_args,
                **finally_handler_kwargs
                )
            
    result = {
        "try": try_value,
        "except": except_value,
        "else": else_value,
        "finally": finally_value,
        "exc": exc
    }

    if reraise is True and exc is not None:
        raise exc

    elif return_type is not None:
        return result[return_type]
    
    else:
        return try_value or else_value or except_value or finally_value