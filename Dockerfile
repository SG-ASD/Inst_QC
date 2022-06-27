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

RUN git clone https://github.com/SG-ASD/Inst_QC

WORKDIR /home/Inst_QC/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY = django-insecure-wkv0eo^r-u#aneynu^*y1j08e4r2c)(#jh9_163)5ilctaqw-e"

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

