from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={

            }
        ),
        help_text='Ajuda texto',
    )
    class Meta:
        model = Contact
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'email',
                  'description',
                  'category')
        widgets = {
            'first_name': forms.TextInput(
                    attrs={
                    'placeholder':'Escreva aqui',
                }
            )
        }
    def clean(self):
        self.add_error(
            'first_name',
            ValidationError(
            'Mensagem de erro',
            code='invalid'
            )
        )
        return super().clean()
    
    def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')

            if first_name == 'ABC':
                self.add_error(
                    'first_name',
                    ValidationError(
                        'Veio do add_error',
                        code='invalid'
                    )
                )

            return first_name
    