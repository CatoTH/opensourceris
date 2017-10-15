from django_elasticsearch_dsl import DocType, fields

from mainapp.models import Committee
from .utils import autocomplete_analyzer, fileIndex


@fileIndex.doc_type
class CommitteeDocument(DocType):
    autocomplete = fields.StringField(attr="name_autocomplete", analyzer=autocomplete_analyzer)

    body = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.StringField(),
    })

    class Meta:
        model = Committee

        fields = [
            'id',
            'name',
            'short_name',
        ]
