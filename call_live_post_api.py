
import requests

# The API endpoint
url = "https://hfmiwfnuzmsjlyfpyxgwpztdgu0pbklb.lambda-url.us-east-1.on.aws/"
print(url)
# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)


# Define new data to create
new_data = {
"age": 37,
"workclass": "Private",
"fnlwgt": 280464,
"education": "Some-college",
"education-num": 10,
"marital-status": "Married-civ-spouse",
"occupation": "Exec-managerial",
"relationship": "Husband",
"race": "Black",
"sex": "Male",
"capital-gain": 0,
"capital-loss": 0,
"hours-per-week": 80,
"native-country": "United-States"
}

predict_url = url+"/predict"
# A POST request to the API
post_response = requests.post(predict_url, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)
