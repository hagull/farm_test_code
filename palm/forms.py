from django import forms
from .models import Record, VegiType, Emergency, Operating

class VegiTypeForm(forms.ModelForm):
    class Meta:
        model = VegiType
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['vegi_type']
        # fields = '__all__'
        # 일단 온도 등에 관한 정보는 자동으로 입력될 정보로 표현됨
        # 즉 일단 온도등에 관한 정보는 숨겨둔다 그리고 위 주석과 같이 처리
class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = '__all__'
class OperatingForm(forms.ModelForm):
    class Meta:
        model = Operating
        fields = '__all__'
