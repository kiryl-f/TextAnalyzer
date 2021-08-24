from django.db import models


# Create your models here.

class Text(models.Model):
    title = models.CharField(null=True, max_length=50)
    text = models.TextField(null=True)

    language = models.ForeignKey('Language', null=True, on_delete=models.PROTECT, verbose_name='Язык')

    class Meta:
        verbose_name_plural = 'Текст'
        verbose_name = 'Текст'
        ordering = ['title', 'text']

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.title) + '\n' + str(self.text) + '\n'


class Language(models.Model):
    name = models.CharField(max_length=10, verbose_name='Language', db_index=True)

    class Meta:
        verbose_name_plural = 'Язык'
        verbose_name = 'Язык'
        ordering = ['name']

    def __str__(self):
        return self.name


