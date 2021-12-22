from django.contrib import admin

from posts.models import *


class PostInline(admin.TabularInline):
    model = Post
    ordering = ('order',)


class PageInline(admin.TabularInline):
    model = Page


class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('name', 'public', 'visibility', 'source_code_url', 'created', 'deployment_code')
    inlines = [
        PageInline,
    ]


admin.site.register(Project, ProjectAdmin)


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'created', 'updated',)
    inlines = [
        PostInline
    ]


admin.site.register(Page, PageAdmin)
