from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.backends import BaseBackend
from apis.models import Users

class PanelUserAuthBackend(BaseBackend):
	def authenticate(self, request, email=None, password=None, **kwargs):
		try:
			user = PanelUser.objects.get(email=email)
			if user.check_password(password):
				return user
			else:
				return None
		except ObjectDoesNotExist:
			return None
	def get_user(self, user_id):
		try:
			return PanelUser.objects.get(pk=user_id)
		except ObjectDoesNotExist:
			return None
		
class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(email=self.normalize_email(email), **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_fields):
		user = self.create_user(email, password, **extra_fields)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

	def get_or_none(self, **kwargs):
		try:
			return self.get(**kwargs)
		except ObjectDoesNotExist:
			return None

class PanelUser(AbstractBaseUser):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone= models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	user_type = models.CharField( blank=True, max_length=20 ,choices=[('Admin', 'Admin'), ('Execution', 'Execution'), ('Service_support', 'Service support'), ('Freelancers', 'Freelancers') ,('referral', 'referral')])
	is_staff = models.BooleanField(default=False)

	objects = CustomUserManager()
	USERNAME_FIELD = 'email'

	def has_perm(self, perm, obj=None):
		return self.is_staff

	def has_module_perms(self, app_label):
		return self.is_staff
	
class Assessments(models.Model):
	id = models.AutoField(primary_key=True)
	supplier_address = models.CharField(max_length=100, blank=True, null=True)
	supplier_location = models.CharField(max_length=100, blank=True, null=True)
	items = models.CharField(max_length=100,blank=True, null=True)
	item_type = models.CharField(max_length=100,blank=True, null=True)
	item_size = models.CharField(max_length=100,blank=True, null=True)
	item_process = models.CharField(max_length=100,blank=True, null=True)
	assessed_mode = models.CharField(max_length=1000,blank=True, null=True)
	assessed_by = models.CharField(max_length=100,blank=True, null=True)
	assessment_date = models.DateField(blank=True, null=True)
	assessment_for = models.CharField(max_length=100, choices=[('Scrap', 'Scrap'), ('Raw material', 'Raw material'), ('Services', 'Services')],blank=True, null=True)
	previous_assessment_date = models.DateField(blank=True, null=True)
	organization_structure_details = models.FileField(blank=True, null=True)
	satuatory_documents_details = models.FileField(blank=True, null=True)
	work_resistration = models.FileField(blank=True, null=True)
	work_address_ownership_lease_document = models.FileField(blank=True, null=True)
	quality_managment_system = models.FileField(blank=True, null=True)
	design_capability = models.FileField(blank=True, null=True)
	manufacturing_facility = models.FileField(blank=True, null=True)
	testing_facility = models.FileField(blank=True, null=True)
	processing_capability = models.FileField(blank=True, null=True)
	supply_experience = models.FileField(blank=True, null=True)
	safety_aspect = models.FileField(blank=True, null=True)
	rating = models.IntegerField(blank=True, null=True) # TODO: 1 to 5 add this in form
	established_year = models.DateField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(Users, on_delete=models.CASCADE,blank=True, null=True,related_name='created_by')
	updated_by = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True,related_name='updated_by')
