from django import forms

class FormularioEditarEmpleados(forms.Form):

    salarioEmpleados = forms.CharField(
        widget= forms.NumberInput(attrs = {'class':'form-control mb-3'}),
        required=- True,
    )

contactoEmpleados = forms.CharField(
    widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
    required=True,
    max_length= 20
)