from django.contrib import admin

from .models.site import Category, New, Comment, Subscribe, Contact

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug","is_menyu"]
    readonly_fields = ['slug']


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ["short_title", "tag", "data", "view"]

    @admin.display(empty_value="???")
    def short_title(self, obj, *args, **kwargs):
      return obj.title.strip()[::2]

    @admin.display(empty_value="???")
    def tag(self, obj, *args, **kwargs):
        if obj.tags:
            return obj.tags.replace("#", "").title().split()[:2]



admin.site.register(Comment)
admin.site.register(Subscribe)
admin.site.register(Contact)
