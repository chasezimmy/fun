<?php

// Reverse String

class Solution {

	public function reverseString($string) {
		
		$length = strlen($string);
		$revString = '';

		for ($i=$length-1; $i>=0; $i--)
			 $revString .= $string[$i];

		return $revString;
	}

}

$string = 'Test String';
$sol = new Solution();

print $sol->reverseString($string);