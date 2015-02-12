#!/usr/bin/env python

import unittest
import os
import sys
import subprocess
import glob

TOPDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

class Tests(unittest.TestCase):
    def test_modeling(self):
        """Test modeling script"""
        os.chdir(TOPDIR)
        p = subprocess.check_call(["python", "glycophorin_modeling.py"])
        # Require that output files were produced (todo: test them for accuracy)
        os.unlink("best.scores.rex.py")
        os.unlink("initial.0.rmf3")
        os.unlink("stat.0.out")
        os.unlink("stat_replica.0.out")
        os.unlink("rmfs/0.rmf3")
        pdbs = glob.glob("pdbs/*.pdb")
        self.assertEqual(len(pdbs), 500)
        for p in pdbs:
            os.unlink(p)

if __name__ == '__main__':
    unittest.main()
