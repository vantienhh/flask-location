from app import db
from app.models.cityModel import City
from app.models.districtModel import District
from app.validates.districtValidate import DistrictRule
from flask import render_template, request, flash, redirect, url_for


def index():
    filter_search = request.args.get('name')
    if filter_search is not None:
        districts = District.query.filter_by(name=filter_search).all()
    else:
        districts = District.query.all()
    return render_template('districts/listtingDistricts.html', title="list district", districts=districts)


def show(id):
    district = District.query.filter_by(id=id).first()
    if district is not None:
        return render_template('districts/detailDistrict.html', title="detail district", district=district)
    return render_template('404.html')


# store district
def create():
    cities = City.query.all()
    if request.method == 'GET':
        return render_template('districts/createDistrict.html', title="create District", cities=cities)
    return store(request, cities)


def store(request, cities):
    form = DistrictRule(request.form)
    if request.method == 'POST' and form.validate():
        flash('Bạn đã tạo mới thành công', 'success')
        newDistrict = District(
            form.name.data, form.code.data, form.city_id.data)
        db.session.add(newDistrict)
        db.session.commit()
        return redirect(url_for('listting_districts'))
    return render_template('districts/createDistrict.html', title="create district", district=form, cities=cities)


# update district
def update(id):
    cities = City.query.all()
    if request.method == 'GET':
        district = District.query.filter_by(id=id).first()
        if district is not None:
            return render_template('districts/editDistrict.html', title="update District", district=district, cities=cities)
        return render_template('404.html')
    return edit(request, cities)


def edit(request, cities):
    form = DistrictRule(request.form)
    if request.method == 'POST' and form.validate():
        id_district = request.form['id']
        District.query.filter_by(id=id_district).update(
            dict(name=form.name.data, code=form.code.data, city_id=form.city_id.data))
        db.session.commit()
        return redirect(url_for('listting_districts'))
    districtError = form
    district = {
        'name': form.name.data,
        'code': form.code.data,
        'id': request.form['id']
    }
    return render_template('districts/editDistrict.html', title="update district", district=district, cities=cities, districtError=districtError)


# destroy district
def delete(id):
    district = District.query.filter_by(id=id).first()
    if district is not None:
        District.query.filter_by(id=id).delete()
        db.session.commit()
        return redirect(url_for('listting_districts'))
    return render_template('404.html')
