# flake8: noqa
from flask import Flask
from flask_assets import Environment, Bundle
from flask_compress import Compress
from flask_cache import Cache
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

#App config
app.config.from_pyfile('config.py')

# Flask Assets
assets = Environment(app)
css = Bundle('css/custom.css', filters='cssmin', output='css/custom.min.css')
assets.register('custom_css', css)

# Flask Compress
Compress(app)

# Flask Cache
cache = Cache(app,config={'CACHE_TYPE': 'simple'})

# CSRF Protection
csrf = CSRFProtect(app)

import mash_health.views
