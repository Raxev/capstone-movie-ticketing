from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    num_child = forms.IntegerField(initial=0, min_value=0, max_value=500)
    num_adult = forms.IntegerField(initial=0, min_value=0, max_value=500)
    num_senior = forms.IntegerField(initial=0, min_value=0, max_value=500)
    num_student  = forms.IntegerField(initial=0, min_value=0, max_value=500)
    num_matinee = forms.IntegerField(initial=0, min_value=0, max_value=500)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['num_child'].label = "Child tickets ($5.00)"
        self.fields['num_adult'].label = "Adult tickets ($10.00)"
        self.fields['num_senior'].label = "Senior tickets ($5.50)"
        self.fields['num_student'].label = "Student tickets ($8.00)"
        self.fields['num_matinee'].label = "Matinee tickets ($4.50)"
   
    
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        num_child =  cleaned_data.get( 'num_child')
        num_adult =  cleaned_data.get( 'num_adult')
        num_senior = cleaned_data.get( 'num_senior')
        num_student  = cleaned_data.get('num_student')  
        num_matinee = cleaned_data.get( 'num_matinee' )
        if not name and not email:
            raise forms.ValidationError('Invalid data!')
            
    def total(self):
        num_child =0
        num_adult=0 
        num_senior=0
        num_student=0
        num_matinee=0
        cleaned_data = super(ContactForm, self).clean()
        num_child =  cleaned_data.get('num_child')
        num_adult =  cleaned_data.get('num_adult')
        num_senior = cleaned_data.get('num_senior')
        num_student  = cleaned_data.get('num_student')  
        num_matinee = cleaned_data.get('num_matinee')
    
        total = (num_child * 5.00) + (num_adult * 10.00) + (num_senior * 5.50) + (num_student * 8.00) + (num_matinee * 4.50)
        
        return total