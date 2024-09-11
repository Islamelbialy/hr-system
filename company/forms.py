from django import forms
from .models import departments 


class newDepartmentToBrancheForm(forms.ModelForm):

    class Meta:
        model = departments
        fields = ['name','description']

    def clean(self):
        cleaned_data = self.cleaned_data

        try:
            departments.objects.get(name=cleaned_data['name'], branch_id=self.branch_id)
        except departments.DoesNotExist:
            pass
        else:
            raise ValidationError('Deprtment name is already exists in this branch')

        # Always return cleaned_data
        return cleaned_data
