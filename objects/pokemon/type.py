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
from objects.models import NamedAPIResource, Name, GenerationGameIndex

if TYPE_CHECKING:
    from objects import Generation, MoveDamageClass, Move
    from . import Pokemon


class TypeRelations(BaseObject):

    __slots__ = (
        'no_damage_to',
        'half_damage_to',
        'double_damage_to',
        'no_damage_from',
        'half_damage_from',
        'double_damage_from',
    )

    def __init__(
        self,
        no_damage_to: list[NamedAPIResource['Type']],
        half_damage_to: list[NamedAPIResource['Type']],
        double_damage_to: list[NamedAPIResource['Type']],
        no_damage_from: list[NamedAPIResource['Type']],
        half_damage_from: list[NamedAPIResource['Type']],
        double_damage_from: list[NamedAPIResource['Type']]
    ) -> None:
        self.no_damage_to: list[NamedAPIResource['Type']] = no_damage_to
        self.half_damage_to: list[NamedAPIResource['Type']] = half_damage_to
        self.double_damage_to: list[NamedAPIResource['Type']] = double_damage_to
        self.no_damage_from: list[NamedAPIResource['Type']] = no_damage_from
        self.half_damage_from: list[NamedAPIResource['Type']] = half_damage_from
        self.double_damage_from: list[NamedAPIResource['Type']] = double_damage_from

    @staticmethod
    def loads(data: dict) -> TypeRelations:
        return TypeRelations(**{attr: NamedAPIResource.loads_list(data[attr]) for attr in TypeRelations.__slots__})


class TypeRelationsPast(BaseObject):

    __slots__ = (
        'generation',
        'damage_relations'
    )

    def __init__(
        self,
        generation: NamedAPIResource['Generation'],
        damage_relations: TypeRelations
    ) -> None:
        self.generation: NamedAPIResource['Generation'] = generation
        self.damage_relations: TypeRelations = damage_relations

    @staticmethod
    def loads(data: dict) -> TypeRelationsPast:
        return TypeRelationsPast(
            generation=NamedAPIResource.loads(data['generation']),
            damage_relations=TypeRelations.loads(data['damage_relations'])
        )


class TypePokemon(BaseObject):

    __slots__ = (
        'slot',
        'pokemon'
    )

    def __init__(
        self,
        slot: int,
        pokemon: NamedAPIResource['Pokemon']
    ) -> None:
        self.slot: int = slot
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon

    @staticmethod
    def loads(data: dict) -> TypePokemon:
        return TypePokemon(
            slot=data['slot'],
            pokemon=NamedAPIResource.loads(data['pokemon'])
        )


class Type(BaseObject):

    __slots__ = (
        'id',
        'name',
        'damage_relations',
        'past_damage_relations',
        'game_indices',
        'generation',
        'move_damage_class',
        'names',
        'pokemon',
        'moves'
    )

    def __init__(
        self,
        id: int,
        name: str,
        damage_relations: TypeRelations,
        past_damage_relations: list[TypeRelationsPast],
        game_indices: list[GenerationGameIndex],
        generation: NamedAPIResource['Generation'],
        move_damage_class: NamedAPIResource['MoveDamageClass'],
        names: list[Name],
        pokemon: list[TypePokemon],
        moves: list[NamedAPIResource['Move']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.damage_relations: TypeRelations = damage_relations
        self.past_damage_relations: list[TypeRelationsPast] = past_damage_relations
        self.game_indices: list[GenerationGameIndex] = game_indices
        self.generation: NamedAPIResource['Generation'] = generation
        self.move_damage_class: NamedAPIResource['MoveDamageClass'] = move_damage_class
        self.names: list[Name] = names
        self.pokemon: list[TypePokemon] = pokemon
        self.moves: list[NamedAPIResource['Move']] = moves

    @staticmethod
    def loads(data: dict) -> Type:
        return Type(
            id=data['id'],
            name=data['name'],
            damage_relations=TypeRelations.loads(data['damage_relations']),
            past_damage_relations=TypeRelationsPast.loads_list(data['past_damage_relations']),
            game_indices=GenerationGameIndex.loads_list(data['game_indices']),
            generation=NamedAPIResource.loads(data['generation']),
            move_damage_class=NamedAPIResource.loads(data['move_damage_class']),
            names=Name.loads_list(data['names']),
            pokemon=TypePokemon.loads_list(data['pokemon']),
            moves=NamedAPIResource.loads_list(data['moves'])
        )
