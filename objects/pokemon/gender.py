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
from objects.models import NamedAPIResource

if TYPE_CHECKING:
    from . import PokemonSpecies


class PokemonSpeciesGender(BaseObject):

    __slots__ = (
        'rate',
        'pokemon_species'
    )

    def __init__(
        self,
        rate: int,
        pokemon_species: NamedAPIResource['PokemonSpecies']
    ) -> None:
        self.rate: int = rate
        self.pokemon_species: NamedAPIResource['PokemonSpecies'] = pokemon_species

    @staticmethod
    def loads(data: dict) -> PokemonSpeciesGender:
        return PokemonSpeciesGender(
            rate=data['rate'],
            pokemon_species=NamedAPIResource.loads(data['pokemon_species'])
        )

    @property
    def species(self) -> NamedAPIResource['PokemonSpecies']:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')


class Gender(BaseObject):

    __slots__ = (
        'id',
        'name',
        'pokemon_species_details',
        'required_for_evolution'
    )

    def __init__(
        self,
        id: int,
        name: str,
        pokemon_species_details: list[PokemonSpeciesGender],
        required_for_evolution: list[NamedAPIResource['PokemonSpecies']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.pokemon_species_details: list[PokemonSpeciesGender] = pokemon_species_details,
        self.required_for_evolution: list[NamedAPIResource['PokemonSpecies']] = required_for_evolution

    @staticmethod
    def loads(data: dict) -> Gender:
        return Gender(
            id=data['id'],
            name=data['name'],
            pokemon_species_details=PokemonSpeciesGender.loads_list(data['pokemon_species_details']),
            required_for_evolution=NamedAPIResource.loads_list(data['required_for_evolution'])
        )

    @property
    def details(self) -> list[PokemonSpeciesGender]:
        """alias for pokemon_species_details attribute"""

        return getattr(self, 'pokemon_species_details')


    @property
    def evolutions(self) -> list[NamedAPIResource['PokemonSpecies']]:
        """alias for required_for_evolution attribute"""

        return getattr(self, 'required_for_evolution')
