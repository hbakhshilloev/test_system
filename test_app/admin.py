from django.contrib import admin
from test_app.models import Category , TestModel
# Register your models here.

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('category' , 'question')
    list_filter = ('category',)
    list_display_links = ('question',)
    search_fields = ('category', 'question')

admin.site.register(Category)
