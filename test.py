import m
print(__name__) # __name__명령어가 실행된 파일의 위치, 자기자신과 같으면 __main__리턴
m.hello() # 여기서 m.hello()는 print('hello')와 print(__name__)을 실행해야한다.
#모듈함수에서 __name__은 모듈이름 그 자체를 리턴한다는 것을 알 수 있다. 