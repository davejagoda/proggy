#!/usr/bin/env php
<?php
/* indentation in php is flexible */

$lower =   0; /* lower limit of temperature table */
$upper = 300; /* upper limit of temperature table */
$step  =  20; /* step size */

$fahr = $lower;
$format = "%3.0f %6.1f\n";
while ($fahr <= $upper) {
    $celsius = (5.0/9.0) * ($fahr-32.0);
    printf($format, $fahr, $celsius);
    $fahr = $fahr + $step;
}
?>
