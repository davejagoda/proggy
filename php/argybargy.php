#!/usr/bin/env php
<?php
while (count($argv)) {
    echo count($argv), " ", array_pop($argv), "\n";
}
?>
