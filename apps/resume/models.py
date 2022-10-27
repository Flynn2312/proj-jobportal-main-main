from django.db import models

# Create your models here.
class Resume(models.Model):
    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male"),
    )
    """Резюме"""
    description = models.TextField("ПЕРСОНАЛЬНЫЕ ДАННЫЕ")
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    email = models.EmailField("Почта",unique=True)
    data_of_birth= models.DateTimeField("Дата рождения",max_length=10)
    age = models.IntegerField("Возраст")
    gender = models.CharField("Пол", max_length = 8, choices = GENDER_CHOICES, default='F')
    phone = models.CharField("Телефон",max_length=11, unique=True)
    country = models.CharField("Страна", max_length=60)
    hometown = models.CharField("Родной город/аул", max_length=100)
    adress = models.CharField("Адрес", max_length=100)
    postindex = models.IntegerField("Почтовый индекс")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Резюме пользователя"
        verbose_name_plural = "Резюме пользователей"