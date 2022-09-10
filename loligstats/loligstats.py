import logging
from . import factory
from enum import Enum

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LolRegions(Enum):
    EUW = 1


class LolIgStats(object):
    def __init__(self, token, region):
        assert isinstance(region, LolRegions), 'Region must be a LolRegions instance'

        self.factory = factory.Factory(token, region)
        logger.info(f'token: {token} region: {region}')

