# plex-version-slack-notifier
Simple Docker Container which regurarly checks the current Plex version and notifies using a Slack Webhook if the version changed.

## Usage

### Docker run command:

`docker run -e SLACK_WEBHOOK="https://some.slack.webhook" muyajil/plex-version-slack-notifier:latest`

### Docker compose config:

```
version: "3.5"

services:
  plex-version-monitor:
    image: muyajil/plex-version-slack-notifier:latest
    environment:
      SLACK_WEBHOOK: "https://some.slack.webhook"
```