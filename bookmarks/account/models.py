from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



class Contact(models.Model):
    user_from = models.ForeignKey(User , on_delete=models.CASCADE , related_name='rel_from_set')
    user_to = models.ForeignKey(User , on_delete=models.CASCADE , related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))