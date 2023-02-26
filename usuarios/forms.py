from django import forms

class LoginForms(forms.Form):
    emailLogin = forms.EmailField(
        label="Email",
        required=True,
        max_length=150,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Digite seu e-mail"}
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
    nomeCadastro= forms.CharField(
        label="Nome",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite seu nome completo. Ex: Maria da Silva"}
        )
    )
    emailCadastro = forms.EmailField(
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
    senhaConfirmar = forms.CharField(
        label="Confirmar de Senha",
        required=True,
        max_length=80,
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite sua senha novamente"}
        )
    )

