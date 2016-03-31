# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2016 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""MARC21 rules."""

from __future__ import absolute_import, print_function

from dojson import utils
from dojson.contrib.to_marc21.model import to_marc21


@to_marc21.over('980', '^(resource_type|communities)$')
@utils.for_each_value
@utils.filter_values
def reverse_resource_type(self, key, value):
    """Reverse - Resource Type."""
    if key == 'resource_type':
        return {
            'a': value.get('type'),
            'b': value.get('subtype'),
            '$ind1': '_',
            '$ind2': '_',
        }
    elif key == 'communities':
        return {
            'a': 'user-{0}'.format(value),
            '$ind1': '_',
            '$ind2': '_',
        }
