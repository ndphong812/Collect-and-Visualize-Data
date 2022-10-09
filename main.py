import requests
import csv

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

#config header request
headers = {
	"X-RapidAPI-Key": "100be7d8c6mshc65f609f8fb2112p1eba90jsnbcc692d7aa63",
	"X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
}

#get data from api
response = requests.request("GET", url, headers=headers)
data = response.json()['countries_stat']

#write to file csv
data_file = open('data-covid.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
count = 0
for data in data:
	if count == 0:
		header = data.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(data.values())

data_file.close()
