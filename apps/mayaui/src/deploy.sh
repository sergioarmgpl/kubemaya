DEST_APPS=/tmp/apps
APP_PORT=80
DEST_IMAGE=/tmp/imgs
function deploy_app(){
    app=$1
    cp *.tar $DEST_IMAGE
    kubectl create ns $app
    kubectl apply -f $DEST_APPS/$app -n $app
    #kubectl rollout status deployment/$app -n $app --timeout=1m
    kubectl expose deployment $app --port=$APP_PORT -n $app
    kubectl create ingress $app --rule=/$app=$app:$APP_PORT -n $app
    echo "app installed"
    exit 0
}

"$@"