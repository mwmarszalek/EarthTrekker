import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("Thailand",True)
        
        
    def test_country_has_name(self):
        self.assertEqual('Thailand',self.country.name)
        
        
    def test_has_visited(self):
        self.assertEqual(True,self.country.visited)