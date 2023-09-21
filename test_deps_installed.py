import os
import shutil
import sys
import unittest

class DepsTest(unittest.TestCase):
    def test_pip(self):
        print(sys.executable)
        print(os.getenv("PATH"))
        self.assertTrue(shutil.which("pip"))
