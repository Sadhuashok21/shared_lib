from django.db import models 

class HackathonUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, default="user")
    status = models.CharField(max_length=20, default="active")
    user_id = models.CharField(max_length=50, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'hackathon_users'
        

class HackathonTeams(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="active")
    type = models.CharField(max_length=20, default="member")
    team_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'hackathon_teams'


class HackathonProjects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'hackathon_projects'




class Payment(models.Model):
    razorpay_order_id = models.CharField(max_length=100, unique=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=50, default='Created')  # Created, Success, Failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.razorpay_order_id} - {self.status}"



class HackathonPayments(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    payment = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'hackathon_payments'


from django.db import models