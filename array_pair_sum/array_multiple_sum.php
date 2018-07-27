<?php
/*
 
 Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

S = [2, 3, 7, 8, 10], k = 11

 */

class Solution {

	public function arraySum($arr, $k) {
		$truth = [[],[]];
		$lenth = count($arr);

		for ($i=0; $i <= $length; $i++) {
			$truth[$i][0] = true;
		}

		for ($i=1; $i<=$k; $i++) {
			$truth[0][$i] = false;
		}

		print_r($truth);

	}

}

$sol = new Solution();
$sol->arraySum([2, 3, 7, 8, 10], 11);