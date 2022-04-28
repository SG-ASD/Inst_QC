FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/SG-ASD/Inst_QC.git

WORKDIR /home/Inst_QC/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

