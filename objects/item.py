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
from .models import (
    NamedAPIResource,
    Name,
    VerboseEffect,
    VersionGroupFlavorText,
    GenerationGameIndex,
    APIResource,
    MachineVersionDetail,
    Description,
    Effect
)

if TYPE_CHECKING:
    from .evolution import EvolutionChain
    from .game import Version
    from .pokemon.pokemon import Pokemon


class ItemHolderPokemonVersionDetail(BaseObject):

    __slots__ = (
        'rarity',
        'version'
    )

    def __init__(
        self,
        rarity: int,
        version: NamedAPIResource['Version']
    ) -> None:
        self.rarity: int = rarity
        self.version: NamedAPIResource['Version'] = version

    @staticmethod
    def loads(data: dict) -> ItemHolderPokemonVersionDetail:
        return ItemHolderPokemonVersionDetail(
            rarity=data['rarity'],
            version=NamedAPIResource.loads(data['version'])
        )


class ItemHolderPokemon(BaseObject):

    __slots__ = (
        'pokemon',
        'version_details'
    )

    def __init__(
        self,
        pokemon: NamedAPIResource['Pokemon'],
        version_details: list[ItemHolderPokemonVersionDetail]
    ) -> None:
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon
        self.version_details: list[ItemHolderPokemonVersionDetail] = version_details

    @staticmethod
    def loads(data: dict) -> ItemHolderPokemon:
        return ItemHolderPokemon(
            pokemon=NamedAPIResource.loads(data['pokemon']),
            version_details=ItemHolderPokemonVersionDetail.loads_list(data['version_details'])
        )

    @property
    def details(self) -> list[ItemHolderPokemonVersionDetail]:
        """alias for version_details attribute"""

        return getattr(self, 'version_details')


class ItemSprites(BaseObject):

    __slots__ = ('default')

    def __init__(
        self,
        default: Optional[str] = None,
    ) -> None:
        self.default: Optional[str] = default

    @staticmethod
    def loads(data: dict) -> ItemSprites:
        return ItemSprites(data.get('default'))


