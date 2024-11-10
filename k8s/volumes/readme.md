###### nginx
- touch /sample-folder/madhu/test-document.txt




#### port-forward
- Used for connecting the localhost to service
    syntax : `kubectl port-forward service/service-name <host_port>:<service_port>`
    ex: `kubectl port-forward service/mongo-svc 9001:27017`

#### How to connect to mongo compass
- step-1 download mongo-compass in ubuntu
    https://www.mongodb.com/try/download/compass

- step-2 connect the mongo-compass with mongoDB
    click `new connection`

- step-3
    enter url in the box `mongodb://localhost:9001`

- step-3
    - click `Advanced connection options`
    - click Authentication
    - put userName as `admin`
    - put password as `password`
    - click `connect`