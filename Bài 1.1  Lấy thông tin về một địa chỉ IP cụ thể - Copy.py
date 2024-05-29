import shodan  #pip install shodan
import pprint  #pip install pprintpp cái này để in cho đẹp
api = shodan.Shodan('5fRPVOHjXOiDpWUZDbxzYtS8SCTqecqo')

def seacrh_via_ip():
 while(True):
  ip = input()
  if ip.lower() != 'quit':
   info = api.host(ip) #lấy toàn bộ thông tin có thể về 1 ip cụ thể
   pprint.pprint(info)
  else:
      break

if __name__ == "__main__" :
   seacrh_via_ip() 
  