from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from core.models import BaseModel


class UserProfile(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.')
    phno = models.CharField(
        _('Phone number'),
        max_length=16,
        unique=True,
        default='',
        blank=True,
        help_text=_('Only digits allowed'),
        validators=[phone_regex],
    )
    zipcode = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')

    objects = UserManager()
    USERNAME_FIELD = 'username'

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def __unicode__(self):
        return unicode('{}'.format(self.username))

    class Meta:
        db_table = 'tb_userprofile'

    @property
    def to_json(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'email': self.email,
            'phno': self.phno,
            'address': self.address
        }


class Gallery(BaseModel):
    user = models.ForeignKey(UserProfile, related_name='user_gallery', db_index=True)
    photo_filename = models.CharField(max_length=250, default='', blank=True)
    title = models.CharField(max_length=250, default='', blank=True)
    short_description = models.TextField(default='')

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    def __unicode__(self):
        return unicode('{}'.format(self.title))

    class Meta:
        db_table = 'tb_gallery'

    @property
    def to_json(self):
        return {
            'short_description': self.short_description,
            'filename': self.photo_filename,
            'title': self.title
        }
