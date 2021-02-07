from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentView)
# GET  /students -- JSON Array of all students
# POST /students -- request body should have student object
# GET  /students/<pk> -- json object of student of id pk
router.register('teachers', views.TeacherView)

urlpatterns = [
]

urlpatterns+= router.urls