import unittest
import numpy as np
from searchTool import my_map


class TestWheretoPark(unittest.TestCase):
    def test_my_map_smoke(self):
        my_map()
        self.assertTrue(True)


    # def test_entropy_smoke(self):
    #     entropy([0.5, 0.2, 0.3])
    #     self.assertTrue(True)
