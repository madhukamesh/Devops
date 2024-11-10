#### Examples for node-affinity

syntax url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/


Types of Node-Affinity
- requiredDuringSchedulingIgnoredDuringExecution ( similar to NodeSelector hard rule )
- preferredDuringSchedulingIgnoredDuringExecution ( soft rule ) means even if the affinity is not there pods can be scheduled

- To get all nodes names
`kubectl get nodes`

- To see the yaml file of node
`kubectl get node <node-name> -o yaml | yq .`

Step 1:
    Add label to node

- `kubectl edit node <node-name>`
- add label
    key: value ( operating-system: windows )

Step 2:
    - Add `nodeSelector` to container in pod


##### preferredDuringSchedulingIgnoredDuringExecution:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:

 ### changes start
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: operating-system
            operator: In
            values:
            - windows
  ### changes end

  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
```

##### requiredDuringSchedulingIgnoredDuringExecution:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    env: test
spec:

 ### changes start
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: operating-system
            operator: In
            values:
            - windows
  ### changes end

  containers:
  - name: nginx
    image: nginx
    imagePullPolicy: IfNotPresent
```

Output
check where the pods are scheduled in node
`kubectl get pod -o wide`