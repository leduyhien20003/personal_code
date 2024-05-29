import requests
logins = []
with open('C:\\Users\\leduy\\OneDrive\\Documents\\LêDuyHiển_AT180316_TH2\\Logins.txt', 'r') as filehandle:
    for line in filehandle:
        login = line[:-1]
        logins.append(login)
domain = "http://testphp.vulnweb.com"
for login in logins:
    #print("Cheking..."+ domain + login)
    response = requests.get(domain + login)
    if response.status_code == 200:
        print("Login resource detected: " + login)        