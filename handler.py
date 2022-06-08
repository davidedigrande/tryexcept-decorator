from __future__ import annotations
from typing import Callable, Union, Any
from functools import partial

from decorator import decorator

class TryExceptHandler:
    def __init__(
        self,
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

        self.except_handler             = except_handler
        self.except_handler_args        = except_handler_args
        self.except_func_kwargs         = except_handler_kwargs
        self.except_handled_value       = except_handled_value
        self.else_handler               = else_handler
        self.else_handler_args          = else_handler_args
        self.else_handler_kwargs        = else_handler_kwargs
        self.finally_handler            = finally_handler
        self.finally_handler_args       = finally_handler_args
        self.finally_handler_kwargs     = finally_handler_kwargs
        self.exception_type             = exception_type
        self.exception_log              = exception_log

        self.__decorator = self.make_decorator()

    def make_decorator(self) -> Callable:
        return partial(
            decorator,
            self.except_handler,
            self.except_handler_args,
            self.except_func_kwargs,
            self.except_handled_value,
            self.else_handler,
            self.else_handler_args,
            self.else_handler_kwargs,
            self.finally_handler,
            self.finally_handler_args,
            self.finally_handler_kwargs,
            self.exception_type,
            self.exception_log,
            )

    def __call__(self, **kwargs):
        return self.__decorator()