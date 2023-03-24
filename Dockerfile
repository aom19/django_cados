FROM python:3.10

RUN pip install --upgrade pip

COPY ./req.txt .

RUN pip install -r req.txt

COPY .    /app

WORKDIR /app

COPY ./entry.sh /
ENTRYPOINT ["sh", "/entry.sh"]
