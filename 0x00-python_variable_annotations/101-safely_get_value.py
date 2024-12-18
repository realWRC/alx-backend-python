#!/usr/bin/env python3
# """
# Given the parameters and the return values, add
# type annotations to the function
# """
#
#
# from typing import Mapping, Any, Union, TypeVar
#
#
# T = TypeVar('T')
#
#
# def safely_get_value(dct: Mapping[Any, Any], key: Any, default:
#                      Union[T, None] = None) -> Union[Any, T]:
#     """Type annotations for the function"""
#     if key in dct:
#         return dct[key]
#     else:
#         return default
"""
Given the parameters and the return values, add type
annotations to the function
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key:
                     typing.Any, default: typing.Union[T, None] = None) -> \
                             typing.Union[typing.Any, T]:
    """Type annotations for the function"""
    if key in dct:
        return dct[key]
    else:
        return default
