from rest_framework import serializers

from .models import TalkMongo
from .models_dj import Bairro, Concorrente

from rest_framework_mongoengine import serializers as mongoserializers

from app.models import Tool, Author, Book, BairroMongo, ConcorrenteMongo


class ToolSerializer(mongoserializers.DocumentSerializer):
    id = serializers.CharField(read_only=False)

    class Meta:
        model = Tool
        fields = '__all__'


class AuthorSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class TalkMongoSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = TalkMongo
        fields = '__all__'


class BairroSerializer (serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = '__all__'
        

class BairroMongoSerializer (mongoserializers.DocumentSerializer):
# class BairroMongoSerializer (DynamicDocument):
    # id = serializers.CharField(read_only=False, required=False)
    # codigo = serializers.CharField(read_only=False, required=True)
    # codigo = serializers.UUIDField()
    # uuid = fields.UUIDField(default=uuid.uuid4)
    class Meta:
        model = BairroMongo
        fields = '__all__'
        # fields = ('codigo', 'nome', 'municipio', 'uf', 'area',)


class ConcorrenteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Concorrente
        fields = '__all__'


class ConcorrenteMongoSerializer (serializers.ModelSerializer):
    class Meta:
        model = ConcorrenteMongo
        fields = '__all__'