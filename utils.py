import apis 
import configs

def createJiraTicket(data):
    ticketSummary = data.get("data").get("summary", "")
    ticketDescription = data.get("data").get("description", "")
    ticketType = data.get("data").get("type", "")
    prior = data.get("data").get("priority", "")
    gridName = data.get("grid", "")
    viewName = data.get("view", "")
    columnId = data.get("data").get("columnId", "")
    recordId = data.get("data").get("recordId", "")
    createdDate = data.get("data").get("audit", {}).get("createdTime", "")

    payload = {
            "fields": {
                "project":
                {
                    "key": configs.jiraProjectKey
                },
                "summary": ticketSummary,
                "description": ticketDescription + "\n" + "\n" + "*Gridly data*" + """
                    |Ticket type|{ticketType}|
                    |Priority|{prior}|
                    |Grid name|{gridName}|
                    |View name|{viewName}|
                    |Column ID|{columnId}|
                    |Record ID|{recordId}|
                    |Created date|{createdDate}|
                """.format(ticketType=ticketType, prior=prior, gridName=gridName, viewName=viewName, columnId=columnId, recordId=recordId, createdDate=createdDate),
                "issuetype": {
                    "name": "Bug"
                }
            }
        }

    createTicket = apis.createTicket(payload)