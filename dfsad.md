
# 예외처리

의도대로 프로그램이 작동하지 않으면 , 비정상적으로 발생한 오류
예측이 가능한 오류


 systaxerror : 문법오류
print('a)
 print('a'))
 if True;

 typeerror : 다른 자료형끼리 연산하거나, 알맞지않은 자료형을 메서드에 쓸때 
 a = [1,2,3]
 print(a['1'])

 nameerror : 참조 불가능한 변수
 a = 10
 b = 15
 print(c)

 zerodivisionerror : 0으로 나누는 경우
 print(100/0)



 indexerror : 인덱스 범위밖의 인덱스를 불러올때
 x = [50,70,90]
 print(x[4])


 valueerror : 참조 불가능한 값
 x = [10,50,90]
 x.remove(100)


 attribute error : 모듈, 클래스의 잘못된 속성사용
 import time
 print(time.time2())



 keyerror
 dic = {'name' : 'kang', 'age' : 21}
 print(dic['age'])
  print(dic['from'])
 print(dic.get('from'))

 filenotfounderror
 f = open('text.txt')




# 예외처리 문법

## try-except
try:예외가 발생할 가능성이 있는 코드 실행
 except예외명1:예외발생시 실행할 코드
 except예외명2:예외명을 적지않고 except: 만 적으면 모든 종류의예외를 캐치
또는 except exception 도 가능 zw
그리고 
except예외명 as 변수:
하고 e를 변수처럼 사용도 가능하다(e =예외발생)

## try~else
try:예외가 발생할 가능성이 있는 코드 실행
except예외명1:예외발생시 실행할 코드
except예외명2:
else: try 블록의예외가 없으면 실행되는 코드(for-else문과 비슷)



## finally
예외와 상관없이 항상 실행하는 코드이다.  

except가 예외가 발생했을 시 실행되는 코드이고   
else가 try에서 예외가 발생하지 않았을 때 실행되는 코드라면  
finally는 예외 발생에 상관없이 항상 실행되는 코드이다. 


# 예외 발생시키기

raise 키워드로 예외를 직접 발생시킬 수 있다. 
보통은 try에서 raise로 예외를 던진다음에
except로 해당 예외를 잡아내는 방식이다.

예외를 발생시키는 함수를 만들고, 함수를 호출해 예외를 발생시킨다음, 함수바깥에서 이를 바탕으로
예외처리를 하는 방법도 있다. 

```python
def errorraiser():
    x = int(input())
    if x != 1:
        raise Exception('0이 아닙니다.') #예외에 에러메시지를 넣을 수 있다.
    print(x)

try:
    errorraiser()
except Exception as e:
    print('예외발생', e)

>>> 1
>>> '예외발생 0이 아닙니다.'    
```

## 현재 발생한 예외를 다시 발생시키기

try~except에서 처리한 예외를 다시 발생시키는 방법도 있다.   
하위 코드블록에서 except 안에서 raise를 사용하면 ㅎ녀재 예외를 다시 발생 시킨다.

```python
def errorraiser():
    try:
        x = int(input())
        if x != 1:
            raise Exception('0이 아닙니다.') #예외에 에러메시지를 넣을 수 있다.
        print(x)
    except Exception as e:
        print('errorraiser에서 예외가 발생', e)
        raise #현재 예외를 다시 발생시켜서 상위블록으로 보낸다.


try:
    errorraiser()
except Exception as e: #하위블록코드에서 발생한 예외가 상위블록코드에서 인식된다.
    print('예외발생', e)
```

# 예외 만들기

파이썬에 내장되어있는 예외 말고도, 직접 예외를 만드는 방법도 있다.  
프로그래머가 직접 만든 예외를 사용자 정의 예외라고 한다.  

```python
class 예외이름(Exception):
    def __init__(self):
        super().__init__('에러메시지')
```

exception을 상속받아 예외이름의 새로운 클래스를 만들어준다.  
그리고 이 예외이름의 __init__ 메서드에 에러메시지를 넣어줄 수 있다. 

