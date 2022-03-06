# checking for balanced PARENTHESIS USING STACK
# hello !
# God Bless you
def parcheck(word):
    st = []
    ind = 0
    balanced=True
    while ind <len(word):
        val=word[ind]
        if val in "({[":
            st.append(val)
        else:
            if len(st)==0:
                balanced=False
            else:
                stack_top=st.pop()
                if not match(stack_top,val):
                    balanced= False
        ind+=1
    if balanced and len(st)==0:
        return True
    else:
        return False
    

def match(o,c):
    first= '({['
    second= ')}]'
    return first.index(o)==second.index(c)

w ="[({)]"
print(parcheck(w))     


print('hi')