<?php

$user = 'root';
$password = 'root';
$db = 'SouthernHospitality';
$host = 'localhost';
$port = 3306;

//Create connection
$conn = new mysqli($host, $username, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "you're a real dad now";


?>
