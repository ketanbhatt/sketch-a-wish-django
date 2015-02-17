from django.contrib import admin
from saw.models import Wish, Sketch, UserProfile

# Register your models here.
class WishAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'wisher', 'sketcher', 'created_on', 'locked', 'sketched')

class SketchAdmin(admin.ModelAdmin):
    model = Sketch
    list_display = ('pk', 'image_temp', 'wish', 'get_wisher', 'get_sketcher', 'likes', 'assigned_on', 'submitted_on')

    def get_wisher(self, obj):
        return obj.wish.wisher
    get_wisher.short_description = "Wisher"

    def get_sketcher(self, obj):
        return obj.wish.sketcher
    get_sketcher.short_description = "Sketcher"

admin.site.register(Wish, WishAdmin)
admin.site.register(Sketch, SketchAdmin)
admin.site.register(UserProfile)
