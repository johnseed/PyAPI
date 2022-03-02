FROM python:3.8.9
WORKDIR /app
COPY . .
RUN pip3 install --no-index --find-links=libs -r requirements.txt
RUN rm -rf libs
EXPOSE 8000
ENTRYPOINT [ "python", "fastapi-client.py" ]