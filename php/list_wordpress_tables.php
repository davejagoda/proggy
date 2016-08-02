#!/usr/bin/env php
<?php
if (2 != $argc) {
    echo "need exactly one argument: full path to wp-config.php file\n";
    exit;
}

require_once $argv[1];

if (! mysql_connect(DB_HOST, DB_USER, DB_PASSWORD)) {
    echo "MySQL error:" . mysql_error();
    exit;
}

$tables = mysql_list_tables(DB_NAME);
while($table = mysql_fetch_row($tables)) {
    echo "$table[0]\n";
}
