from django import forms

class FormularioEditarPlatos(forms.form):

    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
    )

