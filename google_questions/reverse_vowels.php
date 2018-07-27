<?php

class Solution {

	public function reverseVowels($str) {
		$vowels = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"];
		$arr = str_split($str);
		$arr_vowels = [];
		
		for ($i=0; $i<strlen($str);$i++) {
			if (in_array($str[$i], $vowels)) {
				$temp = $str[$i];
				$str[$i] = '_';
				$arr_vowels[] = $temp;

			}
		}

		for ($i=0; $i<strlen($str); $i++) {
			if ($str[$i] == '_') {
				$str[$i] = array_pop($arr_vowels);
			}
		}

		return $str;
	}
}

$sol = new Solution();
$str = "United States";
echo $sol->reverseVowels($str);