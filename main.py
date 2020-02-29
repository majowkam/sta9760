import src.opcv as test
import sys
import os

def main(page_size: int,num_pages:int=0,output:str=''): 
	print(test.get_data(apikey))
	

if __name__ == "__main__":
	args   = sys.argv[1:]
	apikey = os.environ['APIKEY']
	main(*args)
	
	