from django.shortcuts import render
from carton.models import Course, Instructor, Session
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Session
from django.views.generic import TemplateView
from collections import Counter
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import forms
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.views import View
from django.urls import reverse
from carton.models import Comment
from datetime import datetime
from django.db.models import Sum

# Keeps track of the mapping from letter to number
letters = {
    'm': 1,
    't': 2,
    'w': 3,
    'r': 4,
    'f': 5
}
# The opposite
reverse_letters = {v:k for (k, v) in letters.items()}

def convert_dow_to_list(dow):
    return [letters.get(day) for day in dow if day in letters.keys()]

def convert_dow_to_str(dow):
    return ''.join(reverse_letters.get(day, '') for day in dow)

def merge_course_queries(*queries):
    """
    Combines course queries into a single flattened query
    Removes duplicates (by name), and tracks the number of times each name pops up
    Returns the flattened query, as well as the number of times each query is shown
    """
    # Use a modified dict that returns dict[invalid_key] as 0
    seen = Counter()
    final_query = list()
    for query in queries:
        for course in query:
            if not seen[course.name]:
                final_query.append(course)
            seen[course.name] += 1
    return final_query, seen

def search_courses(search_text):
    all_courses = Course.objects.all()
    if search_text:
        """
        In case search functionality is extended in the future, types of searching functionality listed here:
            https://docs.djangoproject.com/en/2.0/ref/models/querysets/
        Basic functionality is .filter(field__method="searchterm")
        """
        # Get all non-empty space-seperated search terms
        search_terms = filter(None, search_text.split())
        print("Search terms: {}".format(search_terms))
        # For each search term, get all courses that contain the search term or a professor's name contains the term
        matching_courses = [
            merge_course_queries(
                all_courses.filter(name__icontains=term), all_courses.filter(session__instructor__name__icontains=term),
                all_courses.filter(code__icontains=term)
            )[0]
            for term in search_terms
            ]
        courses, frequency = merge_course_queries(*matching_courses)
        # First sort by class type, then number (lowest to highest)
        courses.sort(key=lambda course: course.code)
        # Then sort by highest to lowest frequency
        courses.sort(key=lambda course: frequency[course.name], reverse=True)
    else:
        courses = all_courses
    return courses


#FIXME: implement redirect_field_name in decorator once authorization is restructured to be project-wide
@login_required(login_url='/carton/accounts/login')
def calendar(request):
    #FIXME: no verification at all lol
    if(request.method == "POST"): #user tried to add a session to fullCalendar
        added_pk = request.POST.get('added_session')
        removed_pk = request.POST.get('removed_session')
        if added_pk:
            request.user.profile.sessions_current.add(Session.objects.get(pk=added_pk))
        elif removed_pk:
            request.user.profile.sessions_current.remove(Session.objects.get(pk=removed_pk))
        request.user.profile.save()

    # sessions describes all of the class sessions that will be displayed by the calendar
    # Expected to store the items as a list with the format:
    # [course name, start time, end time, days of the week] for each session

    all_sessions = request.user.profile.sessions_current.all()

    sessions = [
        [session.course.name, session.start_time.strftime('%H:%M'), session.end_time.strftime('%H:%M'),
         convert_dow_to_list(session.dow)]
        for session
        in all_sessions
    ]
    # If there was a non-empty search, do logic on accordion courses
    search_text = request.GET.get('search', '')
    accordion_courses = search_courses(search_text)
    print("Post search courses: {}".format(accordion_courses))
    accordion_courses = [
        [course.name, course.rating, course.session_set.all().order_by('start_time'), course.id]
        for course
        in accordion_courses
    ]

    return render(request, 'main.html', {"sessions": sessions, "courses": accordion_courses})

def index(request):

    template = get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/carton/accounts/login')
def profile_page(request):
    if(request.method == "POST"):
        all_courses = Course.objects.all()
        added_pk = request.POST.get('added_course')
        removed_pk = request.POST.get('removed_course')
        if added_pk:
            request.user.profile.courses_past.add(all_courses.get(pk=added_pk))
        else:
            request.user.profile.courses_past.remove(all_courses.get(pk=removed_pk))
        request.user.profile.save()
    total_credits = request.user.profile.courses_past.aggregate(Sum('credits'))['credits__sum']
    # Coerce to 0 if false
    total_credits = total_credits or 0
    search_text = request.GET.get('search', '')
    return render(request, 'accounts/profile.html', {
        'total_credits': total_credits,
        'remaining_credits': 120-total_credits,
        'courses': search_courses(search_text)
    })

# def doot(request):
#     #template = get_template('course_detail.html')
#     if(request.method == "POST"):
#         if('upd' in request.POST):
#             updooted = request.user.profile.updooted.all()
#         if('downd' in request.POST):
#             downdooted = request.user.profile.downdooted.all()



class CommentForm(forms.Form):
    message = forms.CharField()

class DumbForm(forms.Form):
    pass
class CourseDisplay(generic.DetailView):
    model = Course
    template_name = "class_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CourseComment(SingleObjectMixin, FormView):
    template_name = "class_detail.html"
    form_class = CommentForm
    model = Course

    def post(self, request, *args, **kwargs):
        print(request, args, kwargs)
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        comment = Comment(course = self.object, name = request.user, comment_text=request.POST.get("message", ""),date=datetime.now)
        comment.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('course-detail', kwargs={'pk': self.object.pk})


class DumbDoot(SingleObjectMixin, FormView):
    template_name = "class_detail.html"
    form_class = DumbForm
    model = Course

    def post(self, request, *args, **kwargs):
        print(request, args, kwargs)
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        print(self.object.name)
        if('upd' in request.POST):
            request.user.profile.updooted.add(self.object)
        if('downd' in request.POST):
            print("inside downd")
            request.user.profile.downdooted.add(self.object)
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('course-detail', kwargs={'pk': self.object.pk})
class Doot(SingleObjectMixin, FormView):
    template_name = "class_detail.html"
  
    
    model = Course
    def post(self, request, *args, **kwargs):
        print(request, args, kwargs)
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('course-detail', kwargs={'pk': self.object.pk})

class CourseDetailView(View):

    def get(self, request, *args, **kwargs):
        view = CourseDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if('comment_form_post' in request.POST):
            view = CourseComment.as_view()
            return view(request, *args, **kwargs)
        elif('upd' in request.POST):
            print("py sux")
            view = DumbDoot.as_view()
            return view(request, *args, **kwargs)
        elif('downd' in request.POST):
            view = DumbDoot.as_view()
            return view(request, *args, **kwargs)

class CourseCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'add_Course'
    model = Course
    fields = '__all__'
    template_name = 'course_new.html'

class InstructorListView(generic.ListView):
    model = Instructor
    template_name = "instructor_list.html"

class InstructorDetailView(generic.DetailView):
    model = Instructor
    template_name = "instructor_detail.html"

class InstructorCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'add_Instructor'
    model = Instructor
    fields = '__all__'
    template_name = 'instructor_new.html'


#class InstructorDelete(UpdateView):
#    model = Instructor
#    success_url = reverse_lazy('instructors')
