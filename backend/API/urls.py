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
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls'))
]

urlpatterns+= router.urls