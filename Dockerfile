FROM python:3.10-slim-buster
WORKDIR /app

# expose port for container
EXPOSE 9999

# copy required dependencies
COPY requirements.txt /app/
COPY pyproject.toml /app/

# install dependencies packages to run app
RUN pip install pip setuptools --upgrade
RUN pip install -r requirements.txt

# copy source code to image
COPY . .

# entry point
CMD [ "uvicorn", "src.burger95s.main:app", "--host=0.0.0.0", "--port=9999"]