FROM python:3.9

EXPOSE 8000

WORKDIR /code
ADD Pipfile /code/Pipfile
ADD Pipfile.lock /code/Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install pipenv-to-requirements
RUN pipenv run pipenv_to_requirements -f
RUN pip install -r requirements.txt
COPY . /code/
USER 10001

CMD [ "python", "runserver.py" ]