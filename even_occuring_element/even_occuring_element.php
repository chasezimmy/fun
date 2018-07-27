<?php

class Solution {

	// O(n)
	public function evenOcurringElement($arr) {

		$hash = [];

		foreach($arr as $elem) {
			if(!array_key_exists($elem, $hash)) {
				$hash[$elem] = 1;
			} else {
				$hash[$elem] += 1;
			}
		}

		foreach($hash as $key=>$elem) {
			if ($elem % 2 == 0) {
				return $key;
			}
		}

		return null;
	}
}

$sol = new Solution();
$arr = [1, 4, 2, 3, 4, 5, 2, 4];
echo $sol->evenOcurringElement($arr);