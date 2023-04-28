from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
# from django.core.urlresolvers import 
# from django.http import rever
from django.urls import reverse




class Image(models.Model):
    user = models.ForeignKey(User,related_name='images_created' , on_delete=models.CASCADE)
    users_like = models.ManyToManyField(User,  related_name='images_liked', blank=True )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
    blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
    db_index=True)
    total_likes = models.PositiveIntegerField(db_index=True,default=0)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title

    


    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)

