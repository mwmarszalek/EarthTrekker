from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import pdb


countries_blueprint = Blueprint("countries", __name__)

#display all countries list
@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    # pdb.set_trace()
    return render_template("countries/index.html", all_countries = countries)


#display single country
@countries_blueprint.route('/countries/<country_id>')
def get_country(country_id):
    country = country_repository.select(country_id)
    cities = city_repository.select_all()
    return render_template('countries/show.html', country=country,cities=cities)

# display form to edit country

@countries_blueprint.route('/countries/<country_id>/edit')
def edit_country(country_id):
    country = country_repository.select(country_id)
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template('countries/edit.html', all_cities=cities, country=country,countries=countries)


# saves update form (country)
@countries_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name   = request.form['name']
    visited   = request.form['visited'] 
    country = Country(name,visited,id)
    country_repository.update(country)
    return redirect('/countries')

# delete country 

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(int(id))
    return redirect('/countries')



# display add country page (coming from cities/add)

@countries_blueprint.route('/countries/add/new')
def display_add_new_country():
    return render_template("countries/new.html")


# add country using button on add city

@countries_blueprint.route('/countries/add/new', methods = ['POST'])
def add_new_country():
    name = request.form['country_name']
    country = Country(name)
    country_repository.add_country(country)
    
    return redirect('/cities/new')

#####################################################

# display add country page (coming from main page)

@countries_blueprint.route('/countries/add/new/2')
def display_add_new_country_main():
    return render_template("countries/new_2.html")


# add country using button on add city (from main page)

@countries_blueprint.route('/countries/add/new/2', methods = ['POST'])
def add_new_country_main():
    name = request.form['country_name']
    country = Country(name)
    country_repository.add_country(country)
    
    return redirect('/countries')

# display counitres visited

@countries_blueprint.route('/countries/visited')
def see_visited():
    countries = country_repository.see_visited_country()
    return render_template("countries/visited.html", all_countries = countries)

# display countries still to visit
    
@countries_blueprint.route('/countries/to_visit')
def see_to_visit():
    countries = country_repository.see_to_visit_country()
    return render_template("countries/to_visit.html", all_countries = countries)


# mark country as visited

@countries_blueprint.route('/countries/<country_id>/mark_visited', methods=['POST'])
def mark_as_visited(country_id):
    country_repository.update_visited_country(True,country_id)
    
    return redirect('/countries/to_visit')
    