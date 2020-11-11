from django.db import models

class Form(models.Model):
    name = models.CharField('Name', max_length = 100)
    email = models.EmailField('E-mail', max_length = 100)
    tel = models.CharField('Phone', max_length = 20)
    idea = models.TextField('Idea')

    def __str__(self):
        return self.name