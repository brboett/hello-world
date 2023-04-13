##### Podman
```sh
podman build --tag flask-app .
podman run -p 5000:5000 flask-app
```

##### Docker
```sh
docker build --tag flask-app .
docker run -p 5000:5000 flask-app
```

