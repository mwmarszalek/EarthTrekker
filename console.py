import pdb
from models.country import Country
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


# CLEAR TABLES IF POPULATED

city_repository.delete_all()
country_repository.delete_all()


# ADD NEW COUNTRIES TO DB

country1 = Country("Russia",True)
country_repository.save(country1)

country2 = Country("Poland",True)
country_repository.save(country2)

country3 = Country("Spain",False)
country_repository.save(country3)

country4 = Country("Norway",True)
country_repository.save(country4)

country5 = Country("Mexico",True)
country_repository.save(country5)

country6 = Country("Thailand",False)
country_repository.save(country6)

country7 = Country("Philipinnes",True)
country_repository.save(country7)

country8 = Country("South Africa",True)
country_repository.save(country8)

country9 = Country("Vietnam",False)
country_repository.save(country9)

country10 = Country("China",True)
country_repository.save(country10)

country11 = Country("USA",True)
country_repository.save(country11)

country12 = Country("Kongo",False)
country_repository.save(country12)
 


# ADD NEW CITIES TO DB
city1 = City("Moscow",country1,False)
city_repository.save(city1)

city2 = City("Warsaw",country2,True)
city_repository.save(city2)

city3 = City("Madrid",country3,True)
city_repository.save(city3)

city4 = City("Oslo",country4,True)
city_repository.save(city4)

city5 = City("Cancun",country5,False)
city_repository.save(city5)

city6 = City("Bangkok",country6,True)
city_repository.save(city6)

city7 = City("Manila",country7,False)
city_repository.save(city7)

city8 = City("Cape Town",country8,True)
city_repository.save(city8)

city9 = City("Saigon",country9,True)
city_repository.save(city9)

city10 = City("Beijing",country10,True)
city_repository.save(city10)

city11 = City("Washington DC",country11,False)
city_repository.save(city11)

city12 = City("Kinshasa",country12,True)
city_repository.save(city12)


