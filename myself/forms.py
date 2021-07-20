from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm) :
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #상속받은 값을 그대로 사용

        self.fields['username'].disabled = True