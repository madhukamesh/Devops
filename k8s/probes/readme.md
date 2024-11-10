step1: create docker image
`docker build . -t sample-flask-app:v1`

step2: use the image in the deployment-failure.yaml

step3: load image into minikube
`minikube image load sample-flask-app:v1`

Practical Test

Scenario 1: Failure case of readiness probes
`kubectl apply -f deployment-failure.yaml`
`kubectl apply -f service.yaml`

output:
`kubectl get all or kubectl get pod`
`kubectl get svc`
`kubectl describe svc my-service` # to check endpoint (whether endpoint ip address connected to service or not)

Expectation
    - Pod will NOT be ready, to get pod IP address `kubectl get pod -owide`
    - Inspecting endpoints/service with `kubectl describe svc/my-service ` will NOT have endpoint/ip-address of new pod

Scenario 2: Success case of all probes working
`minikube apply -f deployment-success.yaml`

output:
`kubectl get all or kubectl get pod`

Expectation
    - Pod will be READY, to get pod IP address `kubectl get pod -owide`
    - Inspecting endpoints/service with `kubectl describe svc/my-service ` will have endpoint/ip-address of new pod

To get Count:
kubectl logs pod/<pod-name> | grep "unknown_path" -c to check count 

Scenario 2: Failure case of liveness probes
kubectl apply -f deployment-failure.yaml`
`kubectl apply -f service.yaml`

output:
`kubectl get all or kubectl get pod`
`kubectl get svc`
`kubectl describe svc my-service` # to check endpoint (whether endpoint ip address connected to service or not)

Expectation
    - Pod will NOT be ready, to get pod IP address `kubectl get pod -owide`  
