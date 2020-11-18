from django.db import models

class Form(models.Model):
    name = models.CharField('Name', max_length = 100)
    email = models.EmailField('E-mail', max_length = 100)
    phone = models.CharField('Phone', max_length = 20)
    idea = models.TextField('Idea')
    #cover = models.FileField(upload_to='img/')

    def __str__(self):
        return self.name