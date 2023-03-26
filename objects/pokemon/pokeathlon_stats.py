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
from typing import TYPE_CHECKING
from objects.common import BaseObject
from objects.models import NamedAPIResource, Name

if TYPE_CHECKING:
    from . import Nature


class NaturePokeathlonStatAffect(BaseObject):

    __slots__ = (
        'max_change',
        'nature'
    )

    def __init__(
        self,
        max_change: int,
        nature: NamedAPIResource['Nature']
    ) -> None:
        self.max_change: int = max_change
        self.nature: NamedAPIResource['Nature'] = nature

    @staticmethod
    def loads(data: dict) -> NaturePokeathlonStatAffect:
        return NaturePokeathlonStatAffect(
            max_change=data['max_change'],
            nature=NamedAPIResource.loads(data['nature'])
        )


class NaturePokeathlonStatAffectSet(BaseObject):

    __slots__ = (
        'increase',
        'decrease'
    )

    def __init__(
        self,
        increase: list[NaturePokeathlonStatAffect],
        decrease: list[NaturePokeathlonStatAffect]
    ) -> None:
        self.increase: list[NaturePokeathlonStatAffect] = increase
        self.decrease: list[NaturePokeathlonStatAffect] = decrease

    @staticmethod
    def loads(data: dict) -> NaturePokeathlonStatAffectSet:
        return NaturePokeathlonStatAffectSet(
            increase=NaturePokeathlonStatAffect.loads_list(data['increase']),
            decrease=NaturePokeathlonStatAffect.loads_list(data['decrease'])
        )


class PokeathlonStat(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names',
        'affecting_natures'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name],
        affecting_natures: NaturePokeathlonStatAffectSet
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.names: list[Name] = names
        self.affecting_natures: NaturePokeathlonStatAffectSet = affecting_natures

    @staticmethod
    def loads(data: dict) -> PokeathlonStat:
        return PokeathlonStat(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names']),
            affecting_natures=NaturePokeathlonStatAffectSet.loads(data['affecting_natures'])
        )

    @property
    def natures(self) -> NaturePokeathlonStatAffectSet:
        """alias for affecting_natures attribute"""

        return getattr(self, 'affecting_natures')