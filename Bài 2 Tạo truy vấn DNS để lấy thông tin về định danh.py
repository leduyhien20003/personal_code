import dns.resolver 
def dns_search():
    host = input()
    ip = dns.resolver.resolve(host)
    for i in ip:
      print(i)
     

if __name__ == "__main__":
    dns_search()            