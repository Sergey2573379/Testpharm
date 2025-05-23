from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200, verbose_name='имя')
    family = models.CharField(max_length=200, verbose_name='фамилия')
    email = models.CharField(max_length=200, verbose_name='емаил')
    img = models.FileField(upload_to="upl/", default=None, verbose_name='Фото')
    status = models.CharField(max_length=200, verbose_name='статус')
    password = models.CharField(max_length=200, verbose_name='пароль')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    editdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.name


class Dorixona(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    article = models.TextField(max_length=20000, verbose_name='Описание')
    email = models.CharField(max_length=200, verbose_name='емаил')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    editdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    users = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Caetegory_drug(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title




class Drug(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=200, verbose_name='Название')
    article = models.CharField(max_length=2000, verbose_name='Описание')
    img = models.FileField(upload_to="upl/", verbose_name='Фото')
    price = models.IntegerField(verbose_name='цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    editdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    caetegorydrug = models.ForeignKey(Caetegory_drug, on_delete=models.CASCADE)
    caetegorydorixona = models.ForeignKey(Dorixona, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Commentdrug(models.Model):
    article = models.CharField(max_length=2000, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    editdate = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    comusers = models.ForeignKey(Users, on_delete=models.CASCADE)
    comudrug = models.ForeignKey(Drug, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Card(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    img = models.FileField(upload_to="upl/", verbose_name='Фото')
    price = models.IntegerField(verbose_name='цена')
    quantity = models.IntegerField(verbose_name='количество')
    user_id = models.IntegerField()
    prod_id = models.IntegerField()

class Order(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    price = models.IntegerField(verbose_name='цена')
    qty = models.IntegerField(verbose_name='количество')
    user_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')




class Check(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    drug = models.CharField(max_length=200, verbose_name='лекарства')
    img = models.FileField(upload_to="upl/", verbose_name='Фото')
    price = models.IntegerField(verbose_name='цена')
    quantity = models.IntegerField(verbose_name='количество')
    total = models.IntegerField(verbose_name='итого')
    user_id = models.IntegerField()

    def __str__(self):
        return self.title











