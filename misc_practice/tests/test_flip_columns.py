''' Unit tests for flip_columns.py'''

# imports
from pathlib import Path
import sys
import unittest

# define path
module_dir = Path('../src')
sys.path.append(str(module_dir))


# import the module
import flip_columns

class TestFlipColumns(unittest.TestCase):

    def test_flip_one(self):

        self.assertEqual(flip_columns.flip_one([[1,2,3],[4,5,6],[7,8,9]],1), [[1,8,3],[4,5,6],[7,2,9]])

        with self.assertRaises(IndexError):
            flip_columns.flip_one([[1,2,3],[4,5,6],[7,8,9]],3)
