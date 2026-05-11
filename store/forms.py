from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_seller = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'is_seller', 'password1', 'password2')
# Importa tu modelo de Producto (ajusta el nombre si es 'Producto' o 'Product')
from .models import User, Product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image'] # Pon aquí los campos de tu modelo