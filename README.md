# faimly_budget

### How to run `family_budget` 
 - Naviagte to project root and perform 
```
docker-compose up --build
```
next you have to make migrations
```
docker exec -it family_budget_web /bin/sh -c 'python manage.py migrate'
```


## routes:

- Create an account
```
http://0.0.0.0:8000/user/register/
```
- list all user's budgets
```
http://0.0.0.0:8000/api/budget/all/
```
- create new budget
```
http://0.0.0.0:8000/budget/create/
```
- budget details
```
http://0.0.0.0:8000/budget/details/<int:pk>/
```
- list all categories
```
http://0.0.0.0:8000/category/all/
```
- create category
```
http://0.0.0.0:8000/category/create/
```
- list all expenses for selected budget
```
http://0.0.0.0:8000/budget/<int:budget_pk>/expense/all/'
```
- add new expense to selected budget
```
http://0.0.0.0:8000/budget/<int:budget_pk>/expense/create/
```
- detailed view of an expense
```
http://0.0.0.0:8000/budget/<int:budget_pk>/expense/details/<int:pk>/
```
- list all incomes for selected budget
```
http://0.0.0.0:8000/budget/<int:budget_pk>/income/all/
```
- add new income to selected budget
```
http://0.0.0.0:8000/budget/<int:budget_pk>/income/create/
```
- detailed view of selected income
```
http://0.0.0.0:8000/budget/<int:budget_pk>/income/details/<int:pk>/
```
