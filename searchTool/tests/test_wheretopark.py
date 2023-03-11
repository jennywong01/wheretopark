"""
Tests functions created for wheretopark project.

TestMyMap is a class that tests my_map through various tests.
TestFindPlaces is a class that tests find_places through various tests.

"""

import unittest
from searchTool import my_map
from searchTool import find_places

# Define a class in which the tests will run for my_map
class TestMyMap(unittest.TestCase):
    """Perform testing of my_map"""

    # Smoke test
    def test_my_map_smoke(self):
        """Test to see if there is an unexpected exception."""
        map_smoke = my_map(47.6062,-122.3321, 12)
        self.assertTrue(map_smoke)

    # Edge test (1 parameter)
    def test_my_map_edge1(self):
        """Test when there is only one input to see if expected exception occurs."""
        with self.assertRaises(TypeError):
            my_map(47.6062)
            
    # Edge test (2 parameters)
    def test_my_map_edge2(self):
        """Test when there are only 2 inputs to see if expected exception occurs."""
        with self.assertRaises(TypeError):
            my_map(47.6062, -122.3321)

    # Edge test (3 parameters)
    def test_my_map_edge3(self):
        """Test when 3rd input is not integer to see if expected exception occurs."""
        with self.assertRaises(ValueError):
            my_map(47.6062,-122.3321,122.3321)
            
    # Edge test (non-float parameters)
    def test_my_map_edge4(self):
        """Test when inputs are string."""
        with self.assertRaises(ValueError):
            my_map('47.6062','-122.3321','12')
            
    # Edge test (range of latitude)
    def test_my_map_edge5(self):
        """Test when the latitude is not within Seattle."""
        lat = 50
        my_map(lat,-122.3321,12)
        self.assertAlmostEqual(47.6, lat, 'Latitude is out of the range of Seattle')
            
    # Edge test (range of longitude)
    def test_my_map_edge6(self):
        """Test when the longitude is not within Seattle."""
        lng = -100
        my_map(47.6062,lng,12)
        self.assertAlmostEqual(-122.3, lng, 'Longitude is out of the range of Seattle')
        
    # Edge test (zoom cannot be negative)
    def test_my_map_edge7(self):
        """Test when zoom value is negative."""
        zoom = -100
        my_map(47.6062,-122.3321,zoom)
        assert (zoom <= 0),'Zoom is negative'
        
    # Edge test (zoom cannot be too large)
    def test_my_map_edge8(self):
        """Test when zoom value is too large."""
        zoom = 20
        my_map(47.6062,-122.3321,zoom)
        assert (zoom >= 20),'Zoom in too far'

    # Edge test (No parameters)
    def test_my_map_edge0(self):
        """Test when there is no input to see if expected exception occurs."""
        with self.assertRaises(TypeError):
            my_map()
            
    # One-shot test
    def test_my_map_oneshot(self):
        """Test to ensure there are 5 tools in gmap."""
        self.assertEqual(5,len(my_map(47.6062,-122.3321, 12).tools))


# Define a class in which the tests will run for find_places
class TestFindPlaces(unittest.TestCase):
    """Perform testing of find_places through smoke tests, one-shot tests, and edge tests."""

    # Smoke test
    def test_find_places_smoke(self):
        """Test to see if there is an unexpected exception."""
        find_places('Starbucks')
        # pylint: disable=redundant-unittest-assert
        self.assertTrue(True)

    # One-Shot test (given address, find latitude)
    def test_find_places_oneshot_lat(self):
        """Test using arguments where the expected result is known to be 47.614002."""
        self.assertAlmostEqual(47.6140019,
                               find_places('1124 Pike St, Seattle').iloc[0]
                               ['geometry.location.lat'])

    # One-Shot test (given cafe name, find place_id)
    def test_find_places_oneshot_id(self):
        """Test using arguments where the expected place_id is known."""
        self.assertEqual('ChIJCUNyPKEVkFQR94JP8mIGtbA',find_places('Sip House').iloc[0]['place_id'])

    # Edge test (place doesn't exist)
    def test_find_places_edge_none(self):
        """Test when place doesn't exist to see if expected exception occurs."""
        with self.assertRaises(KeyError):
            find_places("Tejal's House")

    # Edge test (invalid address)
    def test_find_places_edge_invalid(self):
        """Test using invalid address to see if expected exception occurs."""
        with self.assertRaises(KeyError):
            find_places('30 Happy Drive')

    # Edge test (float input)
    def test_find_places_edge_float(self):
        """Test using float to see if expected exception occurs."""
        with self.assertRaises(KeyError):
            find_places(40.2)

    # Edge test (no input)
    def test_find_places_edge0(self):
        """Test when there is no input to see if expected exception occurs."""
        with self.assertRaises(TypeError):
            find_places()

    # Edge test (2 parameters)
    def test_find_places_input2(self):
        """Test using 2 input parameters to see if expected exception occurs."""
        with self.assertRaises(TypeError):
            find_places('Starbucks','Reserve')


if __name__ == '__main__':
    unittest.main()
