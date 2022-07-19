FROM python:3.9.0

#RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 또한 압수 가능!
#ADD D:/.ssh/id_rsa /root/.ssh/id_rsa

# 권한 추가
#RUN chmod 600 /root/.ssh/id_rsa
#
#RUN touch /root/.ssh/known_hosts
#
#RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN echo "testing_operater2"

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


