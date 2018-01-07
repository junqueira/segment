# from __future__ import unicode_literalsc

from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from .serializers import TalkMongoSerializer, ToolSerializer, BookSerializer, AuthorSerializer, BairroSerializer, ConcorrenteSerializer, BairroMongoSerializer, ConcorrenteMongoSerializer

from .models import TalkMongo, Tool, Book, Author, BairroMongo, ConcorrenteMongo
from .models_dj import Bairro, Concorrente

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from rest_framework import generics, permissions


def index_view(request):
    context = {}
    return TemplateResponse(request, 'index.html', context)


class ToolViewSet(MongoModelViewSet):
    """
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    """
    lookup_field = 'id'
    serializer_class = ToolSerializer

    def get_queryset(self):
        return Tool.objects.all()


class BookViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class AuthorViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = AuthorSerializer
    # permission_classes = [AuthorCanEditPermission,
	# 	                  permissions.IsAuthenticated
    # ]

    def get_queryset(self):
        return Author.objects.all()


class ImportViewSet(MongoModelViewSet):
    """
    API endpoint that allows import to be viewed or edited.
    """
    parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)

    """
    Try out this view with the following curl command:

    curl -X POST http://localhost:81/talks/bulk_upload/ \
        -d "speaker,topic,scheduled_at
            Ana Balica,Testing,2016-11-03T15:15:00+01:00
            Aymeric Augustin,Debugging,2016-11-03T16:15:00+01:00" \
        -H "Content-type: text/csv" \
        -H "Accept: text/csv"
    """


# class BairroMongoViewSet(ImportViewSet):
class BairroMongoViewSet(MongoModelViewSet):
    # lookup_field = 'id'
    parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = (CSVRenderer,) + tuple(api_settings.DEFAULT_RENDERER_CLASSES)
    serializer_class = BairroMongoSerializer

    meta = {
        'indexes': [
            {'fields': ['-codigo'], 'unique': True,
              'sparse': True, 'types': False },
        ],
    }

    def get_queryset(self):
        return BairroMongo.objects.all()

    def get_renderer_context(self):
        context = super(BairroMongoViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context

    @list_route(methods=['POST'])
    def bulk_upload(self, request, *args, **kwargs):

        # import ipdb; ipdb.set_trace()
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_303_SEE_OTHER, headers={'Location': reverse('api:bairro-list')})


class BairroViewSet(ImportViewSet):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer

    def get_renderer_context(self):
        context = super(BairroViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context

    @list_route(methods=['POST'])
    def bulk_upload(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_303_SEE_OTHER, headers={'Location': reverse('api:bairro-list')})


class ConcorrenteViewSet(ImportViewSet):
    queryset = Concorrente.objects.all()
    serializer_class = ConcorrenteSerializer

    def get_renderer_context(self):
        context = super(ConcorrenteViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else '')
        return context