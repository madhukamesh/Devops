#### Examples for Node-selector

minikube start -n 3

- To get all nodes names
`kubectl get nodes`

- To see the yaml file of node
`kubectl get node <node-name> -o yaml`

Step 1:
    Add label to node

- `kubectl edit node <node-name>`
- add label
    key: value ( operating-system: windows )

Step 2:
    - Add `nodeSelector` to container in pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:
  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
  nodeSelector:
    operating-system: windows # Node selector label goes here.
```

Output
check where the pods are scheduled in node
`kubectl get pod -o wide`