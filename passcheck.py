'''
Name : Rohan Karmakar;   Dept.: ECE; Year : 2nd;
Roll No. : 34900319031;
'''
import requests
import hashlib
import sys

def request_api_data(querry_char):
   url = 'https://api.pwnedpasswords.com/range/'+querry_char
   res = requests.get(url)
   if res.status_code != 200:
       raise RuntimeError(f'Error Fetching: {res.status_code},Try again👍')
   return res

def leaked_pass_count(hashes,has_to_check):  
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for hs, count in hashes:
        if hs == has_to_check:
            return count
    return 0

def pwned_pass_check(password):  
    hashedPass= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = hashedPass[:5], hashedPass[5:]
    response = request_api_data(first5_char)
    return leaked_pass_count(response,tail)

def main(args):
    for password in args:
        counts = pwned_pass_check(password)
        if counts:
            print(f'{password} was found {counts} times.You must change your Password😨')
        else:
            print(f'Your Password {password} is in Good Condition✔')
    return "Checked."

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))                                  
