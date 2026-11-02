from django import forms
from .models import LugarPatrimonial

class LugarPatrimonialForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre','descripcion','ubicacion','anio_construccion','imagen','categoria']