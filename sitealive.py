from colorama import Back,Fore,init,Style
import requests as r
import argparse


def res_headers(headers,show_all=False):
    ih=["Server","Content-Type","Content-Length","X-Powered-By"]
    print(Fore.YELLOW + "[INFO] RESPONSE HEADERS")
    print(Fore.BLUE + ("******* Showing all headers *******"
        if show_all else "******* Showing only important headers *******"))
    for k,v in headers.items():
            if show_all or k in ih:
                            print(Fore.CYAN+f"{k}:"+Fore.WHITE+Style.BRIGHT+f"{v}")


parser=argparse.ArgumentParser(description=Fore.YELLOW+"SiteAlive - A tool to check if a website is alive.",
epilog=Fore.YELLOW+"""
Example:
    python sitealive.py --url example.com
    python sitealive.py --url http://example.com
Note:
    You can skip http since it includes one by default.

                     -Developed by Santhosh 
""",formatter_class=argparse.RawTextHelpFormatter)


parser.add_argument("--url",required=True,help="Insert the url to check (e.g):google.com")
parser.add_argument("--show-headers",action="store_true",help="Display the headers")
args=parser.parse_args()
url=args.url

init(autoreset=True)
if not url.startswith("http"):
    url="http://"+url


print(Fore.CYAN + r"""
  ____      _ _          _    _ _            
 / ___|(_) |_ ___   / \  | (_)_   _____   
 \___ \| | __/ _ \ / _ \ | | \ \ / / _ \  
  ___) | | ||  __// ___ \| | |\ V /  __/  
 |____/|_|\__\___/_/   \_\_|_| \_/ \___|  
""" + Style.RESET_ALL)
print(Fore.YELLOW + Style.BRIGHT + "🛠️  SiteLive - Website Status Checker v1.0\n" + Style.RESET_ALL)



try:
    res=r.get(url,timeout=5)
    if args.show_headers:
        res_headers(res.headers,show_all=True)
    else:
        res_headers(res.headers)
    if res.status_code == 200:
        print(Back.GREEN+Fore.WHITE+f"{res.status_code}- Website is active.")
    elif res.status_code in [400,401,403,404]:
          print(Fore.WHITE+Back.RED+f"{res.status_code}- Client Error:Website is not active/Unauthorized.")
    else:
        print(Back.RED+Fore.WHITE+f"{res.status_code}- No website found/Invalid website input.")

except r.exceptions.RequestException as e :
    print(Back.RED+Fore.WHITE+f"❌ Website not found or connection failed.\nError: {str(e)}")
except KeyboardInterrupt:
    print(Fore.RED+"......**Exiting**.......")
    
