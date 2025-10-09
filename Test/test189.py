class Solution:
    # 사용자에게 입력 값을 받음
    n1, n2 = map(int, (input().split()))
    # a,b 배열 초기화
    a = []
    b = []
    # 첫 번째 입력값 for문으로 값 뽑아냄
    for i in range(1, n1 + 1):
        # 2부터 n1까지 값을 모두 돌림
        i += 1
        # n1을 i로 나눈 약수를 찾음
        if (n1 % i == 0):
            # 약수가 있다면 a 배열에 저장
            a.append(i)
            # 다음 for문으로 넘어감
            pass
    # 첫 번째 입력값의 약수들을 사용해서 for문 값 뽑아냄
    for j in a:
        # 첫 번재 입력값의 약수 중에 두 번째 입력값의 약수가 있는지 찾음
        if(n2 % j == 0):
            # b 배열 초기화
            b.clear()
            # b 배열에 최대 공약수 저장
            b.append(j)
            # 다음 for문으로 넘어감
            pass
        # 약수가 없다면 1로 저장
        else:
            b.append(1)
    # b 배열이 비어있다면 1로 저장
    if not b:
        b.append(1)
    # 최대공약수 출력
    print(b[0])
    # 최대공약수인지 확인
    if(n1 % b[0] == 0 and n2 % b[0] == 0):
        # 최대공약수로 n1을 나눠서 몫을 구함
        aa = n1 // b[0]
        # 최대공약수로 n2을 나눠서 몫을 구함
        bb = n2 // b[0]
        # 최대공약수, n1의 몫, n2의 몫을 곱해서 최소공배수를 찾음
        num = aa * bb * b[0]
    # 최소공배수 출력
    print(num)
