<?php

$username="";
$password="";
$database="";

$pdo = new PDO('mysql:host=localhost;dbname=temp_database',$username,$password);

$values = array();

$i = 0;

foreach($pdo->query('SELECT * FROM log') as $row) {
	$values[$i] = $row;
	$i++;
}

$json = json_encode($values,JSON_PRETTY_PRINT);
printf("<pre>%s</pre>", $json);
?>
