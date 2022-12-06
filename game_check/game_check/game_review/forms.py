from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from game_check.game_review.models import Profile, GameComment, GameScore
from game_check.game_review.validators import age_validator

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    name = forms.CharField()
    age = forms.IntegerField(
        validators=(
            age_validator,
        ),
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'name', 'age', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            name=self.cleaned_data['name'],
            age=self.cleaned_data['age'],


        )

        if commit:
            profile.save()

        return user


# TODO: Finish form and view for change password
class ChangeUserPasswordForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = ('old_password', 'new_password1', 'new_password2')


class GameCommentForm(forms.ModelForm):
    class Meta:
        model = GameComment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 5,
                    'placeholder': 'Add comment...',
                },
            ),
        }


class GameRatingForm(forms.ModelForm):
    class Meta:
        model = GameScore
        fields = ('value',)