from django.contrib import admin
from classdoor.models import ClassDesc, Review, University, User, Subject

# Register your models here.

@admin.register(ClassDesc)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher", "description", "rating", "avgGrade")
    fields = ["name", "teacher", "description", "preReqs", ("rating", "avgGrade"), "reviews", "subject", "universityName"]

@admin.register(Review)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("title", "starRating")
    fields = ["title", "text", "starRating", "gradeReceived", "classDesc", "author", "likes", "dislikes"]

@admin.register(University)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    fields = ["name", "location", "classes", "subjectsOffered"]

@admin.register(User)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    fields = ["username", "email", "password", "major", "writtenReviews"]

@admin.register(Subject)
class ClassDescAdmin(admin.ModelAdmin):
    list_display = ("name", "universityName")
    fields = ["name", "universityName"]
