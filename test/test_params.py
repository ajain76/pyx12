#! /usr/bin/env python

import sys
sys.path.insert(0, '..')
import unittest

from pyx12.tests.params import *
from pyx12.errors import *
from helper import get_testcases, print_testcases, get_suite

ns = pyx12.tests.params
if len(sys.argv) > 1 and sys.argv[1] == '-h':
    print_testcases(ns)
else:
    unittest.TextTestRunner(verbosity=2).run(get_suite(ns, sys.argv[1:]))
