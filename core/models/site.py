from django.db import models

# Create your models here.

from django.utils.text import  slugify


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True)
    is_menyu = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.name} | {self.slug}'

    class Meta:
        verbose_name = 'Toifa'
        verbose_name_plural = "1-Toifalar"

class New(models.Model):
    title = models.CharField (max_length=512)
    short_desc = models.TextField()
    desc2 = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='news/')
    img1 = models.ImageField(upload_to='news/', null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True,auto_now=False)
    tags = models.CharField(max_length=152)
    view = models.IntegerField (default = 0, editable = False)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.tags and '#' not in self.tags:
            self.tags ='#'+' #'.join(self.tags.lower().split())
        return super(New ,self).save(*args, **kwargs)

    # def tags(self):
    #     return self.tag.split('#')

    def get_date_cr(self):
      import datetime
      now = datetime.datetime.now()
      calc = int((now - self.data).total_seconds() // 60)
      if calc <= 0:
        return "Hozirgina"

      if 60 > calc > 0:
        return f"{calc} minut oldin"

      if 60 <= calc < 60 * 24:
        return f"{int(calc // 60)} soat oldin"

      if 60 * 24 <= calc:
        return self.data.strftime("%H:%M / %d-%B %Y-yil  ")

    def __str__(self):
        return f"{' '.join(self.title.split()[:2])}"

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = "2-Yangiliklar"

class Comment (models.Model):
    user = models.CharField(max_length=56)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}|{self.text}'

    class Meta:
        verbose_name = 'Fkir'
        verbose_name_plural = "3-Fkirlar"

class Subscribe (models.Model):
    email = models.EmailField()
    is_trash = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email}|{self.is_trash}'

    class Meta:
        verbose_name = 'Obuna'
        verbose_name_plural = "4-Obunalar"



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    is_trash = models.BooleanField(default=True)
    is_read = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.name} | {self.email} '

    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = "4-Kontaktlar"
