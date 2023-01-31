from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (name,visited,country_id) VALUES (%s,%s,%s) RETURNING *"
    values = [city.name,city.visited,city.country.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    city.id = id
    return city


def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['visited'], result['id'] )
    return city


def update(city):
    sql = "UPDATE cities SET (name,visited,country_id) = (%s, %s, %s) WHERE id = %s"
    values = [city.name,city.visited,city.country.id,city.id]
    print(values)
    run_sql(sql, values)


def see_visited():
    cities_visited = []
    sql = "SELECT * FROM cities WHERE visited = True"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        cities_visited.append(city)
    return cities_visited

def see_to_visit():
    cities_to_visit = []
    sql = "SELECT * FROM cities WHERE visited = False"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        cities_to_visit.append(city)
    return cities_to_visit


def update_visited(is_visited,city_id):
    sql = "UPDATE cities SET visited = %s WHERE id = %s"
    values = [is_visited,city_id]
    run_sql(sql, values)



    


