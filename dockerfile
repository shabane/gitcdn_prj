FROM python
RUN apt-get update && apt-get upgrade
COPY . /code
RUN pip3 install -r /code/requarment.txt
WORKDIR /code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
