from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    members = models.ManyToManyField(User, blank=True, related_name='teams', through='TeamMembership')

    @property
    def leads(self):
        return self.members.filter(memberships__is_lead=True).all()

    @property
    def non_leads(self):
        return self.members.filter(memberships__is_lead=False).all()

    def __str__(self):
        return self.name

