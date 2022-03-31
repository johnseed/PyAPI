FROM continuumio/miniconda3 as extract
WORKDIR /app
COPY . .
ADD conda-pack/miniconda-satellite.tar.gz conda-satellite
# RUN mkdir conda-satellite && tar -xf conda-pack/satellite.tar.gz -C conda-satellite
RUN rm -rf conda-pack

FROM continuumio/miniconda3
WORKDIR /app
COPY --from=extract /app /app
EXPOSE 8000
ENTRYPOINT [ "./entrypoint.sh", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "fastapi-server:app" ]