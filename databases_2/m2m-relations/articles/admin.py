# from django.contrib import admin
#
# from .models import Article, Relationship, Thematics
#
#
# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]
#
#
# @admin.register(Thematics)
# class ThematicsAdmin(admin.ModelAdmin):
#     pass

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Relationship, Article, Thematics


class RelationshipInline(admin.TabularInline):
    model = Relationship


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Thematics)
class ThematicsAdmin(admin.ModelAdmin):
    pass
