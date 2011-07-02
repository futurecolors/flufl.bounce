# Copyright (C) 1998-2011 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <http://www.gnu.org/licenses/>.

"""Parse mystery style generated by MTA at caiwireless.net."""

from __future__ import absolute_import, unicode_literals

__metaclass__ = type
__all__ = [
    'Caiwireless',
    ]


import re

from email.iterators import body_line_iterator
from flufl.enum import Enum
from zope.interface import implements

from flufl.bounce.interfaces import IBounceDetector


tcre = re.compile(r'the following recipients did not receive this message:',
                  re.IGNORECASE)
acre = re.compile(r'<(?P<addr>[^>]*)>')


class ParseState(Enum):
    start = 0
    tag_seen = 1



class Caiwireless:
    """Parse mystery style generated by MTA at caiwireless.net."""

    implements(IBounceDetector)

    def process(self, msg):
        if msg.get_content_type() != 'multipart/mixed':
            return (), ()
        state = ParseState.start
        # This format thinks it's a MIME, but it really isn't.
        for line in body_line_iterator(msg):
            line = line.strip()
            if state is ParseState.start and tcre.match(line):
                state = ParseState.tag_seen
            elif state is ParseState.tag_seen and line:
                mo = acre.match(line)
                if not mo:
                    return (), ()
                return (), set(mo.group('addr'))
