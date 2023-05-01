from django.db import models

# Create your models here.
class Student(models.Model):
    num = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    brith = models.DateField()
    Depart = models.CharField(max_length=100)
    image = models.ImageField(upload_to='single_pages/images/%Y/%m/%d', blank=True)  #이미지 폴더 지정하기 //setting건들기


    def get_absolute_url(self):
        return f'/exam/prob/{self.pk}/'