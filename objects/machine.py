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
from .common import BaseObject
from .models import NamedAPIResource

if TYPE_CHECKING:
    from .item import Item
    from .move import Move
    from .game import VersionGroup


class Machine(BaseObject):

    __slots__ = (
        'id',
        'item',
        'move',
        'version_group'
    )

    def __init__(
        self,
        id: int,
        item: NamedAPIResource['Item'],
        move: NamedAPIResource['Move'],
        version_group: NamedAPIResource['VersionGroup']
    ) -> None:
        self.id: int = id
        self.item: NamedAPIResource['Item'] = item
        self.move: NamedAPIResource['Move'] = move
        self.version_group: NamedAPIResource['VersionGroup'] = version_group

    @staticmethod
    def loads(data: dict) -> Machine:
        return Machine(
            id=data['id'],
            item=NamedAPIResource.loads(data['item']),
            move=NamedAPIResource.loads(data['move']),
            version_group=NamedAPIResource.loads(data['version_group'])
        )