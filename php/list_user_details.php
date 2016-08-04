#!/usr/bin/env php
<?php
if (3 != $argc) {
    echo "need exactly two arguments: full path to wp-config.php file and user to search\n";
    exit;
}

require_once $argv[1];
$user = $argv[2];

if (! mysql_connect(DB_HOST, DB_USER, DB_PASSWORD)) {
    echo "MySQL error:" . mysql_error();
    exit;
}

$result = mysql_query("SELECT id, user_login, user_nicename, user_email, display_name FROM wp_users WHERE
    user_login LIKE '%$user%' or
    user_nicename LIKE '%$user%' or
    user_email LIKE '%$user%' or
    display_name LIKE '%$user%'");
while($row = mysql_fetch_row($result)) {
    echo "$row[0] $row[1] $row[2] $row[3] $row[4]\n";
}
?>
