from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu nome de Login"}
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite sua senha"}
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro= forms.CharField(
        label="Nome",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu nome completo. Ex: Maria da Silva"}
        )
    )
    email_cadastro = forms.EmailField(
        label="Email",
        required=True,
        max_length=150,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Digite seu e-mail. Ex: maria@mail.com"}
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite sua senha"}
        )
    )
    senha_confirmar = forms.CharField(
        label="Confirmar de Senha",
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite sua senha novamente"}
        )
    )

