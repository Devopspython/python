# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post,Details
# Register your models here.
admin.site.register(Post)

admin.site.register(Details)