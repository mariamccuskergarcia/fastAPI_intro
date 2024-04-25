## Docker

# building image
docker build -t <image_name> .

# running image to check it works on docker desktop
docker run -it -p 3000:8080 <image_name>

# deploying image to registry to then be used in Kubernetes

docker build . -t <image_name:version>
docker push <image_name:version>

## Kubernetes

kubectl apply -f prod.yaml --force=true --grace-period=0

minikube tunnel

# Rollout update

kubectl rollout restart deployment company-app-prod --namespace=company-app-prod

kubectl rollout status deployment company-app-prod --namespace=company-app-prod 


<!-- kubectl run mmg-pod --image=localhost:5000/mmg_ex5 --port 8080 --namespace=mmg-namespace

curl http://localhost:5000/v2/_catalog

kubectl create namespace ducktales-dev

kubectl port-forward service/ducktales-dev 8100:8100  --namespace=ducktales-dev
curl http://localhost:8101 -->