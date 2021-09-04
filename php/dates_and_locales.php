#!/usr/bin/env php
<?php
setlocale(LC_ALL, '');
$l = locale_get_default();
echo "$l\n";
$t = time();
$s = strftime("%x %X", $t);
echo "$s\n";
?>
