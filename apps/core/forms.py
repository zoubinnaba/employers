from django.forms import ModelForm

from .models import Employer

class EmployerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployerForm, self).__init__(*args, **kwargs)

        self.fields['nom'].widget.attrs['class']= 'input mb-4'
        self.fields['prenom'].widget.attrs['class']= 'input mb-4'
        self.fields['numero_de_telephone'].widget.attrs['class']= 'input mb-4'
        self.fields['biographie'].widget.attrs['class']= 'textarea mb-4'
    class Meta:
        model = Employer
        fields = '__all__'