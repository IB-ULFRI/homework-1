import unittest
import numpy as np
from Bio.Seq import Seq

from .helper_functions import find_orfs, find_all_orfs, translate_to_protein


def assert_sets_same(expected, actual):
    expected, actual = set(expected), set(actual)

    missing = [s for s in expected if s not in actual]
    extra = [s for s in actual if s not in expected]

    errmsg = "\n"
    if len(missing):
        errmsg += f"Missing: {missing}\n"
    if len(extra):
        errmsg += f"Extra:   {extra}\n"

    if len(errmsg) > 1:
        raise AssertionError(errmsg)


class TestORFFinder(unittest.TestCase):
    def test_find_orfs(self):
        seq = (
            "ATGGATTCCAATACTAAGCAGCACTCTTGGTCTGGACATCCTCATCGGAGGATTTGAATGGAATGA"
            "TAACACAGTTCGAGTCTCTGAAACTCTACAGAGATTCGCTTGGAGAAGCAGCGATGAGGATGGGAG"
            "ATCTCCACTCTCTACAAAGTAG"
        )
        result = find_orfs(seq, ["ATG"], ["TAA", "TAG", "TGA"])
        solution = [[0, 57], [57, 66]]  # start position, stop position
        np.testing.assert_equal(np.array(result), solution)

    def test_find_all_orfs(self):
        seq = (
            "ATGGATTCCAATACTAAGCAGCACATGTGGTCTGGACATCCTCATCGGAGGATTTGAATGGAATGA"
            "TAACACAGTTCGAGTCTCTAGAAACTCTACAGAGATTCGCTTGGAGAAGCAGCGATGAGGATGGGA"
            "GATCTCCACTCTCTACAAAGTAG"
        )
        seq = Seq(seq)

        result = find_all_orfs(seq, ["ATG"], ["TAA", "TAG", "TGA"])
        solution = {
            (1, 0, 57),  # strand, start position, stop position
            (1, 57, 66),
            (1, 62, 155),
        }
        assert_sets_same(solution, result)


class TestProteinTranslation(unittest.TestCase):
    def test_translation(self):
        seq = (
            "ATGGATTCCAATACTAAGCAGCACATGTGGTCTGGACATCCTCATCGGAGGATTTGAATGGAATGA"
            "TAACACAGTTCGAGTCTCTAGAAACTCTACAGAGATTCGCTTGGAGAAGCAGCGATGAGGATGGGA"
            "GATCTCCACTCTCTACAAAGTAG"
        )
        result = translate_to_protein(seq)
        solution = "MDSNTKQHMWSGHPHRRIMEHSSSLKLYRDSLGEAAMRMGDLHSLQS"
        self.assertEqual(result, solution)


if __name__ == "__main__":
    unittest.main()
