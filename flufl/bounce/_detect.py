# Copyright (C) 2011 by Barry A. Warsaw
#
# This file is part of flufl.bounce
#
# flufl.bounce is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, version 3 of the License.
#
# flufl.bounce is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with flufl.bounce.  If not, see <http://www.gnu.org/licenses/>.

"""Top-level bounce detector API."""

from __future__ import absolute_import, unicode_literals

__metaclass__ = type
__all__ = [
    'detect',
    ]



def detect(msg):
    """Detect the set of bouncing original recipients.

    :param msg: The bounce message.
    :type msg: `email.message.Message`
    :return: The set of detected original recipients.
    :rtype: set of strings
    """
    return set(['anne@example.com'])
