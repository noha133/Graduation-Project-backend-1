from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from . views import TestView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('students', views.StudentView)
# GET  /students -- JSON Array of all students
# POST /students -- request body should have student object
# GET  /students/<pk> -- json object of student of id pk
router.register('teachers', views.TeacherView)
#router.register('test', views.TestView)

urlpatterns = [
    path('', TestView.as_view(), name='test'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]

urlpatterns+= router.urls


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