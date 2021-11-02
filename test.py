#  systaxerror : 문법오류
# print('a)
#  print('a'))
#  if True;

#  typeerror : 다른 자료형끼리 연산하거나, 알맞지않은 자료형을 메서드에 쓸때 
#  a = [1,2,3]
#  print(a['1'])

#  nameerror : 참조 불가능한 변수
#  a = 10
#  b = 15
#  print(c)

#  zerodivisionerror : 0으로 나누는 경우
#  print(100/0)



#  indexerror : 인덱스 범위밖의 인덱스를 불러올때
#  x = [50,70,90]
#  print(x[4])


#  valueerror : 참조 불가능한 값
#  x = [10,50,90]
#  x.remove(100)


#  attribute error : 모듈, 클래스의 잘못된 속성사용
#  import time
#  print(time.time2())



#  keyerror
#  dic = {'name' : 'kang', 'age' : 21}
#  print(dic['age'])
#   print(dic['from'])
#  print(dic.get('from'))

#  filenotfounderror
#  f = open('text.txt')


#  문법적으로는 예외가 없지만, 코드 실행단계에서 발생하는 예외
#  예외는 반드시 처리해야한다.
#  로그는 반드시 남긴다. 어떤 예외가 발생했었는지 기록으로 남겨야한다.
#  예외는 던져진다.,,다른곳으로 처리위임이 가능하다
#  예외의 무시처리가 가능하다.


#  예외처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
#  except 에러명1: 에러발생시 실행할 코드
#  except 에러명2:
#  else: try 블록의 에러가 없으면 실행되는 코드(for-else문과 비슷)
#  finally: 항상 마지막에 실행된다.

#  name = ['kim','lee','park']
#  1
#  try:
#      z = 'asd'
#      x = name.index(z)
#      print('found!', x + 1)
#  except ValueError:
#      print('notfound, valueerror')
#  else:
#      print('ok')
#      print()

# except Exception 을 하게되면 모든 종류의 에러를 잡아준다. 또는 except: 도 동일한 역할을 한다.
# 특히 except Exception을 사용할때 as e 로 별칭을 붙이면 이 e가 에러의 내용을 담아 print(e)를 해보면 에러의 내용을 알 수 있다.



# raise
#  raise 키워드로 예외를 직접 발생시킬수도 있다. 
#  보통은 try에서 raise로 에러를 던진다음에
#  except로 해당 에러를 잡아내는  방식이다.

# per = ["10.31", "", "8.00"]
# new_per = []

# for i in per:
#     try:
#         v = float(i)
#     except:
#         v = 0
#     new_per.append(v)

# print(new_per)
