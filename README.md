# slack-imgur

[![Code Climate](https://codeclimate.com/github/juanpabloaj/slack-imgur/badges/gpa.svg)](https://codeclimate.com/github/juanpabloaj/slack-imgur)

Get a random image from Imgur in a Slack Channel, with Slack Outgoing WebHooks.

![gif](http://i.imgur.com/pUZq3U3.gif)

## Usage

Create a [Slack Outgoing WebHooks][webhook], select a channel, set a trigger word and add [slack-imgur.herokuapp.com][slack-imgur] to URL(s) field.

![img](http://i.imgur.com/79u5e7L.png)

### Call a random image

Call a random image from [Imgur][imgur] (if you set `imgur` as trigger word)

    imgur

### Tag filter

Get a random image tagged with the tag called lolcat

    imgur lolcat

[webhook]: https://getscreenshots.slack.com/services/new/outgoing-webhook
[slack-imgur]: http://slack-imgur.herokuapp.com
[imgur]: http://imgur.com/
