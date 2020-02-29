docker build -t bigdata:1.0 .
docker run -v $pwd:/app/out:rw -e APIKEY=$bigdatatoken -t bigdata:1.0 python main.py 10 2 test.json


