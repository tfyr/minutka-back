from datetime import datetime

from django.db import models


class Review(models.Model):
    name = models.CharField('Имя', max_length=100)
    text = models.CharField('Сообщение', max_length=5000)
    pub_date = models.DateTimeField('date published', default=datetime.now, blank=True)
    published = models.BooleanField('Опубликовано', default=False, null=False,)
