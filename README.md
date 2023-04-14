##### Podman
```sh
$ podman build --tag flask-app .
$ podman run -p 5000:5000 flask-app
```

##### Docker
```sh
$ docker build --tag flask-app:v1.0.0 .
$ docker run -p 5000:5000 flask-app
```


##### Quay
```sh
$ podman login quay.io
$ podman push <img_id> quay.io/<user>/myfirstrepo
```

##### Deploy to OCP
```sh
$ oc new-app quay.io/<user>/myfirstrepo
$ oc get svc -o wide
$ curl <ip_address>:5000
```

##### New Build in OCP
```sh
$ oc new-build .
$ oc get is
$ oc new-app hello-world:latest
$ oc get service -o wide
$ curl <ip_address>:5000
```