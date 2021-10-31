from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from profanity.validators import validate_is_profane

# Create your models here.
#User = get_user_model()

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(validators=[validate_is_profane])
    posted_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.message)

    def get_absolute_url(self):
	      return reverse('chat:all')
    

