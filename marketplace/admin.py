from django.contrib import admin

from marketplace.models import User, Bid, Project


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'project', 'amount', 'is_accepted', 'created_at')
    list_filter = ('is_accepted', 'freelancer')
    search_fields = ('freelancer__username', 'project__title')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'budget', 'status', 'created_at')
    list_filter = ('status', 'client')
    search_fields = ('title', 'client__username')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

