import requests

baseURL = "http://127.0.0.1:5000/"

commonGetRequestsFile = open('commonGetRequests.txt', 'r')
allCommonGetRequests = commonGetRequestsFile.readlines()

for currGetRequest in allCommonGetRequests:
    testedGetRequest = baseURL + currGetRequest.strip()
    request = requests.get(testedGetRequest)
    if request.status_code == 404:
        print "         [-] 404 " + testedGetRequest
    elif request.status_code == 405:
        print "      [-] 405 " + testedGetRequest
    elif request.status_code == 200:
        print "[+] 200 " + testedGetRequest
    else:
        print request.status_code
