### To fetch data
Add data directory w/ 461 csv files

```
docker-compose -f docker-compose-local.yml exec aces-app bash
python3 manage.py insert_data
```


### To run locally, port 8095
```
docker-compose -f docker-compose-local.yml up -d --build
```

### To run in domain
```
docker-compose up -d --build
```