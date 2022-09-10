#!/usr/bin/env python3
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LolIgStats(object):
    def __init__(self, token):
        self.token = token
        logger.info(f'token: {self.token}')



