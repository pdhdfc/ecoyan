from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class BookTestRode(models.Model):
    ANDHRA_PRADESH = 'AP'
    ARUNACHAL_PRADESH = 'AR'
    ASSAM = 'AS'
    BIHAR = 'BR'
    CHHATTISGARH = 'CT'
    GOA = 'GA'
    GUJARAT = 'GJ'
    HARYANA = 'HR'
    HIMACHAL_PRADESH = 'HP'
    JHARKHAND = 'JH'
    KARNATAKA = 'KA'
    KERALA = 'KL'
    MAHARASHTRA = 'MH'
    MADHYA_PRADESH = 'MP'
    MANIPUR = 'MN'
    MEGHALAYA = 'ML'
    MIZORAM = 'MZ'
    NAGALAND = 'NL'
    ODISHA = 'OR'
    PUNJAB = 'PB'
    RAJASTHAN = 'RJ'
    SIKKIM = 'SK'
    TAMIL_NADU = 'TN'
    TRIPURA = 'TR'
    TELANGANA = 'TG'
    UTTAR_PRADESH = 'UP'
    UTTARAKHAND = 'UT'
    WEST_BENGAL = 'WB'
    ANDAMAN_NICOBAR = 'AN'
    CHANDIGARH = 'CH'
    DADRA_NAGAR_HAVELI_DAMAN_DIU = 'DN'
    DELHI = 'DL'
    JAMMU_KASHMIR = 'JK'
    LADAKH = 'LA'
    LAKSHADWEEP = 'LD'
    PUDUCHERRY = 'PY'

    STATE_CHOICES = [
        (ANDHRA_PRADESH, 'Andhra Pradesh'),
        (ARUNACHAL_PRADESH, 'Arunachal Pradesh'),
        (ASSAM, 'Assam'),
        (BIHAR, 'Bihar'),
        (CHHATTISGARH, 'Chhattisgarh'),
        (GOA, 'Goa'),
        (GUJARAT, 'Gujarat'),
        (HARYANA, 'Haryana'),
        (HIMACHAL_PRADESH, 'Himachal Pradesh'),
        (JHARKHAND, 'Jharkhand'),
        (KARNATAKA, 'Karnataka'),
        (KERALA, 'Kerala'),
        (MAHARASHTRA, 'Maharashtra'),
        (MADHYA_PRADESH, 'Madhya Pradesh'),
        (MANIPUR, 'Manipur'),
        (MEGHALAYA, 'Meghalaya'),
        (MIZORAM, 'Mizoram'),
        (NAGALAND, 'Nagaland'),
        (ODISHA, 'Odisha'),
        (PUNJAB, 'Punjab'),
        (RAJASTHAN, 'Rajasthan'),
        (SIKKIM, 'Sikkim'),
        (TAMIL_NADU, 'Tamil Nadu'),
        (TRIPURA, 'Tripura'),
        (TELANGANA, 'Telangana'),
        (UTTAR_PRADESH, 'Uttar Pradesh'),
        (UTTARAKHAND, 'Uttarakhand'),
        (WEST_BENGAL, 'West Bengal'),
        (ANDAMAN_NICOBAR, 'Andaman & Nicobar (UT)'),
        (CHANDIGARH, 'Chandigarh (UT)'),
        (DADRA_NAGAR_HAVELI_DAMAN_DIU, 'Dadra & Nagar Haveli and Daman & Diu (UT)'),
        (DELHI, 'Delhi [National Capital Territory (NCT)]'),
        (JAMMU_KASHMIR, 'Jammu & Kashmir (UT)'),
        (LADAKH, 'Ladakh (UT)'),
        (LAKSHADWEEP, 'Lakshadweep (UT)'),
        (PUDUCHERRY, 'Puducherry (UT)'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    city = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content_sort = models.CharField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    click_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace(" ", "-"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[self.slug])  # Ensure this matches the URL name



class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)  # Add this line
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)  # Add slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace(" ", "-"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_detail', args=[self.slug])




class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.job.title}'
