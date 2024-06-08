from rest_framework import generics
from .models import User, Worker
from .serializers import UserSerializer, WorkerSerializer
import datetime
import openpyxl
from django.http import HttpResponse
from rest_framework.views import APIView

class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.exclude(is_staff=True)
        return queryset


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkerCreateView(generics.CreateAPIView):
    serializer_class = WorkerSerializer


class WorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    

class WorkerList(generics.ListAPIView):
    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        month = self.request.query_params.get('month')
        attendance_status = self.request.query_params.get('attendance_status')

        if month and attendance_status:
            
            month_date = datetime.datetime.strptime(month, '%Y-%m')
            queryset = queryset.filter(
                attendance_status=attendance_status,
                attendance_date__year=month_date.year,
                attendance_date__month=month_date.month
            )
        return queryset


class ExportWorkersView(APIView):
    
    def get(self, request):
        workers = Worker.objects.all()

        wb = openpyxl.Workbook()
        ws = wb.active

        headers = ['First Name', 'Attendance Status', 'Attendance Date']
        ws.append(headers)

        for worker in workers:
            row = [
                worker.user.first_name,
                worker.get_attendance_status_display(),  
                worker.attendance_date.strftime('%Y-%m-%d'),
               
            ]
            ws.append(row)

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Workers_Attendance.xlsx'

        wb.save(response)

        return response
