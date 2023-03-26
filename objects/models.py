"""
The MIT License (MIT)

Copyright (c) 2021-present beastmatser
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
from dataclasses import field
from typing import (
    TYPE_CHECKING,
    Optional,
    TypeVar,
    Generic,
    Callable,
    Coroutine,
    Union,
    Any
)
from .common import BaseObject

if TYPE_CHECKING:
    from api import Client
    from .encounter import EncounterConditionValue, EncounterMethod
    from .game import Version, Generation, VersionGroup
    from .machine import Machine
    from .language import Language


T = TypeVar('T', bound=BaseObject)
Param = Union[str, int]
Func = Callable[[Param], Coroutine[Any, Any, Union[T, list[T], None]]]
BuildMapPayload =  dict[str, Func]

class Url(BaseObject, Generic[T]):

    _client: Optional['Client'] = field(default=None, repr=False)

    def __init__(self, url: str) -> None:
        self.url: str = url

    @property
    def _endpoint(self) -> str:
        return self.url.split('/')[-3]

    @property
    def _id(self) -> str:
        return self.url.split('/')[-2]

    @property
    def client(self) -> Optional['Client']:
        return getattr(self, '_client', None)

    @classmethod
    def link(cls, client: 'Client') -> None:
        cls._client = client

    async def fetch(self, *, client: Optional['Client'] = None) -> T:
        client = self.client or client

        if client is None:
            raise ValueError("A client must be provided.")

        build_map: BuildMapPayload = {
            "ability": client.get_ability,
            "berry": client.get_berry,
            "berry-firmness": client.get_berry_firmness,
            "berry-flavor": client.get_berry_flavor,
            "characteristic": client.get_characteristic,
            "contest-effect": client.get_contest_effect,
            "contest-type": client.get_contest_type,
            "egg-group": client.get_egg_group,
            "encounter-condition": client.get_encounter_condition,
            "encounter-condition-value": client.get_encounter_condition_value,
            "encounter-method": client.get_encounter_method,
            "evolution-chain": client.get_evolution_chain,
            "evolution-trigger": client.get_evolution_trigger,
            "gender": client.get_gender,
            "generation": client.get_generation,
            "growth-rate": client.get_growth_rate,
            "item": client.get_item,
            "item-attribute": client.get_item_attribute,
            "item-category": client.get_item_category,
            "item-fling-effect": client.get_item_fling_effect,
            "item-pocket": client.get_item_pocket,
            "language": client.get_language,
            "location": client.get_location,
            "location-area": client.get_location_area,
            "machine": client.get_machine,
            "move": client.get_move,
            "move-ailment": client.get_move_ailment,
            "move-battle-style": client.get_move_battle_style,
            "move-category": client.get_move_category,
            "move-damage-class": client.get_move_damage_class,
            "move-learn-method": client.get_move_learn_method,
            "move-target": client.get_move_target,
            "nature": client.get_nature,
            "pal-park-area": client.get_pal_park_area,
            "pokeathlon-stat": client.get_pokeathlon_stat,
            "pokedex": client.get_pokedex,
            "pokemon": client.get_pokemon,
            "pokemon-color": client.get_pokemon_color,
            "pokemon-form": client.get_pokemon_form,
            "pokemon-habitat": client.get_pokemon_habitat,
            "pokemon-shape": client.get_pokemon_shape,
            "pokemon-species": client.get_pokemon_species,
            "region": client.get_region,
            "stat": client.get_stat,
            "super-contest-effect": client.get_super_contest_effect,
            "type": client.get_type,
            "version": client.get_version,
            "version-group": client.get_version_group,
        }

        obj: T = await build_map[self._endpoint](self._id)

        return obj

    @staticmethod
    def loads(data: dict) -> Url:
        return Url(data['url'])

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()

    def __str__(self) -> str:
        return f'<{self.__class__.__name__}>: {str(self.to_dict())}'


class APIResource(Url[T]):

    def __init__(self, url: str) -> None:
        super().__init__(url=url)

    @staticmethod
    def loads(data: dict) -> APIResource:
        return APIResource(data['url'])


class NamedAPIResource(Url[T]):

    def __init__(
        self,
        name: str,
        url: str
    ) -> None:
        super().__init__(url=url)
        self.name: str = name

    @staticmethod
    def loads(data: dict) -> NamedAPIResource:
        return NamedAPIResource(
            name=data['name'],
            url=data['url']
        )


class Description(BaseObject):

    __slots__ = (
        'description',
        'language'
    )

    def __init__(
        self,
        description: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.description: str = description
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> Description:
        return Description(
            description=data['description'],
            language=NamedAPIResource.loads(data['language'])
        )


class Effect(BaseObject):

    __slots__ = (
        'effect',
        'language'
    )

    def __init__(
        self,
        effect: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.effect: str = effect
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> Effect:
        return Effect(
            effect=data['effect'],
            language=NamedAPIResource.loads(data['language'])
        )


class Encounter(BaseObject):

    __slots__ = (
        'min_level',
        'max_level',
        'condition_values',
        'chance',
        'method'
    )

    def __init__(
        self,
        min_level: int,
        max_level: int,
        condition_values: list[NamedAPIResource['EncounterConditionValue']],
        method: NamedAPIResource['EncounterMethod']
    ) -> None:
        self.min_level: int = min_level
        self.max_level: int = max_level
        self.condition_values: list[NamedAPIResource['EncounterConditionValue']] = condition_values
        self.method: NamedAPIResource['EncounterMethod'] = method

    @staticmethod
    def loads(data: dict) -> Encounter:
        return Encounter(
            min_level=data['min_level'],
            max_level=data['max_level'],
            condition_values= NamedAPIResource.loads_list(data['condition_values']),
            method=NamedAPIResource.loads(data['method'])
        )


class PartialFlavorText(BaseObject):

    __slots__ = (
        'flavor_text',
        'language'
    )

    def __init__(
        self,
        flavor_text: str,
        language: NamedAPIResource['Language'],
    ) -> None:
        self.flavor_text: str = flavor_text
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> PartialFlavorText:
        return PartialFlavorText(
            flavor_text=data['flavor_text'],
            language=NamedAPIResource.loads(data['language']),
        )


class FlavorText(BaseObject):

    __slots__ = (
        'flavor_text',
        'language',
        'version'
    )

    def __init__(
        self,
        flavor_text: str,
        language: NamedAPIResource['Language'],
        version: NamedAPIResource['Version']
    ) -> None:
        self.flavor_text: str = flavor_text
        self.language: NamedAPIResource['Language'] = language
        self.version: NamedAPIResource['Version'] = version

    @staticmethod
    def loads(data: dict) -> FlavorText:
        return FlavorText(
            flavor_text=data['flavor_text'],
            language=NamedAPIResource.loads(data['language']),
            version=NamedAPIResource.loads(data['version'])
        )


class GenerationGameIndex(BaseObject):

    __slots__ = (
        'game_index',
        'generation'
    )

    def __init__(
        self,
        game_index: int,
        generation: NamedAPIResource['Generation']
    ) -> None:
        self.game_index: int = game_index
        self.generation: NamedAPIResource['Generation'] = generation

    @staticmethod
    def loads(data: dict) -> GenerationGameIndex:
        return GenerationGameIndex(
            game_index=data['game_index'],
            generation=NamedAPIResource.loads(data['generation'])
        )


class MachineVersionDetail(BaseObject):

    __slots__ = (
        'machine',
        'version_group'
    )

    def __init__(
        self,
        machine: APIResource['Machine'],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.machine: APIResource['Machine'] = machine
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> MachineVersionDetail:
        return MachineVersionDetail(
            machine=APIResource.loads(data['machine']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )


class Name(BaseObject):

    __slots__ = (
        'name',
        'language'
    )

    def __init__(
        self,
        name: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.name: str = name
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> Name:
        return Name(
            name=data['name'],
            language=NamedAPIResource.loads(data['language'])
        )


class VerboseEffect(BaseObject):

    __slots__ = (
        'effect',
        'short_effect',
        'language'
    )

    def __init__(
        self,
        effect: str,
        short_effect: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.effect: str = effect
        self.short_effect: str = short_effect,
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> VerboseEffect:
        return VerboseEffect(
            effect=data['effect'],
            short_effect=data['short_effect'],
            language=NamedAPIResource.loads(data['language'])
        )


class VersionEncounterDetail(BaseObject):

    __slots__ = (
        'version',
        'max_chance',
        'encounter_details'
    )

    def __init__(
        self,
        version: NamedAPIResource['Version'],
        max_chance: int,
        encounter_details: list[Encounter]
    ) -> None:
        self.version: NamedAPIResource['Version'] = version
        self.max_chance: int = max_chance
        self.encounter_details: list[Encounter] = encounter_details

    @staticmethod
    def loads(data: dict) -> VersionEncounterDetail:
        return VersionEncounterDetail(
            version=NamedAPIResource.loads(data['version']),
            max_chance=data['max_chance'],
            encounter_details=Encounter.loads_list(data['encounter_details'])
        )


class VersionGameIndex(BaseObject):

    __slots__ = (
        'game_index',
        'version'
    )

    def __init__(
        self,
        game_index: int,
        version: NamedAPIResource['Version']
    ) -> None:
        self.game_index: int = game_index
        self.version: NamedAPIResource['Version'] = version

    @staticmethod
    def loads(data: dict) -> VersionGameIndex:
        return VersionGameIndex(
            game_index=data['game_index'],
            version=NamedAPIResource.loads(data['version'])
        )


class VersionGroupFlavorText(BaseObject):

    __slots__ = (
        'text',
        'language',
        'version_group'
    )

    def __init__(
        self,
        text: str,
        language: NamedAPIResource['Language'],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.text: str = text
        self.language: NamedAPIResource['Language'] = language
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> VersionGroupFlavorText:
        return VersionGroupFlavorText(
            text=data['text'],
            language=NamedAPIResource.loads(data['language']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )
