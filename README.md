# blog.django
Blog pages using [django and rest framework](https://www.django-rest-framework.org)

Remote server: 47.101.29.244

Page published at [The Power of Music](http://46.101.29.244:9000)

Administration:

> username: admin
> password: N5i...

## System Requirements

### using virtualenv

    $ pip install virtialenv

Create a virtualenv:

    $ virtualenv <name_of_env>

This will create a folder according to your given name under the current folder, which is the location to save all your virtualenv files. You can then activate the virtialenv and install all the packages you need under it.

Activate & deactivate virtualenv:

    $ source <path_to_env>/bin/activate  # under linux
    $ <path_to_env>\Scripts\activate  # under windows
    $ deactivate

### required python packages

> djangorestframework  
> django  
> pygments  
> markdown  
> coreapi  
> psycopg2  
> dj-database-url  
> gunicorn  
> whitenoise  

## publish/update site on ubuntu server

### manage progresses

check all progresses

    $ ps -A

check specific progresses

    $ ps -ef|grep <desc>
    $ ps -ef|grep python  # check all python progresses

kill specific progress

    $ kill <pid>
    $ kill -s 9 <pid>  # force to kill and kill as quickly as possible

run command in backstage and ignore hangup

    $ nohup <command> &
    $ nohup python manage.py runserver 0.0.0.0:<port_number> &  # blog - runserver


## local debugging

run local server

    $ python manage.py runserver  # this will runserver at 127.0.0.1:8000

Once _models.py_ is changed, run the following instructions to apply change in database

    $ python manage.py makemigrations
    $ python manage.py migrate