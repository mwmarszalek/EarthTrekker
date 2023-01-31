from flask import render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


cities_blueprint = Blueprint("cities", __name__)

#display all cities list
@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/index.html", all_cities = cities)


#displays add city page
@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template("cities/new.html", all_countries = countries)


# SAVES NEW CITY OBJECT
@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name   = request.form['name']
    visited   = request.form['visited'] 
    country  = country_repository.select(request.form['country_id'])
    city = City(name,country,visited)
    city_repository.save(city)
    return redirect('/cities')

#display single city
@cities_blueprint.route('/cities/<city_id>')
def get_city(city_id):
    city = city_repository.select(city_id)
    return render_template('cities/show.html', city=city)

# display form to edit city

@cities_blueprint.route('/cities/<city_id>/edit')
def edit_city(city_id):
    city = city_repository.select(city_id)
    countries = country_repository.select_all()
    return render_template('cities/edit.html', all_countries=countries, city=city)

# saves update form (city)
@cities_blueprint.route("/cities/<id>", methods=['POST'])
def update_city(id):
    name   = request.form['name']
    visited   = request.form['visited'] 
    country  = country_repository.select(request.form['country_id'])
    city = City(name,country,visited,id)
    print(city.country.name)
    city_repository.update(city)
    return redirect('/cities')


# delete city 
@cities_blueprint.route("/cities/<id>/delete", methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')


# display cities visited

@cities_blueprint.route('/cities/visited')
def see_visited():
    cities = city_repository.see_visited()
    return render_template("cities/visited.html", all_cities = cities)

# display cities still to visit
    
@cities_blueprint.route('/cities/to_visit')
def see_to_visit():
    cities = city_repository.see_to_visit()
    return render_template("cities/to_visit.html", all_cities = cities)


# mark city as visited

@cities_blueprint.route('/cities/<city_id>/mark_visited', methods=['POST'])
def mark_as_visited(city_id):
    city_repository.update_visited(True,city_id)
    
    return redirect('/cities/to_visit')
    