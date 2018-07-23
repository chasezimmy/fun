<?php 
// Largest Continuous Sum
// http://www.ardendertat.com/2011/09/24/programming-interview-questions-3-largest-continuous-sum/


class Solution {

	// O(N)
	function largestContinuousSum($arr) {
		if (count($arr) == 0)
			return "None";

		$maxSum = $currentSum = $arr[0];

		foreach ($arr as $key => $value) {
			if($key == 0) continue;
			$currentSum = max($currentSum+$value, $value);
			$maxSum = max($currentSum, $maxSum);
		}
		echo $maxSum . "\n";
	}
}

$obj = new Solution();

$arr = [1, 2, -1, -5, 1];
$obj->largestContinuousSum($arr);

?>