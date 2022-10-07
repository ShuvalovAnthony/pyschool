from django import forms
from .models import Profile, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}))
    subject = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема сообщения'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'}))


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label='О себе', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    klass = forms.CharField(label='Класс', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'phone', 'klass')
