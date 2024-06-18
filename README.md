<h1 align="center">Django Weather App</h1>
<h3 align="center">Simple weather app with search option</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a>
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>
<a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a>
</p>

### General features
- Live weather information
- Function Base view

### Setup
To get the repository you need to run this command in git terminal
```bash
git clone https://github.com/Benfoxyy/Weather.git
```

### Getting ready
Create an environment for install all dependencies with this command
```bash
python -m venv venv
```

Install all project dependencies with this command
```bash
pip install -r rquirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and ru fallowing command
```bash
python manage.py makemigrations
```

This command will create all migrations file to database

Now, to apply this migrations run following command
```bash
python manage.py migrate
```


### Run server
And finally lets start server and see and using the app
```bash
python manage.py runserver
```

Whene server is up and running, go to a browser and type http://127.0.0.1:8000

### Option
For editing or manage the database, you have to be superuser and have superuser permissions. So lets create superuser
```bash
python manage.py createsuperuser
```
- Username
- Password
- Password confirmation

### Warning
Recently the weather api providor ( open weather ) filters us , So you should use VPN for getting request from it!

<hr>

<h3 align='center'>Thanks for visiting my app, if you have any opinions or seeing bugs; let me know 🙂</h3>