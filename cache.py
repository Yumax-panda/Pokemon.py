"""
The MIT License (MIT)

Copyright (c) 2021-present beastmatser
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

from __future__ import annotations
from typing import (
    Any,
    Callable,
    Coroutine,
    TYPE_CHECKING,
    TypeVar,
    Union
)
U = TypeVar('U')
Param = Union[str, int]

if TYPE_CHECKING:
    from api import Client


class Cache:

    cache: dict[str, Any] = {}

    def get(self, key: Union[str, int]) -> Any:
        return self.cache.get(str(key))

    def put(self, key: Union[str, int], value: Any) -> None:
        self.cache[str(key)] = value

    def __str__(self) -> str:
        return str(self.cache)


def cached_resource(endpoint: str) -> Callable[['Client', Param], Coroutine[Any, Any, U]]:

    def decorator(coroutine: Callable[['Client', Param], Coroutine[Any, Any, U]]):

        async def wrapper(client: Client, id_or_name: Param) -> U:

            if (url := f'{endpoint}/{id_or_name}') in client._cache.cache.keys():
                return client._cache.get(url)

            obj: U = await coroutine(client, id_or_name)
            client._cache.put(url, obj)
            return obj
        return wrapper

    return decorator
