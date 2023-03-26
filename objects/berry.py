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
from .models import NamedAPIResource, Name

if TYPE_CHECKING:
    from .item import Item
    from .pokemon.type import Type as PokemonTypePayload
    from .contest import ContestType


class BerryFlavorMap(BaseObject):

    __slots__ = (
        'potency',
        'flavor'
    )

    def __init__(
        self,
        potency: int,
        flavor: NamedAPIResource['BerryFlavor']
    ) -> None:
        self.potency: int = potency
        self.flavor: NamedAPIResource['BerryFlavor'] = flavor


class Berry(BaseObject):

    __slots__ = (
        'id',
        'name',
        'growth_time',
        'max_harvest',
        'natural_gift_power',
        'size',
        'smoothness',
        'soil_dryness',
        'firmness',
        'flavors',
        'item',
        'natural_gift_type'
    )

    def __init__(
        self,
        id: int,
        name: str,
        growth_time: int,
        max_harvest: int,
        natural_gift_power: int,
        size: int,
        smoothness: int,
        soil_dryness: int,
        firmness: NamedAPIResource['BerryFirmness'],
        flavors: list[BerryFlavorMap],
        item: NamedAPIResource['Item'],
        natural_gift_type: NamedAPIResource['PokemonTypePayload']
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.growth_time: int = growth_time
        self.max_harvest: int = max_harvest
        self.natural_gift_power: int = natural_gift_power
        self.size: int = size
        self.smoothness: int = smoothness
        self.soil_dryness: int = soil_dryness
        self.firmness: NamedAPIResource['BerryFirmness'] = firmness
        self.flavors: list[BerryFlavorMap] = flavors
        self.item: NamedAPIResource['Item'] = item
        self.natural_gift_type: NamedAPIResource['PokemonTypePayload'] = natural_gift_type


    @staticmethod
    def loads(data: dict) -> Berry:
        return Berry(
            id=data['id'],
            name=data['name'],
            growth_time=data['growth_time'],
            max_harvest=data['max_harvest'],
            natural_gift_power=data['natural_gift_power'],
            size=data['size'],
            smoothness=data['smoothness'],
            soil_dryness=data['soil_dryness'],
            firmness=NamedAPIResource.loads(data['firmness']),
            flavors=BerryFlavorMap.loads_list(data['flavors']),
            item=NamedAPIResource.loads(data['item']),
            natural_gift_type=NamedAPIResource.loads(data['item'])
        )

    @property
    def time(self) -> int:
        """alias for growth_time attribute"""

        return getattr(self, 'growth_time')

    @property
    def gift_power(self) -> int:
        """alias for natural gift power attribute"""

        return getattr(self, 'natural_gift_power')

    @property
    def dryness(self) -> int:
        """alias for soil_dryness attribute"""

        return getattr(self, 'soil_dryness')

    @property
    def gift_type(self) -> NamedAPIResource['PokemonTypePayload']:
        """alias for natural_gift_type attribute"""

        return getattr(self, 'natural_gift_type')


class BerryFirmness(BaseObject):

    __slots__ = (
        'id',
        'name',
        'berries',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        berries: list[NamedAPIResource['Berry']],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.berries: list[NamedAPIResource['Berry']] = berries
        self.names: list[Name] = names


    @staticmethod
    def loads(data: dict) -> BerryFirmness:
        return BerryFirmness(
            id=data['id'],
            name=data['name'],
            berries= NamedAPIResource.loads_list(data['berries']),
            names=Name.loads_list(data['names'])
        )


class FlavorBerryMap(BaseObject):

    __slots__ = (
        'potency',
        'berry'
    )

    def __init__(
        self,
        potency: int,
        berry: NamedAPIResource['Berry']
    ) -> None:
        self.potency: int = potency
        self.berry: NamedAPIResource['Berry'] = berry



class BerryFlavor(BaseObject):

    __slots__ = (
        'id',
        'name',
        'berries',
        'contest_type',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        berries: list[FlavorBerryMap],
        contest_type: NamedAPIResource['ContestType'],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.berries: list[FlavorBerryMap] = berries
        self.contest_type: NamedAPIResource['ContestType'] = contest_type
        self.names: list[Name] = names


    @staticmethod
    def loads(data: dict) -> BerryFlavor:
        return BerryFlavor(
            id=data['id'],
            name=data['name'],
            berries=FlavorBerryMap.loads_list(data['berries']),
            contest_type=NamedAPIResource.loads(data['contest_type']),
            names=Name.loads_list(data['names'])
        )

