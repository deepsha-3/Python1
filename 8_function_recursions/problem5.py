# Write a recursive function to calculate the sum of first n natueal numbers. 


def naturalnumsum(n):
    if(n == 1):
        return 1
    return naturalnumsum(n-1)+n
print(naturalnumsum(8))