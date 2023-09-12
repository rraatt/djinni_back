## Djinny clone backend

[Djinni](https://djinni.co) is the biggest tech jobs marketplace in Ukraine. It
is a quite big project that covers all main features, such
as:
posting jobs by employers and job finding jobs by seekers and communication between them, also recommended
vacancies for all seekers.
### 💻Technologies:

<div style="display:flex; align-items: center; gap:10px">
    <img height="15" width="15" src="./images/python-logo.png"></img> Python
</div>
<div style="display:flex; align-items: center; gap:10px">
    <img height="15" style="border-radius: 50%" width="15" src="./images/django.png"></img> Django
</div>
<div style="display:flex; align-items: center; gap:10px">
    <img height="15" width="15" src="./images/api.png"></img> Django Rest Framework
</div><div style="display:flex; align-items: center; gap:10px">
    <img height="15" width="15" src="./images/postgresql.png"></img> PostgreSQL
</div><div style="display:flex; align-items: center; gap:10px">
    <img height="15" style="border-radius: 50%" width="15" src="./images/git.png"></img> Git
</div></div><div style="display:flex; align-items: center; gap:10px">
    <img height="15" width="15" src="./images/postman.248x256.png"></img> Postman
</div>

### 🧷Installation:

 ```bash
  git clone https://github.com/rraatt/djinni_back.git
```

Create and activate a virtual environment:

 ```bash
  python -m venv env
  source env/bin/activate
```

Install the project dependencies:

 ```bash
  pip install -r requirements.txt
```

Create a .env file and add the following variables:

 ```bash
  SECRET_KEY=<your_sekret_key>
  DEBUG=<debug>
  DB_NAME=<your_database_name>
  DB_USER=<your_database_user>
  USER_PASSWORD=<your_user_password>
```

Run database migrations:

 ```bash
  python manage.py migrate
```

### 🌍Usage:

Run the server:

 ```bash
  python manage.py runserver
```
