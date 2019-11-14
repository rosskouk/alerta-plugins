# Alerta Plugins

Custom plugins for Alerta

Copyright (c) 2019 Ross A. Stewart

https://github.com/rosskouk/alerta-plugins

## Plugins

### routing

This plugin provides plugin routing rules for alerts, this allows decisions to be made on what to do with different types of alerts, e.g to not send information alerts to Telegram.

https://docs.alerta.io/en/latest/api/alert.html#attributes-added-when-processing-alerts
https://docs.alerta.io/en/latest/gettingstarted/tutorial-3-plugins.html#step-2-write-a-plugin

#### Installation

Install the plugin in a traditional installation with:

```
python setup.py install
```

or install the plugin in the alerta docker container by adding the following to your Dockerfile:

```
RUN /venv/bin/pip install git+https://path/to/git/file@branch#subdirectory=subdirectroy

