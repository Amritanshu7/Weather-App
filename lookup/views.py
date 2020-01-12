from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		
		city = request.POST['city']
		
		api_request = requests.get("https://api.waqi.info/feed/"+city+"/?token=cfea963f782b0517441e1679d740ea5078ac72e2")
		
		try:
			api = json.loads(api_request.content.decode('utf-8'))
			if api['data']['aqi'] < 51:
				quality="Good"
				col="good" 
				aqi_range="0 - 50"
				desc="Air quality is considered satisfactory, and air pollution poses little or no risk"
			elif api['data']['aqi'] < 101:
				quality="Moderate"
				col="moderate"
				aqi_range="51 - 100"
				desc="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			elif api['data']['aqi'] < 151:	
				quality="Unhealthy for Sensitive Groups"
				col="usg"
				aqi_range="101 - 150"
				desc="Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			elif api['data']['aqi'] < 201:	
				quality="Unhealthy"
				col="unhealthy"
				aqi_range="151 - 200"
				desc="Everyone may begin to experience health effects. Members of sensitive groups may experience more serious health effects"
			elif api['data']['aqi'] < 301:
				quality="Very Unhealthy"
				col="veryunhealthy"
				aqi_range="201 - 300"
				desc="Health warnings of emergency conditions. The entire population is more likely to be affected."
			else:
				quality="Hazardous"
				col="hazardous"
				aqi_range="300+"
				desc="Health alert: everyone may experience more serious health effects"	
			


			return render(request,'home.html',{
				'api': api,
				'quality':quality,
				'col':col,
				'aqi_range':aqi_range,
				'desc':desc
				})
		except Exception as e:
		 	api = "Error"
		 	return render(request,'home.html',{
				'api': api,
				})

		
	else:
		api_request = requests.get("https://api.waqi.info/feed/guwahati/?token=cfea963f782b0517441e1679d740ea5078ac72e2")
		
		try:
			api = json.loads(api_request.content.decode('utf-8'))
			if api['data']['aqi'] < 51:
				quality="Good"
				col="good" 
				aqi_range="0 - 50"
				desc="Air quality is considered satisfactory, and air pollution poses little or no risk"
			elif api['data']['aqi'] < 101:
				quality="Moderate"
				col="moderate"
				aqi_range="51 - 100"
				desc="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			elif api['data']['aqi'] < 151:	
				quality="Unhealthy for Sensitive Groups"
				col="usg"
				aqi_range="101 - 150"
				desc="Members of sensitive groups may experience health effects. The general public is not likely to be affected."
			elif api['data']['aqi'] < 201:	
				quality="Unhealthy"
				col="unhealthy"
				aqi_range="151 - 200"
				desc="Everyone may begin to experience health effects. Members of sensitive groups may experience more serious health effects"
			elif api['data']['aqi'] < 301:
				quality="Very Unhealthy"
				col="veryunhealthy"
				aqi_range="201 - 300"
				desc="Health warnings of emergency conditions. The entire population is more likely to be affected."
			else:
				quality="Hazardous"
				col="hazardous"
				aqi_range="300+"
				desc="Health alert: everyone may experience more serious health effects"	
			


			return render(request,'home.html',{
				'api': api,
				'quality':quality,
				'col':col,
				'aqi_range':aqi_range,
				'desc':desc
				})
		except Exception as e:
		 	api = "Error"
		 	return render(request,'home.html',{
				'api': api,
				})
		
def about(request):
	return render(request,'about_me.html',{})	
