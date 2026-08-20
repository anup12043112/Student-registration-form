from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken 

from .views import FormViewAPI, CourseViewAPI, DepartmentViewAPI

router = DefaultRouter()
router.register("form", FormViewAPI, basename="form")
router.register("course", CourseViewAPI, basename="course")
router.register("department", DepartmentViewAPI, basename="department")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', ObtainAuthToken.as_view()),
]