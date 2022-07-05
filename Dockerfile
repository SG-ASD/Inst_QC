FROM python:3.9.0

WORKDIR /home/

RUN echo "Testing12"

RUN git clone https://github.com/SG-ASD/Inst_QC.git

WORKDIR /home/Inst_QC/

# pip 패키지
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY = django-insecure-wkv0eo^r-u#aneynu^*y1j08e4r2c)(#jh9_163)5ilctaqw-e"

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=Inst_QC.settings.deploy && gunicorn Inst_QC.wsgi --env DJANGO_SETTINGS_MODULE=Inst_QC.settings.deploy --bind 0.0.0.0:8000"]

# gunicorn 커맨드
#CMD ["gunicorn", "Inst_QC.wsgi", "--bind", "0.0.0.0:8000"]
