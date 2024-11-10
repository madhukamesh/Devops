### Job
- Jobs are used to a run a command one or many times until they are completed
- After job completed the POD status turns to "completed".

step 1: Deploy job to cluster
`kubectl apply -f .`

step 2: see the status
`kubectl get all`

step 3: verify the logs after completed
`kubectl logs pod/pod-name`