from django import forms
from django.core.exceptions import ValidationError
from user.models import PersonInfo
from user.models import MyUser


class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = MyUser
        # model = PersonInfo
        fields = '__all__'


def payment_validate(value):
    if value > 30000:
        raise ValidationError('请输入合理的薪资')


class VocationForm(forms.Form):

    job = forms.CharField(max_length=20, label='职位')
    title = forms.CharField(max_length=20, label='职称',
                            widget=forms.widgets.TextInput(attrs={"class": "c1"}),
                            error_messages={"required": "职称不能为空"})
    payment = forms.IntegerField(label='薪资', validators=[payment_validate])

    value = PersonInfo.objects.values('name')
    choices = [(i+1, v['name']) for i , v in enumerate(value)]
    persion = forms.ChoiceField(choices=choices, label='姓名')

    def clean_title(self):
        data = self.cleaned_data['title']
        return '初级' + data




