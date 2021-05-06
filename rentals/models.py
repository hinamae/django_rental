from django.db import models
from django.contrib.auth.models import User

# 本のテーブル
class Equ_Model(models.Model):
    # 項目を作る
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    memo = models.TextField()
    isbn = models.CharField(max_length=13)
    status = models.IntegerField()
    # 管理者画面から管理するためのラベル付け
    def __str__(self):
        return self.title

# 貸し出し明細テーブル(本1冊ごと)
class Lending_Book(models.Model):
    # ユーザテーブルを参照する外部キー(参照しているユーザレコードが削除された場合にLending_Bookテーブルのレコードを残す)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # 本テーブルを参照する外部キー(参照しているユーザレコードが削除された場合にLending_Bookテーブルのレコードを削除する)
    equ_model = models.ForeignKey(Equ_Model, on_delete=models.CASCADE)
    rental_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()
    # 管理者画面から管理するためのラベル付け
    def __int__(self):
        return self.user

    