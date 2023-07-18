from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from administracion.models import Reportes
from .serializers import ReportesSerializer

class APIRootView(APIView):
    def get(self, request):
        # Generamos los enlaces a todas las URLs del API
        data = {
            'reportes': reverse('reportes-list-create', request=request),
            # Puedes agregar más enlaces a otras URLs del API aquí si es necesario
        }
        return Response(data)
        
class ReportesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer

class ReportesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer
