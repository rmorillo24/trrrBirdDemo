# trrrBirdDemo
A demo of the trrrBird project, twitting changes on JF improvements and balenaHub catalog

## How it works

There are three services
- jf_poll that checks for Improvement changes. When completed it will call the soro service
- hub_poll that checks for new blocks in the balena catalog. When completed it will call the soro service
- soro block that serves as the social media broker to publish the above notifications
