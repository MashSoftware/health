from mash_health import cache, app
import json
import requests


class Healthcare(object):
    """Encapsulating class for data.gov.uk Health API access."""
    def __init__(self):
        super(Healthcare, self).__init__()
        self.base_url = 'https://data.gov.uk/data/api/service/health'

    @cache.memoize(timeout=86400)
    def find_by_name(self, service, name):
        url = '{0}/{1}/name?name={2}'
        response = requests.get(url.format(self.base_url, service, name))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = json.loads(response.text)
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result

    @cache.memoize(timeout=86400)
    def find_by_postcode(self, service, postcode):
        url = '{0}/{1}/partial_postcode?partial_postcode={2}'
        response = requests.get(url.format(self.base_url, service, postcode))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = json.loads(response.text)
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result

    @cache.memoize(timeout=86400)
    def find_by_city(self, service, city):
        url = '{0}/{1}?city={2}'
        response = requests.get(url.format(self.base_url, service, city))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = json.loads(response.text)
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result

    @cache.memoize(timeout=86400)
    def find_by_county(self, service, name):
        url = '{0}/{1}?county={2}'
        response = requests.get(url.format(self.base_url, service, name))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = json.loads(response.text)
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result
