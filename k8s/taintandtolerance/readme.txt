#### Examples for taint-and-tolerance

syntax url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/


Types of Effects
- NoExecute ( hard taint, delete existing pods in node )
- NoSchedule ( hard taint, but won't delete existing pods in node )
- PreferNoSchedule ( soft taint )

- To get all nodes names
`kubectl get nodes`

```yaml
minikube - control-plane
minikube-m02 - worker-node-1
minikube-m03 - worker-node-2
```

- To see the yaml file of node
`kubectl get node <node-name> -o yaml `

kubectl get pod <pod name> -o yaml

Step 1:
Taint an node

- `kubectl taint nodes <node-name> key=value:NoSchedule`
- ex: `kubectl taint nodes minikube-m02 degredation=commence:NoSchedule`

Step 2:
    - tolerations to pod
```yaml
tolerations:
- key: "degredation"
  operator: "Equal"
  value: "commence"
  effect: "NoSchedule"
```


##### Example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:

 ### changes start
  tolerations:
  - key: "degredation"
    operator: "Equal"
    value: "commence"
    effect: "NoSchedule"
  ### changes end

  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
```


Output
check where the pods are scheduled in node
`kubectl get pod -o wide`
`kubectl get all -o wide`