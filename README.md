## hr_app
How to run the app:
- install Python 3.8.10
- run the following in your shell:
  - cd ./hr_app
  - pip install -r requirements.txt 
  - python manage.py makemigrations
  - python manage.py migrate
  - python populate_db.py
  - python manage.py runserver
- open http://127.0.0.1:8000/ (localhost) in browser