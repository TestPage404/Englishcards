FROM python:3
WORKDIR /app/cards
COPY . /app/cards
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
EXPOSE 80
CMD python ./app.py