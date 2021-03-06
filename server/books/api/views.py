"""
DOCSTRINGS
"""

from rest_framework import generics, mixins
from books.models import Book
from .serializers import bookSerializer


class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer
  queryset = Book.objects.all()
    
def get_queryset(self):
  return queryset

def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)
