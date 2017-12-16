FROM python:2.7-alpine

RUN mkdir /home/RecuentoVotos-EGC-G1

ADD requirements.txt /home/RecuentoVotos-EGC-G1/requirements.txt
RUN cd /home/RecuentoVotos-EGC-G1 && pip install --no-cache-dir -r requirements.txt

ADD . /home/RecuentoVotos-EGC-G1

WORKDIR /home/RecuentoVotos-EGC-G1

RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
RUN python manage.py test --noinput

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py", "runserver",  "0.0.0.0:8000"]
