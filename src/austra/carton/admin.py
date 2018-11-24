from django.contrib import admin

from carton.models import Course, Instructor, Session, Comment, Profile


class CourseAdmin(admin.ModelAdmin) :
	list_display = ("code", "name", "rating", "display_prereqs")

admin.site.register(Course, CourseAdmin)


class InstructorAdmin(admin.ModelAdmin) :
	list_display = ("name", "rating")

admin.site.register(Instructor, InstructorAdmin)

class SessionAdmin(admin.ModelAdmin) :
	list_display = ("course", "instructor", "max_seats", "get_rating")

admin.site.register(Session, SessionAdmin)

class CommentAdmin(admin.ModelAdmin) :
	list_display = ("course", "name", "comment_text", "date")
admin.site.register(Comment, CommentAdmin)

#class SessionsCurrentInline(admin.TabularInline):
#    model = Profile.sessions_current.through

class ProfileAdmin(admin.ModelAdmin) :
	list_display = ("user",)
	#inlines = [ SessionsCurrentInline ]
	#exclude = ('sessions_current',)
admin.site.register(Profile, ProfileAdmin)
