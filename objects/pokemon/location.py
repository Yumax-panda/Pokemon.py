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
from objects.models import NamedAPIResource, VersionEncounterDetail

if TYPE_CHECKING:
    from objects import LocationArea

class LocationAreaEncounter(BaseObject):

    __slots__ = (
        'location_area',
        'version_details'
    )

    def __init__(
        self,
        location_area: NamedAPIResource['LocationArea'],
        version_details: list[VersionEncounterDetail]
    ) -> None:
        self.location_area: NamedAPIResource['LocationArea'] = location_area
        self.version_details: list[VersionEncounterDetail] = version_details

    @staticmethod
    def loads(data: dict) -> LocationAreaEncounter:
        return LocationAreaEncounter(
            location_area=NamedAPIResource.loads(data['location_area']),
            version_details=VersionEncounterDetail.loads_list(data['version_details'])
        )

    @property
    def location(self) -> NamedAPIResource['LocationArea']:
        """alias for location_area attribute"""

        return getattr(self, 'location_area')

    @property
    def details(self) -> list[VersionEncounterDetail]:
        """alias for version_details"""

        return getattr(self, 'version_details')