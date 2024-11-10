kubectl get pv,pvc,deploy
kubectl apply -f pv.yaml,pvc.yaml,deploy-pvc.yaml

Excersice output

step-1: go inside container 
step-2: cd /sample-folder/madhu
step-3: create any file
step-4: exit and go into control-plane node ( minikube ssh )
step-5: verify the file exists in /data/db

Note: if folder is not existing in control plane create the folder `/data/db`