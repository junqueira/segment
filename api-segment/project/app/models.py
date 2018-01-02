from mongoengine import Document, EmbeddedDocument, fields


class Author(Document):
    name = fields.StringField()


class Book(Document):
    name = fields.StringField()
    author = fields.ReferenceField(Author, dbref=True)


class ToolInput(EmbeddedDocument):
    id = fields.StringField(required=True)
    type = fields.ListField(fields.DynamicField(null=True))
    label = fields.StringField(required=True, null=True)
    description = fields.StringField(required=False, null=True)
    default = fields.DynamicField(required=False)
    inputBinding = fields.DynamicField(required=True)
    required = fields.BooleanField(required=False, default=True)


class ToolOutput(EmbeddedDocument):
    id = fields.StringField(required=True)
    type = fields.ListField(fields.DynamicField(null=True))
    label = fields.StringField(required=False)
    default = fields.DynamicField(required=False, null=True)
    description = fields.StringField(required=False)
    outputBinding = fields.DynamicField(required=False)
    required = fields.BooleanField(required=False, default=True)


class Tool(Document):
    id = fields.StringField(required=True, primary_key=True)
    # 'class' is a reserved word in python, so to get a field called "class", we use the following trick with vars():
    vars()['class'] = fields.StringField(verbose_name="class", required=True)
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    owner = fields.ListField(fields.StringField())
    contributor = fields.ListField(fields.StringField())
    inputs = fields.EmbeddedDocumentListField(ToolInput)
    outputs = fields.EmbeddedDocumentListField(ToolOutput)
    baseCommand = fields.DynamicField(required=True)
    arguments = fields.DynamicField(required=True)
    requirements = fields.DynamicField(required=True, null=True)
    hints = fields.DynamicField(required=False, null=True)
    cwlVersion = fields.StringField(required=False, null=True, choices=['cwl:draft-2'])
    stdin = fields.StringField(required=False, null=True)
    stdout = fields.StringField(required=False, null=True)
    successCodes = fields.ListField(fields.IntField(), required=False)
    temporaryFailCodes = fields.ListField(fields.IntField(), required=False)
    permanentFailCodes = fields.ListField(fields.IntField(), required=False)


class TalkMongo (Document):
    topic = fields.StringField(required=False)
    speaker = fields.StringField(required=False)
    scheduled_at = fields.StringField(required=False)


class BairroMongo(Document):
    # codigo = fields.StringField(required=False, primary_key=True)
    codigo = fields.StringField(required=False, null=True)
    nome = fields.StringField(required=False, null=True)
    municipio = fields.StringField(required=False, null=True)
    uf = fields.StringField(required=False, null=True)
    area = fields.StringField(required=False, null=True)


class ConcorrenteMongo(Document):
    codigo = fields.StringField(required=True, primary_key=True)
    nome = fields.StringField(required=False)
    categoria = fields.StringField(required=False)
    faixa_preco = fields.StringField(required=False)
    endereco = fields.StringField(required=False)
    municipio = fields.StringField(required=False)
    uf = fields.StringField(required=False)
    codigo_bairro = fields.StringField(required=False)
