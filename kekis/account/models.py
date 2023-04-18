from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    age = models.IntegerField()
    email = models.EmailField(max_length=200)
    teacher = models.CharField(max_length=40)
    time_created = models.DateTimeField(auto_now_add=True)
    
<<<<<<< HEAD
    def __str__(self) -> str:
=======
    def __str__(self):
>>>>>>> 3977d66382862d63c2a04e4b105e41d7f87b28e0
        return self.name
    