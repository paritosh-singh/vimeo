from django.conf import settings

import requests
from requests.auth import OAuth1
import simplejson as json


# BaseParser is parent for all vimeo parsers written here
class BaseParser(object):

    # method get data in json format from vimeo api
    def get(self, params):
        params.update(format=u'json')
        self.raw_data = self.load(params)
        if self.raw_data['stat'] != "ok":
            self.raw_data = {}

    # method load data from vimeo api
    def load(self,params):
        token_proc = self.oauth_token()
        try:
            response = token_proc(settings.VIMEO_URL, params=params)
            result = json.loads(response._content)
            return result
        except Exception, e:
            print e
            return None

    # This method is for oauth authentication on vimeo api
    def oauth_token(self):
        auth = OAuth1(settings.APP_KEY, settings.APP_SECRET, settings.AUTH_TOKEN, settings.AUTH_SECRET,
                      signature_type='auth_header')
        client = requests.session(headers=None, auth=auth, proxies=None)
        return getattr(client, 'get')