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

$result = mysql_list_tables(DB_NAME);
while($row = mysql_fetch_row($result)) {
    $tables[] = $row[0];
}

foreach ($tables as $table) {
    $result = mysql_query("SELECT COUNT(*) FROM $table");
    echo $table, " ", mysql_result($result, 0), "\n";
}
?>
