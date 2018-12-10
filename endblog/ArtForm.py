
from django import forms


class AddArtForm(forms.Form):
    # required=True表示必填项
    # min_length表示最小长度
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '文章简短描述必填',
                                'min_length': '文章描述不能少于5个字符'
                            })
    desc = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章简短描述必填',
                                'min_length': '文章描述不能少于5个字符'
                            })
    content = forms.CharField(required=True,
                            error_messages={
                                'required': '文章简短描述必填'
                            })
    icon = forms.ImageField(required=True,error_messages={
        'required': '首图必填'
    })


class EditArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True,
                            error_messages={
                                'required': '文章简短描述必填',
                                'min_length': '文章描述不能少于5个字符'
                            })
    desc = forms.CharField(min_length=5, required=True,
                           error_messages={
                               'required': '文章简短描述必填',
                               'min_length': '文章描述不能少于5个字符'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章简短描述必填'
                              })
    icon = forms.ImageField(required=True, error_messages={
        'required': '首图必填'
    })