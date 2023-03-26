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

from __future__ import annotations
from .common import BaseObject
from .models import Name

class Language(BaseObject):

    __slots__ = (
        'id',
        'name',
        'official',
        'iso639',
        'iso3166',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        official: bool,
        iso639: str,
        iso3166: str,
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.official: bool = official
        self.iso639: str = iso639
        self.iso3166: str = iso3166
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> Language:
        return Language(
            id=data['id'],
            name=data['name'],
            official=data['official'],
            iso639=data['iso639'],
            iso3166=data['iso3166'],
            names=Name.loads_list(data['names'])
        )