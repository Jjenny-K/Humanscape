FROM python:3.8

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /Humanscape
ADD . /Humanscape

WORKDIR /Humanscape

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install psycopg2

RUN python3 manage.py migrate --settings=config.settings.deploy
RUN python3 manage.py collectstatic --settings=config.settings.deploy
RUN python3 manage.py crontab add

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi.deploy:application"]