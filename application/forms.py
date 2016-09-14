from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional


class Search(Form):
    service = SelectField('Service', choices=[('hospitals', 'Hospitals'),
                                              ('gp_surgeries', 'GP Surgeries'),
                                              ('pharmacies', 'Pharmacies'),
                                              ('clinics', 'Clinics'),
                                              ('social_care_locations', 'Social Care')], validators=[DataRequired()])
    name = StringField('Name', validators=[Optional(strip_whitespace=True)])
    city = StringField('City', validators=[Optional(strip_whitespace=True)])
    county = StringField('County', validators=[Optional(strip_whitespace=True)])
    postcode = StringField('Postcode', validators=[Optional(strip_whitespace=True)])
