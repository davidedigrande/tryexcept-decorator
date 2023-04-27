from __future__ import annotations

import inspect
import logging
from functools import partial
from logging import Logger
from typing import Union


class TryExceptDecorator:
    def __init__(
        self,
        except_handler: function = lambda: None,
        except_handler_kwargs: dict = {},
        exception_type: Union[Exception, tuple[Exception]] = Exception,
        logger: Logger = logging.getLogger(),
    ):
        """
        The TryExcept Decorator is a configurable Python decorator that wraps a function around a try-except statement.
        It allows you to write cleaner code in your functions where an exception may happen and you want to handle it even in complex ways.

        Args:
            except_handler (function, optional): a function used to handle the decorated function in case it raises an exception. Defaults to lambda:None. In this case will simply handle the exception by returning a None value.
            except_handler_kwargs (dict, optional): keyword arguments for the except_handler function. Defaults to {}.
            exception_type (Union[Exception, tuple[Exception]], optional): type or types of exceptions to be catched by the handler. Defaults to Exception.
            logger (Logger, optional): logger to be used to log the exception traceback. Defaults to logging.getLogger().
        """

        self.except_handler = except_handler
        self.except_handler_kwargs = except_handler_kwargs
        self.exception_type = exception_type
        self.logger = logger

    @staticmethod
    def get_f_locals(func):
        frameinfo = None
        for _frameinfo in inspect.trace():
            if _frameinfo[3] == func.__name__:
                frameinfo = _frameinfo

        frame = frameinfo[0]
        return frame.f_locals

    def tryexcept(
        self,
        handled_function: function,
        handled_function_args: tuple = (),
        handled_function_kwargs: dict = {},
        except_handler: function = lambda: None,
        except_handler_kwargs: dict = {},
        exception_type: Union[Exception, tuple[Exception]] = Exception,
    ):
        try:
            try_value = handled_function(
                *handled_function_args, **handled_function_kwargs
            )

            return try_value

        except exception_type as exception:
            f_exc = exception
            f_locals = self.get_f_locals(func=handled_function)
            f_name = handled_function.__name__

            except_handler_parameters = inspect.signature(except_handler).parameters

            if except_handler_parameters.get("f_exc"):
                except_handler_kwargs["f_exc"] = f_exc

            if except_handler_parameters.get("f_locals"):
                except_handler_kwargs["f_locals"] = f_locals

            if except_handler_parameters.get("f_name"):
                except_handler_kwargs["f_name"] = f_name

            self.logger.exception("TryExcept decorator handled an exception. Traceback below.")

            except_value = except_handler(**except_handler_kwargs)

            return except_value

    def decorator(
        self,
        handled_function: function,
        except_handler: function,
        except_handler_kwargs: dict,
        exception_type: Exception,
    ):
        def wrapper(*handled_function_args, **handled_function_kwargs):
            return self.tryexcept(
                handled_function=handled_function,
                handled_function_args=handled_function_args,
                handled_function_kwargs=handled_function_kwargs,
                except_handler=except_handler,
                except_handler_kwargs=except_handler_kwargs,
                exception_type=exception_type,
            )

        return wrapper

    def __call__(
        self,
        func: function = None,
    ):
        _kwargs = {
            "handled_function": func,
            "except_handler": self.except_handler,
            "except_handler_kwargs": self.except_handler_kwargs,
            "exception_type": self.exception_type,
        }

        decorator = partial(self.decorator, **_kwargs)

        return decorator()


decorator = TryExceptDecorator
