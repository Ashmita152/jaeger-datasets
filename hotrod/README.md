## HotRod Application Dataset

This dataset is generated via [locust](https://locust.io/) for [hotrod](https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941) application.

#### Steps to generate this dataset:

- Start jaeger all-in-one docker container.

```
$ docker run -d --name jaeger \
      -e COLLECTOR_ZIPKIN_HTTP_PORT=9411 \
      -p 5775:5775/udp \
      -p 6831:6831/udp \
      -p 6832:6832/udp \
      -p 5778:5778 \
      -p 16686:16686 \
      -p 14268:14268 \
      -p 14250:14250 \
      -p 9411:9411 \
      jaegertracing/all-in-one:1.21
```

- Start example-hotrod docker container.

```
$ docker run -d --name hotrod --rm -it \
      --link jaeger \
      -p 8080-8083:8080-8083 \
      -e JAEGER_AGENT_HOST="jaeger" \
      jaegertracing/example-hotrod:1.21 \
      all
```

- Run locust.

```
$ locust -f locust.py
```

- Extract data from jaeger to json.

```
$ python extract.py
```
