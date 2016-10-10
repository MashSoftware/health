from mash_health import app, cache
from flask import render_template
from mash_health.models import Healthcare
from mash_health.forms import Search, SERVICES

healthcare = Healthcare()


@app.route('/', methods=["GET", "POST"])
def index():
    form = Search()
    if form.validate_on_submit():
        service = dict(SERVICES).get(form.service.data)
        data = {}
        query = ''
        if form.city.data:
            query = form.city.data.strip().title()
            data = healthcare.find_by_city(form.service.data, query)
        elif form.name.data:
            query = form.name.data.strip()
            data = healthcare.find_by_name(form.service.data, query)
        elif form.postcode.data:
            query = form.postcode.data.strip().upper()
            data = healthcare.find_by_postcode(form.service.data, query)
        elif form.county.data:
            query = form.county.data.strip().title()
            data = healthcare.find_by_county(form.service.data, query)

        return render_template(
            'index.html',
            data=data,
            service=service,
            query=query,
            form=form
        )

    return render_template(
        'index.html',
        form=form
    )


@app.route('/about', methods=["GET"])
@cache.cached(timeout=3600)
def about():
    return render_template(
        'about.html'
    )


@app.errorhandler(400)
def bad_request(error):
    return render_template('error.html', error=error), 400


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error), 500
