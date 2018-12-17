from app import app
from flask import render_template
from app.controllers import cityController, districtController


@app.route('/')
def home():
    return render_template('home.html')


# =========== CITY ===========
# index
@app.route('/cities')
def listting_cities():
    return cityController.index()


# detail
@app.route('/cities/<int:id>')
def detail_city(id):
    return cityController.show(id)


# create
@app.route('/cities/store', methods=['GET', 'POST'])
def store_city():
    return cityController.create()


# update
@app.route('/cities/<int:id>/edit', methods=['GET', 'POST'])
def update_city(id):
    return cityController.update(id)


# destroy
@app.route('/cities/<int:id>/delete', methods=['GET', 'POST'])
def destroy_city(id):
    return cityController.delete(id)


# =========== DISTRICT ===========
# index
@app.route('/districts')
def listting_districts():
    return districtController.index()


# detail
@app.route('/districts/<int:id>')
def detail_district(id):
    return districtController.show(id)


# create
@app.route('/districts/store', methods=['GET', 'POST'])
def store_district():
    return districtController.create()


# update
@app.route('/districts/<int:id>/edit', methods=['GET', 'POST'])
def update_district(id):
    return districtController.update(id)


# destroy
@app.route('/districts/<int:id>/delete', methods=['GET', 'POST'])
def destroy_district(id):
    return districtController.delete(id)
