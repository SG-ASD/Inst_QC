FROM python:3.9.0

RUN mkdir /root/.ssh/

# 이미지를 가지는 사람은 private key 또한 압수 가능!
ADD ./.ssh/id_rsa /root/.ssh/id_rsa

# 권한 추가
RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/known_hosts

RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

WORKDIR /home/

RUN echo "test"

RUN git clone git@github.com:SG-ASD/Inst_QC.git

WORKDIR /home/Inst_QC/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

