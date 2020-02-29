docker build -t bigdata:1.0 .
docker run -e APIKEY=$nycapikey -t bigdata:1.0 python main.py 1