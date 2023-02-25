<?php
// Configuration de la base de données
$serveur = "localhost"; // Adresse du serveur MySQL
$utilisateur = "joord"; // Nom d'utilisateur de la base de données
$motdepasse = "sanjor18"; // Mot de passe de la base de données
$basededonnees = "hackaton"; // Nom de la base de données

// Connexion à la base de données
$connexion = mysqli_connect($serveur, $utilisateur, $motdepasse, $basededonnees);

// Vérifier la connexion
if (!$connexion) {
    die("La connexion à la base de données a échoué : " . mysqli_connect_error());
}

// Préparation de la requête SQL
$sql = "INSERT INTO user (nom, prenom, email) VALUES (?, ?, ?)";

// Préparation de la déclaration préparée
$stmt = mysqli_prepare($connexion, $sql);

// Vérifier la préparation
if (!$stmt) {
    die("La préparation de la requête a échoué : " . mysqli_error($connexion));
}

// Définition des valeurs à insérer
$nom = "Doe";
$prenom = "John";
$email = "john.doe@example.com";

// Remplacement des marqueurs de positionnement par les valeurs correspondantes
mysqli_stmt_bind_param($stmt, "sss", $nom, $prenom, $email);

// Exécution de la requête
if (mysqli_stmt_execute($stmt)) {
    echo "Les informations ont été insérées avec succès dans la table 'test'.";
} else {
    echo "Une erreur est survenue lors de l'insertion des informations : " . mysqli_error($connexion);
}

// Fermeture de la connexion et de la déclaration préparée
mysqli_stmt_close($stmt);
mysqli_close($connexion);
?>
