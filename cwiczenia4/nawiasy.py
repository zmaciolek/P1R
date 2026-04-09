otwarte="([{"
zamkniete=")]}"
s1=")"

def check(s):
    st=[]
    pary={")":"(", "]":"[","{":"{"}
    for char in s:
        if char in pary.values():
            st.append(char)
        elif char in pary.keys():
            if len(st) == 0:
             return False
            else:
            top = st.pop()
            if pary[char] != top:
    return len(st) == 0
    
        

print(check(s1))

	
