from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from avatars.models import Avatar
from missions.models import Quest
import random

class Command(BaseCommand):
    help = 'Genere des donnees de test aleatoires pour CareerQuest'

    def handle(self, *args, **kwargs):
        self.stdout.write("Suppression des anciennes donnees de test...")
        # On supprime tout pour repartir a zero (sauf ton compte super-utilisateur !)
        Quest.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        self.stdout.write("Generation des Missions...")
        types = ['PRJ', 'FRM', 'CRT']
        adjectifs = ['epique', 'Difficile', 'Rapide', 'Legendaire', 'Complexe']
        sujets = ['React', 'Docker', 'Python', 'Kubernetes', 'CI/CD']
        
        for _ in range(15): # Genere 15 missions
            Quest.objects.create(
                title=f"Quete {random.choice(adjectifs)} : {random.choice(sujets)}",
                description="Une mission generee automatiquement par notre script de test.",
                quest_type=random.choice(types),
                xp_reward=random.randint(5, 50) * 10  # Donne entre 50 et 500 XP
            )

        self.stdout.write("Generation des Joueurs et de leurs Avatars...")
        appearances = ['NOOB', 'INT', 'PRO']
        
        for i in range(1, 6): # Genere 5 joueurs
            # 1. Creation de l'utilisateur classique
            user = User.objects.create_user(
                username=f"etudiant_{i}", 
                password="password123!"
            )
            
            # 2. Creation de son Avatar lie
            Avatar.objects.create(
                user=user,
                level=random.randint(1, 10),
                current_xp=random.randint(0, 1000),
                appearance=random.choice(appearances)
            )

        self.stdout.write(self.style.SUCCESS(" Base de donnees peuplee avec succes !"))
