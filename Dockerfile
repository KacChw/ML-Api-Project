WORKDIR /code

COPY ./req.txt /code/req.txt

RUN pip install --no-cache-dir -r /code/req.txt

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
