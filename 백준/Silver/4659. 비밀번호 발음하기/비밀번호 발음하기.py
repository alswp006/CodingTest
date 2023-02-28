import sys
input=sys.stdin.readline
aa=['a','e','i','o','u']
while True:
    be=''
    n=input().rstrip()
    if n=='end':break
    if 'a' not in n and 'e' not in n and 'i' not in n and 'o' not in n and 'u' not in n:
        print(f'<{n}> is not acceptable.')
        continue
    mo,ja=0,0
    for i in range(len(n)):
        if be==n[i] and be!='e' and be!='o':
            print(f'<{n}> is not acceptable.')
            break
        if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u':
            ja=0
            mo+=1
        else:
            mo=0
            ja+=1
        if mo==3:
            print(f'<{n}> is not acceptable.')
            break
        if ja==3:
            print(f'<{n}> is not acceptable.')
            break
        be=n[i]
    else:
        print(f'<{n}> is acceptable.')