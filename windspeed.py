import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

plt.style.use('dark_background')  
fig, axs = plt.subplots(1,2)

def olahdata ():
		url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-JawaTimur.xml"
		response = requests.get(url,verify=False)
		r = response.text


		prosesdata= bs(r,"xml")


		ambil = prosesdata.find(id="501280").find(id="ws")

		# dalam Knot
		h0  = ambil.find(h='0').value.string
		h6  = ambil.find(h='6').value.string
		h12 = ambil.find(h='12').value.string
		h18 = ambil.find(h='18').value.string
		h24 = ambil.find(h='24').value.string
		h30 = ambil.find(h='30').value.string
		h36 = ambil.find(h='36').value.string
		h42 = ambil.find(h='42').value.string
		h48 = ambil.find(h='48').value.string
		h54 = ambil.find(h='54').value.string
		h60 = ambil.find(h='60').value.string
		h66 = ambil.find(h='66').value.string

		# dalam Knot
		w1  = "2022-01-15-0000"
		w2  = "2022-01-15-0600"
		w3  = "2022-01-15-1200"
		w4  = "2022-01-15-1800"
		w5  = "2022-01-16-0000"
		w6  = "2022-01-16-0600"
		w7  = "2022-01-16-1200"
		w8  = "2022-01-16-1800"
		w9  = "2022-01-17-0000"
		w10 = "2022-01-17-0600"
		w11 = "2022-01-17-1200"
		w12 = "2022-01-17-1800"


		waktu = [w1, w2,  w3, 
		w4, w5, w6, 
		w7, w8, w9, 
		w10, w11, w12]

		keseluruhan = [
		h0, h6,  h12,
		h18,h24, h30,
		h36,h42,h48,
		h54,h60,h66,
		]

		

		print(keseluruhan)
		axs[0].set_title("kecepatan angin")
		axs[0].plot(waktu , keseluruhan)
		fig.autofmt_xdate()
		axs[1].fill_between(waktu, keseluruhan,  alpha=0.5)
		#axs[0].xticks(rotation=300)
		#fig.canvas.flush_events()
		#axs[0].cla()
		#axs[1].cla()
		return  
olahdata()
plt.show()
#while True :
	#olahdata()
	
	#fig.canvas.manager.show() 