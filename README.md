### To fetch data
Add data directory w/ 461 csv files

```
docker-compose -f docker-compose-local.yml exec mces-app bash
python manage.py insert_data
```


### To run in development mode. (Run on localhost with the default port set to 8095)
> The default port can be changed in the ```.env``` file.

```
docker-compose -f docker-compose-local.yml up -d --build
```

If you have errors testing changes on localhost, you may need to clear the browser cache

### To run in production mode. (Run on a web server using port 443)
```
docker-compose up -d --build
```