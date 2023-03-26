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
from objects.common import BaseObject
from objects.models import (
    APIResource,
    NamedAPIResource,
    Name,
    Description,
    FlavorText
)

if TYPE_CHECKING:
    from . import (
        EggGroup,
        GrowthRate,
        PokemonColor,
        PokemonShape,
        PokemonHabitat,
        Pokemon
    )

    from objects import (
        EvolutionChain,
        Generation,
        Language,
        Pokedex,
        PalParkArea
    )


class PokemonSpeciesVariety(BaseObject):

    __slots__ = (
        'is_default',
        'pokemon'
    )

    def __init__(
        self,
        is_default: bool,
        pokemon: NamedAPIResource['Pokemon']
    ) -> None:
        self.is_default: bool = is_default
        self.pokemon: NamedAPIResource['Pokemon'] = pokemon

    @staticmethod
    def loads(data: dict) -> PokemonSpeciesVariety:
        return PokemonSpeciesVariety(
            is_default=data['is_default'],
            pokemon=NamedAPIResource.loads(data['pokemon'])
        )


class PalParkEncounterArea(BaseObject):

    __slots__ = (
        'base_score',
        'rate',
        'area'
    )

    def __init__(
        self,
        base_score: int,
        rate: int,
        area: NamedAPIResource['PalParkArea']
    ) -> None:
        self.base_score: int = base_score
        self.rate: int = rate
        self.area: NamedAPIResource['PalParkArea'] = area

    @staticmethod
    def loads(data: dict) -> PalParkEncounterArea:
        return PalParkEncounterArea(
            base_score=data['base_score'],
            rate=data['rate'],
            area=NamedAPIResource.loads(data['area'])
        )


class PokemonSpeciesDexEntry(BaseObject):

    __slots__ = (
        'entry_number',
        'pokedex'
    )

    def __init__(
        self,
        entry_number: int,
        pokedex: NamedAPIResource['Pokedex']
    ) -> None:
        self.entry_number: int = entry_number
        self.pokedex: NamedAPIResource['Pokedex'] = pokedex

    @staticmethod
    def loads(data: dict) -> PokemonSpeciesDexEntry:
        return PokemonSpeciesDexEntry(
            entry_number=data['entry_number'],
            pokedex=NamedAPIResource.loads(data['pokedex'])
        )


class Genus(BaseObject):

    __slots__ = (
        'genus',
        'language'
    )

    def __init__(
        self,
        genus: str,
        language: NamedAPIResource['Language']
    ) -> None:
        self.genus: str = genus
        self.language: NamedAPIResource['Language'] = language

    @staticmethod
    def loads(data: dict) -> Genus:
        return Genus(
            genus=data['genus'],
            language=NamedAPIResource.loads(data['language'])
        )


