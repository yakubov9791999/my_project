from django.contrib import admin
from .models import Article

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    def body_short(self, obj: Article):
        return f'{obj.body[:30]}...'
    list_display = ['id', 'title','body_short','type','pub_date']
