for _ in range(int(input())):
    N,M=map(int,input().split())
    base=dict()
    for _ in range(M):
        c=input().split()
        if c[0]=='UPDATE':
            x,y,z,w=map(int,c[1:])
            base[(x,y,z)]=w
        else:
            r=list(map(int,c[1:]))
            X,Y,Z=[range(r[i],r[i+3]+1) for i in range(3)]
            print(sum(base[(x,y,z)] for x,y,z in base if x in X and y in Y and z in Z))
