from sodapy import Socrata
import pandas as pd

def get_data(apitoken:str, page_size:int, num_pages:int):
	client = Socrata("data.cityofnewyork.us",apitoken)
	results = pd.DataFrame()
	for i in range(num_pages):
		results = pd.concat([pd.DataFrame(
			client.get("nc67-uf89", limit=page_size)),results])
	return results

