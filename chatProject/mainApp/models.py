from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

from django.utils import timezone
import datetime

# Create your models here.
# соглашение именовать в ед. числе
# slugify генерация уникальных слагов
# slugify('\dfj -= 34l;kjf as фв -32"%;:"№?:*(.эЭ,?"}{}|":?><M+_)(*&^%$#@!230p-[=]\';/.,sd', allow_unicode=True)

#
# obj_master.namemodelsecondary_set.all() из экз главн получить экзем-ры ссылающ ForeignKey
# obj_master.namemodelsecondary_set.count()
#
class Ttt_k(models.Model):
    ttttt = models.CharField('мой тест', max_length=50)

class MyTesst(models.Model):
    key = models.ForeignKey(Ttt_k, on_delete=models.CASCADE)
    ttttt = models.CharField('мой тест', max_length=50)
    body = models.TextField('уууыыы', blank=True, db_index=True)
    date_pub = models.DateTimeField('ууqqq', auto_now_add=True)

    def was_published_resently(self):
        return self.date_pub >= (timezone.now() - datetime.timedelta(days=7))
        pass

    def __str__(self):
        return self.ttttt



def slug_create(title: str=''):
    slug = slugify(title + str(time())[:-5])
    return slug


class Tags(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('mainApp:tags_detail_url', kwargs={'slug': self.slug})
    
    def get_update_url(self):
        return reverse('mainApp:tags_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('mainApp:tags_delete_url', kwargs={'slug': self.slug})
    #{% url 'mainApp:posts_update_url' slug=post.slug %

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_create(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Таг'
        verbose_name_plural = 'Таги'
        ordering = ['title']
    #t1=Tag.objects.get(id=1)
    #t1.posts.all()

class Posts(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField()
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tags, blank=True, related_name='posts')
    #a1 = Posts.objects.get(id=1)
    #a1.tags.add(t1)
    #a1.tags.add(t2)
    #a1.tags.all()

    def get_absolute_url(self):
        return reverse('mainApp:posts_detail_url', kwargs={'slug': self.slug})
    
    def get_update_url(self):
        return reverse('mainApp:posts_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('mainApp:posts_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_create(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стфтья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_pub']
        pass


