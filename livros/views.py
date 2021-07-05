from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LivrosSerializer
from .models import Livro


class LivrosApiView(ListAPIView):
    """
    Utilize este endereço para gerenciar seus livros
    """
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer

class LivroCreateView(CreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer

class LivroUpdateView(UpdateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivrosSerializer


livros_view = LivrosApiView.as_view()
livros_create_view = LivroCreateView.as_view()
livros_update_view = LivroUpdateView.as_view()






      

  
