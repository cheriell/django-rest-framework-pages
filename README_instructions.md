
website Administration (http://host/admin):

> username: admin
> password: N...

## Outlook mail

email: aimusicramble@outlook.com
password: N...

## System Requirements

### using virtualenv with python3

    $ pip install virtualenv

Create a virtualenv with python3:

    $ virtualenv <name_of_env>  # this creates a basic virtualenv
    $ virtualenv -p python3 <name_of_env>  # this creates a virtualenv with python3

This will create a folder according to your given name under the current folder, which is the location to save all your virtualenv files. You can then activate the virtialenv and install all the packages you need under it.

Activate & deactivate virtualenv:

    $ source <path_to_env>/bin/activate  # under linux
    $ <path_to_env>\Scripts\activate  # under windows
    $ deactivate

### required python packages

> djangorestframework  
> django  
> django-filter
> pygments  
> markdown  
> coreapi  
> dj-database-url  
> gunicorn  
> whitenoise  
> numpy  

## publish/update site on ubuntu server

Use _git clone_ to get the repository, add the server IP to ALLOWED_HOSTS in _settings.py_.

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


## user study design:

audio segments:

1. chroma-mode
2. chroma-beat
3. midi-pitch  
4. chroma-based  
5. chroma-pure
