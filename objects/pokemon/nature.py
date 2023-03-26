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
from objects.models import NamedAPIResource, Name

if TYPE_CHECKING:
    from objects import BerryFlavor, MoveBattleStyle
    from . import Stat, PokeathlonStat


class NatureStatChange(BaseObject):

    __slots__ = (
        'max_change',
        'pokeathlon_stat'
    )

    def __init__(
        self,
        max_change: int,
        pokeathlon_stat: NamedAPIResource['PokeathlonStat']
    ) -> None:
        self.max_change: int = max_change
        self.pokeathlon_stat: NamedAPIResource['PokeathlonStat'] = pokeathlon_stat

    @staticmethod
    def loads(data: dict) -> NatureStatChange:
        return NatureStatChange(
            max_change=data['max_change'],
            pokeathlon_stat=NamedAPIResource.loads(data['pokeathlon_stat'])
        )

    @property
    def stat(self) -> NamedAPIResource['PokeathlonStat']:
        """alias for pokeathlon_stat attribute"""

        return getattr(self, 'pokeathlon_stat')


class MoveBattleStylePreference(BaseObject):

    __slots__ = (
        'low_hp_preference',
        'high_hp_preference',
        'move_battle_style'
    )

    def __init__(
        self,
        low_hp_preference: int,
        high_hp_preference: int,
        move_battle_style: NamedAPIResource['MoveBattleStyle']
    ) -> None:
        self.low_hp_preference: int = low_hp_preference
        self.high_hp_preference: int = high_hp_preference
        self.move_battle_style: NamedAPIResource['MoveBattleStyle'] = move_battle_style

    @staticmethod
    def loads(data: dict) -> MoveBattleStylePreference:
        return MoveBattleStylePreference(
            low_hp_preference=data['low_hp_preference'],
            high_hp_preference=data['high_hp_preference'],
            move_battle_style=NamedAPIResource.loads(data['move_battle_style'])
        )

    @property
    def low_preference(self) -> int:
        """alias for low_hp_preference attribute"""

        return getattr(self, 'low_hp_preference')

    @property
    def high_preference(self) -> int:
        """alias for high_hp_preference attribute"""

        return getattr(self, 'high_hp_preference')

    @property
    def style(self) -> NamedAPIResource['MoveBattleStyle']:
        """alias for move_battle_style attribute"""

        return getattr(self, 'move_battle_style')


class Nature(BaseObject):

    __slots__ = (
        'id',
        'name',
        'decreased_stat',
        'increased_stat',
        'hates_flavor',
        'likes_flavor',
        'pokeathlon_stat_changes',
        'move_battle_style_preferences',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        pokeathlon_stat_changes: list[NatureStatChange],
        move_battle_style_preferences: list[MoveBattleStylePreference],
        names: list[Name],
        decreased_stat: Optional[NamedAPIResource['Stat']] = None,
        increased_stat: Optional[NamedAPIResource['Stat']] = None,
        hates_flavor: Optional[NamedAPIResource['BerryFlavor']]= None,
        likes_flavor: Optional[NamedAPIResource['BerryFlavor']] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.decreased_stat: Optional[NamedAPIResource['Stat']] = decreased_stat
        self.increased_stat: Optional[NamedAPIResource['Stat']] = increased_stat
        self.hates_flavor: Optional[NamedAPIResource['BerryFlavor']] = hates_flavor
        self.likes_flavor: Optional[NamedAPIResource['BerryFlavor']] = likes_flavor
        self.pokeathlon_stat_changes: list[NatureStatChange] = pokeathlon_stat_changes
        self.move_battle_style_preferences: list[MoveBattleStylePreference] = move_battle_style_preferences
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> Nature:
        nature = Nature(
            id=data['id'],
            name=data['name'],
            pokeathlon_stat_changes=NatureStatChange.loads_list(data['pokeathlon_stat_changes']),
            move_battle_style_preferences=MoveBattleStylePreference.loads_list(data['move_battle_style_preferences']),
            names=Name.loads_list(data['names'])
        )

        for attr in (
            'decreased_stat',
            'increased_stat',
            'hates_flavor',
            'likes_flavor'
        ):
            if (var := data[attr]) is not None:
                setattr(nature, attr, NamedAPIResource.loads(var))

        return nature

    @property
    def low(self) -> Optional[NamedAPIResource['Stat']]:
        """alias for decreased_stat attribute"""

        return getattr(self, 'decreased_stat')

    @property
    def high(self) -> Optional[NamedAPIResource['Stat']]:
        """alias for increased_stat attribute"""

        return getattr(self, 'increased_stat')

    @property
    def hate(self) -> Optional[NamedAPIResource['BerryFlavor']]:
        "alias for hates_flavor attribute"

        return getattr(self, 'hates_flavor')

    @property
    def like(self) -> Optional[NamedAPIResource['BerryFlavor']]:
        "alias for likes_flavor attribute"

        return getattr(self, 'likes_flavor')

    @property
    def stat_changes(self) -> list[NatureStatChange]:
        """alias for pokeathlon_stat_changes"""

        return getattr(self, 'pokeathlon_stat_changes')

    @property
    def preferred_styles(self) -> list[MoveBattleStylePreference]:
        """alias for move_battle_style_preferences"""

        return getattr(self, 'move_battle_style_preferences')