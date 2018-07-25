<?php

class Solution {

	public function fibonacciDynamic($n) {
		$n1 = 0;
		$n2 = 1;

		for ($i=1; $i<=$n; $i++) {
			$temp = $n1 + $n2;
			$n1 = $n2;
			$n2 = $temp;
		}

		return $n1 + $n2;
	}


	public function fibonacciRecursive($n) {
		if ($n == 0 || $n == 1)
			return 1;
		
		return $this->fibonacci($n-1) + $this->fibonacci($n-2);

	}

}

$sol = new Solution();

print($sol->fibonacciDynamic(3));