from django.shortcuts import render
import requests
# Create your views here.
def index(request):
	r = requests.get('http://128.2.7.38:7000/api/v1/clusters/legend/services/HDFS/components/DATANODE', 
		auth=('admin','ravi666!'))
	context = {}
	if r.status_code == 200:
		context = {'ServiceComponentInfo': r.json()['ServiceComponentInfo']}
	return render(request, 'dashboard/index.html', context)
