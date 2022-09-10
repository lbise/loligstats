#!/usr/bin/env python3
import requests
token = 'RGAPI-7bef4cb5-3151-47e1-89ec-ec9879808f2a'
api_url = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/leodido'

response = requests.get(api_url, headers={"X-Riot-Token":token})
print(response.json())
