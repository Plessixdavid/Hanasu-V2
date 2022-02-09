from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        # parcours chacun des caracteres du password pour verifie s'il s'agit d'une lettre.
        if not any(char.isalpha() for char in password):
            # s'il n'y pas de lettre dans le password envoie un message d'erreur.
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        # renvoie un message pour aider l'utilisateur.
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'