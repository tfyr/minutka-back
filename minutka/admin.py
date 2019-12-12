from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'pub_date',
        'name',
        'text',
        'published',
    )

#admin.site.register(Pirog, PirogAdmin)
admin.site.register(Review, ReviewAdmin)
