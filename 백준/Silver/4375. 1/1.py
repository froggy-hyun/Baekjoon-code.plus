# import sys
# input = sys.stdin.readline

while(True): # 입력 개수 안 알려줌
    try: # 종료조건이 따로 주어져있지 않으므로 try except를 이용해 예외처리를 해주어 프로그램이 종료
        n = int(input())

    except:
        break
    
    m = 1
    count = 1
    while(m % n != 0):
        m = (m*10)+1
        count += 1
    
    print(count)
