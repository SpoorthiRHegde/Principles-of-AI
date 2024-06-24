# function to check string is palindrome or not
def p(s):
    rev=''.join(reversed(s))
    if(s==rev):
        return True
    return False
s="malayalmam"
ans=p(s)
if(ans):
    print("Yes")
else:
    print("No")
