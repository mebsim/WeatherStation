<?php
/*
loggerjson.php

Mohamed Ebsim

Contqact Jesse Rogerson, @ jrogerson@ingeniumcanada.org
Originally created on Jully 16, 2018
-------------------------------------

This program has the purpose of converting an MySQL
database into a text format that a user can access via
the internet. Formats into a JSON file.

*/

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
