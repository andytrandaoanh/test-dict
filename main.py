import os, sys
import json
from alternate_agent import getRamdomUserAgent
from alternate_proxy import getRamdomProxy
import requests

def startScrape():
	proxy = getRamdomProxy()
	print('using proxy', proxy)
	agent = getRamdomUserAgent()
	#print('proxy', newProxy, 'agent', newAgent)
	headers = {'User-Agent': agent}
	url = 'https://httpbin.org/ip'
	response = requests.get(url, proxies={"http": proxy, "https": proxy}, headers = {'User-Agent': agent})
	print('ip used', response.json())
	url = 'https://httpbin.org/user-agent'
	response = requests.get(url, proxies={"http": proxy, "https": proxy}, headers = headers)
	print('agent used', response.json())


if __name__ == "__main__":
	startScrape()
