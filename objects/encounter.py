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
from .models import NamedAPIResource, Name


class EncounterMethod(BaseObject):

    __slots__ = (
        'id',
        'name',
        'order',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        order: int,
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.order: int = order
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> EncounterMethod:
        return EncounterMethod(
            id=data['id'],
            name=data['name'],
            order=data['order'],
            names=Name.loads_list(data['names'])
        )


class EncounterCondition(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names',
        'values'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name],
        values: list[NamedAPIResource['EncounterConditionValue']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.names: list[Name] = names
        self.values: list[NamedAPIResource['EncounterConditionValue']] = values

    @staticmethod
    def loads(data: dict) -> EncounterCondition:
        return EncounterCondition(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names']),
            values=NamedAPIResource.loads_list(data['values'])
        )


class EncounterConditionValue(BaseObject):

    __slots__ = (
        'id',
        'name',
        'condition',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        condition: NamedAPIResource['EncounterCondition'],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.condition: NamedAPIResource['EncounterCondition'] = condition
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> EncounterConditionValue:
        return EncounterConditionValue(
            id=data['id'],
            name=data['name'],
            condition=NamedAPIResource.loads(data['condition']),
            names=Name.loads_list(data['names'])
        )