from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Username"
            }
        ),
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Password"
            }
        ),
        max_length=20,
        required=True,
    )


class SignupForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "First Name"
            }
        ),
        max_length=50,
        required=True,
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Last Name"
            }
        ),
        max_length=50,
        required=True,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Email"
            }
        ),
        max_length=50,
        required=True,
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Username"
            }
        ),
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Password"
            }
        ),
        max_length=20,
        required=True,
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control mb-4",
                'placeholder': "Confirm Password"
            }
        ),
        max_length=20,
        required=True,
    )
