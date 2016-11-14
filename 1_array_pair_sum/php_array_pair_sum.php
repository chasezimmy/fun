<?php
// Array Pair Sum
// http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/

class Solution {

	// O(NlogN)
	function pair_sum($arr, $k) {
		sort($arr);

		$left = 0;
		$right = count($arr) - 1;

		while ($left < $right) {
			$currentSum = $arr[$left] + $arr[$right];

			if ($currentSum == $k) {
				echo $arr[$left] . ' ' . $arr[$right] . "\n";
				$left++;
			} elseif ($currentSum < $k) {
				$left++;
			} else {
				$right--;
			}
		}

	}

	// O(N)
	function pair_sum1($arr, $k) {
		if (count($arr) < 2)
			return "no match";

		$seen = array();
		$output = array();

		foreach ($arr as $value) {
			$target = $k - $value;
			if (!in_array($target, $seen)) {
				array_push($seen, $value);
			} else {
				//echo $value;
				array_push($output,  min($value, $target) . ',' .  max($value, $target) );
			}
		}
		foreach ($output as $value) {
			echo $value . "\n";
		}

	}
}


$obj = new Solution();

$arr = [4, 3, 2, 1, 1];
$obj->pair_sum1($arr, 5);


?>