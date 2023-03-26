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
    Name,
    GenerationGameIndex,
    VersionEncounterDetail
)

if TYPE_CHECKING:
    from .game import Version, Generation, Pokedex, VersionGroup
    from .encounter import EncounterMethod
    from .pokemon.pokemon import Pokemon
    from .pokemon.species import PokemonSpecies



class Location(BaseObject):

    __slots__ = (
        'id',
        'name',
        'region',
        'names',
        'game_indices',
        'areas'
    )

    def __init__(
        self,
        id: int,
        name: str,
        region: NamedAPIResource['Region'],
        names: list[Name],
        game_indices: list[GenerationGameIndex],
        areas: list[NamedAPIResource['LocationArea']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.region: NamedAPIResource['Region'] = region
        self.names: list[Name] = names
        self.game_indices: list[GenerationGameIndex] = game_indices
        self.areas: list[NamedAPIResource['LocationArea']] = areas

    @staticmethod
    def loads(data: dict) -> Location:
        return Location(
            id=data['id'],
            name=data['name'],
            region=NamedAPIResource.loads(data['region']),
            names=Name.loads_list(data['names']),
            game_indices=GenerationGameIndex.loads_list(data['game_indices']),
            areas=NamedAPIResource.loads_list(data['areas'])
        )


class PokemonEncounter(BaseObject):

    __slots__ = (
        'pokemon',
        'version_details'
    )

    def __init__(
        self,
        pokemon: NamedAPIResource['Pokemon'],
        version_details: list[VersionEncounterDetail]
    ) -> None:
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon
        self.version_details : list[VersionEncounterDetail]= version_details

    @staticmethod
    def loads(data: dict) -> PokemonEncounter:
        return PokemonEncounter(
            pokemon=NamedAPIResource.loads((data['pokemon'])),
            version_details=VersionEncounterDetail.loads_list(data['version_details'])
        )


class EncounterVersionDetails(BaseObject):

    __slots__ = (
        'rate',
        'version'
    )

    def __init__(
        self,
        rate: int,
        version: NamedAPIResource['Version']
    ) -> None:
        self.rate: int = rate
        self.version: NamedAPIResource['Version'] = version

    @staticmethod
    def loads(data: dict) -> EncounterVersionDetails:
        return EncounterVersionDetails(
            rate=data['rate'],
            version=NamedAPIResource.loads(data['version'])
        )


class EncounterMethodRate(BaseObject):

    __slots__ = (
        'encounter_method',
        'version_details'
    )

    def __init__(
        self,
        encounter_method: NamedAPIResource['EncounterMethod'],
        version_details: list[EncounterVersionDetails]
    ) -> None:
        self.encounter_method: NamedAPIResource['EncounterMethod'] = encounter_method
        self.version_details: list[EncounterVersionDetails] = version_details

    @staticmethod
    def loads(data: dict) -> EncounterMethodRate:
        return EncounterMethodRate(
            encounter_method=NamedAPIResource.loads(data['encounter_method']),
            version_details=EncounterVersionDetails.loads_list(data['version_details'])
        )


class LocationArea(BaseObject):

    __slots__ = (
        'id',
        'name',
        'game_index',
        'encounter_method_rates',
        'location',
        'names',
        'pokemon_encounters'
    )

    def __init__(
        self,
        id: int,
        name: str,
        game_index: int,
        encounter_method_rates: list[EncounterMethodRate],
        location: NamedAPIResource['Location'],
        names: list[Name],
        pokemon_encounters: list[PokemonEncounter]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.game_index: int = game_index
        self.encounter_method_rates: list[EncounterMethodRate] = encounter_method_rates
        self.location: NamedAPIResource['Location'] = location
        self.names: list[Name] = names
        self.pokemon_encounters: list[PokemonEncounter] = pokemon_encounters

    @staticmethod
    def loads(data: dict) -> LocationArea:
        return LocationArea(
            id=data['id'],
            name=data['name'],
            game_index=data['game_index'],
            encounter_method_rates=EncounterMethodRate.loads_list(data['encounter_method_rates']),
            location=NamedAPIResource.loads(data['location']),
            names=Name.loads_list(data['names']),
            pokemon_encounters=PokemonEncounter.loads_list(data['pokemon_encounters'])
        )


class PalParkEncounterSpecies(BaseObject):

    __slots__ = (
        'base_score',
        'rate',
        'pokemon_species'
    )

    def __init__(
        self,
        base_score: int,
        rate: int,
        pokemon_species: NamedAPIResource['PokemonSpecies']
    ) -> None:
        self.base_score: int = base_score
        self.rate: int = rate
        self.pokemon_species: NamedAPIResource['PokemonSpecies'] = pokemon_species

    @staticmethod
    def loads(data: dict) -> PalParkEncounterSpecies:
        return PalParkEncounterSpecies(
            base_score=data['base_score'],
            rate=data['rate'],
            pokemon_species=NamedAPIResource.loads(data['pokemon_species'])
        )

    @property
    def species(self) -> NamedAPIResource['PokemonSpecies']:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')


class PalParkArea(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names',
        'pokemon_encounters'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name],
        pokemon_encounters: list[PalParkEncounterSpecies]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.names: list[Name] = names
        self.pokemon_encounters: list[PalParkEncounterSpecies] = pokemon_encounters

    @staticmethod
    def loads(data: dict) -> PalParkArea:
        return PalParkArea(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names']),
            pokemon_encounters=PalParkEncounterSpecies.loads_list(data['pokemon_encounters'])
        )

    @property
    def encounters(self) -> list[PalParkEncounterSpecies]:
        """alias for pokemon_encounters attribute"""

        return getattr(self, 'pokemon_species')


class Region(BaseObject):

    __slots__ = (
        'id',
        'locations',
        'name',
        'names',
        'main_generation',
        'pokedexes',
        'version_groups'
    )

    def __init__(
        self,
        id: int,
        locations: list[NamedAPIResource['Location']],
        name: str,
        names: list[Name],
        main_generation: NamedAPIResource['Generation'],
        pokedexes: list[NamedAPIResource['Pokedex']],
        version_groups: list[NamedAPIResource['VersionGroup']],
    ) -> None:
        self.id: int = id
        self.locations: list[NamedAPIResource['Location']] = locations
        self.name: str = name
        self.names: list[Name] = names
        self.main_generation: NamedAPIResource['Generation'] = main_generation
        self.pokedexes: list[NamedAPIResource['Pokedex']] = pokedexes
        self.version_groups: list[NamedAPIResource['VersionGroup']] = version_groups

    @staticmethod
    def loads(data: dict) -> Region:
        return Region(
            id=data['id'],
            locations=NamedAPIResource.loads_list(data['locations']),
            name=data['name'],
            names=Name.loads_list(data['names']),
            main_generation=NamedAPIResource.loads(data['main_generation']),
            pokedexes=NamedAPIResource.loads_list(data['pokedexes']),
            version_groups=NamedAPIResource.loads_list(data['version_groups'])
        )

    @property
    def generation(self) -> NamedAPIResource['Generation']:
        """alias for main_generation attribute"""

        return getattr(self, 'main_generation')