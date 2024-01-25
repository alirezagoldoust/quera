# This will provide a sample data in your database
import os
os.system('python ./manage.py makemigrations')
os.system('python ./manage.py migrate')
os.system('python ./manage.py loaddata sample_data.json')
os.system('python ./manage.py migrate')
print(' ------------------------\n  Succecfuly initialized \n ------------------------')
