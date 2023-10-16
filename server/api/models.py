from django.db import models

# Create your models here.

class TelegramUser(models.Model):
    external_id = models.BigIntegerField(verbose_name='tg id', unique=True)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=256, null=True,blank=True, verbose_name='Ник в тг')
    first_name = models.CharField(max_length=256, null=True, blank=True,verbose_name='Имя в тг')
    second_name = models.CharField(max_length=256, null=True, blank=True,verbose_name='Фамилия в тг')
    is_notificated = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.username is not None:
            return self.username
        return str(self.external_id)

    class Meta:
        verbose_name = 'Telegram пользователь'
        verbose_name_plural = 'Telegram пользователи'

class Location(models.Model):
    name = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

class ActionType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Тип действия'
        verbose_name_plural = 'Типы действий'

class UserAction(models.Model):
    user = models.ForeignKey(to=TelegramUser, on_delete=models.CASCADE)
    action =  models.ForeignKey(to=ActionType, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Действие пользователя'
        verbose_name_plural = 'Действия пользователей'
