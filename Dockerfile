FROM python:3.14.6-slim AS builder
RUN python -m venv /opt/venv
COPY requirements.txt /build/requirements.txt
WORKDIR /build
ENV PATH=/opt/venv/bin:$PATH
RUN pip install --no-cache-dir -r /build/requirements.txt

FROM python:3.14.6-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN useradd --no-create-home --system appuser -s /usr/sbin/nologin

COPY --from=builder /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY ./app/ /app/app/

EXPOSE 8000

USER appuser

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000" ]

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD [ "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health').status" ]
