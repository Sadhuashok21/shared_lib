from django.db import models
from shared_lib.sfs_core.models import AllUsers

class Companies(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    description = models.TextField()
    company_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_companies"


class Internship(models.Model):

    name = models.CharField(max_length=255)
    internship_id = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(
        Companies,
        db_column = "company_id",
        on_delete = models.CASCADE,
        to_field='company_id',
        related_name="internship_company",
    )
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_internship"

class Courses(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField()
    type = models.CharField(max_length=30, default="beginner")
    is_paid = models.BooleanField(default=0)
    price = models.FloatField(default=0)
    course_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        AllUsers,
        db_column="user_id",
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="courses_user_id"
    )
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_courses"


class Videos(models.Model):
    title = models.CharField(max_length=105)
    description = models.TextField()
    video = models.CharField(max_length=55)
    image = models.CharField(max_length=50, default="image.webp")
    course = models.ForeignKey(
        Courses,
        db_column="course_id",
        to_field="course_id",
        on_delete=models.CASCADE,
        related_name="courses_video_id"
    )
    user = models.ForeignKey(
        AllUsers,
        db_column="user_id",
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="courses_videos_user_id"
    )
    video_id =  models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_course_videos"

class Ratings(models.Model):
    rating = models.IntegerField(default=0)
    rating_id = models.CharField(max_length=50)
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        db_column = "course_id",
        to_field="course_id",
        related_name="course_ratings",
    )
    user = models.ForeignKey(
        AllUsers,
        on_delete=models.CASCADE,
        to_field="user_id",
        db_column="user_id",
        related_name="ratings_user"
    )
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_ratings"
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    language_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        AllUsers,
        db_column="user_id",
        to_field="user_id",
        on_delete=models.CASCADE,
        related_name="language_user",
    )   
    status = models.CharField(max_length=12, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = "languages"
        managed = True
    


class CourseCategories(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(
        Courses,
        db_column = "course_id",
        on_delete = models.CASCADE,
        to_field='course_id',
        related_name="course_categories_course",

    )
    user = models.ForeignKey(
        AllUsers,
        on_delete = models.CASCADE,
        to_field='user_id',
        db_column="user_id",
        related_name="course_categories_user",
    )
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "course_categories"
        managed = True


class Resumes(models.Model):

    name = models.CharField(max_length=255)
    resume_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='user_id',
        related_name="resumes_user",

    )
    status = models.CharField(max_length=20, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        managed = True
        db_table = "st_resumes"


class Skills(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='user_id',
        related_name="skills_user",

    )
    skill_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "st_skills"

class Education(models.Model):
    name = models.CharField(max_length=255)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    percentage = models.FloatField()
    course_name = models.TextField()
    college_name = models.TextField()
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        on_delete = models.CASCADE,
        to_field='user_id',
        related_name="education_user",

    )
    education_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = "st_education"



class Code(models.Model):
    user = models.ForeignKey(
        AllUsers,
        db_column = "user_id",
        to_field = "user_id",
        on_delete = models.CASCADE,
        related_name = "code_user"
    )
    code = models.TextField()
    code_id = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = "st_code"