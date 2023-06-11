from django.db import models

class Item(models.Model):
    '''элемент списка'''
    text = models.TextField(default='')
