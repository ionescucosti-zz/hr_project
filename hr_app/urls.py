from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("employees", views.EmployeesViewSet, basename="employees")
router.register("employees_over_60", views.EmployeesOver60ViewSet, basename="employees over age 60")
urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('employee/<int:id>', views.employee.as_view(), name='employee'),
    path('avg_age_industry', views.avg_age_industry.as_view(), name='age_industry'),
    path('avg_salary_industry', views.avg_salary_industry.as_view(), name='salary_industry'),
    path('avg_salary_experience', views.avg_salary_experience.as_view(), name='salary_experience'),
    path('total_salary', views.total_salary.as_view(), name='total_salary'),
    path('salary_per_industry', views.salary_per_industry.as_view(), name='salary_per_industry'),
    # path('employees_over_60', views.employees_over_60.as_view(), name='employees_over_60'),
]
