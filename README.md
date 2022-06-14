# Orwell Translators
This repository holds all the different translator scripts built for reading different Kafka topics and outputing valid Prometheus format.

Translators were written using Orwell's [Python package](https://pypi.org/project/orwell-translators/) and, therefore, they can all be executed with the arguments and evironment variables, which are documented in the [package's repository](https://github.com/OrwellMonitoring/orwell-python-package/blob/v1/README.md). 

<br/><br/>

## Developing New Translators
The process of creating a new translator, the script itself, is described in both PyPI's project description and the package's repository. After that, a new folder should be created for that translator with a `main.py` script and a `requirements.txt` file. 

Adding a reference to that folder inside of `docker-compose.yml` and pushing the changes to the repository is all that is required for triggering the CD pipeline and deploying the updated translators in the configured machine(s).

<br/><br/>

## Current Translators
### eSight Translators
Two translators are provided for eSight metrics, one for the interfaces and another for the routers. These metrics are generated from a [custom connector](https://github.com/OrwellMonitoring/esight_connector).

### PerfSonar Translator
Translation of network metrics pushed from a [custom connector](https://github.com/OrwellMonitoring/perfsonar-utils/tree/main/pull-service).

### Prometheus' Node Exporter Translator
Despite these metrics already coming in the desired format, this translator is responsible for reading from Kafka and writing to Redis.

### Gnocchi Translator
This translator is the responsible for the metrics that come directly from the OpenStack hypervisor. Metrics are pushed to Kafka from [Orwell's core](https://github.com/OrwellMonitoring/orwell-core/tree/main/middleware/app/gnocchi) and its output follow the same nomenclature of Prometheus' Node Exporter's metrics.

### Telegraf Translator
Translator for the Telegraf tool, which more than exporting Prometheus' format, rearranges its metrics so as that its metrics follow the same nomenclature of Prometheus' Node Exporter's.