<?php

$total_sum = $_GET['total_sum'];
$end_range = $_GET['end_range'];

for($j = 0 ; $j < $end_range + 1 ; $j++){
    $total_sum += $j;
}

echo $total_sum;
