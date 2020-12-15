# (C) Copyright 2005-2020 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

""" The implementation of a workbench window layout. """


# Import the toolkit specific version.
from pyface.toolkit import toolkit_object

WorkbenchWindowLayout = toolkit_object(
    "workbench.workbench_window_layout:WorkbenchWindowLayout"
)
