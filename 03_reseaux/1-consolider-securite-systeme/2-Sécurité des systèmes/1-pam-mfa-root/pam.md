Configurer une authentification multi-facteurs (MFA) sur Ubuntu en utilisant Google Authenticator est une excellente mesure de sécurité. Voici un guide étape par étape pour installer et configurer Google Authenticator pour SSH sur Ubuntu :

### 1. Installer `libpam-google-authenticator`

Commencez par installer le package `libpam-google-authenticator` :

```bash
sudo apt update
sudo apt install libpam-google-authenticator
```

### 2. Configurer Google Authenticator pour votre utilisateur

Exécutez la commande `google-authenticator` pour configurer Google Authenticator pour votre utilisateur. Vous devrez répondre à quelques questions pour générer une clé secrète, un QR code, et des codes de secours.

```bash
google-authenticator
```

Voici ce que chaque question signifie :

1. **Do you want authentication tokens to be time-based (y/n)** : Répondez "y" pour utiliser les tokens basés sur le temps.
2. **Your new secret key is ...** : Notez cette clé. Vous pouvez également scanner le QR code avec votre application Google Authenticator.
3. **Do you want me to update your "/home/username/.google_authenticator" file (y/n)** : Répondez "y".
4. **Do you want to disallow multiple uses of the same authentication token? (y/n)** : Répondez "y" pour plus de sécurité.
5. **By default, tokens are good for 30 seconds... Do you want to do so? (y/n)** : Répondez "y".
6. **If the computer's time is not synchronized... Do you want to enable rate-limiting (y/n)** : Répondez "y" pour limiter le nombre de tentatives.

### 3. Configurer PAM pour utiliser Google Authenticator

Éditez le fichier de configuration PAM pour SSH :

```bash
sudo nano /etc/pam.d/sshd
```

Ajoutez la ligne suivante en haut du fichier :

```bash
auth required pam_google_authenticator.so
```

### 4. Configurer le service SSH

Éditez la configuration SSH pour obliger l'utilisation de l'authentification PAM :

```bash
sudo nano /etc/ssh/sshd_config
```

Assurez-vous que les lignes suivantes sont présentes et correctement configurées :

```bash
ChallengeResponseAuthentication yes
UsePAM yes
AuthenticationMethods publickey,keyboard-interactive
```

### 5. Redémarrer le service SSH

Redémarrez le service SSH pour appliquer les modifications :

```bash
sudo systemctl restart ssh
```

### 6. Tester la configuration

Ouvrez une nouvelle session SSH pour tester la configuration. Vous devrez entrer votre mot de passe SSH habituel, puis le code généré par Google Authenticator.

```bash
ssh your_username@your_server_ip
```

### Conclusion

En suivant ces étapes, vous avez configuré une authentification multi-facteurs (MFA) sur Ubuntu en utilisant Google Authenticator. Cela ajoute une couche supplémentaire de sécurité à votre serveur SSH, rendant l'accès non autorisé beaucoup plus difficile.