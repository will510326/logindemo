from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# title -str
# text -str(blank = True)
# created -datetime -(auto=True)
# important -bool - (defaullt = False)
# completed -bool - (default = False)


class Todo(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    # Foreignkey外鍵關聯(user_id <=> Todo_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}- {self.user}'
