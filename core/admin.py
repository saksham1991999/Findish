from django.contrib import admin
from . import models
# Register your models here.

class board_of_membersAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'designation',
                    'contact',
                    ]
    list_display_links = [
        'name',
    ]
    list_filter = ['name',
                    'designation',
    ]
    search_fields = [
        'name',
        'designation'
    ]

class productAdmin(admin.ModelAdmin):
    list_display = ['product_id',
                    'title',
                    'category',
                    'price',
                    'label',
                    ]
    list_display_links = [
        'title',
    ]
    list_filter = ['title',
                    'category',
                    'label',
    ]
    search_fields = [
        'title',
        'category',
        'label',
    ]

class team_membersAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'designation',
                    'contact',
                    ]
    list_display_links = [
        'name',
    ]
    list_filter = ['name',
                    'designation',
    ]
    search_fields = [
        'name',
        'designation'
    ]

class notisficationAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'product',
                    'country',
                    ]
    list_display_links = [
        'name',
    ]
    list_filter = ['name',
                    'product',
                    'date',
                    'country',
    ]
    search_fields = [
        'name',
        'sender_email',
        'message',
        'country',
        'product',
    ]

class messageAdmin(admin.ModelAdmin):
    list_display = ['receiver',
                    'name',
                    'date',
                    'message',
                    ]
    list_display_links = [
        'name',
        'receiver',
    ]
    list_filter = ['name',
                    'receiver',
                    'date',
    ]
    search_fields = [
        'name',
        'receiver',
        'message',
    ]


admin.site.register(models.board_of_members, board_of_membersAdmin)
admin.site.register(models.product, productAdmin)
admin.site.register(models.team_members, team_membersAdmin)
admin.site.register(models.notisfication, notisficationAdmin)
admin.site.register(models.message, messageAdmin)
admin.site.register(models.HomeSlideshow)
admin.site.register(models.RandDSlideshow)