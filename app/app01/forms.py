from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'placeholder': 'What is on your mind?'
            }
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.Form):
    # 假设'content'字段用于帖子的内容
    content = forms.CharField(widget=forms.Textarea, label='内容')
    # 根据需要添加其它字段

