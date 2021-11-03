FROM python:3.8.9
WORKDIR /app
COPY . .
RUN pip3 install --no-index --find-links=libs -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "fastapi-server:app" ]