from typing import Any, Callable, List

author = "courte_e"


def printer(text: str, err: bool = False) -> int:
    """ Function to print string in stderr output if err is True else stdout"""
    return (sys.stderr if err is True else sys.stdout).write(text)


def my_map(function: Callable, data: List[Any]) -> List[Any]:
    """ Function to apply a function to all elements in a list """
    return [function(x) for x in data]


def my_filter(function: Callable, data: List[Any]) -> List[Any]:
    """ Function to filter all elements of array using a function"""
    return [x for x in data if function(x)]


def my_reduce(function: Callable, data: List[Any]) -> Any:
    """ Function to apply a function recursively to all elements in a list """
    if len(data) == 0:
        return None
    result = data[0]
    for i in range(1, len(data)):
        result = function(result, data[i])
    return result


"""
print(printer("abc\n", True))
print(my_map(lambda x: x * x, range(5)))
print(my_filter(lambda x: x % 2 == 0, range(5)))
print(my_reduce(lambda x, y: x * y, range(1, 5)))
"""
