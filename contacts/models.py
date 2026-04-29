from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f"{self.name} ({self.email})"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.email
    
#class ContactInfo(models.Model):
    #email = models.EmailField(verbose_name='Email')
    #phone = models.CharField(max_length=30, verbose_name='Телефон')
    #address = models.CharField(max_length=255, verbose_name='Адрес')

    #facebook = models.URLField(blank=True, verbose_name='Facebook')
    #instagram = models.URLField(blank=True, verbose_name='Instagram')
    #twitter = models.URLField(blank=True, verbose_name='Twitter')
    #linkedin = models.URLField(blank=True, verbose_name='LinkedIn')

    #class Meta:
        #verbose_name = 'Контактная информация'
        #verbose_name_plural = 'Контактная информация'

    #def __str__(self):
        #return 'Контактная информация сайта'
        
class ContactInfo(models.Model):
    title = models.CharField(max_length=100, default='Контакты', verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return self.title


class ContactEmail(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='emails')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return self.email


class ContactPhone(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='phones')
    phone = models.CharField(max_length=30, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.phone


class ContactAddress(models.Model):
    contact_info = models.ForeignKey(
        ContactInfo,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    address = models.CharField(max_length=255, verbose_name='Полный адрес')
    #map_url = models.URLField(blank=True, verbose_name='Ссылка на карту')
    map_url = models.TextField(blank=True, verbose_name='Ссылка на карту')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city}: {self.street}'


class SocialLink(models.Model):
    slug = models.SlugField(max_length=50, verbose_name='Код (facebook, instagram)')
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='social_links')
    name = models.CharField(max_length=50, verbose_name='Название')
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

    def __str__(self):
        return self.name