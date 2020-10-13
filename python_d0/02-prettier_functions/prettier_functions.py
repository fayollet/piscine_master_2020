from typing import Any, Callable, List

author = "courte_e"


def nullifier(function: Callable) -> Callable:
    """ Nullify the return of a function """
    return (lambda: None)


def stealer(amount: int) -> Callable[[Callable], Any]:
    """ Substract 'amount' to the return of a function """
    return (lambda function: (lambda: function() - amount))


"""
@nullifier
def super_function():
    return 5
print(super_function())

@stealer(12)
def super_function():
    return 5
print(super_function())
"""
