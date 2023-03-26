"""
The MIT License (MIT)

Copyright (c) 2023-present Yumax-panda

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Type, TypeVar, Any

T = TypeVar('T')


class BaseObject:

    __slots__ = ()

    def to_dict(self) -> dict[str, Any]:
        """Converts this object into a dict.
        Returns
        -------
        Dict
            A dictionary of :class:`str` keys bound to the respective value.
        """

        ret = {}

        for attr in self.__slots__:
            var = getattr(self, attr)

            if isinstance(var, BaseObject):
                ret[attr] = var.to_dict()
            elif isinstance(var, list):
                items = []
                for item in var:
                    if isinstance(item, BaseObject):
                        items.append(item.to_dict())
                    else:
                        items.append(item)
                ret[attr] = items
            else:
                ret[attr] = var

        return ret


    def __str__(self):
        return f'<{self.__class__.__name__}>: {str({attr: getattr(self, attr) for attr in self.__slots__})}'


    @classmethod
    def loads(cls: Type[T], data: dict) -> T:
        return cls(**{attr: data.get(attr) for attr in cls.__slots__})


    @classmethod
    def loads_list(cls: Type[T], data: list[dict]) -> list[T]:
        return list(map(lambda x: cls.loads(x), data))