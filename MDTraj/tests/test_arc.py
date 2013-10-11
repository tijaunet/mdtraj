# Copyright 2012 mdtraj developers
#
# This file is part of mdtraj
#
# mdtraj is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# mdtraj is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# mdtraj. If not, see http://www.gnu.org/licenses/.

import tempfile, os
import numpy as np
import mdtraj as md
from mdtraj import ArcTrajectoryFile, arc, PDBTrajectoryFile
from mdtraj.testing import get_fn, eq, DocStringFormatTester
TestDocstrings = DocStringFormatTester(arc, error_on_none=True)

temp = tempfile.mkstemp(suffix='.arc')[1]
def teardown_module(module):
    """remove the temporary file created by tests in this file
    this gets automatically called by nose"""
    os.unlink(temp)


def test_read_0():
    with ArcTrajectoryFile(get_fn('4waters.arc')) as f:
        xyz = f.read()
    with PDBTrajectoryFile(get_fn('4waters.pdb')) as f:
        xyz2 = f.positions
    eq(xyz, xyz2, decimal=3)
