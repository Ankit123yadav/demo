from django.db import models

class Registration(models.Model):
    # Personal Details
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    guardian_number = models.CharField(max_length=20)
    email = models.EmailField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = models.DateField()
    address = models.CharField(max_length=255)

    # Educational Details
    qualification = models.CharField(max_length=20, choices=[
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('Diploma', 'Diploma'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('Other', 'Other'),
    ])
    branch = models.CharField(max_length=50, choices=[
        ('Computer Science', 'Computer Science'),
        ('Electrical', 'Electrical'),
        ('Mechanical', 'Mechanical'),
        ('Civil', 'Civil'),
        ('Information Technology', 'Information Technology'),
        ('Electronics', 'Electronics'),
        ('Other', 'Other'),
    ])
    year = models.CharField(max_length=20, choices=[
        ('1 Year', '1 Year'),
        ('2 Year', '2 Year'),
        ('3 Year', '3 Year'),
        ('4 Year', '4 Year'),
    ])
    semester = models.CharField(max_length=10, choices=[
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
        ('5th', '5th'),
        ('6th', '6th'),
        ('7th', '7th'),
        ('8th', '8th'),
    ])
    college_name = models.CharField(max_length=200)
    percentage_or_cgpa = models.CharField(max_length=10, blank=True, null=True)

    # Course Details
    course_name = models.CharField(max_length=100, choices=[
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science'),
        ('Python Programming', 'Python Programming'),
        ('JavaScript', 'JavaScript'),
        ('React Native', 'React Native'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Other', 'Other'),
    ])
    duration = models.CharField(max_length=20, choices=[
        ('1 Month', '1 Month'),
        ('2 Months', '2 Months'),
        ('3 Months', '3 Months'),
        ('45 Days', '45 Days'),
        ('6 Months', '6 Months'),
        ('JOT', 'JOT'),
    ])
    mode = models.CharField(max_length=20, choices=[
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Hybrid', 'Hybrid'),
    ])
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name





class Contactus(models.Model):
    name= models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    



#Workshop Registration



