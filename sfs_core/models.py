from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class AllUsers(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    profile = models.CharField(max_length=500, default="profile.webp")
    user_type = models.CharField(max_length=5, default="user")
    platform = models.CharField(max_length=10)
    platform_name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    user_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default="approved")
    ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'all_users'



class BpCat(models.Model):
    bp_category = models.CharField(max_length=20)
    bp_name = models.CharField(max_length=35)
    bp_img = models.CharField(max_length=40)
    bp_para = models.TextField()
    category_id = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field = "user_id",
        related_name = "bp_cat_user",
    )
    status = models.CharField(max_length=11)
    ip = models.CharField(max_length=50)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_bp_cat'



class BP(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    fviews = models.IntegerField(default=0)
    flikes = models.IntegerField(default=0)
    fdownloads = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    fshare = models.IntegerField(default=0)
    zipfiles = models.CharField(max_length=50)
    sfs_link = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    bp_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=12)
    ip = models.CharField(max_length=50)
    feature = models.BooleanField(default=0)
    description = models.TextField()
    time = models.DateTimeField()
    user = models.ForeignKey(
        AllUsers, 
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='user_id',
        related_name="bp_user",
    )

    class Meta:
        managed = True
        db_table = 'sfs_bp'


class BPCategories(models.Model):
    category = models.ForeignKey(
        BpCat,
        db_column = "category_id",
        to_field = "category_id",
        on_delete = models.CASCADE,
        related_name = "bp_categories",
    )
    bp = models.ForeignKey(
        BP,
        db_column = "bp_id",
        to_field = "bp_id",
        on_delete = models.CASCADE,
        related_name = "bp_category_bp",
    )
    status = models.CharField(max_length=11)
    ip = models.CharField(max_length=50)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_bp_categories'



class Favorites(models.Model):
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='user_id',
        related_name="bp_favorites_user",

    )
    bp = models.ForeignKey(
        BP,
        db_column = "bp_id",
        on_delete = models.CASCADE,
        to_field='bp_id',
        related_name="bp_favorites_bp",
    )
    
    status = models.CharField(max_length=12)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_favorites'

class BPImages(models.Model):
    image = models.CharField(max_length=70)
    bp = models.ForeignKey(
        BP,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='bp_id',
        related_name="bp_user_image",
    )
    status = models.CharField(max_length=12)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_images'




class BpDlv(models.Model):
    ip = models.CharField(max_length=50)
    bp_pla_id = models.CharField(max_length=35)
    download_type = models.CharField(max_length=10)
    user_id = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    dlv_id = models.CharField(max_length=50, unique=True)
    platform = models.CharField(max_length=10)
    platform_name = models.CharField(max_length=50)
    version = models.CharField(max_length=15)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_bp_dlv'


class Comments(models.Model):
    ip = models.CharField(max_length=50)
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field = "user_id",
        related_name = "comments_user",
    )
    bp = models.ForeignKey(
        BP,
        db_column = "bp_id",
        on_delete = models.CASCADE,
        to_field = "bp_id",
        related_name = "comments_bp",
    )
    comment = models.TextField()
    status = models.CharField(max_length=15)
    time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'sfs_comments'



