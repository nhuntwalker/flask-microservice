FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.pip

EXPOSE 9090
CMD ["python", "/code/app.py"]