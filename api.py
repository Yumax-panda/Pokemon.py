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
from typing import Optional, Final, Any, Type, TypeVar, Union
import aiohttp

from objects import (
    BaseObject,
    Berry,
    BerryFirmness,
    BerryFlavor,
    ContestType,
    ContestEffect,
    SuperContestEffect,
    EncounterMethod,
    EncounterCondition,
    EncounterConditionValue,
    EvolutionChain,
    EvolutionTrigger,
    Generation,
    Pokedex,
    Version,
    VersionGroup,
    Item,
    ItemAttribute,
    ItemCategory,
    ItemFlingEffect,
    ItemPocket,
    Location,
    LocationArea,
    PalParkArea,
    Region,
    Machine,
    Move,
    MoveAilment,
    MoveBattleStyle,
    MoveCategory,
    MoveDamageClass,
    MoveLearnMethod,
    MoveTarget,
    Language,
    Url
)

from objects.pokemon import (
    Ability,
    Characteristic,
    EggGroup,
    Gender,
    GrowthRate,
    Nature,
    PokeathlonStat,
    Pokemon,
    LocationAreaEncounter,
    PokemonColor,
    PokemonForm,
    PokemonHabitat,
    PokemonShape,
    PokemonSpecies,
    Stat
)
from objects.pokemon import Type as PokemonTypePayload
from cache import Cache, cached_resource


BASE_URL: Final[str] = 'https://pokeapi.co/api/v2'

Param = Union[str, int]
JsonResponse = Union[list, dict[str, Any]]
T = TypeVar('T', bound=BaseObject)


class HttpClient:

    def __init__(
        self,
        *,
        session: Optional[aiohttp.ClientSession]
    ) -> None:
        self._session = session or aiohttp.ClientSession()
        self.inexistent_endpoints: list[str] = []

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()

    async def get(self, endpoint: str) -> Optional[JsonResponse]:
        async with self._session.get(f'{BASE_URL}/{endpoint}') as response:
            if endpoint in self.inexistent_endpoints:
                return None
            if response.status != 200:
                self.inexistent_endpoints.append(endpoint)
                return None
            else:
                return await response.json()

