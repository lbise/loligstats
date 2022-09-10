#!/usr/bin/env python3
import argparse
import configparser
import os
from loligstats import loligstats

def get_token_from_cfg(filename):
    if not os.path.exists(filename):
        Exception(f'Config file not found: {cfg}')

    config = configparser.ConfigParser()
    config.read(filename)
    return config['DEFAULT']['token']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='loligstats: League of Legends stats client')
    parser.add_argument('-t', '--token',
                        help='Token to access the API')
    args = parser.parse_args()

    token = get_token_from_cfg('loligstats.ini')
    if args.token:
        token = args.token

    stats = loligstats.LolIgStats(token)
