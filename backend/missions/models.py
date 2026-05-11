from django.db import models

class Quest(models.Model):
    TYPE_CHOICES = [
        ('PRJ', 'Projet'),
        ('FRM', 'Formation'),
        ('CRT', 'Certification'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre de la mission")
    description = models.TextField(verbose_name="Description detaillee")
    quest_type = models.CharField(
        max_length=3, 
        choices=TYPE_CHOICES, 
        default='PRJ',
        verbose_name="Type"
    )
    xp_reward = models.PositiveIntegerField(
        default=50, 
        verbose_name="Points d'experience (XP)"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_quest_type_display()})"
