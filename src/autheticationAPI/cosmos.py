from azure.cosmos import CosmosClient, PartitionKey, exceptions
import os
import json
import asyncio

URI = os.getenv("URI")
COSMOS_KEY = os.getenv("COSMOS_KEY")

client = CosmosClient(URI, credencial=COSMOS_KEY)

DATABASE_NAME = "ToDoList"

database = client.get_database_client(DATABASE_NAME)

CONTAINER_NAME = "Users"

container = database.get_container_client(CONTAINER_NAME)

print(container)
