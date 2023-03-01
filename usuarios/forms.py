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
            attrs={"class": "form-control", "placeholder": "Digite seu nome completo. Ex: MariaSilva"}
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

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError(
                    'Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_confirmar(self):
        senha = self.cleaned_data.get('senha')
        senha_confirmar = self.cleaned_data.get('senha_confirmar')

        if senha and senha_confirmar:
            if senha != senha_confirmar:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_confirmar
            


