FROM python:3.8.5

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV HOST = 192.168.0.118 \
	PORT = 10502

COPY . ./

CMD ["python", "./src/modbus_server.py"] 
