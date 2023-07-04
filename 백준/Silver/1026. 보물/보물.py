import sys
from collections import deque
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    a=deque(a)
    b=deque(b)
    answer=0
    for i in range(len(b)):
        min=a.popleft()
        answer+=min*max(b)
        b.remove(max(b))
    print(answer)
if __name__ == "__main__":
    sys.exit(main())