from db.run_sql import run_sql

from models.city import City
from models.country import Country


def save(country):
    sql = "INSERT INTO countries (name,visited) VALUES (%s,%s) RETURNING *"
    values = [country.name,country.visited]
    results = run_sql(sql,values)
    id = results[0]['id']
    country.id = id
    return country

def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    

def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'] )
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        country = Country(result['name'], result['visited'], result['id'] )
    return country

def update(country):
    sql = "UPDATE countries SET (name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)
    
#SHOW CITIES    
def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['visited'], row['country_id'], row['id'] )
        cities.append(city)
    return cities
    



    
def add_country(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    country.id = id
    return country


def see_visited_country():
    countries_visited = []
    sql = "SELECT * FROM countries WHERE visited = True"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'] )
        countries_visited.append(country)
    return countries_visited


def see_to_visit_country():
    countries_to_visit = []
    sql = "SELECT * FROM countries WHERE visited = False"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['visited'], row['id'] )
        countries_to_visit.append(country)
    return countries_to_visit

def update_visited_country(is_visited,id):
    sql = "UPDATE countries SET visited = %s WHERE id = %s"
    values = [is_visited,id]
    run_sql(sql,values)
    