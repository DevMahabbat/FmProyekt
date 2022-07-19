from django import forms






class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Username")
    password = forms.CharField(max_length=20,label="Passowrd",widget = forms.PasswordInput)
    confirm  = forms.CharField(max_length=20,label = "Password Tekrar", widget=forms.PasswordInput)

    def clean(self):
        
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        
        if password and confirm and password!=confirm:
            raise forms.ValidationError("parollar eyni deyil")

        values = {
            "username": username,
            "password" :password
        }

        return values 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,label="Username")
    password  =forms.CharField(max_length=20,label ="Password" ,widget=forms.PasswordInput)
   