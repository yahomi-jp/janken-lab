from django.db import models
from django.db.models.base import Model
from django.conf import settings

# Create your models here.

class Opponent(models.Model):
    name = models.CharField('対戦相手', max_length=12)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='作成者',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'Opponents'

    def __str__(self):
        return self.name

class Game(models.Model):
    HANDS = (
        ('0', 'グー'),
        ('1', 'チョキ'),
        ('2', 'パー'),
    )
    opponent = models.ForeignKey(
        Opponent,
        verbose_name='対戦相手',
        on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='作成者',
        on_delete=models.CASCADE
    )
    opponent_hand = models.CharField(
        '相手の手',
        max_length=1,
        choices=HANDS
    )
    my_hand = models.CharField(
        '自分の手',
        max_length=1,
        choices=HANDS
    )
    result = models.CharField(
        '対戦結果',
        max_length=4,
    )

    class Meta:
        db_table = 'games'

    def __str__(self):
        return  f'{self.opponent} - {self.created_by}'