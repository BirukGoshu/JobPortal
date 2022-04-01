from django.db import models

Gender_Male = 'male'
Gender_Female = 'female'
Gender_Choice = (
    (Gender_Male, 'male'),
    (Gender_Female, 'female')
)

Status_Accepted = 'accepted'
Status_Pending = 'pending'
Status_Rejected = 'rejected'
Status_Choice = (
    (Status_Accepted, 'accepted'),
    (Status_Pending, 'pending'),
    (Status_Rejected, 'rejected')
)

class Candidate(models.Model):
    """
    -name 
    -age
    -gender
    -mobile
    -city
    -salary expectation
    -are they willing to relocate
    """
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=Gender_Choice, default=Gender_Male)
    mobile = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    expected_salary = models.IntegerField()
    relocation = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class CandidateJobMapping(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=Status_Choice, default=Status_Pending)
    feedback = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.candidate.name, self.job.position_name)