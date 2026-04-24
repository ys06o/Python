# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력

import os
import csv
def menu2():
  menu_input=input('1.지역명 검색 2.금액 범위 검색 3.전체 통계 조회')
  
  if menu_input=='1':
    pass
  else:
    pass

def signup():
    users = 'users.txt'
    if not os.path.exists(users):
        with open(users, 'w', encoding="utf-8") as f:
            pass

    print("--- 회원가입 ---")
    id_input = input('아이디 입력: ')
    pw_input = input('비밀번호 입력: ')
    name_input = input('이름 입력: ')

    if not id_input or not pw_input:
        print("아이디와 비밀번호를 입력해주세요.")
        return menu1()

    count = 0
    with open(users, 'r', encoding="utf-8") as file:
        for line in file:
            count += 1
            if f"id:{id_input}," in line:
                print("이미 존재하는 아이디입니다.")
                return menu1()

    uno = count + 1

    with open(users, 'a', encoding="utf-8") as file:
        file.write(f'uno:{uno},id:{id_input},pw:{pw_input},name:{name_input}\n')
        print('회원가입 성공')
        menu1()
        
        

def login():
    id_input = input('아이디 입력: ')
    pw_input = input('비밀번호 입력: ')
    with open('users.txt', 'r', encoding='utf-8') as file:
      user_db=file.readlines()
      for line in user_db:
        if f"id:{id_input}," in line and f"pw:{pw_input}" in line:
          print('로그인 성공')
          menu2()
        else:
          print('로그인 실패')
          menu1()      


def menu1():  
  user_input = input('1.회원가입 2.로그인 3.로그아웃 : ')

  if user_input == '1':
    pass
    
  elif user_input=='2':
    login()
  else:
    print('다시입력')
    menu1()
    
menu1()


a=input('시군구를 입력하세요:')
print(a)

with open('exam.csv', 'r') as file:
  for line in file:
    print(line)
  