# forms.py
from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from apis.models import Assessment
from.models import PanelUser,Assessments,Banner
from apis.models import Users,ItemsCategory,ItemsSubCategories,Domains,UserType,Products
from django.utils.html import format_html

class DynamicAssessmentForm(forms.ModelForm):
	class Meta:
		model = Assessment
		fields = ['data']




class LoginForm(forms.ModelForm):
	class Meta:
		model = PanelUser
		fields = ['email', 'password','user_type']






class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['id','name', 'email', 'phone', 'password', 'user_type', 'address', 'company_name', 'company_size', 'manufacturer_category', 'adhaar_number', 'is_approved']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)




class AssessmentForm(forms.ModelForm):
    file_field = forms.FileField(label='Upload File', required=False)

    class Meta:
        model = Assessments
        exclude = ('is_approved','updated_by')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = field.label.title()
            field.widget.attrs['placeholder'] = ('Enter '+ field.label).title()
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'
            if field.required:
                field.label = format_html('<span style="color:red">* </span> {}', field.label)





class ItemsCategoryForm(forms.ModelForm):
	class Meta:
		model = ItemsCategory
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)



class ItemsSubCategoriesForm(forms.ModelForm):

	category_id = forms.ChoiceField(choices=[])
	class Meta:
		model = ItemsSubCategories
		fields = "__all__"

	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Fetch choices for the category_id field
		self.fields['category_id'].choices = [(i.id, i.category) for i in ItemsCategory.objects.all()]





class MyprofleForm(forms.ModelForm):
	class Meta:
		model = PanelUser
		exclude = ('is_staff',)



	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)



class DomainsForm(forms.ModelForm):
	class Meta:
		model = Domains
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)



class UserTypeForm(forms.ModelForm):
	class Meta:
		model = UserType
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)



class ProductForm(forms.ModelForm):

	class Meta:
		model = Products
		exclude = ('is_approved',)
	
	   

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)


class BannerForm(forms.ModelForm):

	class Meta:
		model = Banner
		fields = "__all__"
	
	   

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			field.widget.attrs['autocomplete'] = 'off'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)


