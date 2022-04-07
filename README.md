# telegraf-translator

Telegraf translator for Prometheus' format.
Supports three modes of operation: command line, HTTP server and Production Mode which reads from Kafka and writes in Redis.

For testing the following telegraf's output was used, encoded in ascii for the Production Mode:
```
> mem,host=testbed-monitoring-vm-1 active=1154629632i,available=1115447296i,available_percent=53.64338336682031,buffered=40411136i,cached=1162199040i,commit_limit=1039687680i,committed_as=2643795968i,dirty=16384i,free=113623040i,high_free=0i,high_total=0i,huge_page_size=2097152i,huge_pages_free=0i,huge_pages_total=0i,inactive=538869760i,low_free=0i,low_total=0i,mapped=364326912i,page_tables=8900608i,shared=2150400i,slab=200482816i,sreclaimable=116854784i,sunreclaim=83628032i,swap_cached=0i,swap_free=0i,swap_total=0i,total=2079375360i,used=763142144i,used_percent=36.700547610605526,vmalloc_chunk=0i,vmalloc_total=35184372087808i,vmalloc_used=24150016i,write_back=0i,write_back_tmp=0i 1648683860000000000\r\n> cpu,cpu=cpu0,host=testbed-monitoring-vm-1 usage_guest=0,usage_guest_nice=0,usage_idle=95.9183673668181,usage_iowait=0,usage_irq=0,usage_nice=0,usage_softirq=0,usage_steal=0,usage_system=4.081632653227896,usage_user=0 1648683861000000000\r\n> cpu,cpu=cpu1,host=testbed-monitoring-vm-1 usage_guest=0,usage_guest_nice=0,usage_idle=95.99999999627471,usage_iowait=0,usage_irq=0,usage_nice=0,usage_softirq=0,usage_steal=0,usage_system=2.0000000000436557,usage_user=1.999999999998181 1648683861000000000\r\n> cpu,cpu=cpu-total,host=testbed-monitoring-vm-1 usage_guest=0,usage_guest_nice=0,usage_idle=94.99999999650754,usage_iowait=0,usage_irq=0,usage_nice=0,usage_softirq=0,usage_steal=0,usage_system=2.9999999991850927,usage_user=1.9999999995325197 1648683861000000000
```


## Command-Line Mode
```python main.py cmd <output>```

The output will be processed and printed.


## Server Mode
```python main.py server```

A Flask server will start on port 5000 accepting POST requests for /metrics. 
The body of the request that a dictionary with the only key ```metrics```.
The response will be the processed output whenever the status code is 200.


## Production Mode
```python main.py prod```

### Environment Variables
```REDIS_PASSWORD```
**Default** "root"

```KAFKA_HOST```
**Default** "localhost""

```KAFKA_PORT```
**Default** 9092

```KAFKA_TOPIC```
**Default** "telegraf"