`kubectl rollout command deploy/<deploy-name>`

history: `kubectl rollout history deploy/<deploy-name>`

undo: `kubectl rollout undo deploy/<deploy-name>`

to-go-specific-revision: `kubectl rollout undo deploy/<deploy-name> --to-revision=3`


link: https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/

to check errors when pod is 0 ready state:kubectl describe deploy
to check errors :kubectl get events
to check errors in pod: kubectl logs <pod-name>          

output 

kubectl get deploy -oyaml