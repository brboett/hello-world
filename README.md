##### Podman
```sh
$ podman build --tag flask-app .
$ podman run -p 5000:5000 flask-app
```

##### Docker
```sh
$ docker build --tag flask-app .
$ docker run -p 5000:5000 flask-app
```


##### Quay
```sh
$ podman login quay.io
$ push quay.io/brboett/myfirstrepo
```

##### Deploy to OCP
```sh
$ oc new-app quay.io/brboett/myfirstrepo
$ oc get svc -o wide
$ curl 172.30.154.35:5000
```