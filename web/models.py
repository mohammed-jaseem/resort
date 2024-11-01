from django.db import models
from django.contrib.auth.models import User


ROOMS_TYPE_CHOICES = (
    ('single_room','single_room'),
    ('double_room','double_room'),
    ('suite','suite'),
    ('family_room','family_room'),
)

RATING_TYPE_CHOICES = (
    ('Excellent','Excellent'),
    ('Good','Good'),
    ('Average','Average'),
    ('Poor','Poor'),
    ('Terrible','Terrible'),
)

class Room(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=225)
    short_discription = models.CharField(max_length=225)
    price = models.FloatField()


    class Meta:
        db_table = "room"
        verbose_name = "room"
        verbose_name_plural = "rooms"
        ordering = ["-id"]

    def __str__(self):
        return self.name
    
class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=225)
    email = models.EmailField()
    rooms_type = models.CharField(max_length=255,choices=ROOMS_TYPE_CHOICES)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_date = models.DateField(auto_now_add=True)
    checkout_date = models.DateField(auto_now_add=True)
    number = models.IntegerField()
    request_guests = models.CharField(max_length=225)

    class Meta:
        db_table = "detail"
        verbose_name = "detail"
        verbose_name_plural = "details"
        ordering = ["-id"]

    def __str__(self):
        return self.email
    
class Rewiew(models.Model):
    name = models.CharField(max_length=225)
    short_discription = models.TextField()
    rating = models.CharField(choices=RATING_TYPE_CHOICES)


    class Meta:
        db_table = "rewiew"
        verbose_name = "rewiew"
        verbose_name_plural = "rewiews"
        ordering = ["-id"]

    def __str__(self):
        return self.name
