import sys
input = sys.stdin.readline

while True:
    nx,ny,w = map(float, input().split())
    if nx == ny == w == 0.0 :
        break
    width = sorted(list(map(float,input().split())))
    length = sorted(list(map(float,input().split())))
    present = 0.0

    for i in range(int(nx)):
        if width[i] - w/2 > present:
            print("NO")
            break
        present = width[i] + w/2
    else:
        if width[-1] + w / 2 < 75.0:
            print("NO")
        else:
            present = 0.0
            for i in range(int(ny)):
                if length[i] - w / 2 > present:
                    print("NO")
                    break
                present = length[i] + w / 2
            else:
                if length[-1] + w / 2 < 100.0:
                    print("NO")
                else:
                    print("YES")