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
