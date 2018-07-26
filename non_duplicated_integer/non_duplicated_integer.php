<?php
/*
 *	Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
 *
 *	For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
 *
 */

class Solution {

	public function nonDuplicatedInt($arr) {
		$assocArr = [];

		foreach($arr as $value) {
			if(array_key_exists($value, $assocArr)) {
				$assocArr[$value] += 1;
			} else {
				$assocArr[$value] = 1;
			}
		}

		foreach ($assocArr as $key => $value) {
			if ($value == 1)
				return $key;
		}

		return;
	}
}

$sol = new Solution();
echo $sol->nonDuplicatedInt([13, 19, 13, 13]);