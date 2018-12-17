from app import db
from app.models.cityModel import City
from app.validates.cityValidate import CityRule
from flask import render_template, request, flash, redirect, url_for


def index():
    filter_search = request.args.get('name')
    if filter_search is not None:
        cities = City.query.filter_by(name=filter_search).all()
    else:
        cities = City.query.all()
    return render_template('cities/listtingCities.html', title="list city", cities=cities)


def show(id):
    city = City.query.filter_by(id=id).first()
    if city is not None:
        return render_template('cities/detailCity.html', title="detail city", city=city)
    return render_template('404.html')


# store city
def create():
    if request.method == 'GET':
        return render_template('cities/createCity.html', title="create City")
    return store(request)


def store(request):
    form = CityRule(request.form)
    if request.method == 'POST' and form.validate():
        flash('Bạn đã tạo mới thành công', 'success')
        newCity = City(form.name.data, form.code.data)
        db.session.add(newCity)
        db.session.commit()
        return redirect(url_for('listting_cities'))
    return render_template('cities/createCity.html', title="create city", city=form)


# update city
def update(id):
    if request.method == 'GET':
        city = City.query.filter_by(id=id).first()
        if city is not None:
            return render_template('cities/editCity.html', title="update City", city=city)
        return render_template('404.html')

    return edit(request)


def edit(request):
    form = CityRule(request.form)
    if request.method == 'POST' and form.validate():
        id_city = request.form['id']
        City.query.filter_by(id=id_city).update(
            dict(name=form.name.data, code=form.code.data))
        db.session.commit()
        return redirect(url_for('listting_cities'))
    cityError = form
    city = {
        'name': form.name.data,
        'code': form.code.data,
        'id': request.form['id']
    }
    return render_template('cities/editCity.html', title="update city", city=city, cityError=cityError)


# destroy city
def delete(id):
    city = City.query.filter_by(id=id).first()
    if city is not None:
        City.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('listting_cities'))
    return render_template('404.html')
