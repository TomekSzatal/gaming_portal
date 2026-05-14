from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Game, Article, Review


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("bio",),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": ("bio",),
            },
        ),
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("genre",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("created_at",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_filter = ("rating", "created_at")
