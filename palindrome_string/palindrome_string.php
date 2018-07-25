<?php
// String is a palindrome

class Solution {

	public function palindrome($string) {
		$length = strlen($string);
		$checkString = '';

		for ($i = $length-1; $i>=0; $i--) {
			$checkString .= $string[$i];
		}

		return $checkString == $string ? 1 : 0;

	}

	public function palindromInPlace($string) {
		$length = strlen($string) - 1;
		for ($i=0; $i<=$length; $i++) {
			if ($string[$i] != $string[$length - $i])
				return False;
		}
		return True;
	}

	public function palindromRunner($string) {
		$length = (int)floor(strlen($string)/2) - 1;

		for ($i=0; $i<=$length; $i++) {
			if ($string[$i] != $string[(2*$length) + 2 - $i]) {
				return False;
			} 
		}

		return True;
	}

}

$sol = new Solution();

echo $sol->palindrome('racecar');
echo $sol->palindromInPlace('racecar');
echo $sol->palindromRunner('rracecarr');