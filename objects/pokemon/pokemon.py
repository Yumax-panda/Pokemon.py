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
from objects.models import NamedAPIResource, VersionGameIndex

if TYPE_CHECKING:
    from . import (
        Ability,
        PokemonForm,
        PokemonSpecies,
        Stat
    )
    from . import Type as PokemonTypePayload

    from objects import (
        Generation,
        Item,
        Version,
        Move,
        MoveLearnMethod,
        VersionGroup
    )


class PokemonSprites(BaseObject):

    __slots__ = (
        'front_default',
        'front_shiny',
        'front_female',
        'front_shiny_female',
        'back_default',
        'back_shiny',
        'back_female',
        'back_shiny_female'
    )

    def __init__(
        self,
        front_default: str,
        front_shiny: str,
        front_female: str,
        front_shiny_female: str,
        back_default: str,
        back_shiny: str,
        back_female: str,
        back_shiny_female: str
    ) -> None:
        self.front_default: str = front_default
        self.front_shiny: str = front_shiny
        self.front_female: str = front_female
        self.front_shiny_female: str = front_shiny_female
        self.back_default: str = back_default
        self.back_shiny: str = back_shiny
        self.back_female: str = back_female
        self.back_shiny_female: str = back_shiny_female


class PokemonStat(BaseObject):

    __slots__ = (
        'stat',
        'effort',
        'base_stat'
    )

    def __init__(
        self,
        stat: NamedAPIResource['Stat'],
        effort: int,
        base_stat: int
    ) -> None:
        self.stat: NamedAPIResource['Stat'] = stat
        self.effort: int = effort
        self.base_stat: int = base_stat

    @staticmethod
    def loads(data: dict) -> PokemonStat:
        return PokemonStat(
            stat=NamedAPIResource.loads(data['stat']),
            effort=data['effort'],
            base_stat=data['base_stat']
        )


class PokemonMoveVersion(BaseObject):

    __slots__ = (
        'move_learn_method',
        'version_group',
        'level_learned_at'
    )

    def __init__(
        self,
        move_learn_method: NamedAPIResource['MoveLearnMethod'],
        version_group: NamedAPIResource['VersionGroup'],
        level_learned_at: int
    ) -> None:
        self.move_learn_method: NamedAPIResource['MoveLearnMethod'] = move_learn_method
        self.version_group: NamedAPIResource['VersionGroup'] = version_group
        self.level_learned_at: int = level_learned_at

    @staticmethod
    def loads(data: dict) -> PokemonMoveVersion:
        return PokemonMoveVersion(
            move_learn_method=NamedAPIResource.loads(data['move_learn_method']),
            version_group=NamedAPIResource.loads(data['version_group']),
            level_learned_at=data['level_learned_at']
        )


class PokemonMove(BaseObject):

    __slots__ = (
        'move',
        'version_group_details'
    )

    def __init__(
        self,
        move: NamedAPIResource['Move'],
        version_group_details: list[PokemonMoveVersion]
    ) -> None:
        self.move: NamedAPIResource['Move'] = move
        self.version_group_details: list[PokemonMoveVersion] = version_group_details

    @staticmethod
    def loads(data: dict) -> PokemonMove:
        return PokemonMove(
            move=NamedAPIResource.loads(data['move']),
            version_group_details=PokemonMoveVersion.loads_list(data['version_group_details'])
        )

    @property
    def versions(self) -> list[PokemonMoveVersion]:
        """alias for version_group_details attribute"""

        return getattr(self, 'version_group_details')


class PokemonHeldItemVersion(BaseObject):

    __slots__ = (
        'version',
        'rarity'
    )

    def __init__(
        self,
        version: NamedAPIResource['Version'],
        rarity: int
    ) -> None:
        self.version: NamedAPIResource['Version'] = version
        self.rarity: int = rarity

    @staticmethod
    def loads(data: dict) -> PokemonHeldItemVersion:
        return PokemonHeldItemVersion(
            version=NamedAPIResource.loads(data['version']),
            rarity=data['rarity']
        )


class PokemonHeldItem(BaseObject):

    __slots__ = (
        'item',
        'version_details'
    )

    def __init__(
        self,
        item: NamedAPIResource['Item'],
        version_details: list[PokemonHeldItemVersion]
    ) -> None:
        self.item: NamedAPIResource['Item'] = item
        self.version_details: list[PokemonHeldItemVersion] = version_details

    @staticmethod
    def loads(data: dict) -> PokemonHeldItem:
        return PokemonHeldItem(
            item=NamedAPIResource.loads(data['item']),
            version_details=PokemonHeldItemVersion.loads_list(data['version_details'])
        )


