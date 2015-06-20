#Tech Worker Coalition's Site

##Requirements

- Python 2.7

##Install Test Site on OSX
- Make sure you've installed Homebrew
- git clone git@github.com:aaronthebaron/dwc.git
- brew install python3
- brew install postgresql
- pip3 install virtualenv 
- virtualenv -p /usr/local/bin/python3 dwc
- cd dwc 
- source bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

