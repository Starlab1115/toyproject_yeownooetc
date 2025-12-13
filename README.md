# 에어컨이 켜지면 문이 닫히는 하드웨어&소프트웨어
가끔식 학교에서 에어컨을 틀었지만 친구들이 지
나다니기위해 문을 열거나 창문을 깜빡하고 안 
다꼬 다니는 경우가 있다. 이런 문제를 해결하기 위해
에어컨이 켜지면 자동으로 문을 닫는 시스템을 만들
어따. 에어컨의 경우 1번을 누르면 에어
컨이 켜지고 2번을 누르면 에어컨 온도가
뭐 조금씩 올라간다. 3번을 누르면 에어컨 온도가
하주 쬐금씩 감소한다. 4번을 누르면 바람세기가 
지짜로 올라간다. 5번누르면 에어컨 바람이 감소하고 6번누르면 에어컨이 종류된다.


ㅋ코드
from hub import port as p
from hub import button as b
from hub import light_matrix as lm
import time as t
import force_sensor as fs
import motor as m
c=0 #에어컨 작동 관리 변수
te=25 #온도 변수

def d(c): #에어컨 동작 여부에 따라 문의 여닫힘 관리
    if c%2==1:
        m.run_to_absolute_position(p.F,12,100,direction=m.SHORTEST_PATH)
        lm.write("On")
    elif c%2==0:
        m.run_to_absolute_position(p.F,210,100,direction=m.SHORTEST_PATH)
        lm.write("Off")
    t.sleep(1.5)

while True: #메인 코드
    if fs.force(p.A)>=90:
        c+=1
        d(c)
    if b.pressed(b.LEFT)==True: #허브의 왼, 오른쪽의 버튼을 눌렀을 때 온도 조정
        te-=1
    elif b.pressed(b.RIGHT)==True:
        te+=1
    print(te)
