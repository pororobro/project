from common.models import DataTransferObject
from django .db import models

class CrimeVO(models.Model): #entity
    police = models.TextField() #어트리뷰트
    crime = models.TextField()
    create_at = models.DateField()

class CrimeDTO(DataTransferObject):#object
    police = '' #프로퍼티
    crime = ''
    create_at = ''

