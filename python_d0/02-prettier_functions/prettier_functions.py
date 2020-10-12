from typing import Any, Callable, List

author = "courte_e"


def nullifier(function: Callable) -> Callable:
    return (lambda: None)


def stealer(amount: int) -> Callable[[Callable], Any]:
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
