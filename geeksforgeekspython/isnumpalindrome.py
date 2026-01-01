x=int(input("enter any number"))
def ispalindrome(x):
    if x<0 or (x%10==0 and x!=0):
        return False
    halfrev_x=0
    while x>halfrev_x:
        halfrev_x=halfrev_x*10+x%10
        x//=10
    return x==halfrev_x or x==halfrev_x//10
    
print(ispalindrome(x))