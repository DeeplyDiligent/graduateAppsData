import urllib3
import requests
import json

def gradConnectRead():
    gradConnectMain = "https://au.gradconnection.com/api/campaigngroups/?job_type=graduate-jobs&disciplines=computer-science&location=melbourne%2CAU&offset=0&limit=100&ordering=-recent_job_created"
    gradConnectData = requests.get(gradConnectMain).text
    parseJson = json.loads(gradConnectData)
    prettyGradConnectData = json.dumps(parseJson, indent=2, sort_keys=True)

    gradConnectFile = open("./diff/gradConnect.json","w+")
    gradConnectFile.write(prettyGradConnectData)
    gradConnectFile.close

if __name__ == "__main__":
    gradConnectRead()