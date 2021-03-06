from django import forms
from .models import Instrument


# class SignupForm(forms.ModelForm):  # 모델폼은 사용할 모델만 알려주면 모델의 필드에 따라서 폼을 알아서 만든다.
#     class Meta:
#         model = User  # Meta 클래스에 사용할 모델을 명시해주면 된다.
#         fields = ["nickname"]  # 추가할 필드 명시
#
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]  # 폼에 기입된 데이터는 cleaned_data로 가져온다.
#         user.save()


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = [
            "SN",
            "Name",
        ]
        widgets = {
            "Name": forms.Select,
        }
