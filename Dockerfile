FROM python:3.11-slim

WORKDIR /app
RUN ln -s /usr/bin/python3 /usr/bin/python 
#This made an alias for python

#-----#

# COPY pyproject.toml . or requirements.txt
COPY run.py .
COPY src/ src/

RUN pip install --upgrade pip && pip install -e .

EXPOSE 5000
CMD ["python", "run.py"]
