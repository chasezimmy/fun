<?php

function mostFreqInt($arr) {
  $counted = array_count_values($arr); 

  arsort($counted); 

  echo key($counted) . "\n";
  return(key($counted));     
}


$arr = [1, 2, 3, 3, 4];

echo mostFreqInt($arr) . "\n";


?>