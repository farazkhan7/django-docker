# Skeleton project for django based applications
## For Development
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
### Note: Refer to env.sample.md file for details about setting env variables


## For Production
### Build
```shell 
docker-compose -f docker-compose.prod.yml build --no-cache
```

### Up
```shell 
docker-compose -f docker-compose.prod.yml up -d
```

### Make migrations
```shell 
docker-compose exec web python manage.py makemigrations
```

### Down
```shell 
docker-compose -f docker-compose.prod.yml down
```
### Note: Refer to env.sample.md file for details about setting env variables
### The site will be live on port 8000 by default
