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
$ push quay.io/<user>/myfirstrepo
```

##### Deploy to OCP
```sh
$ oc new-app quay.io/<user>/myfirstrepo
$ oc get svc -o wide
$ curl <ip_address>:5000
```