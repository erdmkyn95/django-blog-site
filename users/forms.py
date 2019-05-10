from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="Parola")
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label="Parola Doğrulama")
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {'event_date': forms.DateInput(attrs={'class ': 'datepicker'})}
        fields = ('bio', 'birth_date')

        widgets = {
            'birth_date': forms.DateInput(format=('%m/%d/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
        }
