#### What's this?

Docker, Nginx, Consul, Consul Template and Registrator joined together to create an auto scaling reverse proxy.

#### Preparations:

1. Install docker-machine and docker-compose

 ```brew install docker-machine docker-compose```

2. Create a docker host

 ```docker-machine create -d virtualbox --virtualbox-memory "2048" --virtualbox-disk-size "8000" dockhost```

3. Connect to docker engine

 ```eval $(docker-machine env dockhost)```

 ```export DOCKER_IP=$(docker-machine ip dockhost)```


#### Testing:

1. Start building and bringing up containers

 ```docker-compose up -d```

2. Test connectivity

 ```./lb-script.py -s $DOCKER_IP -n 50```

3. Scale up number of backend nodes

 ```docker-compose scale helloworld=10```

4. Test connectivity again

 ```./lb-script.py -s $DOCKER_IP -n 50```

5. Scale down number of backend nodes

 ```docker-compose scale helloworld=3```

6. Test connectivity again

 ```./lb-script.py -s $DOCKER_IP -n 50```
