import requests
import os
import json
from retry import retry
import time


def send_message_to_slack(message, markdown=True):
    data = {"text": message, "markdown": True}
    url = os.environ.get('SLACK_WEBHOOK')
    print(url)
    _ = requests.post(
        url,
        data=json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )


def check_and_update_content(content, path):
    if not os.path.exists(path):
        open(path, 'w').write(content)
        return True
    else:
        last_recorded_content = open(path).read().strip()
        if content != last_recorded_content:
            os.remove(path)
            open(path, 'w').write(content)
            return True
        else:
            return False


@retry(RuntimeError, delay=20)
def get_current_version():
    current_version = requests.get('https://plex.tv/api/downloads/1.json?channel=plexpass').json()
    try:
        current_version = json.dumps(current_version["computer"]["Linux"]["version"], indent=2)
        return current_version.strip('"')
    except:
        raise RuntimeError()


while True:
    current_version = get_current_version()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'current_version.txt')
    changed = check_and_update_content(current_version, file_path)
    if changed:
        send_message_to_slack("New Plex Version available: ```" + current_version + "```")
    time.sleep(300)
