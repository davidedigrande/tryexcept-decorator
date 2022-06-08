from __future__ import annotations
import functools
from typing import Callable, Union, Any

from core import try_exc_else_finally

def decorator(
    except_handler:             Callable = lambda: None,
    except_handler_args:        tuple = (),
    except_handler_kwargs:      dict = {},
    except_handled_value:       Any = None,
    else_handler:               Callable = lambda: None,
    else_handler_args:          tuple = (),
    else_handler_kwargs:        dict = {},
    finally_handler:            Callable = lambda: None,
    finally_handler_args:       tuple = (),
    finally_handler_kwargs:     dict = {},
    exception_type:             Union[Exception, tuple[Exception]] = Exception,
    exception_log:              bool=True,
):
    def decorator(func:Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return try_exc_else_finally(
                handled_callable=           func,
                handled_callable_args=      args,
                handled_callable_kwargs=    kwargs,
                
                except_handler=             except_handler,
                except_handler_args=        except_handler_args,
                except_handler_kwargs=      except_handler_kwargs,
                except_handled_value=       except_handled_value,

                else_handler=               else_handler,
                else_handler_args=          else_handler_args,
                else_handler_kwargs=        else_handler_kwargs,

                finally_handler=            finally_handler,
                finally_handler_args=       finally_handler_args,
                finally_handler_kwargs=     finally_handler_kwargs,

                exception_type=             exception_type,
                exception_log=              exception_log,
                )
        return wrapper
    return decorator