FROM python:3.11
RUN mkdir /we_go_trip
WORKDIR /we_go_trip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache --upgrade pip
COPY ./requirements.txt /we_go_trip/requirements.txt
RUN pip install --no-cache -r requirements.txt

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/local/bin/entrypoint.sh

COPY . .
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
