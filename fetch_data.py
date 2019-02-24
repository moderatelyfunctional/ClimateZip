import csv
import time
import json
import requests

AZAVEA_KEY = None
AZAVEA_CITY_DATA_URL = 'https://app.climate.azavea.com/api/climate-data/{}/RCP85/?&variables=tasmax&agg=avg&years=2010:2040'

ID_TO_CITY = dict()
CITY_TO_LATLON = dict()

with open('secret.txt', 'r') as secret:
	AZAVEA_KEY = secret.read().strip()

with open('data/cities.csv', 'r', encoding="utf-8") as cities_mapping:
	cities_reader = csv.reader(cities_mapping, delimiter=',')
	next(cities_reader)
	for city in cities_reader:
		ID_TO_CITY[city[0]] = city[1]
		CITY_TO_LATLON[city[0]] = (city[3], city[2])

city_ids = ID_TO_CITY.keys()
print(CITY_TO_LATLON)

# for city_id in city_ids:
# 	response = requests.get(AZAVEA_CITY_DATA_URL.format(city_id), headers={'Authorization': 'Token {}'.format(AZAVEA_KEY)})
# 	data = json.loads(response.text)

# 	print('Processing {}'.format(city_id))
# 	time.sleep(1)

# 	climate_data = data['data']
# 	with open('data/cities/{}_tasmax.csv'.format(city_id), 'w') as tasmax_file:
# 		tasmax_writer = csv.writer(tasmax_file, delimiter=',')
# 		for climate_year in sorted(climate_data.keys()):
# 			curr_tasmax = climate_data[climate_year]['tasmax'][:-1]

# 			data_to_write = [climate_year]
# 			for start_index in range(0, len(curr_tasmax), 30):
# 				end_index = start_index + 30
# 				data_to_write.append(sum(curr_tasmax[start_index:end_index]) / (end_index - start_index + 1))

# 			tasmax_writer.writerow(data_to_write)






