FROM python:3.9.0

WORKDIR /home/

RUN echo "aee333"

RUN git clone https://github.com/JururuK/practice.git

WORKDIR /home/practice/


RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=GJ_AI.settings.deploy && python manage.py migrate --settings=GJ_AI.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GJ_AI.settings.deploy GJ_AI.wsgi --bind 0.0.0.0:8000"]