class Item(BaseObject):

    __slots__ = (
        'id',
        'name',
        'cost',
        'fling_power',
        'fling_effect',
        'attributes',
        'category',
        'effect_entries',
        'flavor_text_entries',
        'game_indices',
        'names',
        'sprites',
        'held_by_pokemon',
        'baby_trigger_for',
        'machines'
    )

    def __init__(
        self,
        id: int,
        name: str,
        cost: int,
        attributes: list[NamedAPIResource['ItemAttribute']],
        category: NamedAPIResource['ItemCategory'],
        effect_entries: list[VerboseEffect],
        flavor_text_entries: list[VersionGroupFlavorText],
        game_indices: list[GenerationGameIndex],
        names: list[Name],
        held_by_pokemon: list[ItemHolderPokemon],
        machines: list[MachineVersionDetail],
        fling_power: Optional[int] = None,
        fling_effect: Optional[NamedAPIResource['ItemFlingEffect']] = None,
        sprites: Optional[ItemSprites] = None,
        baby_trigger_for: Optional[APIResource['EvolutionChain']] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.cost: int = cost
        self.attributes: list[NamedAPIResource['ItemAttribute']] = attributes
        self.category: NamedAPIResource['ItemCategory'] = category
        self.effect_entries: list[VerboseEffect] = effect_entries
        self.flavor_text_entries: list[VersionGroupFlavorText] = flavor_text_entries
        self.game_indices: list[GenerationGameIndex] = game_indices
        self.names: list[Name] = names
        self.held_by_pokemon: list[ItemHolderPokemon] = held_by_pokemon
        self.machines: list[MachineVersionDetail] = machines
        self.fling_power: Optional[int] = fling_power
        self.fling_effect: Optional[NamedAPIResource['ItemFlingEffect']] = fling_effect
        self.sprites: Optional[ItemSprites] = sprites
        self.baby_trigger_for: Optional[APIResource['EvolutionChain']] = baby_trigger_for

    @staticmethod
    def loads(data: dict) -> Item:
        item = Item(
            id=data['id'],
            name=data['name'],
            cost=data['cost'],
            attributes=NamedAPIResource.loads_list(data['attributes']),
            category=NamedAPIResource.loads(data['category']),
            effect_entries=VerboseEffect.loads_list(data['effect_entries']),
            flavor_text_entries=VersionGroupFlavorText.loads_list(data['flavor_text_entries']),
            game_indices=GenerationGameIndex.loads_list(data['game_indices']),
            names=Name.loads_list(data['names']),
            held_by_pokemon=ItemHolderPokemon.loads_list(data['held_by_pokemon']),
            machines=MachineVersionDetail.loads_list(data['machines']),
            fling_power=data.get('fling_power')
        )

        for attr, cls in zip(
            ('fling_effect', 'sprites', 'baby_trigger_for'),
            (NamedAPIResource, ItemSprites, APIResource)
        ):
            if (var := data.get(attr)) is not None:
                setattr(item, attr, cls.loads(var))

        return item


class ItemAttribute(BaseObject):

    __slots__ = (
        'id',
        'name',
        'items',
        'names',
        'descriptions'
    )

    def __init__(
        self,
        id: int,
        name: str,
        items: list[NamedAPIResource['Item']],
        names: list[Name],
        descriptions: list[Description]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.items: list[NamedAPIResource['Item']] = items
        self.names: list[Name] = names
        self.descriptions: list[Description] = descriptions

    @staticmethod
    def loads(data: dict) -> ItemAttribute:
        return ItemAttribute(
            id=data['id'],
            name=data['name'],
            items=NamedAPIResource.loads_list(data['items']),
            names=Name.loads_list(data['names']),
            descriptions=Description.loads_list(data['descriptions'])
        )


class ItemCategory(BaseObject):

    __slots__ = (
        'id',
        'name',
        'items',
        'names',
        'pocket'
    )

    def __init__(
        self,
        id: int,
        name: str,
        items: list[NamedAPIResource['Item']],
        names: list[Name],
        pocket: NamedAPIResource['ItemPocket']
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.items: list[NamedAPIResource['Item']] = items
        self.names: list[Name] = names
        self.pocket: NamedAPIResource['ItemPocket'] = pocket

    @staticmethod
    def loads(data: dict) -> ItemCategory:
        return ItemCategory(
            id=data['id'],
            name=data['name'],
            items=NamedAPIResource.loads_list(data['items']),
            names=Name.loads_list(data['names']),
            pocket=NamedAPIResource.loads(data['pocket'])
        )


class ItemFlingEffect(BaseObject):

    __slots__ = (
        'id',
        'name',
        'effect_entries',
        'items'
    )

    def __init__(
        self,
        id: int,
        name: str,
        effect_entries: list[Effect],
        items: list[NamedAPIResource['Item']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.effect_entries: list[Effect] = effect_entries
        self.items: list[NamedAPIResource['Item']] = items

    @staticmethod
    def loads(data: dict) -> ItemFlingEffect:
        return ItemFlingEffect(
            id=data['id'],
            name=data['name'],
            effect_entries=Effect.loads_list(data['effect_entries']),
            items=NamedAPIResource.loads_list(data['items'])
        )

    @property
    def effects(self) -> list[Effect]:
        """alias for effect_entries attribute"""

        return getattr(self, 'effect_entries')


class ItemPocket(BaseObject):

    __slots__ = (
        'id',
        'name',
        'categories',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        categories: list[NamedAPIResource['ItemCategory']],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.categories: list[NamedAPIResource['ItemCategory']] = categories
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> ItemPocket:
        return ItemPocket(
            id=data['id'],
            name=data['name'],
            categories=NamedAPIResource.loads_list(data['categories']),
            names=Name.loads_list(data['names'])
        )