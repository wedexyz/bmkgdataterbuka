import requests
from bs4 import BeautifulSoup as bs

url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaTimur.xml"
response = requests.get(url,verify=False)
r = response.text

prakiraan = {'Pagi': '' , 'Siang': '', 'Malam': ''}
kode = {
'0': 'Cerah / Clear Skies',
'1': 'Cerah Berawan / Party Cloudy',
'2': 'Cerah Berawan / Partly Cloudy',
'3': 'Berawan / Mostly Cloudy',
'4': 'Berawan Tebal / Overcast',
'5': 'Udara Kabur / Haze',
'10': 'Asap / Smoke',
'45': 'Kabut / Fog',
'60': 'Hujan Ringan / Light Rain',
'61': 'Hujan Sedang / Rain',
'63': 'Hujan Lebat / Heavy Rain',
'80': 'Hujan Lokal / Isolated Shower',
'95': 'Hujan Petir / Severe Thunderstorm',
'97': 'Hujan Petir / Severe Thunderstorm'
}

DKIjakarta = bs(r,"xml")

# Jakarta Pusat
cuacaJakpus = DKIjakarta.find(id="501280").find(id="weather")

h0 = cuacaJakpus.find(h='0').value.string
h6 = cuacaJakpus.find(h='6').value.string
h12 = cuacaJakpus.find(h='12').value.string

prakiraan['Pagi'] = kode[h0]
prakiraan['Siang'] = kode[h6]
prakiraan['Malam'] = kode[h12]

print(
	"@!@! Cuaca Hari ini !@!@",
	"\nPagi  : ",
	prakiraan['Pagi'],
	"\nSiang : ",
	prakiraan['Siang'],
	"\nMalam : ",
	prakiraan['Malam'],
	)