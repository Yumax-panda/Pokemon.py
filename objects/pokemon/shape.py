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
    from . import PokemonSpecies
    from objects import Language


class AwesomeName(BaseObject):

    __slots__ = (
        'awesome_name',
        'language'
    )

    def __init__(
        self,
        awesome_name: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.awesome_name: str = awesome_name
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> AwesomeName:
        return AwesomeName(
            awesome_name=data['awesome_name'],
            language=NamedAPIResource.loads(data['language'])
        )

    @property
    def name(self) -> str:
        """alias for awesome_name attribute"""

        return getattr(self, 'awesome_name')


class PokemonShape(BaseObject):

    __slots__ = (
        'id',
        'name',
        'awesome_names',
        'names',
        'pokemon_species'
    )

    def __init__(
        self,
        id: int,
        name: str,
        awesome_names: list[AwesomeName],
        names: list[Name],
        pokemon_species: list[NamedAPIResource['PokemonSpecies']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.awesome_names: list[AwesomeName] = awesome_names
        self.names: list[Name] = names
        self.pokemon_species: list[NamedAPIResource['PokemonSpecies']] = pokemon_species

    @staticmethod
    def loads(data: dict) -> PokemonShape:
        return PokemonShape(
            id=data['id'],
            name=data['name'],
            awesome_names=AwesomeName.loads_list(data['awesome_names']),
            names=Name.loads_list(data['names']),
            pokemon_species=NamedAPIResource.loads_list(data['pokemon_species'])
        )

    @property
    def species(self) -> list[NamedAPIResource['PokemonSpecies']]:
        """alias for pokemon_species attribute"""

        return getattr(self, 'pokemon_species')