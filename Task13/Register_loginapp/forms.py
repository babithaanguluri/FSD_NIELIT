from django import forms


class RegisterForm(forms.Form):

    firstname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter first name',
            'class': 'form-control'
        })
    )

    lastname = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter last name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )

    confirmpassword = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'form-control'
        })
    )


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'form-control'
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control'
        })
    )