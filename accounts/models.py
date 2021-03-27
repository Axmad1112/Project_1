from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    author_image= models.ImageField(default='author.jpg', upload_to='author_image', null=True, blank=True)
    phone       = models.CharField(max_length=20, default="+998", null=True, blank=True)

    def __str__(self):
       return self.user.username

