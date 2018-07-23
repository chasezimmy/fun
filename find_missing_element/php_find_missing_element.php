<?php
// Find Missing Element
// http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/

class Solution {
	// O(N) - Time complexity
	function findMissingElement1($arr1, $arr2) {
		return array_diff($arr1, $arr2);
	}

	// O(N) - Time, O(1) - Space complexity
	function findMissingElement2($arr1, $arr2) {
		$res = 0;
		$merge = array_merge($arr1, $arr2);
		foreach ($merge as $value)
			$res ^= $value;
		return $res;
	}
}

$obj = new Solution();

$a1 = [4, 1, 0, 2, 9, 6, 8, 7, 5, 3];
$a2 = [6, 4, 7, 2, 1, 0, 8, 3, 9];

echo $obj->findMissingElement2($a1, $a2) . "\n";


?>