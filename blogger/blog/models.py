from django.db import models

#crud
#c-create
#R-READ
#U-UPDATE
#D-DELET

# CREATE TABLE author(name VARCHAR(100)) 
class Author(models.Model):
    GENDER_OPTIONS = [
        ("M", "MALE"),
        ("F", "FEMALE"),
    ]
    name = models.CharField(max_length=50, verbose_name="Athour Name")
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True, blank=True, default="N/A")
    gender = models.CharField(max_length=2, 
    choices=GENDER_OPTIONS)
    
class Article(models.Model):
    title = models.CharField(max_length=50)
    summery = models.TextField()
    author = models.ForeignKey("Author",  on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=False)
    is_published = models.BooleanField(default=False)