import functools
from typing import get_type_hints


def return_check(func):
    """
        Decorators to check the retrun type of an api

    Args:
        func (The): The function that calls this decorator

    Raises:
        TypeError: Checks if the function return the correct type.

    Returns:
        Response: The starletter response.
    """

    @functools.wraps(func)
    def check(*args, **kwargs):

        result = func(*args, **kwargs)

        if "return" in func.__annotations__:

            r_type = func.__annotations__.get("return")

            if not isinstance(result, r_type):
                raise TypeError(
                    f"Function {func.__name__} should return {r_type.__name__} but it returned {type(result).__name__}"
                )

        return result

    return check
