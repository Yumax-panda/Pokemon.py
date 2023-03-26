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
from .models import NamedAPIResource, Name, Description

if TYPE_CHECKING:
    from .pokemon.ability import Ability
    from .pokemon.species import PokemonSpecies
    from .pokemon.type import Type as PokemonTypePayload
    from .location import Region
    from .move import Move, MoveLearnMethod



class Generation(BaseObject):

    __slots__ = (
        'id',
        'name',
        'abilities',
        'names',
        'main_region',
        'moves',
        'pokemon_species',
        'types',
        'version_groups'
    )

    def __init__(
        self,
        id: int,
        name: str,
        abilities: list[NamedAPIResource['Ability']],
        names: list[Name],
        main_region: NamedAPIResource['Region'],
        moves: list[NamedAPIResource['Move']],
        pokemon_species: list[NamedAPIResource['PokemonSpecies']],
        types: list[NamedAPIResource['PokemonTypePayload']],
        version_groups: list[NamedAPIResource['VersionGroup']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.abilities: list[NamedAPIResource['Ability']] = abilities
        self.names: list[Name] = names
        self.main_region: NamedAPIResource['Region'] = main_region
        self.moves: list[NamedAPIResource['Move']] = moves
        self.pokemon_species: list[NamedAPIResource['PokemonSpecies']] = pokemon_species
        self.types: list[NamedAPIResource['PokemonTypePayload']] = types
        self.version_groups: list[NamedAPIResource['VersionGroup']] = version_groups

    @staticmethod
    def loads(data: dict) -> Generation:
        return Generation(
            id=data['id'],
            name=data['name'],
            abilities=NamedAPIResource.loads_list(data['abilities']),
            names=Name.loads_list(data['names']),
            main_region=NamedAPIResource.loads(data['main_region']),
            moves=NamedAPIResource.loads_list(data['moves']),
            pokemon_species=NamedAPIResource.loads_list(data['pokemon_species']),
            types=NamedAPIResource.loads_list(data['types']),
            version_groups=NamedAPIResource.loads_list(data['version_groups'])
        )

    @property
    def region(self) -> list[NamedAPIResource['Region']]:
        """alias for main_region attribute"""

        return getattr(self, 'main_region')

    @property
    def species(self) -> list[NamedAPIResource['PokemonSpecies']]:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')


class PokemonEntry(BaseObject):

    __slots__ = (
        'entry_number',
        'pokemon_species'
    )

    def __init__(
        self,
        entry_number: int,
        pokemon_species: NamedAPIResource['PokemonSpecies']
    ) -> None:
        self.entry_number: int = entry_number
        self.pokemon_species: NamedAPIResource['PokemonSpecies'] = pokemon_species

    @staticmethod
    def loads(data: dict) -> PokemonEntry:
        return PokemonEntry(
            entry_number=data['entry_number'],
            pokemon_species=NamedAPIResource.loads(data['pokemon_species'])
        )

    @property
    def number(self) -> int:
        """alias for entry_number attribute"""

        return getattr(self, 'entry_number')

    @property
    def species(self) -> NamedAPIResource['PokemonSpecies']:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')


class Pokedex(BaseObject):

    __slots__ = (
        'id',
        'name',
        'is_main_series',
        'descriptions',
        'names',
        'pokemon_entries',
        'region',
        'version_groups'
    )

    def __init__(
        self,
        id: int,
        name: str,
        is_main_series: bool,
        descriptions: list[Description],
        names: list[Name],
        pokemon_entries: list[PokemonEntry],
        version_groups: list[NamedAPIResource['VersionGroup']],
        region: Optional[NamedAPIResource['Region']] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.is_main_series: bool = is_main_series
        self.descriptions: list[Description] = descriptions
        self.names: list[Name] = names
        self.pokemon_entries: list[PokemonEntry] = pokemon_entries
        self.version_groups: list[NamedAPIResource['VersionGroup']] = version_groups
        self.region: Optional[NamedAPIResource['Region']] = region

    @staticmethod
    def loads(data: dict) -> Pokedex:
        pokedex = Pokedex(
            id=data['id'],
            name=data['name'],
            is_main_series=data['is_main_series'],
            descriptions=Description.loads_list(data['descriptions']),
            names=Name.loads_list(data['names']),
            pokemon_entries=PokemonEntry.loads_list(data['pokemon_entries']),
            version_groups=NamedAPIResource.loads_list(data['version_groups'])
        )

        if (var:= data.get('region')) is not None:
            pokedex.region = NamedAPIResource.loads(var)

        return pokedex


class Version(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names',
        'version_group'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.id: int = id
        self.name: int = name
        self.names: list[Name] = names
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> Version:
        return Version(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )


class VersionGroup(BaseObject):

    __slots__ = (
        'id',
        'name',
        'order',
        'generation',
        'move_learn_methods',
        'pokedexes',
        'regions',
        'versions'
    )

    def __init__(
        self,
        id: int,
        name: str,
        order: int,
        generation: NamedAPIResource['Generation'],
        move_learn_methods: list[NamedAPIResource['MoveLearnMethod']],
        pokedexes: list[NamedAPIResource['Pokedex']],
        regions: list[NamedAPIResource['Region']],
        versions: list[NamedAPIResource['Version']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.order: int = order
        self.generation: NamedAPIResource['Generation'] = generation
        self.move_learn_methods: list[NamedAPIResource['MoveLearnMethod']] = move_learn_methods
        self.pokedexes: list[NamedAPIResource['Pokedex']] = pokedexes
        self.regions: list[NamedAPIResource['Region']] = regions
        self.versions: list[NamedAPIResource['Version']] = versions

    @staticmethod
    def loads(data: dict) -> VersionGroup:
        return VersionGroup(
            id=data['id'],
            name=data['name'],
            order=data['order'],
            generation=NamedAPIResource.loads(data['generation']),
            move_learn_methods=NamedAPIResource.loads_list(data['move_learn_methods']),
            pokedexes=NamedAPIResource.loads_list(data['pokedexes']),
            regions=NamedAPIResource.loads_list(data['regions']),
            versions=NamedAPIResource.loads_list(data['versions'])
        )
