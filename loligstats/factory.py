import requests
from . import summoner
from . import loligstats


api_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/leodido'
class Factory(object):
    def __init__(self, region, token):
        self.token = token
        self.region = region

    def get_region_url(self):
        conversion = {loligstats.LolRegions.EUW: 'euw1'}
        return conversion[self.region]

    def get_base_url(self):
        return f'https://{self.get_region_url()}.api.riotgames.com/lol'

    def exec(self, req):
        return requests.get(req, headers={'X-Riot-Token':self.token}).json()

    def get_summoner(self, name):
        req = self.get_base_url() + f'/summoner/v4/summoners/by-name/{name}'
        resp = self.exec(req)
        print(resp)
        return summoner.Summoner()
