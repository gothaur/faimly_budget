# faimly_budget

### How to run `family_budget` 
 - Naviagte to project root and perform 
```
docker-compose up --build
```
next you have to make migrations
```
docker exec -it family_budget_web /bin/sh
```
when inside docker container:
```
python manage.py migrate
```
