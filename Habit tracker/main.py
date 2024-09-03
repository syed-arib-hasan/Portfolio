import requests
from datetime import datetime
user_name="syedarib"
graph_id="graph1"
TOKEN="Nish@n681"

endpoint="https://pixe.la/v1/users"
user_params={
    "token":"Nish@n681",
    "username": "syedarib", 
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response=requests.post(url=endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{endpoint}/{user_name}/graphs"

graph_config={
    "id": graph_id,
    "name":"My Coding Tracker",
    "unit":"Min",
    "type": "float",
    "color":"sora"
}

headers={
    "X-USER-TOKEN": TOKEN
}

response=requests.put(url=f"{graph_endpoint}/graph1",json=graph_config,headers=headers)
print(response.text)
today=datetime(year=2024,month=8,day=21)

post_endpoint=f"{graph_endpoint}/{graph_id}"
post_config={
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.5",
}


# response=requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)