import shodan
import pprint #de in cho dep

shodanKeyString = '17xz7MYEBoXLPoi8RdqbgkPwTV2T2H0y' #neu bi 403 denied nghia la key nay het han premium r
shodanApi = shodan.Shodan(shodanKeyString)
ip = []
results = shodanApi.search("port: 21 Anonymous user logged in")
for result in results['matches']:
    if result['ip_str'] != None:  #neu ip_str co ton tai them vao cuoi mang ip
        ip.append(result['ip_str'])
for ip1 in ip :
    pprint.pprint(ip1)  #in ip ra bang pprint cho dep