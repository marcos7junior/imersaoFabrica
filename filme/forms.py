from django.forms import ModelForm
from .models import Categoria, Titulo

class TituloForm(ModelForm):
    class Meta:
        model = Titulo
        fields = ['nome', 'classificacao', 'categoria']
