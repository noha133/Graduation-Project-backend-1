from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('course', views.Viewsss)
# # GET  /students -- JSON Array of all students
# # POST /students -- request body should have student object
# # GET  /students/<pk> -- json object of student of id pk
# # router.register('teachers', views.TeacherView)
# #router.register('test', views.TestView)
#
urlpatterns = [
    #path('<int:pk>', TestView.as_view(), name='test'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('usertype/<int:pk>/', views.UserView.as_view()),
    # path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentView.as_view()),
    path('teacher/<int:pk>/', views.TeacherView.as_view()),
    path('supervisor/<int:pk>/', views.SupervisorView.as_view()),
    path('class/<int:pk>/', views.CLassView.as_view()),
    path('course/<int:pk>/', views.CourseView.as_view()),
    path('department/<int:pk>/', views.DepartmentView.as_view()),
    path('scourses/<int:pk>/', views.StudentCourseView.as_view()),
    # path('scourses/', views.StudentCourseView.as_view()),
    path('tcourses/<int:pk>/', views.TeacherCourseView.as_view()),
    # path('tcourses/', views.TeacherCourseView.as_view()),
    path('grades/<int:pk>/', views.GradeView.as_view()),
    # path('grades/', views.GradeView.as_view()),
    path('todolistt/<int:pk>/', views.ToDoListTeacherView.as_view()),
    path('todolistt/', views.ToDoListTeacherView.as_view()),
    path('todolists/<int:pk>/', views.ToDoListStudentView.as_view()),
    path('announcement/<int:pk>/', views.AnnouncementView.as_view()),
    path('supervisoraccess/<int:pk>/', views.SupervisorClassesView.as_view()),
    path('supervisorteachers/<int:pk>/', views.SupervisorTeachersView.as_view()),
    path('supervisorcourses/<int:pk>/', views.SupervisorCoursesView.as_view()),
    path('assignclass/<int:pk>/', views.AssignClassView.as_view()),
    path('assignclass/', views.AssignClassView.as_view()),
    # path('progress/<int:pk>/', views.ProgressView.as_view()),
    # path('progress/', views.ProgressView.as_view()),
]

# urlpatterns+= router.urls


# # # Authentication # # #

# /dj-rest-auth/login/ (POST)
#
# username
# email
# password

#/dj-rest-auth/logout/ (POST)

# /dj-rest-auth/password/reset/ (POST)
#
# email
#
# /dj-rest-auth/password/reset/confirm/ (POST)
#
# uid
# token
# new_password1
# new_password2
#
# /dj-rest-auth/password/change/ (POST)
#
# new_password1
# new_password2
# old_password
#
# /dj-rest-auth/user/ (GET, PUT, PATCH)
#
# username
# first_name
# last_name
# Returns pk, username, email, first_name, last_name
#
# /dj-rest-auth/registration/ (POST)
#
# username
# password1
# password2
# email
# /dj-rest-auth/registration/verify-email/ (POST)
#
# key