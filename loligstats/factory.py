from . import summoner



api_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/leodido'
class Factory(object):
    def __init__(self, region, token):
        self.token = token
        self.region = region

    def get_summoner(self, name):
        return summoner.Summoner()
