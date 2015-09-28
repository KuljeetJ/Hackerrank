testcases =  int(raw_input())

def maxSumSubarray(L):
    current_sum = 0
    current_index = -1
    best_sum = 0
    best_starting_index = -1
    best_ending_index = -1
    for i in xrange(len(L)):
        val = current_sum + L[i]
        if(val>0):
            if(current_sum==0):
                current_index = i
            current_sum = val
        else:
            current_sum = 0

        if(current_sum > best_sum):
            best_sum = current_sum
            best_starting_index = current_index
            best_ending_index = i
    return (L[best_starting_index:best_ending_index+1])


    
for i in xrange(testcases):
    n = int(raw_input())
    m = map(int,raw_input().split())
    ans1 = sum(maxSumSubarray(m))
    non_conti_sum = 0
    mini=-10000000
    for i in m:
        if(i>mini):
            mini=i
        if(i>0):
            non_conti_sum+=i
    ans2 = non_conti_sum
    
    if(ans1 == 0): ans1 = mini
    if(ans2 == 0): ans2 = mini   
    print ans1,
    print ans2
