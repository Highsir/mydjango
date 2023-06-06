from django.contrib.auth.forms import UserCreationForm

from user.models import MyUser


class MyUserCreationnForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields
        fields += ('email', 'mobile', 'weChat', 'qq')