class PokemonType(BaseObject):

    __slots__ = (
        'slot',
        'type'
    )

    def __init__(
        self,
        slot: int,
        type: NamedAPIResource['PokemonTypePayload']
    ) -> None:
        self.slot: int = slot
        self.type: NamedAPIResource['PokemonTypePayload'] = type

    @staticmethod
    def loads(data: dict) -> PokemonType:
        return PokemonType(
            slot=data['slot'],
            type=NamedAPIResource.loads(data['type'])
        )


class PokemonFormType(BaseObject):

    __slots__ = (
        'slot',
        'type'
    )

    def __init__(
        self,
        slot: int,
        type: NamedAPIResource['PokemonTypePayload']
    ) -> None:
        self.slot: int = slot
        self.type: NamedAPIResource['PokemonTypePayload'] = type

    @staticmethod
    def loads(data: dict) -> PokemonFormType:
        return PokemonFormType(
            slot=data['slot'],
            type=NamedAPIResource.loads(data['type'])
        )


class PokemonTypePast(BaseObject):

    __slots__ = (
        'generation',
        'types'
    )

    def __init__(
        self,
        generation: NamedAPIResource['Generation'],
        types: list[PokemonType]
    ) -> None:
        self.generation: NamedAPIResource['Generation'] = generation
        self.types: list[PokemonType] = types

    @staticmethod
    def loads(data: dict) -> PokemonTypePast:
        return PokemonTypePast(
            generation=NamedAPIResource.loads(data['generation']),
            types=PokemonType.loads_list(data['types'])
        )


class PokemonAbility(BaseObject):

    __slots__ = (
        'is_hidden',
        'slot',
        'ability'
    )

    def __init__(
        self,
        is_hidden: bool,
        slot: int,
        ability: NamedAPIResource['Ability']
    ) -> None:
        self.is_hidden: bool = is_hidden
        self.slot: int = slot
        self.ability: NamedAPIResource['Ability'] = ability

    @staticmethod
    def loads(data: dict) -> PokemonAbility:
        return PokemonAbility(
            is_hidden=data['is_hidden'],
            slot=data['slot'],
            ability=NamedAPIResource.loads(data['ability'])
        )


class Pokemon(BaseObject):

    __slots__ = (
        'id',
        'name',
        'base_experience',
        'height',
        'is_default',
        'order',
        'weight',
        'abilities',
        'forms',
        'game_indices',
        'held_items',
        'location_area_encounters',
        'moves',
        'past_types',
        'sprites',
        'species',
        'stats',
        'types'
    )

    def __init__(
        self,
        id: int,
        name: str,
        base_experience: int,
        height: int,
        is_default: bool,
        order: int,
        weight: int,
        abilities: list[PokemonAbility],
        forms: list[NamedAPIResource['PokemonForm']],
        game_indices: list[VersionGameIndex],
        held_items: list[PokemonHeldItem],
        location_area_encounters: str,
        moves: list[PokemonMove],
        past_types: list[PokemonTypePast],
        sprites: PokemonSprites,
        species: NamedAPIResource['PokemonSpecies'],
        stats: list[PokemonStat],
        types: list[PokemonType]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.base_experience: int = base_experience
        self.height: int = height
        self.is_default: bool = is_default
        self.order: int = order
        self.weight: int = weight
        self.abilities: list[PokemonAbility] = abilities
        self.forms: list[NamedAPIResource['PokemonForm']] = forms
        self.game_indices: list[VersionGameIndex] = game_indices
        self.held_items: list[PokemonHeldItem] = held_items
        self.location_area_encounters: str = location_area_encounters
        self.moves: list[PokemonMove] = moves
        self.past_types: list[PokemonTypePast] = past_types
        self.sprites: PokemonSprites = sprites
        self.species: NamedAPIResource['PokemonSpecies'] = species
        self.stats: list[PokemonStat] = stats
        self.types: list[PokemonType] = types

    @staticmethod
    def loads(data: dict) -> Pokemon:
        return Pokemon(
            id=data['id'],
            name=data['name'],
            base_experience=data['base_experience'],
            height=data['height'],
            is_default=data['is_default'],
            order=data['order'],
            weight=data['weight'],
            abilities=PokemonAbility.loads_list(data['abilities']),
            forms=NamedAPIResource.loads_list(data['forms']),
            game_indices=VersionGameIndex.loads_list(data['game_indices']),
            held_items=PokemonHeldItem.loads_list(data['held_items']),
            location_area_encounters=data['location_area_encounters'],
            moves=PokemonMove.loads_list(data['moves']),
            past_types=PokemonTypePast.loads_list(data['past_types']),
            sprites=PokemonSprites.loads(data['sprites']),
            species=NamedAPIResource.loads(data['species']),
            stats=PokemonStat.loads_list(data['stats']),
            types=PokemonType.loads_list(data['types'])
        )