FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/SG-ASD/Inst_QC.git

WORKDIR /home/Inst_QC/

# pip 패키지
RUN pip install -r requirements.txt


RUN echo "SECRET_KEY = django-insecure-wkv0eo^r-u#aneynu^*y1j08e4r2c)(#jh9_163)5ilctaqw-e"

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "Inst_QC.wsgi", "--bind", "0.0.0.0:8000"]
