# php_xor_bypass
利用随机异或无限免杀d盾

Python版请移步 (thx @c0ny1)

https://github.com/c0ny1/WorkScripts/blob/master/php-xor-bypass/php_xor_bypass.py



## 2.0 更新内容

1.	更新免杀

2.	解决了PHP5.4以下没有hex2bin函数的BUG

3.  在变量池中去除导致脚本不能使用的转义符`\`

4.	精简体积 370字节->270字节

5.	Header改为404,更为隐蔽



## 使用方法

 `xor.php?file=test.php`
 
 即可在同目录生成 test.php
