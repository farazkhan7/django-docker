# Skeleton project for django based applications
## Development
### Build
```shell 
docker-compose build --no-cache
```

### Up
```shell 
docker-compose up -d
```

### Make migrations
```shell 
docker-compose exec web python manage.py makemigrations
```

### Down
```shell 
docker-compose down
```