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
from objects.pokemon.pokemon import PokemonFormType

if TYPE_CHECKING:
    from . import Pokemon
    from objects import VersionGroup


class PokemonFormSprites(BaseObject):

    __slots__ = (
        'front_default',
        'front_shiny',
        'back_default',
        'back_shiny',
    )

    def __init__(
        self,
        front_default: str,
        front_shiny: str,
        back_default: str,
        back_shiny: str
    ) -> None:
        self.front_default: str = front_default
        self.front_shiny: str = front_shiny
        self.back_default: str = back_default
        self.back_shiny: str = back_shiny


class PokemonForm(BaseObject):

    __slots__ = (
        'id',
        'name',
        'order',
        'form_order',
        'is_default',
        'is_battle_only',
        'is_mega',
        'form_name',
        'pokemon',
        'types',
        'sprites',
        'version_group',
        'names',
        'form_names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        order: int,
        form_order: int,
        is_default: bool,
        is_battle_only: bool,
        is_mega: bool,
        form_name: str,
        pokemon: NamedAPIResource['Pokemon'],
        types: list[PokemonFormType],
        sprites: PokemonFormSprites,
        version_group: NamedAPIResource['VersionGroup'],
        names: list[Name],
        form_names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.order: int = order
        self.form_order: int = form_order
        self.is_default: bool = is_default
        self.is_battle_only: bool = is_battle_only
        self.is_mega: bool = is_mega
        self.form_name: str = form_name
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon
        self.types: list[PokemonFormType] = types
        self.sprites: PokemonFormSprites = sprites
        self.version_group: NamedAPIResource['VersionGroup'] = version_group
        self.names: list[Name] = names
        self.form_names: list[Name] = form_names

    @staticmethod
    def loads(data: dict) -> PokemonForm:
        return PokemonForm(
            id=data['id'],
            name=data['name'],
            order=data['order'],
            form_order=data['form_order'],
            is_default=data['is_default'],
            is_battle_only=data['is_battle_only'],
            is_mega=data['is_mega'],
            form_name=data['form_name'],
            pokemon=NamedAPIResource.loads(data['pokemon']),
            types=PokemonFormType.loads_list(data['types']),
            sprites=PokemonFormSprites.loads(data['sprites']),
            version_group=NamedAPIResource.loads(data['version_group']),
            names=Name.loads_list(data['names']),
            form_names=Name.loads_list(data['form_names'])
        )