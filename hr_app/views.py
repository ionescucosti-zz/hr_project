from datetime import datetime
from django.db.models import Avg, Sum
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


def index(request):
    employees = Employees.objects.all().values()
    return render(request, "index.html", {"health": employees})


class EmployeesPagination(PageNumberPagination):
    page_size = 10


class EmployeesViewSet(viewsets.ModelViewSet):
    pagination_class = EmployeesPagination
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        gender = self.request.query_params.get('gender')
        try:
            if gender in ["m", "M"]:
                employees = Employees.objects.all().values().filter(gender="M")
            elif gender in ["f", "F"]:
                employees = Employees.objects.all().values().filter(gender="F")
            elif gender not in ["m", "f", "M", "F", None]:
                employees = Employees.objects.exclude(gender__in=["M", "F"])
            else:
                employees = Employees.objects.all().values()
            return employees
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class employee(APIView):
    def get(self, request, id):
        try:
            if id:
                employee = Employees.objects.get(id=id)
                serializer = EmployeesSerializer(employee, many=False)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_404_NOT_FOUND)

        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            if id:
                employee = Employees.objects.get(id=id)
                request = request.data
                employee.id = id
                employee.first_name = request['first_name']
                employee.last_name = request['last_name']
                employee.email = request['email']
                employee.gender = request['gender']
                employee.date_of_birth = request['date_of_birth']
                employee.industry = request['industry']
                employee.salary = request['salary']
                employee.years_of_experience = request['years_of_experience']
                employee.save()
                serializer = EmployeesSerializer(employee, many=False)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_404_NOT_FOUND)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if id:
            snippet = Employees.objects.get(id=id)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class avg_age_industry(APIView):
    def get(self, request):
        try:
            result = Employees.objects.values("industry").annotate(Average_age=Avg("years_of_experience"))
            return Response(result)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class avg_salary_industry(APIView):
    def get(self, request):
        try:
            result = Employees.objects.values("industry").annotate(Average_salaries=Avg('salary'))
            return Response(result)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class avg_salary_experience(APIView):
    def get(self, request):
        try:
            result = Employees.objects.values("years_of_experience").annotate(Average_salaries=Avg('salary'))
            return Response(result)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class total_salary(APIView):
    def get(self, request):
        try:
            result = Employees.objects.all().aggregate(Total_salary=Sum('salary'))
            return Response(result)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class salary_per_industry(APIView):
    def get(self, request):
        try:
            result = Employees.objects.values("industry").annotate(Total_salary=Sum('salary'))
            return Response(result)
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class EmployeesOver60ViewSet(viewsets.ModelViewSet):
    pagination_class = EmployeesPagination
    serializer_class = EmployeesSerializer

    def get_queryset(self):
        try:
            result = Employees.objects.all().values().filter(date_of_birth__year__lte=datetime.now().year - 60)
            return result
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)