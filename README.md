This demonstrates the use of [IMP](http://integrativemodeling.org)
and [PMI](https://github.com/salilab/pmi) in the modeling of a human integrin.
The integrin is modeled partly with low-resolution beads, and partly as
idealized helices. We attempt to reconstruct the native structure
(PDB entry [2k9j](http://www.rcsb.org/pdb/explore.do?structureId=2k9j)) using
cysteine cross-link data [1].

## Running

To run, simply run the `integrin_modeling.py` Python script.

On successful completion, output files (the top-scoring models in PDB format,
a trajectory in [RMF format](http://integrativemodeling.org/rmf/), and
statistics files) will be found in the `output` directory. See the
[IMP tutorial](http://integrativemodeling.org/nightly/doc/tutorial/rnapolii_3.html)
for a full description of these outputs.

## Info
[1] Zhu J, Luo BH, Barth P, Schonbrun J, Baker D, Springer TA. Mol Cell. 2009 Apr 24;34(2):234-49. doi: 10.1016/j.molcel.2009.02.022

_Author(s)_: Riccardo Pellarin

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html).
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Last known good IMP version_: [![build info](https://integrativemodeling.org/systems/?sysstat=8)](http://integrativemodeling.org/systems/)
