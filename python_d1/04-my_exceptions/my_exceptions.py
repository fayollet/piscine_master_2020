#!/usr/bin/env python3
from typing import IO, Union, List

author = "courte_e"

class CustomException(BaseException):
    ''' basic exception class '''
    reason = None


class UnauthorizedException(CustomException):
    reason = "unauthorized"


def login(user_data: dict) -> dict:
    if 'username' not in user_data and 'password' not in user_data:
        raise ValueError
    if 'username' not in user_data or 'password' not in user_data:
        e = 'username' if 'username' not in user_data else 'password'
        raise CustomException(f"key {e} is missing")
    user_data['logged'] = user_data['username'] == user_data["password"][::-1]
    return user_data


def is_admin(user_data: dict) -> bool:
    if 'logged' not in user_data:
        raise UnauthorizedException("unauthorized")
    return user_data['logged'] and user_data['username'] == 'admin'


"""
my_data = {"username": "admi", "password": "nimda"}
authenticated = login(my_data)
admin = is_admin(authenticated)
print(f"user={my_data['username']} admin={admin}")
"""
