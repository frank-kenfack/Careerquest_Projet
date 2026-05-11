from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    # On lie chaque Avatar a un seul Utilisateur
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    
    # Statistiques RPG
    level = models.PositiveIntegerField(default=1, verbose_name="Niveau")
    current_xp = models.PositiveIntegerField(default=0, verbose_name="XP Actuel")
    
    # Pour repondre a la contrainte "Progression visuelle" du sujet
    APPEARANCE_CHOICES = [
        ('NOOB', 'Novice (T-shirt simple)'),
        ('INT', 'Intermediaire (Chemise)'),
        ('PRO', 'Expert (Costume/Armure)'),
    ]
    appearance = models.CharField(
        max_length=4, 
        choices=APPEARANCE_CHOICES, 
        default='NOOB',
        verbose_name="Apparence visuelle"
    )

    def __str__(self):
        return f"Avatar de {self.user.username} - Niv {self.level}"
