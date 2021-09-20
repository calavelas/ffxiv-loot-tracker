from django.db import models
from django.utils import timezone

# Create your models here.

class Patch(models.Model):

    name = models.CharField(max_length=30)
    number = models.CharField(max_length=5)

    def __str__(self):
        return (self.number + " "+self.name)

class Job(models.Model):

    TYPE_CHOICES = [
    ('DOW', 'Disciple of War'),
    ('DOM', 'Disciple of Magic')
    ]

    ROLE_CHOICES = [
    ('TANK', 'Tank'),
    ('HEAL', 'Healer'),
    ('MELEE', 'Melee DPS'),
    ('RANGE', 'Range DPS'),
    ('MAGE', 'Magic DPS'),
    ]

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    lodestoneId = models.CharField(max_length=10)

    def __str__(self):
        return (self.name)

class Item(models.Model):

    TYPE_CHOICES = [
    ('Head', 'Head'),
    ('Body', 'Body'),
    ('Hand', 'Hand'),
    ('Leg', 'Leg'),
    ('Boot', 'Boot'),
    ]

    name = models.CharField(max_length=40)
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    iLevel = models.CharField(max_length=3)
    isRaid = models.BooleanField(default=True)
    xivApiId = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Static(models.Model):

    name = models.CharField(max_length=30)
    leader = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StaticMember(models.Model):

    static = models.ForeignKey(Static, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return (self.static.name+ " : "+self.character.name)

    def getName(self):
        return (self.character.name)

    def getJob(self):
        return (self.job.name)

    def getRole(self):
        return (self.job.role)

class StaticBIS(models.Model):

    member = models.ForeignKey(StaticMember, on_delete=models.CASCADE)
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return(self.member.static.name+" | "+self.member.character.name+" | "+self.item.name)

class StaticLootHistory(models.Model):

    member = models.ForeignKey(StaticMember, on_delete=models.CASCADE)
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=6)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return(str(self.timestamp)+" | "+self.member.static.name+" | "+self.member.character.name+" | "+self.item.name)