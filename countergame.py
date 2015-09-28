cases= int(raw_input())
for i in range(cases):
    counter=1   
    N = int(raw_input())
    while(True):
        flag= False
        if(N==1):break
        else:
            i=0
            while(2**i<N):
                if(2**i == N):
                    N=N/2
                    flag= True
                    break;
                i+=1
            if(not flag):
                N = N -2**(i-1)
        counter+=1
    if(counter%2 == 1): print "Richard"
    else: print "Louise"
