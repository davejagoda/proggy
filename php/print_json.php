#!/usr/bin/env php
<?php
if (count($argv) == 1) {
    print("Usage: $argv[0] json_file_or_url [json_file_or_url ...]\n");
}

while (count($argv) > 1) {
    $arg = array_pop($argv);
    print("Processing: $arg\n");
    $file = file_get_contents($arg);
    print("Raw response: $file\n");
    $data = json_decode($file);
    print("Pretty printed\n");
    print(json_encode($data, JSON_PRETTY_PRINT));
}
?>
