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

-------------------------------------

Resources Used:
https://stackoverflow.com/a/13638998
https://wingoodharry.wordpress.com/2015/05/18/raspberry-pi-temperature-sensor-web-server-part-3-scheduling-temperature-readings-and-php-script/
http://wiki.hashphp.org/PDO_Tutorial_for_MySQL_Developers

*/

// Fill these variables with the appropriate data
$username="";
$password="";
$database="";

// Creates access to the database
$pdo = new PDO('mysql:host=localhost;dbname=temp_database',$username,$password);

// An empty array to fill with data
$values = array();

// A counter
$i = 0;

// Loops through each row of the database and inserts them into the empty array
foreach($pdo->query('SELECT * FROM log') as $row) {
	$values[$i] = $row;
	$i++;
}

// Formats the array
$json = json_encode($values,JSON_PRETTY_PRINT);

// Prints out the database (<pre> used to maintain whitespace)
printf("<pre>%s</pre>", $json);
?>
