from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Status

class UserRegistrationForm(UserCreationForm):


    CHOICES=[('Male','Male'),
         ('Female','Female')]

    gender = forms.ChoiceField(

        choices=CHOICES,
        label= ''

    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


    password2 = forms.CharField(

        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'})
    )

    email = forms.EmailField(

        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})


    )

    first_name = forms.CharField(

        label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})

    )

    last_name = forms.CharField(

        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})

    )

    class Meta:

        model = User
        fields = ['gender', 'first_name', 'last_name', 'email', 'password1', 'password2']
        exclude = ['username']



    def clean_password2(self):

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise forms.ValidationError(message)

        return password2

    def save(self, commit=True):

        instance = super(UserRegistrationForm, self).save(commit=False)

        instance.username = instance.email
        if commit:

            instance.save()
        return instance


class UserLoginForm(forms.Form):

    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class EditProfileForm(forms.ModelForm):


    profileimage = forms.ImageField(label='', widget=forms.FileInput)

    class Meta:

        model = User
        fields = ['profileimage', 'date_of_birth', 'university', 'living', 'seeking', 'likes']


class ProfilePictureForm(forms.ModelForm):

    profileimage =forms.ImageField(label='')


    class Meta:

        model = User
        fields = ['profileimage']


class StatusForm(forms.ModelForm):

    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Share a Fleek!'}))

    class Meta:

        model = Status
        fields = ['content']