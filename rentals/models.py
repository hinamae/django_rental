from django.db import models

class Equ_Model(models.Model):
    # 項目を作る
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    memo = models.TextField()
    isbn = models.CharField(max_length=13)
    status = models.IntegerField()
    def __str__(self):
        return self.title