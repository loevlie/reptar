# MIT License
# 
# Copyright (c) 2022, Alex M. Maldonado
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Paths to files used for tests."""

import pytest
import os

################
###   ORCA   ###
################

path_orca = '../examples/orca'

###   v4.2.0   ###
path_orca_420 = path_orca + '/v4.2.0'

######   engrads   ######
path_orca_420_engrads = path_orca_420 + '/energy-and-gradients'

def get_6h2o_temelso_pr_engrad():
    dir_path = path_orca_420_engrads + '/6h2o.temelso.etal.pr-orca.engrad-mp2.def2tzvp'
    out_path = dir_path + '/6h2o.temelso.etal.pr-orca.engrad-mp2.def2tzvp.out'
    return dir_path, out_path

###############
###   xTB   ###
###############

path_xtb = '../examples/xtb'

###   v6.4.1   ###
path_xtb_641 = path_xtb + '/v6.4.1'

######   MD  ######
path_xtb_641_md = path_xtb_641 + '/md'

def get_1h2o_120meoh_eq_paths():
    dir_path = path_xtb_641_md + '/1h2o.120meoh.pm.gfn2'
    calc_path = dir_path + '/1h2o.120meoh.pm.gfn2-xtb.md.eq1-gfn2.500k.wallpot'
    out_path = calc_path + '/1h2o.120meoh.pm.gfn2-xtb.md.eq1-gfn2.500k.wallpot.out'
    geom_path = calc_path + '/1h2o.120meoh.pm.gfn2.xyz'
    traj_path = calc_path + '/xtb.trj'
    return dir_path, calc_path, out_path, geom_path, traj_path

def get_1h2o_120meoh_prod_paths():
    dir_path = path_xtb_641_md + '/1h2o.120meoh.pm.gfn2'
    calc_path = dir_path + '/1h2o.120meoh.pm.gfn2-xtb.md.prod1-gfn2.500k.wallpot'
    out_path = calc_path + '/1h2o.120meoh.pm.gfn2.eq1-xtb.md.prod1-gfn2.500k.wallpot.out'
    geom_path = calc_path + '/1h2o.120meoh.pm.gfn2.eq1.xyz'
    traj_path = calc_path + '/xtb.trj'
    return dir_path, calc_path, out_path, geom_path, traj_path

def get_1h2o_120meoh_exdir_path():
    dir_path = path_xtb_641_md + '/1h2o.120meoh.pm.gfn2.exdir'
    return dir_path
