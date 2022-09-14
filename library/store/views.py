from rest_framework import generics,authentication,permissions,status
from rest_framework.response import Response
from rest_framework import generics, mixins
from .models import *
from .serializers import BookSerializer, BookDetailSerializer,  ReturnBookSerializer, LibrarianSerializer
from django.http import HttpResponse
class BookList(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibrarianAPIView(generics.GenericAPIView, mixins.CreateModelMixin,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = LibrarianSerializer
    queryset = Librarian.objects.all()
    lookup_field = 'id'

    def  get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request,id=None):
        return self.create(request,id)
    def put(self,request):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)

class ReturnBook(generics.GenericAPIView):
    permission_classes=[permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = ReturnBookSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data = request.data)
        self.serializer.is_valid(raise_exception=True)
        order = self.serializer.remove()
        return Response(status = status.HTTP_200_OK)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer






