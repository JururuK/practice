from django.db import models

# Create your models here.
 #python manage.py makemigrations 하면 생성되는 0001_initial.py 파일은 변화를 추적해주므로 지우지 말것.
class NewModel(models.Model) : #장고에서 기본적으로 제공하는 모델
    text = models.CharField(max_length=255, null=False)
