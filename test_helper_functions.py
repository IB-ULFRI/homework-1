import unittest

from Bio.Seq import Seq

from helper_functions import find_all_orfs


class TestFindAllORFs(unittest.TestCase):
    def test_notebook_example_1(self):
        result = find_all_orfs(Seq("TTATGAAAATGAAATGATT"), ["ATG"], ["TGA", "TAA", "TAG"])
        expected = [(1, 2, 17)]
        self.assertEqual(set(expected), set(result))

    def test_notebook_example_2(self):
        result = find_all_orfs(Seq("AATCATTTCATTTTCATAA"), ["TAT"], ["GAA"])
        expected = [(-1, 12, 18)]
        self.assertEqual(set(expected), set(result))
