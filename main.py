import utils

def processor(event, context):

    createJiraTicket = utils.createJiraTicket(event)

    return {
                "status": 200, 
                "result": str(createJiraTicket)
            }