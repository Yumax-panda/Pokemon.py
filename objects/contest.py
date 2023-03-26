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
from .common import BaseObject
from .models import (
    NamedAPIResource,
    PartialFlavorText,
    Effect
)

if TYPE_CHECKING:
    from .berry import BerryFlavor
    from .language import Language
    from .move import Move



class ContestName(BaseObject):

    __slots__ = (
        'name',
        'color',
        'language'
    )

    def __init__(
        self,
        name: str,
        color: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.name: str = name
        self.color: str = color
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> ContestName:
        return ContestName(
            name=data['name'],
            color=data['color'],
            language=NamedAPIResource.loads(data['language'])
        )


class ContestType(BaseObject):

    __slots__ = (
        'id',
        'name',
        'berry_flavor',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        berry_flavor: NamedAPIResource['BerryFlavor'],
        names: list[ContestName]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.berry_flavor: NamedAPIResource['BerryFlavor'] = berry_flavor
        self.names: list[ContestName] = names

    @staticmethod
    def loads(data: dict) -> ContestType:
        return ContestType(
            id=data['id'],
            name=data['name'],
            berry_flavor=NamedAPIResource.loads(data['berry_flavor']),
            names=ContestName.loads_list(data['names'])
        )


class ContestEffect(BaseObject):

    __slots__ = (
        'id',
        'appeal',
        'jam',
        'effect_entries',
        'flavor_text_entries'
    )

    def __init__(
        self,
        id: int,
        appeal: int,
        jam: int,
        effect_entries: list[Effect],
        flavor_text_entries: list[PartialFlavorText]
    ) -> None:
        self.id: int = id
        self.appeal: int = appeal
        self.jam: int = jam
        self.effect_entries: list[Effect] = effect_entries
        self.flavor_text_entries: list[PartialFlavorText] = flavor_text_entries

    @staticmethod
    def loads(data: dict) -> ContestEffect:
        return ContestEffect(
            id=data['id'],
            appeal=data['appeal'],
            jam=data['jam'],
            effect_entries=Effect.loads_list(data['effect_entries']),
            flavor_text_entries=PartialFlavorText.loads_list(data['flavor_text_entries'])
        )

    @property
    def effects(self) -> list[Effect]:
        """alias for effects_entries attribute"""

        return getattr(self, 'effect_entries')

    @property
    def flavor_texts(self) -> list[PartialFlavorText]:
        """alias for flavor_text_entries attribute"""

        return getattr(self, 'flavor_text_entries')


class SuperContestEffect(BaseObject):

    __slots__ = (
        'id',
        'appeal',
        'flavor_text_entries',
        'moves'
    )

    def __init__(
        self,
        id: int,
        appeal: int,
        flavor_text_entries: list[PartialFlavorText],
        moves: list[NamedAPIResource['Move']]
    ) -> None:
        self.id: int = id
        self.appeal: int = appeal
        self.flavor_text_entries: list[PartialFlavorText] = flavor_text_entries
        self.moves: list[NamedAPIResource['Move']] = moves

    @staticmethod
    def loads(data: dict) -> SuperContestEffect:
        return SuperContestEffect(
            id=data['id'],
            appeal=data['appeal'],
            flavor_text_entries=PartialFlavorText.loads_list(data['flavor_text_entries']),
            moves=NamedAPIResource.loads_list(data['moves'])
        )

    @property
    def flavor_texts(self) -> list[PartialFlavorText]:
        """alias for flavor_text_entries attribute"""

        return getattr(self, 'flavor_text_entries')