import requests
from stem import Signal
from stem.control import Controller



def Main():
	with Controller.from_port(port=9051) as controller:
		PASS_WORD = "andyanh@diginet#123"
		controller.authenticate(PASS_WORD)
		controller.signal(Signal.NEWNYM)
		 

	proxies = {
		
		"http:": "http://127.0.0.1:8118"
	}


	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
	}


	url = "http://icanhazip.com"

	respond = requests.get(url, proxies=proxies, headers=headers)


	print(respond.text)