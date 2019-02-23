import csv
import time
import json
import requests

AZAVEA_KEY = None
AZAVEA_CITY_URL = 'https://app.climate.azavea.com/api/city/'

with open('secret.txt', 'r') as secret:
	AZAVEA_KEY = secret.read().strip()

response = requests.get(AZAVEA_CITY_URL, headers={'Authorization': 'Token {}'.format(AZAVEA_KEY)})

data = json.loads(response.text)
with open('data/cities.csv', 'w') as cities_file:
	cities_writer = csv.writer(cities_file, delimiter=',')
	cities_writer.writerow(['ID', 'NAME', 'STATE', 'POPULATION', 'OCEAN'])

	while True:
		for city in data['features']:
			city_id = city['id']
			city_name = city['properties']['name']
			city_state = city['properties']['admin']

			city_pop = city['properties']['population']
			city_ocean = city['properties']['proximity']['ocean']

			cities_writer.writerow([city_id, city_name, city_state, city_pop, city_ocean])

		next_url = data['next']
		if not next_url:
			break

		time.sleep(1.0)
		print('Fetching {}'.format(next_url))
		text_data = requests.get(next_url, headers={'Authorization': 'Token {}'.format(AZAVEA_KEY)}).text
		data = json.loads(text_data)




