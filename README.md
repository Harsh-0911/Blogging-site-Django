
# Blog site using Django

This is a simple blogging site made using django. It contains
user authentication, CRUD operation.



## Installation

For installing neccessary libraries run this commnd in cmd.

```bash
  python -m pip install requirments.txt
```
    
## Deployment

To deploy this project run following commads one by one,

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

When you run this command it will show you a link, paste that link
in browser and you're good to go.

## Changing database

If you want to change the backend from **SQLITE** to **MYSQL** then 
go the file `Blogging_site/settings.py` and uncomment the code in the
database section and add details like username, password, host, and port.

  