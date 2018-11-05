from django.contrib import admin
from classdoor.models import Course, Teacher, Review, University, User, Subject

#version 2
#description: A different approach for registering models
#Zihang, Matt
#10/26/2018, 11/5/2018

# Register your models here.

@admin.register(Course)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'starRating', 'subject', 'averageGrade')
    #field = ['name', 'teacher', 'description', 'rating', 'review's] 
    #pass
#admin.site.register(Class)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    #pass
#admin.site.register(Teacher, TeacherAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    #the default for field is vertical so it is good enough for displaying them
    #using a list filter to sort results
    list_filter = ('title','date', 'courseOfReview')
    list_display = ('title', 'starRating', 'date', 'courseOfReview')
    #pass
#admin.site.register(Review)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    #pass
#admin.site.register(University)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    #default display
    pass
#admin.site.register(User)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'universityName')
    #pass
#admin.site.register(Subject)
