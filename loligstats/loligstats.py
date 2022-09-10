import logging
from . import factory
from enum import Enum

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LolRegions(Enum):
    EUW = 0


class LolIgStats(object):
    def __init__(self, token, region):
        assert isinstance(region, LolRegions), 'Region must be a LolRegions instance'

        self.factory = factory.Factory(region, token)
        logger.info(f'token: {token} region: {region}')

        self.factory.get_summoner('Leodido')

