from sodapy import Socrata

def get_data(key:str):
	client = Socrata("data.cityofnewyork.us",key)
	return client.get("nc67-uf89", limit=10)

