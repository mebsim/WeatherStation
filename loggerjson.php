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
