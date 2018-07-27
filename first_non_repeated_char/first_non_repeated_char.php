<?php

class Solution {

	// O(n)
	public function firstNonRepeatedChar($str) {
		$count = [];

		foreach(str_split($str) as $char) {
			if (!array_key_exists($char, $count)) {
				$count[$char] = 0;
			}

			$count[$char] += 1;
		}

		foreach($count as $key=>$value) {
			if ($value == 1) {
				return $key;
			}
		}

		return null;
	}

}

$sol = new Solution();
$str = "AABBCDD";
echo $sol->firstNonRepeatedChar($str);
