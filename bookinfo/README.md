## BookInfo Application Dataset

This dataset is generated via [locust](https://locust.io/) for [bookinfo](https://istio.io/latest/docs/examples/bookinfo/) application.

#### Steps to generate this dataset:

- Install Docker Desktop App (https://docs.docker.com/docker-for-mac/install/)

- Enable Kubernetes in the Docker Desktop App.

- Download Istio locally 

```
$ curl -L https://istio.io/downloadIstio | sh -
```

- Move to the Istio directory

```
$ cd istio-1.8.2
```

- Add istioctl to the PATH

```
$ export PATH=$PWD/bin:$PATH
```

- Install Istio

```
$ istioctl install --set profile=demo -y
```

- Add a namespace label to instruct Istio to automatically inject Envoy sidecar proxies 

```
$ kubectl label namespace default istio-injection=enabled
```

- Deploy Jaeger

```
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.8/samples/addons/jaeger.yaml
```

- Verify Jaeger Installation by hitting services endpoint

```
$ curl http://localhost:16686/jaeger/api/services
```

- Deploy BookInfo application

```
$ kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
```

- Wait for some time to let the application containers to start.

```
$ kubectl get services
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
details       ClusterIP   10.0.0.212      <none>        9080/TCP   29s
kubernetes    ClusterIP   10.0.0.1        <none>        443/TCP    25m
productpage   ClusterIP   10.0.0.57       <none>        9080/TCP   28s
ratings       ClusterIP   10.0.0.33       <none>        9080/TCP   29s
reviews       ClusterIP   10.0.0.28       <none>        9080/TCP   29s
```

```
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-558b8b4b76-2llld       2/2     Running   0          2m41s
productpage-v1-6987489c74-lpkgl   2/2     Running   0          2m40s
ratings-v1-7dc98c7588-vzftc       2/2     Running   0          2m41s
reviews-v1-7f99cc4496-gdxfn       2/2     Running   0          2m41s
reviews-v2-7d79d5bd5d-8zzqd       2/2     Running   0          2m41s
reviews-v3-7dbcdcbc56-m8dph       2/2     Running   0          2m41s
```

- Verify the BookInfo installation

```
$ kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -s productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

- Run locust.

```
$ locust -f locust.py
```

- Extract data from jaeger to json.

```
$ python extract.py
```
