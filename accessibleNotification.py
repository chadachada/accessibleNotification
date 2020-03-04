import requests
import slackweb
import time

url = ""
webhool_url = ""
interval = 300 # sec

def main():
    time_count = 0
    while(True):
        res = requests.get(url)
        if res.status_code == 200:
            slack = slackweb.Slack(url=webhool_url)
            slack.notify(text=url + " にアクセス可能になりました. ")
            break
        else:
            print("Error Status: ", res.status_code)
        time.sleep(interval)
        time_count += interval
    print("Access OK: time: [sec]", time_count)


if __name__ == "__main__":
    main()
