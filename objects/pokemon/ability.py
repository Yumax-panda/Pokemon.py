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
from objects.models import (
    NamedAPIResource,
    Effect,
    VerboseEffect,
    Name
)

if TYPE_CHECKING:
    from objects import (
        Generation,
        VersionGroup,
        Language
    )
    from . import Pokemon


class AbilityEffectChange(BaseObject):

    __slots__ = (
        'effect_entries',
        'version_group'
    )

    def __init__(
        self,
        effect_entries: list[Effect],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.effect_entries: list[Effect] = effect_entries
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> AbilityEffectChange:
        return AbilityEffectChange(
            effect_entries=Effect.loads_list(data['effect_entries']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )


class AbilityFlavorText(BaseObject):

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
    def loads(data: dict) -> AbilityFlavorText:
        return AbilityFlavorText(
            flavor_text=data['flavor_text'],
            language=NamedAPIResource.loads(data['language']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )


class AbilityPokemon(BaseObject):

    __slots__ = (
        'is_hidden',
        'slot',
        'pokemon'
    )

    def __init__(
        self,
        is_hidden: bool,
        slot: int,
        pokemon: NamedAPIResource['Pokemon']
    ) -> None:
        self.is_hidden: bool = is_hidden
        self.slot: int = slot
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon

    @staticmethod
    def loads(data: dict) -> AbilityPokemon:
        return AbilityPokemon(
            is_hidden=data['is_hidden'],
            slot=data['slot'],
            pokemon=NamedAPIResource.loads(data['pokemon'])
        )


class Ability(BaseObject):

    __slots__ = (
        'id',
        'name',
        'is_main_series',
        'generation',
        'names',
        'effect_entries',
        'effect_changes',
        'flavor_text_entries',
        'pokemon'
    )

    def __init__(
        self,
        id: int,
        name: str,
        is_main_series: bool,
        generation: NamedAPIResource['Generation'],
        names: list[Name],
        effect_entries: list[VerboseEffect],
        effect_changes: list[AbilityEffectChange],
        flavor_text_entries: list[AbilityFlavorText],
        pokemon: list[AbilityPokemon]
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.is_main_series: bool = is_main_series
        self.generation: NamedAPIResource['Generation'] = generation
        self.names: list[Name] = names
        self.effect_entries: list[VerboseEffect] = effect_entries
        self.effect_changes: list[AbilityEffectChange] = effect_changes
        self.flavor_text_entries: list[AbilityFlavorText] = flavor_text_entries
        self.pokemon: list[AbilityPokemon] = pokemon

    @staticmethod
    def loads(data: dict) -> Ability:
        return Ability(
            id=data['id'],
            name=data['name'],
            is_main_series=data['is_main_series'],
            generation=NamedAPIResource.loads(data['generation']),
            names=Name.loads_list(data['names']),
            effect_entries=VerboseEffect.loads_list(data['effect_entries']),
            effect_changes=AbilityEffectChange.loads_list(data['effect_changes']),
            flavor_text_entries=AbilityFlavorText.loads_list(data['flavor_text_entries']),
            pokemon=AbilityPokemon.loads_list(data['pokemon'])
        )

    @property
    def flavor_texts(self) -> list[AbilityFlavorText]:
        """alias for flavor_text_entries attribute"""

        return getattr(self, 'flavor_text_entries')