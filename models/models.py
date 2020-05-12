from django.contrib.gis.db import models
from authentication.models import User
from django.utils.translation import ugettext_lazy as _

GROUND_TYPE_CHOICES = (
    ('football', _('football')),
    ('basketball', _('basketball')),
    ('pool', _('pool')),
    )


# class SecondDbManager(models.Manager):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         if hasattr(self.model, 'use_db'):
#             qs = qs.using(self.model.use_db)
#         return qs
#
#
# class SecondDbBase(models.Model):
#     use_db = 'models'
#     objects = SecondDbManager()
#
#     class Meta:
#         abstract = True


class Ground(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    coordinates = models.PointField(srid=4326)
    paid = models.BooleanField(null=True)
    ground_type = models.CharField(max_length=25, choices=GROUND_TYPE_CHOICES)
    max_players = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    description = models.TextField(max_length=400, null=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="creator")
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE)
    users = models.ManyToManyField('authentication.User', null=True, related_name='users')
    isPrivate = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Response(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=450, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.text
