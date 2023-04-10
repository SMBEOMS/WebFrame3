from django.db import models

# Create your models here.
class Post(models.Model): #일종의 DB구조, field설정
    title = models.CharField(max_length=30)
    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)#자동으로 시간 맞춰줌
    updated_at = models.DateTimeField(auto_now=True) #자동으로 시간 맞춰줌
    # author

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'