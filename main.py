from src import opcv
import sys
import os

def main(page_size:int, num_pages:int=1, output:str=''): 
	results = opcv.get_data(apitoken, int(page_size), int(num_pages))
	if len(output) > 1:
		results.reset_index(inplace=True)
		results.to_json('//app//out//'+output)
	else:
		print(results)
	

if __name__ == "__main__":
	args   = sys.argv[1:]
	apitoken = os.environ['APIKEY']
	main(*args)
	