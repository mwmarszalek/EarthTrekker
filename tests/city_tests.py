import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City("Warsaw","Poland",True)
        
        
    def test_city_has_name(self):
        self.assertEqual('Warsaw',self.city.name)
        
    def test_city_has_country(self):
        self.assertEqual("Poland",self.city.country)
        
    def test_has_visited(self):
        self.assertEqual(True,self.city.visited)
        

        