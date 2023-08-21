FROM python:3.9

# install pandas
RUN pip install pandas

# this will let docker know to cd to this working directory
WORKDIR /app
# copy file from source to destination
COPY pipeline.py pipeline.py

# overwrite entry point to bash
ENTRYPOINT ["python", "pipeline.py"]