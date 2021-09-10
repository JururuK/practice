from .base import *

# environ 이용하는 방법
env_list = dict()
local_env = open(os.path.join(BASE_DIR, '.env'))
while True :
    line = local_env.readline() #파일의 끝에 도달했을 떄 조건문을 빠져나가라
    if not line :
        break
    line = line.replace('\n','')
    start = line.find('=')
    key = line[:start]
    value = line[start+1:]
    env_list[key] = value

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"] #모든 ip를 접속하게 하겠다


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gj_ai_django',
        'USER': 'gj_ai_django',
        'PASSWORD': 'mypassword1234',
        'HOST': 'gj_ai_mariadb',
        'PORT': '3306',
    }
}