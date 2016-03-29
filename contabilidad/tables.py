import django_tables2 as tables
from .models import Transacciones


class PersonTable(tables.Table):
    class Meta:
        model = Transacciones
        # add class="paleblue" to <table> tag
        attrs = {"class": "table table-bordered"}
