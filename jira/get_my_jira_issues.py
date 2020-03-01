# script returns all issue that are not closed and assigned to user
# TODO update jira_url, jira_username and jira_password

from jira import JIRA

# if usename is not passed it uses ~/.netrc file for username and password. hostname in netrc should match the hostname in url
# see https://ec.haxx.se/usingcurl/usingcurl-netrc
def connect_jira_server(server_url, username=None, password=None):
    options = {'server': server_url}
    if username is None:
        return JIRA(options)
    else:
        return JIRA(options, auth=(username, password))

def get_issue_having_string(text):
    return jira.search_issues('text ~ \"' + text + '\"', 0, 50)

def get_issues_assigned_to(username):
    return jira.search_issues("assignee = " + username)


def get_issues_assigned_to_me():
    return jira.search_issues("assignee = currentUser()")


jira_url = "http://change_me:8080/"
jira_username="username"
jira_userpass="password"
jira = connect_jira_server(jira_url,jira_username,jira_userpass)

print("Connected to JIRA")

issues = get_issues_assigned_to_me()

print("Issue that are not closed yet")
for issue in issues:
    status = issue.fields.status.__str__()
    if status == 'In Progress' or status == 'Blocked' or status == "Open" or status == 'Resolved':
        print(issue.key + " is " + issue.fields.status.__str__())
