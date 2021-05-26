n = 13
answer = 0
sum = 0

for i in range(1, n+1):     # 1부터 14까지
    if n % i == 0:          # 그 중 나눈 나머지가 0이 될 경우
        sum += i            # i의 합을 구한다
        answer = sum

print(answer)

# print(sum([i for i in range(1, n + 1) if n % i == 0]))     - 한 문장으로 줄이기 연습


























