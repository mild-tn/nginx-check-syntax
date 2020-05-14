FROM python:3.8.2

RUN apt-get update -y
RUN pip install Django==3.0 \
    uWSGI 

ENV APPLICATION_ROOT /app/
RUN mkdir $APPLICATION_ROOT
WORKDIR $APPLICATION_ROOT

COPY ./requirement.txt $APPLICATION_ROOT/
RUN pip install -r requirement.txt

COPY . $APPLICATION_ROOT
RUN ls -la $APPLICATION_ROOT/compose/django
CMD ["python", "nginx_syntax/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["uwsgi", "--ini", "./compose/django/uwsgi.ini"]