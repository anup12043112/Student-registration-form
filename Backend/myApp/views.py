from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from .models import RegisterationForm, Course, Department
from .serializers import RegistrationFormSerializer, CourseSerializer, Departmenterializer

# Create your views here.
class FormViewAPI(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    
    authentication_classes = [TokenAuthentication]
    # queryset = RegisterationForm.objects.all()
    serializer_class = RegistrationFormSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = [AllowAny]

        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        order = self.request.query_params.get("order")
        if (order):
            return RegisterationForm.objects.all().order_by(order)
        
        return RegisterationForm.objects.all()


class CourseViewAPI(
    GenericViewSet,
    mixins.ListModelMixin
    ):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class DepartmentViewAPI(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    
    queryset = Department.objects.all()
    serializer_class = Departmenterializer

