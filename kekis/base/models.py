from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Project(models.Model):
    kvantumType = models.TextChoices('kvantumType', 'VR IT MEDIA IND-DESIGN ENERGY BIO NEURO NANO HI-TECH GEO AERO IND-ROBO')
    
    name = models.CharField(max_length=200, verbose_name="Название")
    kvantum = models.CharField(choices=kvantumType.choices, max_length=10, verbose_name="Квантум")
    face = models.ForeignKey("Image", verbose_name="Обложка на главной странице", on_delete=models.CASCADE, related_name='Image_Face', null=True, blank=True)
    description = models.TextField(verbose_name="Описание проекта")
    image = models.ManyToManyField("Image", null=True, blank=True, verbose_name="Дополнительные изображения")
    contacts = models.ManyToManyField("Contacts", verbose_name="Кониакты учеников")
    
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название изображения")
    type = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Project_type', verbose_name="Что за проект")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение")
    
    def __str__(self):
        return f"{self.name}, {str(self.type)}"

class Contacts(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = PhoneNumberField(null=False, blank=False, verbose_name="Номер телефона")
    class Meta:
        unique_together = ("first_name", "last_name", "phone" )
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"


'''
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self) -> str:
        return self.title
''' 