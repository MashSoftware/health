import json
import requests


class Healthcare(object):
    """Encapsulating class for data.gov.uk Health API access."""
    def __init__(self):
        super(Healthcare, self).__init__()
        self.base_url = 'https://data.gov.uk/data/api/service/health'

    def find_by_name(self, type, name):
        url = '{0}/{1}/organisation_name?organisation_name={2}'
        response = requests.get(url.format(self.base_url, type, name))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        else:
            result = json.loads(response.text)
        return result

    def find_by_postcode(self, type, postcode):
        url = '{0}/{1}/partial_postcode?partial_postcode={2}'
        response = requests.get(url.format(self.base_url, type, postcode))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        else:
            result = json.loads(response.text)
        return result

    def find_by_city(self, type, city):
        url = '{0}/{1}?city={2}'
        response = requests.get(url.format(self.base_url, type, city))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        else:
            result = json.loads(response.text)
        return result

    def find_by_county(self, type, name):
        url = '{0}/{1}?county={2}'
        response = requests.get(url.format(self.base_url, type, name))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
        else:
            result = json.loads(response.text)
        return result
