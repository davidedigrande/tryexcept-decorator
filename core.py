from typing import Callable, Any, Union
import logging
from logging import Logger

def try_exc_else_finally(
    handled_callable:               Callable,
    handled_callable_args:          tuple = (),
    handled_callable_kwargs:        dict = {},

    except_handler                  :Callable = lambda: None,
    except_handler_args             :tuple = (),
    except_handler_kwargs           :dict = {},
    except_handled_value            :Any = None,

    else_handler                    :Callable = lambda: None,
    else_handler_args               :tuple = (),
    else_handler_kwargs             :dict = {},

    finally_handler                 :Callable = lambda: None,
    finally_handler_args            :tuple = (),
    finally_handler_kwargs          :dict = {},

    exception_type                  :Union[Exception, tuple[Exception]] = Exception,
    exception_log                   :bool=True,    
):

    logger:Logger = logging.getLogger()

    try:
        try_value = handled_callable(*handled_callable_args, **handled_callable_kwargs)

    except exception_type as exc:
        if exception_log:
            logger.exception("Exception handled by try_exc decorator.")

        if except_handled_value is not None:
            return except_handled_value

        return except_handler(
            *except_handler_args,
            **except_handler_kwargs
            )
    
    else:
        if else_value is not None:
            return else_value
        
        else:
            else_value = else_handler(*else_handler_args, **else_handler_kwargs)
        
        return try_value if else_value is not None else else_value

    finally:
        finally_handler(*finally_handler_args, **finally_handler_kwargs)