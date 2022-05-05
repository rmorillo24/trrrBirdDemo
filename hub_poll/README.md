# jf_poll
Polling balenaCloud API to check value changes

# How to use
- Create the environment variables
  - API_KEY: Your balenaCloud API token

- Execute `python hub_poll.py`

# How it works
- Using balenaCloud API endpoint, it will loop asking for the `block`catalog checking for changes
- If there´s a new block addition, there will be a notification
- The notification function is calling the trrBird block