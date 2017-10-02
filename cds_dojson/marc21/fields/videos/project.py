# -*- coding: utf-8 -*-
#
# This file is part of CERN Document Server.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""CDS Video project fields."""

from __future__ import absolute_import, print_function

from dojson.utils import filter_values, for_each_value

from ...models.videos.project import model


@model.over('related_links', '^773__')
@for_each_value
@filter_values
def related_links(self, key, value):
    """Related links."""
    return {
        'name': value.get('p'),
        'url': value.get('u'),
    }
