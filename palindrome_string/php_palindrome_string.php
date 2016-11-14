<?php
// Palindrome in string

$str = 'madam';
$arr = str_split($str);
$len = sizeof($arr);
$newstring = '';

for ( $i = $len; $i >= 0; $i--) {
	$newstring .= $arr[$i];
}
echo $newstring == $str ? "True\n" : "False\n"; 