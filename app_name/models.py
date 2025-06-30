
# Create your models here.

# Importing the required modules

# The models module is used to create the database tables and the fields
from django.db import models

# The User model is used to create the user table using the default django user model
from django.contrib.auth.models import User


# ------------------ Online Voting System - Models ------------------ #

# The Position model is used to create the position table
class Position(models.Model):

    # The title field is used to store the position title
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title

# The Candidate model is used to create the candidate table
class Candidate(models.Model):

    # The name field is used to store the candidate name
    name = models.CharField(max_length=100)

    # The total_vote field is used to store the total number of votes received by the candidate
    total_vote = models.IntegerField(default=0, editable=False)

    # The position field is used to store the position of the candidate
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    # The image field is used to store the image of the candidate
    image = models.ImageField(verbose_name="Candidate Pic", upload_to='images/')

    def __str__(self):
        return "{} - {}".format(self.name, self.position.title)

# The ControlVote model is used to create the control_vote table
class ControlVote(models.Model):

    # The user field is used to store the user who has voted
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The position field is used to store the position for which the user has voted
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    # The status field is used to store the status of the vote
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.position, self.status)

# Importing the required modules

# The admin module is used to create the admin site for the application
from django.contrib import admin

# The models module is used to import the models from the models.py file
from .models import Candidate, Position


# The admin.site.register() method is used to register the models to the admin site
@admin.register(Position)
# The PositionAdmin class is used to create the admin site for the Position model
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)



@admin.register(Candidate)
# The CandidateAdmin class is used to create the admin site for the Candidate model
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)
