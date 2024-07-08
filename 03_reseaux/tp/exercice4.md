### TP : Création d'un Utilisateur avec des Contraintes de Sécurité Avancées sur le Mot de Passe

#### Etape 1 -> Les contraintes :

Nombre de tentatives autorisées pour entrer un mot de passe correct. 3
Longueur minimale du mot de passe. 10
Nombre de caractères différents par rapport au mot de passe précédent. 4
Au moins une lettre majuscule. -1
Au moins une lettre minuscule. -1
Au moins un chiffre. -1
Au moins un caractère spécial. -1
Nombre maximal de répétitions consécutives de caractères. 3
Nombre maximal de répétitions consécutives de classes de caractères. 2
Vérifie si le mot de passe contient le nom complet de l'utilisateur. 1

### Étape 2 -> Créer un Nouvel Utilisateur et Tester les Contraintes de Sécurité
 
Créez un nouvel utilisateur appelé `testuser` :

### Bonus : Paramètres supplémentaires de `pam_pwquality.so`

Voici quelques paramètres supplémentaires que vous pouvez utiliser pour affiner les règles de sécurité :

Rend les règles de mot de passe obligatoires.
Spécifie le chemin vers un fichier de dictionnaire pour vérifier les mots de passe contre des mots communs.

Modifiez ces paramètres à la ligne `pam_pwquality.so` dans `/etc/pam.d/common-password` si nécessaire.