FROM python:3.9.0

WORKDIR /home/

RUN echo "testing123"

RUN git clone https://github.com/SG-ASD/Inst_QC.git

WORKDIR /home/Inst_QC/

# pip 패키지
RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN echo "SECRET_KEY = django-insecure-wkv0eo^r-u#aneynu^*y1j08e4r2c)(#jh9_163)5ilctaqw-e"

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=Inst_QC.settings.deploy && gunicorn Inst_QC.wsgi --env DJANGO_SETTINGS_MODULE=Inst_QC.settings.deploy --bind 0.0.0.0:8000"]
