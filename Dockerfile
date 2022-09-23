FROM python:3.10.4

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install  -r /code/requirements.txt

COPY ./ /code

EXPOSE 8000

CMD ["uvicorn", "main:app","--host=0.0.0.0","--reload"]