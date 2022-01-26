# raspberrypi

## 인체 감지 센서 아두이노
```C
int sensor = 7;

void setup() {
  Serial.begin(9600);
  pinMode(sensor, INPUT);
}

void loop() {

  Serial.println(digitalRead(sensor));
  delay(1000);

}
```

## Python 소스 코드
```PYTHON

import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(cmd.encode())

a = 1
while a:
    if seri.in_waiting !=0 :
        content = seri.readline()
        print(content.decode())
```
## 아두이노 빛 센서 
```C
int Cds = 0;

void setup(){
  Serial.begin(9600);
  pinMode(A1, INPUT);
}

void loop(){
  Cds = analogRead(A1);
  Serial.println(Cds);
  
  delay(1000);
}
```
# InfluxDB Installation

## 0. 라즈베리파이 업데이트
```
sudo apt update
```
## 1. Repository의 GPG key를 더하기
```
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
```

## 2.Repository를 더하기 
```
echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```

## 3. 프로그램 설치 
```
sudo apt update
sudo apt install influxdb
```
## 3.1 프로그램 실행 전 설정
```
sudo systemctl unmask influxdb
sudo systemctl enable influxdb
sudo systemctl start influxdb
```
## 4. 데이터베이스 만들기
```
$ influx
>create database <데이터베이스이름>
```
```
확인: show databases 
```
# Grafana Installation
## 1. Repository의 GPG key를 더하기
```
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
## 2. Repository를 더하기
```
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
## 3. 프로그램 설치
```
sudo apt update
sudo apt install grafana
```
## 4. 프로그램 실행
```
sudo service grafana-server start
```
## influxdb import with python
```
sudo pip3 install influxdb
```
## gpio pin map
```
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
``` 
