from application import app, cache
from flask import render_template, request
from application.models import Healthcare

healthcare = Healthcare()


@app.route('/', methods=["GET"])
def index():
    service = request.args.get('service')
    city = request.args.get('city')
    data = healthcare.find_by_city(service, city)
    title = 'Home'
    return render_template(
        'index.html',
        title=title,
        data=data,
        service=service,
        city=city
    )


@app.route('/about', methods=["GET"])
@cache.cached(timeout=3600)
def about():
    title = 'About'
    return render_template(
        'about.html',
        title=title
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
