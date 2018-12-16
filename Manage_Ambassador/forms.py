from django import forms


class AmbassadorForm(forms.Form):
    ambassador_name = forms.CharField(max_length=40,
                                      widget=forms.TextInput(
                                          attrs={'class': "form-control",
                                                 'placeholder': "Enter Ambassador name",
                                                 'type': "text"}
                                      ))

    email = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                          attrs={'class': "form-control",
                                                 'placeholder': "Your Email ",
                                                 'type': "text"}
                                      ))

    phone = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                attrs={'class': "form-control",
                                       'placeholder': "Your phone number ",
                                       'type': "text"}
                            ))