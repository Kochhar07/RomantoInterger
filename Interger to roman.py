d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
s='XCCDCMI'
x=0
rest=0
while x+1<len(s):
    ch=s[x]+s[x+1]
    if ch in d:
        rest=rest+d[ch]
        x+=2
    else:
        ch=s[x]
        if ch in d:
         rest=rest+d[ch]
         x+=1
if(x!=len(s)):
    rest=d[s[x]]+rest
    print(rest)