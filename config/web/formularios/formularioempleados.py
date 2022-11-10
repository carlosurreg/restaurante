from django import forms


class formularioEmpleados(forms.Form):

    #CREANDO ATRIBUTO PARA ACRGAR EL SELECTOR
    OPCIONES=(
        (1,'Cocinero'),
        (2,'Ayudante'),
        (3,'Mesero'),
        (4,'Administrador'),
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    nombres=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5
    )

    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        max_length=20
    )

    foto=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
    )

    cargo=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )
    
    salario=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,  
    )

    contacto=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,  
    )

    