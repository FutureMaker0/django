# blog/forms.py

from django import forms
from .models import Post


# 일반 Form: html에 있는 form 태그
# 유효성 검사를 위해서 form을 써준다. 
# modelform:
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']
    

# ModelForm
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         field = ('title', 'writer', ) # 튜플형태라 관용적 콤마
#         weight = {
#             'content': forms.widgets.Textarea
#         }