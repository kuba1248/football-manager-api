from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from .lib.country_list import COUNTRIES
from .lib.player_positions import PLAYER_POSITIONS
from .user_manager import CustomUserManager

TransferStatus = [("UA", "Unavaliable"), ("A", "Avaliable")]


class User(AbstractUser):
    username = models.CharField(max_length=255, null=True)
    team_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email}"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ["-created_at"]


class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRIES)
    value = models.FloatField(default=20000000)
    team_budget = models.FloatField(default=5000000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["-created_at"]


class Player(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=26)
    market_value = models.FloatField(default=0, validators=[MinValueValidator(0)])
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(blank=True, choices=PLAYER_POSITIONS, max_length=20)
    shirt_number = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    country = models.CharField(max_length=255)
    player_value = models.FloatField(default=1000000, validators=[MinValueValidator(1)])
    transfer_status = models.CharField(
        default="UA", max_length=20, choices=TransferStatus
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
