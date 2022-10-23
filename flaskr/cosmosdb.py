from azure.cosmos.aio import CosmosClient as cosmos_client
from azure.cosmos import PartitionKey, exceptions

import asyncio

from . import kvutils

# <method_populate_container_items>
async def populate_container_items(container_obj, item_to_create):
    # Add items to the container
    inserted_item = await container_obj.create_item(body=item_to_create)
    # </create_item>
# </method_populate_container_items>

# <create_database_if_not_exists>
async def get_or_create_db(client, database_name):
    try:
        database_obj  = client.get_database_client(database_name)
        await database_obj.read()
        return database_obj
    except exceptions.CosmosResourceNotFoundError:
        print("Creating database")
        return await client.create_database(database_name)
# </create_database_if_not_exists>
    
# Create a container
# Using a good partition key improves the performance of database operations.
# <create_container_if_not_exists>
async def get_or_create_container(database_obj, container_name):
    try:        
        todo_items_container = database_obj.get_container_client(container_name)
        await todo_items_container.read()   
        return todo_items_container
    except exceptions.CosmosResourceNotFoundError:
        print("Creating container with lastName as partition key")
        return await database_obj.create_container(
            id=container_name,
            partition_key=PartitionKey(path="/category"),
            offer_throughput=400)
    except exceptions.CosmosHttpResponseError:
        raise
# </create_container_if_not_exists>

async def create_item(item_to_create):
    # <add_uri_and_key>
    endpoint = kvutils.cosmosdb_endpoint 
    key = kvutils.cosmosdb_key 
    # </add_uri_and_key>

    # <define_database_and_container_name>
    database_name = kvutils.cosmosdb_database_name 
    container_name = kvutils.cosmosdb_container_name 
    # </define_database_and_container_name>
    async with cosmos_client(endpoint, credential = key) as client:

        database_obj = await get_or_create_db(client, database_name)
        # create a container
        container_obj = await get_or_create_container(database_obj, container_name)
            
        # populate the family items in container
        await populate_container_items(container_obj, item_to_create)  
        
async def get_all_items():
    # <add_uri_and_key>
    endpoint = kvutils.cosmosdb_endpoint 
    key = kvutils.cosmosdb_key 
    # </add_uri_and_key>

    # <define_database_and_container_name>
    database_name = kvutils.cosmosdb_database_name 
    container_name = kvutils.cosmosdb_container_name 
    # </define_database_and_container_name>
    async with cosmos_client(endpoint, credential = key) as client:

        database_obj = await get_or_create_db(client, database_name)
        # create a container
        container_obj = await get_or_create_container(database_obj, container_name)

        allitems = []
        for item in container_obj.query_items(
        query='SELECT * FROM predictions'):
            allitems.append(item)
        
        return(allitems)
            