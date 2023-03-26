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
from typing import Optional, TYPE_CHECKING
from objects.common import BaseObject
from objects.models import APIResource, NamedAPIResource, Name

if TYPE_CHECKING:
    from . import Characteristic, Nature
    from objects import MoveDamageClass, Move


class NatureStatAffectSets(BaseObject):

    __slots__ = (
        'increase',
        'decrease'
    )

    def __init__(
        self,
        increase: list[NamedAPIResource['Nature']],
        decrease: list[NamedAPIResource['Nature']]
    ) -> None:
        self.increase: list[NamedAPIResource['Nature']] = increase
        self.decrease: list[NamedAPIResource['Nature']] = decrease

    @staticmethod
    def loads(data: dict) -> NatureStatAffectSets:
        return NatureStatAffectSets(
            increase=NamedAPIResource.loads_list(data['increase']),
            decrease=NamedAPIResource.loads_list(data['decrease'])
        )


class MoveStatAffect(BaseObject):

    __slots__ = (
        'change',
        'move'
    )

    def __init__(
        self,
        change: int,
        move: NamedAPIResource['Move']
    ) -> None:
        self.change: int = change
        self.move: NamedAPIResource['Move'] = move

    @staticmethod
    def loads(data: dict) -> MoveStatAffect:
        return MoveStatAffect(
            change=data['change'],
            move=NamedAPIResource.loads(data['move'])
        )


class MoveStatAffectSets(BaseObject):

    __slots__ = (
        'increase',
        'decrease'
    )

    def __init__(
        self,
        increase: list[MoveStatAffect],
        decrease: list[MoveStatAffect]
    ) -> None:
        self.increase: list[MoveStatAffect] = increase
        self.decrease: list[MoveStatAffect] = decrease

    @staticmethod
    def loads(data: dict) -> MoveStatAffectSets:
        return MoveStatAffectSets(
            increase=MoveStatAffect.loads_list(data['increase']),
            decrease=MoveStatAffect.loads_list(data['decrease'])
        )


class Stat(BaseObject):

    __slots__ = (
        'id',
        'name',
        'game_index',
        'is_battle_only',
        'affecting_moves',
        'affecting_natures',
        'characteristics',
        'move_damage_class',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        game_index: int,
        is_battle_only: bool,
        affecting_moves: MoveStatAffectSets,
        affecting_natures: NatureStatAffectSets,
        characteristics: list[APIResource['Characteristic']],
        names: list[Name],
        move_damage_class: Optional[NamedAPIResource['MoveDamageClass']] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.game_index: int = game_index
        self.is_battle_only: bool = is_battle_only
        self.affecting_moves: MoveStatAffectSets = affecting_moves
        self.affecting_natures: NatureStatAffectSets = affecting_natures
        self.characteristics: list[APIResource['Characteristic']] = characteristics
        self.move_damage_class: Optional[NamedAPIResource['MoveDamageClass']] = move_damage_class
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> Stat:
        stat = Stat(
            id=data['id'],
            name=data['name'],
            game_index=data['game_index'],
            is_battle_only=data['is_battle_only'],
            affecting_moves=MoveStatAffectSets.loads(data['affecting_moves']),
            affecting_natures=NatureStatAffectSets.loads(data['affecting_natures']),
            characteristics=APIResource.loads_list(data['characteristics']),
            names=Name.loads_list(data['names'])
        )

        if (var:=data['move_damage_class']) is not None:
            stat.move_damage_class = NamedAPIResource.loads(var)

        return stat