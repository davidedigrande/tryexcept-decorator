from __future__ import annotations

from functools import partial
from typing import Callable, Union

from core import try_exc_else_finally


class TryExcept:
    def __init__(
        self,
        except_handler              :Callable = lambda: None,
        except_handler_args         :tuple = (),
        except_handler_kwargs       :dict = {},
        exception_type              :Union[Exception, tuple[Exception]] = Exception,
        exception_log               :bool=True,
        reraise                     :bool = False,
        ):
        self.except_handler = except_handler
        self.except_handler_args = except_handler_args
        self.except_handler_kwargs = except_handler_kwargs
        self.exception_type = exception_type
        self.exception_log = exception_log
        self.reraise = reraise

    @property
    def config(self):
        config = {
            "except_handler": self.except_handler,
            "except_handler_args": self.except_handler_args,
            "except_handler_kwargs": self.except_handler_kwargs,
            "exception_type": self.exception_type,
            "exception_log": self.exception_log,
            "reraise": self.reraise
        }

        return config

    def decorator(self, func:Callable, *args, **kwargs):
        def wrapper(*func_args, **func_kwargs):
            kwargs_ = {**self.config, **kwargs}

            result = try_exc_else_finally(
                handled_callable=           func,
                handled_callable_args=      func_args,
                handled_callable_kwargs=    func_kwargs,
                *args, **kwargs_
                )
            return result
        return wrapper
    
    def __call__(self, *args, **kwargs):
        decorator = partial(self.decorator, *args, **kwargs)

        if args and callable(args[0]):
            return decorator()

        else:
            return decorator
        
tryexcept = TryExcept()