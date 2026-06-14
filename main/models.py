from django.db import models

class SiteContent(models.Model):
    key = models.CharField(max_length=100, unique=True, verbose_name="Ключ")
    title = models.CharField(max_length=200, blank=True, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое (HTML)")
    image = models.ImageField(upload_to='content_images/', blank=True, null=True)

    def __str__(self):
        return self.key

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.name}"