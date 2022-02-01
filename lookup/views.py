from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=A8689474-6ADD-4CEA-B615-BDB296C1CCC6")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory."
            category_color = "good"
            
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is not too bad."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Unsafe for sensity groups."
            category_color = "usg"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Air quality is not good."
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Air quality is detrimental to health."
            category_color = "veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Get out NOW."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description,
            'category_color': category_color
        })

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=A8689474-6ADD-4CEA-B615-BDB296C1CCC6")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory."
            category_color = "good"
            
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is not too bad."
            category_color = "moderate"

        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Unsafe for sensity groups."
            category_color = "usg"

        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Air quality is not good."
            category_color = "unhealthy"

        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Air quality is detrimental to health."
            category_color = "veryunhealthy"

        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Get out NOW."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api, 
            'category_description': category_description,
            'category_color': category_color
        })

def about(request):
    return render(request, 'about', {})
