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
from .common import BaseObject
from .models import NamedAPIResource, Name

if TYPE_CHECKING:
    from .item import Item
    from .move import Move
    from .location import Location
    from .pokemon.species import PokemonSpecies
    from .pokemon.type import Type as PokemonTypePayload


class EvolutionTrigger(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names',
        'pokemon_species'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name],
        pokemon_species: list[NamedAPIResource['PokemonSpecies']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.names: list[Name] = names
        self.pokemon_species: list[NamedAPIResource['PokemonSpecies']] = pokemon_species

    @staticmethod
    def loads(data: dict) -> EvolutionTrigger:
        return EvolutionTrigger(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names']),
            pokemon_species=NamedAPIResource.loads_list(data['pokemon_species'])
        )

    @property
    def species(self) -> list[NamedAPIResource['PokemonSpecies']]:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')


class EvolutionDetail(BaseObject):

    __slots__ = (
        'item',
        'trigger',
        'gender',
        'held_item',
        'known_move',
        'known_move_type',
        'location',
        'min_level',
        'min_happiness',
        'min_beauty',
        'min_affection',
        'needs_overworld_rain',
        'party_species',
        'party_type',
        'relative_physical_stats',
        'time_of_day',
        'trade_species',
        'turn_upside_down'
    )

    def __init__(
        self,
        trigger: NamedAPIResource,
        min_level: int,
        time_of_day: str,
        turn_upside_down: bool,
        item: Optional[NamedAPIResource['Item']] = None,
        gender: Optional[int] = None,
        held_item: Optional[NamedAPIResource['Item']] = None,
        known_move: Optional[NamedAPIResource['Move']] = None,
        known_move_type: Optional[NamedAPIResource['PokemonTypePayload']] = None,
        location: Optional[NamedAPIResource['Location']] = None,
        min_happiness: Optional[int] = None,
        min_beauty: Optional[int] = None,
        min_affection: Optional[int] = None,
        needs_overworld_rain: Optional[bool] = None,
        party_species: Optional[NamedAPIResource['PokemonSpecies']] = None,
        party_type: Optional[NamedAPIResource['PokemonTypePayload']] = None,
        relative_physical_stats: Optional[int] = None,
        trade_species: Optional[NamedAPIResource['PokemonSpecies']] = None
    ) -> None:
        self.trigger: NamedAPIResource = trigger
        self.min_level: int = min_level
        self.time_of_day: str = time_of_day
        self.turn_upside_down: bool = turn_upside_down
        self.item: Optional[NamedAPIResource['Item']] = item
        self.gender: Optional[int] = gender
        self.held_item: Optional[NamedAPIResource['Item']] = held_item
        self.known_move: Optional[NamedAPIResource['Move']] = known_move
        self.known_move_type: Optional[NamedAPIResource['PokemonTypePayload']] = known_move_type
        self.location: Optional[NamedAPIResource['Location']] = location
        self.min_happiness: Optional[int] = min_happiness
        self.min_beauty: Optional[int] = min_beauty
        self.min_affection: Optional[int] = min_affection
        self.needs_overworld_rain: Optional[bool] = needs_overworld_rain
        self.party_species: Optional[NamedAPIResource['PokemonSpecies']] = party_species
        self.party_type: Optional[NamedAPIResource['PokemonTypePayload']] = party_type
        self.relative_physical_stats: Optional[int] = relative_physical_stats
        self.trade_species: Optional[NamedAPIResource['PokemonSpecies']] = trade_species

    @staticmethod
    def loads(data: dict) -> EvolutionDetail:
        detail = EvolutionDetail(
            trigger=NamedAPIResource.loads(data['trigger']),
            min_level=data['min_level'],
            time_of_day=data['time_of_day'],
            turn_upside_down=data['turn_upside_down'],
            gender=data.get('gender'),
            min_happiness=data.get('min_happiness'),
            min_beauty=data.get('min_beauty'),
            min_affection=data.get('min_affection'),
            needs_overworld_rain=data.get('needs_overworld_rain'),
            relative_physical_stats=data.get('relative_physical_stats')
        )

        for attr in (
            'item',
            'held_item',
            'known_move',
            'known_move_type',
            'location',
            'party_species',
            'party_type',
            'trade_species',
        ):
            if (var := data.get(attr)) is not None:
                setattr(detail, attr, NamedAPIResource.loads(var))

        return detail


class ChainLink(BaseObject):

    __slots__ = (
        'is_baby',
        'species',
        'evolution_details',
        'evolves_to'
    )

    def __init__(
        self,
        is_baby: bool,
        species: NamedAPIResource['PokemonSpecies'],
        evolution_details: list[EvolutionDetail],
        evolves_to: list[ChainLink]
    ) -> None:
        self.is_baby: bool = is_baby
        self.species: NamedAPIResource['PokemonSpecies'] = species
        self.evolution_details: list[EvolutionDetail] = evolution_details
        self.evolves_to: list[ChainLink] = evolves_to

    @staticmethod
    def loads(data: dict) -> ChainLink:
        return ChainLink(
            is_baby=data['is_baby'],
            species=NamedAPIResource.loads(data['species']),
            evolution_details=EvolutionDetail.loads_list(data['evolution_details']),
            evolves_to=ChainLink.loads_list(data['evolves_to'])
        )

    @property
    def details(self) -> list[EvolutionDetail]:
        """alias for details attribute"""

        return getattr(self, 'evolution_details')


class EvolutionChain(BaseObject):

    __slots__ = (
        'id',
        'baby_trigger_item',
        'chain'
    )

    def __init__(
        self,
        id: int,
        chain: ChainLink,
        baby_trigger_item: Optional[NamedAPIResource['Item']] = None
    ) -> None:
        self.id: int = id
        self.chain: ChainLink = chain
        self.baby_trigger_item: Optional[NamedAPIResource['Item']] = baby_trigger_item

    @staticmethod
    def loads(data: dict) -> EvolutionChain:
        chain = EvolutionChain(
            id=data['id'],
            chain=ChainLink.loads(data['chain'])
        )

        if (var := data.get('baby_trigger_item')) is not None:
            chain.baby_trigger_item = NamedAPIResource.loads(var)

        return chain