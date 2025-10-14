class Solution:
    # 사용자에게 입력 값을 받음
    n1, n2 = map(int, (input().split()))
    # a,b, unique 배열 초기화
    a = []
    b = []
    unique = []
    # j 초기값 설정
    j = 1

    # 첫 번째 입력값 for문으로 2부터 값 뽑아냄
    for i in range(2, n1 + 1):
        # 모든 값은 a 배열에 저장
        a.append(i)

    # j = 2부터 n1까지의 값
    for j in range(2, (n1//j) + 1):
        # i = 1부터 시작, j * i =  n1 보다 작음
        for i in range(1, (n1//j) + 1):
            # num은 n1 보다 작음
            num = i * j
            # a 배열에 num이 있으면
            if num in a:
                # b 배열에 num 저장
                b.append(num)
                # 중복된 수는 삭제
                unique = list(dict.fromkeys(b))
    # 두번째 입력 받은 수를 unique 배열에서 뽑음
    print(unique[n2-1])
