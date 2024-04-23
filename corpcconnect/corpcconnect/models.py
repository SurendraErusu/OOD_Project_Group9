from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#from django.contrib.auth.models import Permission
from django.contrib.auth.management import create_permissions

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.management import create_permissions
from django.db import models

class NewUser(AbstractUser):
    """
    Here are some of the inherited fields from AbstractUser:

    username (CharField)
    password (CharField)
    email (EmailField)
    first_name (CharField)
    last_name (CharField)
    is_staff (BooleanField)
    is_active (BooleanField)
    date_joined (DateTimeField)

    """
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    groups = models.ManyToManyField('auth.Group', related_name='corpcconnect_newusers_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='corpcconnect_newusers_permissions')
    #email = models.EmailField(unique=True)  # Add email field
    #username = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.username

    #class Meta:
        #db_table = "New_User"

    @classmethod
    def create_permissions(cls):
        # Ensure all content types are created
        create_permissions(ContentType.objects.all())

        # Manually create permissions for the NewUser model
        content_type = ContentType.objects.get_for_model(cls)
        Permission.objects.filter(content_type=content_type).delete()  # Delete existing permissions
        create_permissions([cls])

class CustomUser(NewUser):
    total_likes = models.IntegerField(default=0)
    pending_tasks = models.IntegerField(default=0)
    user_id = models.AutoField(primary_key=True, unique=True)
    #groups = models.ManyToManyField(Group, related_name='corpcconnect_users_groups')
    #user_permissions = models.ManyToManyField(Permission, related_name='corpcconnect_users_permissions')
    user_id = models.AutoField(primary_key=True, unique=True)
    def __str__(self):
        return self.username
    #class Meta:
        #db_table = "User"

class AdminUser(CustomUser):
    def read_all_new_users(self):
        """
        Method to read all data from the NewUser table.
        
        Returns:
        - QuerySet containing all NewUser instances.
        """
        #groups = models.ManyToManyField(Group, related_name='corpcconnect_admin_users_groups')
        #user_permissions = models.ManyToManyField(Permission, related_name='corpcconnect_admin_users_permissions')
        #from .models import NewUser
        return NewUser.objects.all()

    def approve_request(self, new_user_id):
        """
        Method to approve a request by adding a new CustomUser and deleting the corresponding NewUser record.
        
        Args:
        - new_user_id: The ID of the NewUser record to be approved.
        """
        #from .models import NewUser

        # Retrieve the NewUser record to be approved
        new_user = NewUser.objects.get(pk=new_user_id)

        # Create a new CustomUser instance using the data from the NewUser record
        custom_user = CustomUser.objects.create(
            username=new_user.username,
            email=new_user.email,
            company=new_user.company,
            position=new_user.position,
            # Add any additional fields as needed
        )

        # Optionally, perform any additional operations on the custom_user instance

        # Delete the corresponding NewUser record
        new_user.delete()

class Post(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.owner.username} at {self.created_at}"



