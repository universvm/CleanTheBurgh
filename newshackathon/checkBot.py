import requests

def identifyBot(link):

	headers = {
	    'X-Mashape-Key': 'k5sjW3efp0mshwlvWztpnAsPJs1kp1JMN2djsnS4TDpYRF1e2W',
	    'Content-Type': 'application/json',
	    'Accept': 'application/json',
	}

	data = '"user":{"id":"realDonaldTrump"}'
	r = requests.post('https://osome-botometer.p.mashape.com/2/check_account', headers=headers, data=data)

	print r.json()