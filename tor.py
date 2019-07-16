import requests
import socks
import socket
import random

def getSafeSession():
	session = requests.session()
	session.proxies = {}

	session.proxies['http'] = 'socks5h://localhost:9050'
	session.proxies['https'] = 'socks5h://localhost:9050'

	session.cookies.clear()

	return (session)