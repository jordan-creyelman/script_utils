<?php
// Connexion à la base de données
$host = 'localhost';
$user = 'utilisateur_db';
$pass = 'mot_de_passe_db';
$dbname = 'nom_db';

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
	die('Connexion échouée : ' . $conn->connect_error);
}

// Requête SQL pour ajouter une nouvelle table
$sql = "CREATE TABLE utilisateurs (
		id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(30) NOT NULL,
		email VARCHAR(50) NOT NULL,
		password VARCHAR(255) NOT NULL
	)";

// Exécution de la requête SQL
if ($conn->query($sql) === TRUE) {
	echo 'La table utilisateurs a été créée avec succès.';
} else {
	echo 'Erreur lors de la création de la table : ' . $conn->error;
}

$conn->close();
?>
