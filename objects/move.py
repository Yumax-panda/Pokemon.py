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
    APIResource,
    MachineVersionDetail,
    Description
)
from .pokemon.ability import AbilityEffectChange

if TYPE_CHECKING:
    from .contest import ContestType, ContestEffect, SuperContestEffect
    from .game import Generation, VersionGroup
    from .language import Language
    from .pokemon.pokemon import Pokemon
    from .pokemon.type import Type as PokemonTypePayload
    from .pokemon.stat import Stat



class PastMoveStatValues(BaseObject):

    __slots__ = (
        'accuracy',
        'effect_chance',
        'power',
        'pp',
        'effect_entries',
        'type',
        'version_group'
    )

    def __init__(
        self,
        accuracy: int,
        effect_chance: int,
        power: int,
        pp: int,
        effect_entries: list[VerboseEffect],
        type: NamedAPIResource['PokemonTypePayload'],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.accuracy: int = accuracy
        self.effect_chance: int = effect_chance
        self.power: int = power
        self.pp: int = pp
        self.effect_entries: list[VerboseEffect] = effect_entries
        self.type: NamedAPIResource['PokemonTypePayload'] = type
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> PastMoveStatValues:
        return PastMoveStatValues(
            accuracy=data['accuracy'],
            effect_chance=data['effect_chance'],
            power=data['power'],
            pp=data['pp'],
            effect_entries=VerboseEffect.loads_list(data['effect_entries']),
            type=NamedAPIResource.loads(data['type']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )

    @property
    def chance(self) -> int:
        """alias for effect_chance attribute"""

        return getattr(self, 'effect_chance')

    @property
    def effects(self) -> list[VerboseEffect]:
        """alias for effect_entries attribute"""

        return getattr(self, 'effect_entries')

    @property
    def version(self) -> NamedAPIResource['VersionGroup']:
        """alias for version_group attribute"""

        return getattr(self, 'version_group')


class MoveStatChange(BaseObject):

    __slots__ = (
        'change',
        'stat'
    )

    def __init__(
        self,
        change: int,
        stat: NamedAPIResource['Stat']
    ) -> None:
        self.change: int = change
        self.stat: NamedAPIResource['Stat'] = stat

    @staticmethod
    def loads(data: dict) -> MoveStatChange:
        return MoveStatChange(
            change=data['change'],
            stat=NamedAPIResource.loads(data['stat'])
        )


class MoveMetaData(BaseObject):

    __slots__ = (
        'ailment',
        'category',
        'min_hits',
        'max_hits',
        'min_turns',
        'max_turns',
        'drain',
        'healing',
        'crit_rate',
        'ailment_chance',
        'flinch_chance',
        'stat_chance'
    )

    def __init__(
        self,
        ailment: NamedAPIResource['MoveAilment'],
        category: NamedAPIResource['MoveCategory'],
        min_hits: int,
        max_hits: int,
        min_turns: int,
        max_turns: int,
        drain: int,
        healing: int,
        crit_rate: int,
        ailment_chance: int,
        flinch_chance: int,
        stat_chance: int
    ) -> None:
        self.ailment: NamedAPIResource['MoveAilment'] = ailment
        self.category: NamedAPIResource['MoveCategory'] = category
        self.min_hits: int = min_hits
        self.max_hits: int = max_hits
        self.min_turns: int = min_turns
        self.max_turns: int = max_turns
        self.drain: int = drain
        self.healing: int = healing
        self.crit_rate: int = crit_rate
        self.ailment_chance: int = ailment_chance
        self.flinch_chance: int = flinch_chance
        self.stat_chance: int = stat_chance

    @staticmethod
    def loads(data: dict) -> MoveMetaData:
        kwargs: dict = {
            'ailment': NamedAPIResource.loads(data['ailment']),
            'category': NamedAPIResource.loads(data['category'])
        }

        for attr in (
            'min_hits',
            'max_hits',
            'min_turns',
            'max_turns',
            'drain',
            'healing',
            'crit_rate',
            'ailment_chance',
            'flinch_chance',
            'stat_chance'
        ):
            kwargs[attr] = data[attr]

        return MoveMetaData(**kwargs)


class MoveFlavorText(BaseObject):

    __slots__ = (
        'flavor_text',
        'language',
        'version_group'
    )

    def __init__(
        self,
        flavor_text: str,
        language: NamedAPIResource['Language'],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.flavor_text: str = flavor_text
        self.language: NamedAPIResource['Language'] = language
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> MoveFlavorText:
        return MoveFlavorText(
            flavor_text=data['flavor_text'],
            language=NamedAPIResource.loads(data['language']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )


class ContestComboDetail(BaseObject):

    __slots__ = (
        'use_before',
        'use_after'
    )

    def __init__(
        self,
        use_before: Optional[list[NamedAPIResource['Move']]] = None,
        use_after: Optional[list[NamedAPIResource['Move']]] = None
    ) -> None:
        self.use_before: Optional[list[NamedAPIResource['Move']]] = use_before
        self.use_after: Optional[list[NamedAPIResource['Move']]] = use_after

    @staticmethod
    def loads(data: dict) -> ContestComboDetail:
        detail = ContestComboDetail()

        for attr in ('use_before', 'use_after'):
            if (var :=data.get(attr)) is not None:
                setattr(detail, attr, NamedAPIResource.loads_list(var))

    @property
    def before(self) -> Optional[list[NamedAPIResource['Move']]]:
        """alias for use_before attribute"""

        return getattr(self, 'use_before')

    @property
    def after(self) -> Optional[list[NamedAPIResource['Move']]]:
        """alias for use_after attribute"""

        return getattr(self, 'use_after')


class ContestComboSets(BaseObject):

    __slots__ = (
        'normal',
        'super'
    )

    def __init__(
        self,
        normal: Optional[ContestComboDetail] = None,
        super: Optional[ContestComboDetail] = None
    ) -> None:
        self.normal: Optional[ContestComboDetail] = normal
        self.super: Optional[ContestComboDetail] = super

    @staticmethod
    def loads(data: dict) -> ContestComboSets:
        c = ContestComboSets()

        for attr in ('normal', 'super'):
            if (var :=data.get(attr)) is not None:
                setattr(c, attr, ContestComboSets.loads(var))

        return c


class Move(BaseObject):

    __slots__ = (
        'id',
        'name',
        'accuracy',
        'effect_chance',
        'pp',
        'priority',
        'power',
        'contest_combos',
        'contest_type',
        'contest_effect',
        'damage_class',
        'effect_entries',
        'effect_changes',
        'learned_by_pokemon',
        'flavor_text_entries',
        'generation',
        'machines',
        'meta',
        'names',
        'past_values',
        'stat_changes',
        'super_contest_effect',
        'target',
        'type'
    )

    def __init__(
        self,
        id: int,
        name: str,
        accuracy: int,
        effect_chance: Optional[int],
        pp: int,
        priority: int,
        power: int,
        contest_combos: ContestComboSets,
        contest_type: NamedAPIResource['ContestType'],
        contest_effect: APIResource['ContestEffect'],
        damage_class: NamedAPIResource['MoveDamageClass'],
        effect_entries: list[VerboseEffect],
        effect_changes: list[AbilityEffectChange],
        learned_by_pokemon: list[NamedAPIResource['Pokemon']],
        flavor_text_entries: list[MoveFlavorText],
        generation: NamedAPIResource['Generation'],
        machines: list[MachineVersionDetail],
        meta: MoveMetaData,
        names: list[Name],
        past_values: list[PastMoveStatValues],
        stat_changes: list[MoveStatChange],
        super_contest_effect: APIResource['SuperContestEffect'],
        target: NamedAPIResource['MoveTarget'],
        type: NamedAPIResource['PokemonTypePayload']
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.accuracy: int = accuracy
        self.effect_chance: Optional[int] = effect_chance
        self.pp: int = pp
        self.priority: int = priority
        self.power: int = power
        self.contest_combos: ContestComboSets = contest_combos
        self.contest_type: NamedAPIResource['ContestType'] = contest_type
        self.contest_effect: APIResource['ContestEffect'] = contest_effect
        self.damage_class: NamedAPIResource['MoveDamageClass'] = damage_class
        self.effect_entries: list[VerboseEffect] = effect_entries
        self.effect_changes: list[AbilityEffectChange] = effect_changes
        self.learned_by_pokemon: list[NamedAPIResource['Pokemon']] = learned_by_pokemon
        self.flavor_text_entries: list[MoveFlavorText] = flavor_text_entries
        self.generation: NamedAPIResource['Generation'] = generation
        self.machines: list[MachineVersionDetail] = machines
        self.meta: MoveMetaData = meta
        self.names: list[Name] = names
        self.past_values: list[PastMoveStatValues] = past_values
        self.stat_changes: list[MoveStatChange] = stat_changes
        self.super_contest_effect: APIResource['SuperContestEffect'] = super_contest_effect
        self.target: NamedAPIResource['MoveTarget'] = target
        self.type: NamedAPIResource['PokemonTypePayload'] = type

    @staticmethod
    def loads(data: dict) -> Move:
        return Move(
            id=data['id'],
            name=data['name'],
            accuracy=data['accuracy'],
            effect_chance=data.get('effect_chance'),
            pp=data['pp'],
            priority=data['priority'],
            power=data['power'],
            contest_combos=ContestComboSets.loads(data['contest_combos']),
            contest_type=NamedAPIResource.loads(data['contest_type']),
            contest_effect=APIResource.loads(data['contest_effect']),
            damage_class=NamedAPIResource.loads(data['damage_class']),
            effect_entries=VerboseEffect.loads_list(data['effect_entries']),
            effect_changes=AbilityEffectChange.loads_list(data['effect_changes']),
            learned_by_pokemon=NamedAPIResource.loads_list(data['learned_by_pokemon']),
            flavor_text_entries=MoveFlavorText.loads_list(data['flavor_text_entries']),
            generation=NamedAPIResource.loads(data['generation']),
            machines=MachineVersionDetail.loads_list(data['machines']),
            meta=MoveMetaData.loads(data['meta']),
            names=Name.loads_list(data['names']),
            past_values=PastMoveStatValues.loads_list(data['past_values']),
            stat_changes=MoveStatChange.loads_list(data['stat_changes']),
            super_contest_effect=APIResource.loads(data['super_contest_effect']),
            target=NamedAPIResource.loads(data['target']),
            type=NamedAPIResource.loads(data['type'])
        )


class MoveAilment(BaseObject):

    __slots__ = (
        'id',
        'name',
        'moves',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        moves: list[NamedAPIResource['Move']],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.moves: list[NamedAPIResource['Move']] = moves
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> MoveAilment:
        return MoveAilment(
            id=data['id'],
            name=data['name'],
            moves=NamedAPIResource.loads_list(data['moves']),
            names=Name.loads_list(data['names'])
        )


class MoveBattleStyle(BaseObject):

    __slots__ = (
        'id',
        'name',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> MoveBattleStyle:
        return MoveBattleStyle(
            id=data['id'],
            name=data['name'],
            names=Name.loads_list(data['names'])
        )


class MoveCategory(BaseObject):

    __slots__ = (
        'id',
        'name',
        'moves',
        'descriptions'
    )

    def __init__(
        self,
        id: int,
        name: str,
        moves: list[NamedAPIResource['Move']],
        descriptions: list[Description]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.moves: list[NamedAPIResource['Move']] = moves
        self.descriptions: list[Description] = descriptions

    @staticmethod
    def loads(data: dict) -> MoveCategory:
        return MoveCategory(
            id=data['id'],
            name=data['name'],
            moves=NamedAPIResource.loads_list(data['moves']),
            descriptions=Description.loads_list(data['descriptions'])
        )


class MoveDamageClass(BaseObject):

    __slots__ = (
        'id',
        'name',
        'descriptions',
        'moves',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        descriptions: list[Description],
        moves: list[NamedAPIResource['Move']],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.descriptions: list[Description] = descriptions
        self.moves: list[NamedAPIResource['Move']] = moves
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> MoveDamageClass:
        return MoveDamageClass(
            id=data['id'],
            name=data['name'],
            descriptions=Description.loads_list(data['descriptions']),
            moves=NamedAPIResource.loads_list(data['moves']),
            names=Name.loads_list(data['names'])
        )


class MoveLearnMethod(BaseObject):

    __slots__ = (
        'id',
        'name',
        'descriptions',
        'names',
        'version_groups'
    )

    def __init__(
        self,
        id: int,
        name: str,
        descriptions: list[Description],
        names: list[Name],
        version_groups: list[NamedAPIResource['VersionGroup']]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.descriptions: list[Description] = descriptions
        self.names: list[Name] = names
        self.version_groups: list[NamedAPIResource['VersionGroup']] = version_groups

    @staticmethod
    def loads(data: dict) -> MoveLearnMethod:
        return MoveLearnMethod(
            id=data['id'],
            name=data['name'],
            descriptions=Description.loads_list(data['descriptions']),
            names=Name.loads_list(data['names']),
            version_groups=NamedAPIResource.loads_list(data['version_groups'])
        )

    @property
    def versions(self) -> list[NamedAPIResource['VersionGroup']]:
        """alias for version_groups"""

        return getattr(self, 'version_groups')


class MoveTarget(BaseObject):

    __slots__ = (
        'id',
        'name',
        'descriptions',
        'moves',
        'names'
    )

    def __init__(
        self,
        id: int,
        name: str,
        descriptions: list[Description],
        moves: list[NamedAPIResource],
        names: list[Name]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.descriptions: list[Description] = descriptions
        self.moves: list[NamedAPIResource['Move']] = moves
        self.names: list[Name] = names

    @staticmethod
    def loads(data: dict) -> MoveTarget:
        return MoveTarget(
            id=data['id'],
            name=data['name'],
            descriptions=Description.loads_list(data['descriptions']),
            moves=NamedAPIResource.loads_list(data['moves']),
            names=Name.loads_list(data['names'])
        )