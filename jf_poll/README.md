# jf_poll
Polling JellyFish API to check value changes

# How to use
- Create the environment variables
  - IMPROVEMENT_ID: The improvement id to track
  - IMPROVEMENT_SLUG: The improvement slug to track
  - JF_TOKEN: Your JellyFish token

- Execute `python jf_poll.py`

# How it works
- Using jellyfish API endpoint, it will loop asking for `status` and checking for changes
- If the new value is `completed` it call the `notification()` 
- This is stateless and not persisted, but notification will not be called if the status is already completed