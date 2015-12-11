from django import forms

class UploadFileForm(forms.Form):
    # we do not use a ModelForm based on Dataset, since what is uploaded may
    # need to be modified before saving it as a dataset
    description = forms.CharField(max_length=300, label='Describe the dataset content', \
                                  help_text='blabla max: 300 char')
    file = forms.FileField(max_length=100, label='Select a dataset file',
                                   help_text='Read uploading instructions...')