class Client:

    http: HttpClient
    _cache: Cache

    def __init__(
        self,
        *,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        self.http: HttpClient = HttpClient(session=session)
        self._cache: Cache = Cache()
        Url.link(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self.http.close()

    async def _fetch(self, url: str, cls: Type[T]) -> Union[T, list[T], None]:
        """fetch response from Poke API and change JSONResponse into each classes

        Parameters
        ----------
        url: :class:`str`
            The API's endpoint url
        cls: :class:`Type[T]`
            class after changing

        Returns
        -------
        :class:`T | list[T] | None`
            the same type as argument `cls`
        """

        if (data := await self.http.get(url)) is None:
            return None

        if isinstance(data, list):
            return cls.loads_list(data)
        else:
            return cls.loads(data)


    """Berries (Group)"""
    @cached_resource(endpoint='berry')
    async def get_berry(self, id_or_name: Param) -> Optional[Berry]:
        return await self._fetch(f'berry/{id_or_name}', Berry)

    @cached_resource(endpoint='berry-firmness')
    async def get_berry_firmness(self, id_or_name: Param) -> Optional[BerryFirmness]:
        return await self._fetch(f'berry-firmness/{id_or_name}', BerryFirmness)

    @cached_resource(endpoint='berry-flavor')
    async def get_berry_flavor(self, id_or_name: Param) -> Optional[BerryFlavor]:
        return await self._fetch(f'berry-flavor/{id_or_name}', BerryFlavor)


    """Contests (Group)"""
    @cached_resource(endpoint='contest-type')
    async def get_contest_type(self, id_or_name: Param) -> Optional[ContestType]:
        return await self._fetch(f'contest-type/{id_or_name}', ContestType)

    @cached_resource(endpoint='contest-effect')
    async def get_contest_effect(self, id_or_name: Param) -> Optional[ContestEffect]:
        return await self._fetch(f'contest-effect/{id_or_name}', ContestEffect)

    @cached_resource(endpoint='super-contest-effect')
    async def get_super_contest_effect(self, id: Param) -> Optional[SuperContestEffect]:
        return await self._fetch(f'super-contest-effect/{id}', SuperContestEffect)


    """Encounters (Group)"""
    @cached_resource(endpoint='encounter-method')
    async def get_encounter_method(self, id_or_name: Param) -> Optional[EncounterMethod]:
        return await self._fetch(f'encounter-method/{id_or_name}', EncounterMethod)

    @cached_resource(endpoint='encounter-condition')
    async def get_encounter_condition(self, id_or_name: Param) -> Optional[EncounterCondition]:
        return await self._fetch(f'encounter-condition/{id_or_name}', EncounterCondition)

    @cached_resource(endpoint='encounter-condition-value')
    async def get_encounter_condition_value(self, id_or_name: Param) -> Optional[EncounterConditionValue]:
        return await self._fetch(f'encounter-condition-value/{id_or_name}', EncounterConditionValue)


    """Evolution (Group)"""
    @cached_resource(endpoint='evolution-chain')
    async def get_evolution_chain(self, id: Param) -> Optional[EvolutionChain]:
        return await self._fetch(f'evolution-chain/{id}', EvolutionChain)

    @cached_resource(endpoint='evolution-trigger')
    async def get_evolution_trigger(self, id_or_name: Param) -> Optional[EvolutionTrigger]:
        return await self._fetch(f'evolution-trigger/{id_or_name}', EvolutionTrigger)


    """Games (Group)"""
    @cached_resource(endpoint='generation')
    async def get_generation(self, id_or_name: Param) -> Optional[Generation]:
        return await self._fetch(f'generation/{id_or_name}', Generation)

    @cached_resource(endpoint='pokedex')
    async def get_pokedex(self, id_or_name: Param) -> Optional[Pokedex]:
        return await self._fetch(f'pokedex/{id_or_name}', Pokedex)

    @cached_resource(endpoint='version')
    async def get_version(self, id_or_name: Param) -> Optional[Version]:
        return await self._fetch(f'version/{id_or_name}', Version)

    @cached_resource(endpoint='version-group')
    async def get_version_group(self, id_or_name: Param) -> Optional[VersionGroup]:
        return await self._fetch(f'version-group/{id_or_name}', VersionGroup)


    """Items (Group)"""
    @cached_resource(endpoint='item')
    async def get_item(self, id_or_name: Param) -> Optional[Item]:
        return await self._fetch(f'item/{id_or_name}', Item)

    @cached_resource(endpoint='item-attribute')
    async def get_item_attribute(self, id_or_name: Param) -> Optional[ItemAttribute]:
        return await self._fetch(f'item-attribute/{id_or_name}', ItemAttribute)

    @cached_resource(endpoint='item-category')
    async def get_item_category(self, id_or_name: Param) -> Optional[ItemCategory]:
        return await self._fetch(f'item-category/{id_or_name}', ItemCategory)

    @cached_resource(endpoint='item-fling-effect')
    async def get_item_fling_effect(self, id_or_name: Param) -> Optional[ItemFlingEffect]:
        return await self._fetch(f'item-fling-effect/{id_or_name}', ItemFlingEffect)

    @cached_resource(endpoint='item-pocket')
    async def get_item_pocket(self, id_or_name: Param) -> Optional[ItemPocket]:
        return await self._fetch(f'item-pocket/{id_or_name}', ItemPocket)


    """Locations (Group)"""
    @cached_resource(endpoint='location')
    async def get_location(self, id_or_name: Param) -> Optional[Location]:
        return await self._fetch(f'location/{id_or_name}', Location)

    @cached_resource(endpoint='location-area')
    async def get_location_area(self, id_or_name: Param) -> Optional[LocationArea]:
        return await self._fetch(f'location-area/{id_or_name}', LocationArea)

    @cached_resource(endpoint='pal-park-area')
    async def get_pal_park_area(self, id_or_name: Param) -> Optional[PalParkArea]:
        return await self._fetch(f'pal-park-area/{id_or_name}', PalParkArea)

    @cached_resource(endpoint='region')
    async def get_region(self, id_or_name: Param) -> Optional[Region]:
        return await self._fetch(f'region/{id_or_name}', Region)


    """Machines (Group)"""
    @cached_resource(endpoint='machine')
    async def get_machine(self, id: Param) -> Optional[Machine]:
        return await self._fetch(f'machine/{id}', Machine)


    """Moves (Group)"""
    @cached_resource(endpoint='move')
    async def get_move(self, id_or_name: Param) -> Optional[Move]:
        return await self._fetch(f'move/{id_or_name}', Move)

    @cached_resource(endpoint='move-ailment')
    async def get_move_ailment(self, id_or_name: Param) -> Optional[MoveAilment]:
        return await self._fetch(f'move-ailment/{id_or_name}', MoveAilment)

    @cached_resource(endpoint='move-battle-style')
    async def get_move_battle_style(self, id_or_name: Param) -> Optional[MoveBattleStyle]:
        return await self._fetch(f'move-battle-style/{id_or_name}', MoveBattleStyle)

    @cached_resource(endpoint='move-category')
    async def get_move_category(self, id_or_name: Param) -> Optional[MoveCategory]:
        return await self._fetch(f'move-category/{id_or_name}', MoveCategory)

    @cached_resource(endpoint='move-damage-class')
    async def get_move_damage_class(self, id_or_name: Param) -> Optional[MoveDamageClass]:
        return await self._fetch(f'move-damage-class/{id_or_name}', MoveDamageClass)

    @cached_resource(endpoint='move-learn-method')
    async def get_move_learn_method(self, id_or_name: Param) -> Optional[MoveLearnMethod]:
        return await self._fetch(f'move-learn-method/{id_or_name}', MoveLearnMethod)

    @cached_resource(endpoint='move-target')
    async def get_move_target(self, id_or_name: Param) -> Optional[MoveTarget]:
        return await self._fetch(f'move-target/{id_or_name}', MoveTarget)


    """Pokémon (Group)"""
    @cached_resource(endpoint='ability')
    async def get_ability(self, id_or_name: Param) -> Optional[Ability]:
        return await self._fetch(f'ability/{id_or_name}', Ability)

    @cached_resource(endpoint='characteristic')
    async def get_characteristic(self, id_or_name: Param) -> Optional[Characteristic]:
        return await self._fetch(f'characteristic/{id_or_name}', Characteristic)

    @cached_resource(endpoint='egg-group')
    async def get_egg_group(self, id_or_name: Param) -> Optional[EggGroup]:
        return self._fetch(f'egg-group/{id_or_name}', EggGroup)

    @cached_resource(endpoint='gender')
    async def get_gender(self, id_or_name: Param) -> Optional[Gender]:
        return self._fetch(f'gender/{id_or_name}', Gender)

    @cached_resource(endpoint='growth-rate')
    async def get_growth_rate(self, id_or_name: Param) -> Optional[GrowthRate]:
        return self._fetch(f'growth-rate/{id_or_name}', GrowthRate)

    @cached_resource(endpoint='nature')
    async def get_nature(self, id_or_name: Param) -> Optional[Nature]:
        return self._fetch(f'nature/{id_or_name}', Nature)

    @cached_resource(endpoint='pokeathlon-stat')
    async def get_pokeathlon_stat(self, id_or_name: Param) -> Optional[PokeathlonStat]:
        return await self._fetch(f'pokeathlon-stat/{id_or_name}', PokeathlonStat)

    @cached_resource(endpoint='pokemon')
    async def get_pokemon(self, id_or_name: Param) -> Optional[Pokemon]:
        return await self._fetch(f'pokemon/{id_or_name}', Pokemon)

    @cached_resource(endpoint='pokemon-encounters')
    async def get_pokemon_encounters(self, id_or_name: Param) -> list[LocationAreaEncounter]:
        return (await self._fetch(f'pokemon/{id_or_name}/encounters', LocationAreaEncounter)) or []

    @cached_resource(endpoint='pokemon-color')
    async def get_pokemon_color(self, id_or_name: Param) -> Optional[PokemonColor]:
        return await self._fetch(f'pokemon-color/{id_or_name}', PokemonColor)

    @cached_resource(endpoint='pokemon-form')
    async def get_pokemon_form(self, id_or_name: Param) -> Optional[PokemonForm]:
        return await self._fetch(f'pokemon-form/{id_or_name}', PokemonForm)

    @cached_resource(endpoint='pokemon-habitat')
    async def get_pokemon_habitat(self, id_or_name: Param) -> Optional[PokemonHabitat]:
        return await self._fetch(f'pokemon-habitat/{id_or_name}', PokemonHabitat)

    @cached_resource(endpoint='pokemon-shape')
    async def get_pokemon_shape(self, id_or_name: Param) -> Optional[PokemonShape]:
        return await self._fetch(f'pokemon-shape/{id_or_name}')

    @cached_resource(endpoint='pokemon-species')
    async def get_pokemon_species(self, id_or_name: Param) -> Optional[PokemonSpecies]:
        return await self._fetch(f'pokemon-species/{id_or_name}', PokemonSpecies)

    @cached_resource(endpoint='stat')
    async def get_stat(self, id_or_name: Param) -> Optional[Stat]:
        return await self._fetch(f'stat/{id_or_name}', Stat)

    @cached_resource(endpoint='type')
    async def get_type(self, id_or_name: Param) -> Optional[PokemonTypePayload]:
        return await self._fetch(f'type/{id_or_name}', PokemonTypePayload)


    """Utility (Group)"""
    @cached_resource(endpoint='language')
    async def get_language(self, id_or_name: Param) -> Optional[Language]:
        return await self._fetch(f'language/{id_or_name}', Language)