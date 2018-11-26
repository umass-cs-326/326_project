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

#FIXME: implement redirect_field_name in decorator once authorization is restructured to be project-wide
@login_required(login_url='/carton/accounts/login')
def calendar(request):
    # sessions describes all of the class sessions that will be displayed by the calendar
    # Expected to store the items as a list with the format:
    # [course name, start time, end time, days of the week] for each session

    all_courses = Course.objects.all()
    all_sessions = all_sessions = request.user.profile.sessions_current.all()

    sessions = [
        [session.course.name, session.start_time.strftime('%H:%M'), session.end_time.strftime('%H:%M'),
         convert_dow_to_list(session.dow)]
        for session
        in all_sessions
    ]
    # If there was a non-empty search, do logic on accordion courses
    search_term = request.GET.get('search', '')
    if search_term:
        """
        In case search functionality is extended in the future, types of searching functionality listed here:
            https://docs.djangoproject.com/en/2.0/ref/models/querysets/
        Basic functionality is .filter(field__method="searchterm")
        """
        # Get all non-empty space-seperated search terms
        search_terms = filter(None, search_term.split())
        print("Search terms: {}".format(search_terms))
        # For each search term, get all courses that contain the search term or a professor's name contains the term
        matching_courses = [
            merge_course_queries(
                all_courses.filter(name__icontains=term), all_courses.filter(session__instructor__name__icontains=term),
                all_courses.filter(code__icontains=term)
            )[0]
            for term in search_terms
        ]
        accordion_courses, frequency = merge_course_queries(*matching_courses)
        accordion_courses.sort(key=lambda course: frequency[course.name], reverse=True)
    else:
        accordion_courses = all_courses
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

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "class_detail.html"

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
    template_name = "instructor_new.html"

#class InstructorDelete(UpdateView):
#    model = Instructor
#    success_url = reverse_lazy('instructors')