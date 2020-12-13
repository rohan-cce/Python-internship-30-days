'''

Task Given by Best enlist 
30 days Python Internship 
Add the links to scan in urls.txt 
Usage :-
        Open command line in the same directory of the python file
        Then Type  python Malicious_url_scanner -t url -p urls.txt
        Create a Account in virustotal.com and get copy the api key in clipboard
        
'''
import requests
import time
import argparse
import sys
import base64


def errors(status,value_for_scan,scan_type,values):
    if status in (404, 429):
        print(f"""Error Code: {values['error']['code']}\nError Description: {values['error']['message']}\n""")
            

        if scan_type=="url":
            unscanned_urls.append(f"{value_for_scan}\n")
            print("Sleeping for 45 seconds.")
            time.sleep(45)

           
    elif status in (400, 401, 403, 409, 503, 504):            
        sys.exit(f"""Error Code: {values['error']['code']}\nError Description: {values['error']['message']}""")
    
    else:
        sys.exit(f"unknown error")

def url_scanner(api,url_path,type_url):
    url = 'https://www.virustotal.com/api/v3/urls/'
    headers = {'x-apikey':api}

    with open(url_path,"r",encoding="utf-8") as r_file:
        for url_vt in r_file.read().split():
            url_id = base64.urlsafe_b64encode(url_vt.strip().encode()).decode().strip("=")

            response = requests.get(url+url_id,headers=headers)
            values = response.json()
            status = response.status_code

            if status == 200:
                try:
                    if values['data']['attributes']['last_analysis_stats']['malicious'] > 0:
                        print(f"""{url_vt} is malicious.\n
                        Harmless: {values['data']['attributes']['last_analysis_stats']['harmless']}
                        Malicious: {values['data']['attributes']['last_analysis_stats']['malicious']}
                        Suspicious: {values['data']['attributes']['last_analysis_stats']['suspicious']}
                        Undetected: {values['data']['attributes']['last_analysis_stats']['undetected']}\n
                        VT link for URL: https://virustotal.com/gui/url/{values['data']['id']}/detection
                        """)

                    else:
                        print(f"""{url_vt} is clean.\n
                        Harmless: {values['data']['attributes']['last_analysis_stats']['harmless']}
                        Malicious: {values['data']['attributes']['last_analysis_stats']['malicious']}
                        Suspicious: {values['data']['attributes']['last_analysis_stats']['suspicious']}
                        Undetected: {values['data']['attributes']['last_analysis_stats']['undetected']}\n
                        VT link for URL: https://virustotal.com/gui/url/{values['data']['id']}/detection
                        """)

                    report_urls.append((url_vt,values['data']['attributes']['last_analysis_stats']['harmless'],values['data']['attributes']['last_analysis_stats']['malicious'],
                                      values['data']['attributes']['last_analysis_stats']['suspicious'],values['data']['attributes']['last_analysis_stats']['undetected'],
                                      f"https://virustotal.com/gui/url/{values['data']['id']}/detection"))

                except Exception:
                    # Possible error causes; not valid domain pattern or Domain not found in VT Database. If the reasons is not these, please don't be hesitate for contact me.
                    print(values['error']['message'])
                    
                time.sleep(15)
            
            else:
                print(errors(status,url_vt,type_url,values))
    print("Thank you for using this program ! \n The program will exit now")
def main():
    print("""Sample Usage:
    python Malicious_url_scanner.py -t url -p urls.txt
    """)
    user_ip=input("Do You have virus total api key ? y/n : ")
    if(user_ip=='Y' or user_ip=='y'):
        api = input("\n Enter your API key: ")
        print("\n\n")

        parser = argparse.ArgumentParser(description='You can submit multiple file hashes and urls with this script.')
        parser.add_argument("-t","--type",help="You should type what you want for submitting VT (url or file or domain).",required=True)
        parser.add_argument("-p","--path",help="Type file path",required=True)
    
        args=parser.parse_args()

    

        if args.type in ("url","Url","URL"):
            url_scanner(api,args.path,args.type)
        else:
            sys.exit("You entered wrong values.")
    if(user_ip=='N' or user_ip=='n'):
        print("Goto Virustotal.com signup for a account and then get the api key")
        
 
if __name__=="__main__":
    unscanned_hashes = list()
    unscanned_urls = list()
    report_urls = list()
    main()
    