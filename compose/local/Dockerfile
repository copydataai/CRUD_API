FROM python:3.8-alpine3.13
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
COPY ./app /app
EXPOSE 8000
CMD ["uvicorn", "app.server.app:app", "--host", "0.0.0.0", "--port", "8000"]
