from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .managers import Manager

import uuid
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    front_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    won_games = models.IntegerField(default=0)
    lost_games = models.IntegerField(default=0)
    draw_games = models.IntegerField(default=0)
    image = models.ImageField(default='images/default.png', upload_to='images')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = Manager()

    @property
    def total_games(self):
        return self.won_games + self.lost_games + self.draw_games

    @property
    def name(self):
        return self.__str__()

    @property
    def profile_url(self):
        return reverse('accounts:view_user', kwargs={"id":self.front_id})

    def win(self):
        self.won_games += 1
        self.save() 

    def lose(self):
        self.lost_games += 1
        self.save() 

    def draw(self):
        self.draw_games += 1
        self.save() 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    