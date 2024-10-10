import requests
		
def get_categories():
	r = requests.get('https://api.escuelajs.co/api/v1/categories')
	print(r.status_code) #Tenemos un estado
	print(r.text) #Informacion esta retornando
	print(type(r.text))
	categories = r.json()
	for category in categories:
		print(category['name'])