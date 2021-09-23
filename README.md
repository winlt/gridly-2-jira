# Jira demo

This is a demo script to simulate the connection of Gridly and Jira via Lambda function of the Gridly's Trigger. User can create a Jira/Asana/Trello/Timecamp ticket using LQA ticket of Gridly. 

## Configuration

Before using the script via the Gridly's Trigger, you need to set up Jira credentials in configs.py. Credentials include the following items:

### Jira
- username: Enter your username in Jira. For common cases, email is the username.
- apiKey: Enter your API key that is created for your account. If you don't know about the API key, please follow [this documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).
- domain: Enter your Jira domain.
- projectKey: Enter your Jira project key.

## Installation
Run below command to install package dependencies if you do not have package dependencies:
```
pip install -t . -r requirements.txt --no-user
```

After that, you need to wrap this script into a .zip file without the parent directory. Then upload to Gridly's Trigger.
In Gridly's Trigger, please following these steps:
1. Create a new trigger.
2. Select the condition is Ticket created.
3. Select Invoke Lambda function section.
4. Create new function with the .zip file.
5. Enter the payload with this format: 
```
{
    "data": "${rawData}",
    "view": "${view.name}",
    "grid": "${grid.name}",
    "user": "${user.email}"
}
```
6. Save the trigger configuration.

## Usage

To create a Jira ticket via the Gridly's LQA ticket, please following these steps:
1. Right click on any cell.
2. Select Add ticket.
3. Fill the information.
4. Click on Add button.
5. Check the Jira board.
