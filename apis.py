import requests
import json
import configs

def createTicket(payload):
    headers = {
            'Content-Type': 'application/json'
        }

    response = requests.post(f"{configs.jiraDomain}/rest/api/2/issue/", auth=(configs.jiraUsername, configs.jiraApiKey), headers=headers, data=json.dumps(payload)).json()

    print(response)

    return {
            "ticketId": response["id"],
            "ticketKey": response["key"],
            "ticketLink": response["self"]
            }