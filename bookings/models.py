from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Table(models.Model):
    number = models.PositiveSmallIntegerField(unique=True, verbose_name="Номер столика")
    seats = models.PositiveSmallIntegerField(verbose_name="Количество мест")
    location = models.CharField(max_length=100, blank=True, verbose_name="Расположение (зал/терраса)")

    class Meta:
        ordering = ['number']
        verbose_name = "Столик"
        verbose_name_plural = "Столики"

    def __str__(self):
        return f"Столик {self.number} ({self.seats} мест)"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('cancelled', 'Отменено'),
        ('completed', 'Завершено'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', verbose_name="Пользователь")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings', verbose_name="Столик")
    date = models.DateField(verbose_name="Дата бронирования")
    time = models.TimeField(verbose_name="Время")
    guests = models.PositiveSmallIntegerField(verbose_name="Количество гостей")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time']
        unique_together = [['table', 'date', 'time']]  # один столик не может быть забронирован дважды в одно время
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

    def __str__(self):
        return f"{self.user.username} - {self.table} - {self.date} {self.time}"