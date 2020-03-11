from django.contrib import admin

from .models import Article, Relationship


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

