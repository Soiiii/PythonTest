class no1000:
    # 1000번 A+B
    # 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장
    # split() 안에 아무것도 없으면 공백으로 나눈다는 것 [2 3]
    # split(".")으로 되어 있으면 . 기준으로 나눈다는 것 [2.3]
    A,B = input().split()
    print(int(A)+int(B))