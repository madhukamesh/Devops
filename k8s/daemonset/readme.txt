### DaemonSet
- Adds pod into every node
- Also possible to add NodeAffinity and Tolerations

step 1: Deploy daemonset to cluster
`kubectl apply -f .`

step 2a: See the lables of master node
`kubectl get node minikube -oyaml`

step 2b: if you want to see colorful yaml (optional)
`kubectl get node minikube -oyaml | yq .`

step 3: add a node to check pod is getting added to that node automatically by daemonset
`minikube add node`

step 4: verify
`kubectl get pods -o wide`