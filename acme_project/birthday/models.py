from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        blank=True, help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField(
        'Дата рождения', validators=(real_age,)
    )
    image = models.ImageField(
        'Фото', upload_to='birthdays_images', blank=True
    )
    constraints = (
        models.UniqueConstraint(
            fields=('first_name', 'last_name', 'birthday'),
            name='Unique person constraint',
        ),
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE,
        null=True
    )
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse(
            'birthday:detail', kwargs={'pk': self.pk}
        )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
