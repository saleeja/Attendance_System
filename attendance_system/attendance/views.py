from rest_framework import generics
from .models import User, Worker
from .serializers import UserSerializer, WorkerSerializer
import datetime

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
