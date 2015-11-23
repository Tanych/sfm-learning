from django.contrib import admin
from .models import Weibo
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('weibo_id', 'context', 'pub_date', 'update_time',)

admin.site.register(Weibo, ArticleAdmin)
