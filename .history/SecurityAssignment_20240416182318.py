
import json
import mysql.connector
import docker

# Connect to the Docker Network
client = docker.from_env()
networks = client.networks.list()
aim_network = None
for network in networks:
    if network.name == 'monitoring_network':
        aim_network = network
        break
print(aim_network.attrs)
print(aim_network.name)
containers = aim_network.Containers
print(aim_network.Containers)
# If the network was found, print the names of all containers in it
if aim_network is not None:
    for container in aim_network.containers:
        print(container.name)
else:
    print("Network 'monitoring_network' not found")