class PokemonSpecies(BaseObject):

    __slots__ = (
        'id',
        'name',
        'order',
        'gender_rate',
        'capture_rate',
        'base_happiness',
        'is_baby',
        'is_legendary',
        'is_mythical',
        'hatch_counter',
        'has_gender_differences',
        'forms_switchable',
        'growth_rate',
        'pokedex_numbers',
        'egg_groups',
        'color',
        'shape',
        'evolves_from_species',
        'evolution_chain',
        'habitat',
        'generation',
        'names',
        'pal_park_encounters',
        'flavor_text_entries',
        'form_descriptions',
        'genera',
        'varieties'
    )

    def __init__(
        self,
        id: int,
        name: str,
        order: int,
        gender_rate: int,
        capture_rate: int,
        base_happiness: int,
        is_baby: bool,
        is_legendary: bool,
        is_mythical: bool,
        hatch_counter: int,
        has_gender_differences: bool,
        forms_switchable: bool,
        growth_rate: NamedAPIResource['GrowthRate'],
        pokedex_numbers: list[PokemonSpeciesDexEntry],
        egg_groups: list[NamedAPIResource['EggGroup']],
        color: NamedAPIResource['PokemonColor'],
        shape: NamedAPIResource['PokemonShape'],
        evolution_chain: APIResource['EvolutionChain'],
        generation: NamedAPIResource['Generation'],
        names: list[Name],
        pal_park_encounters: list[PalParkEncounterArea],
        flavor_text_entries: list[FlavorText],
        form_descriptions: list[Description],
        genera: list[Genus],
        varieties: list[PokemonSpeciesVariety],
        evolves_from_species: Optional[NamedAPIResource['PokemonSpecies']] = None,
        habitat: Optional[NamedAPIResource['PokemonHabitat']] = None
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.order: int = order
        self.gender_rate: int = gender_rate
        self.capture_rate: int = capture_rate
        self.base_happiness: int = base_happiness
        self.is_baby: bool = is_baby
        self.is_legendary: bool = is_legendary
        self.is_mythical: bool = is_mythical
        self.hatch_counter: int = hatch_counter
        self.has_gender_differences: bool = has_gender_differences
        self.forms_switchable: bool = forms_switchable
        self.growth_rate: NamedAPIResource['GrowthRate'] = growth_rate
        self.pokedex_numbers: list[PokemonSpeciesDexEntry] = pokedex_numbers
        self.egg_groups: list[NamedAPIResource['EggGroup']] = egg_groups
        self.color: NamedAPIResource['PokemonColor'] = color
        self.shape: NamedAPIResource['PokemonShape'] = shape
        self.evolves_from_species: Optional[NamedAPIResource['PokemonSpecies']] = evolves_from_species
        self.evolution_chain: APIResource['EvolutionChain'] = evolution_chain
        self.habitat: Optional[NamedAPIResource['PokemonHabitat']] = habitat
        self.generation: NamedAPIResource['Generation'] = generation
        self.names: list[Name] = names
        self.pal_park_encounters: list[PalParkEncounterArea] = pal_park_encounters
        self.flavor_text_entries: list[FlavorText] = flavor_text_entries
        self.form_descriptions: list[Description] = form_descriptions
        self.genera: list[Genus] = genera
        self.varieties: list[PokemonSpeciesVariety] = varieties

    @staticmethod
    def loads(data: dict) -> PokemonSpecies:
        species = PokemonSpecies(
            id=data['id'],
            name=data['name'],
            order=data['order'],
            gender_rate=data['gender_rate'],
            capture_rate=data['capture_rate'],
            base_happiness=data['base_happiness'],
            is_baby=data['is_baby'],
            is_legendary=data['is_legendary'],
            is_mythical=data['is_mythical'],
            hatch_counter=data['hatch_counter'],
            has_gender_differences=data['has_gender_differences'],
            forms_switchable=data['forms_switchable'],
            growth_rate=NamedAPIResource.loads(data['growth_rate']),
            pokedex_numbers=PokemonSpeciesDexEntry.loads_list(data['pokedex_numbers']),
            egg_groups=NamedAPIResource.loads_list(data['egg_groups']),
            color=NamedAPIResource.loads(data['color']),
            shape=NamedAPIResource.loads(data['shape']),
            evolution_chain=APIResource.loads(data['evolution_chain']),
            generation=NamedAPIResource.loads(data['generation']),
            names=Name.loads_list(data['names']),
            pal_park_encounters=PalParkEncounterArea.loads_list(data['pal_park_encounters']),
            flavor_text_entries=FlavorText.loads_list(data['flavor_text_entries']),
            form_descriptions=Description.loads_list(data['form_descriptions']),
            genera=Genus.loads_list(data['genera']),
            varieties=PokemonSpeciesVariety.loads_list(data['varieties'])
        )

        for attr in (
            'evolves_from_species',
            'habitat'
        ):
            if (var:=data.get(attr)) is not None:
                setattr(species, attr, NamedAPIResource.loads(var))

        return species

    @property
    def evolves_from(self) -> list[NamedAPIResource['PokemonSpecies']]:
        """alias for `evolves_from_species attribute"""

        return getattr(self, 'evolves_from_species')