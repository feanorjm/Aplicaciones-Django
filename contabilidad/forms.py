from django import forms

from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo_transaccion','consumidor', 'monto', 'nombre_entrada', 'fecha', 'descripcion']
        widgets = {
            'tipo_transaccion': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'consumidor': forms.Select(attrs={'class': 'form-control col-md-7 col-xs-12"'}),
            'monto': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'pattern': '[0-9]*'}),
            #'nombre_entrada': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'id': 'birthday', 'class': 'date-picker form-control col-md-7 col-xs-12"'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control col-md-7 col-xs-12"', 'style': 'height: 90px;'}),

        }


