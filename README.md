# Cassava Leaf Disease Detection         

## Problem Statement
We would implement a Cassava Leaf Disease detection system.
Cassava is a rich, affordable source of carbohydrates. It can provide more calories per acre of the crop than cereal grain crops, which makes it a very useful crop in developing nations.          
              

As the 2nd largest provider of carbohydrates in Africa, cassava is a key food security crop grown by small-holder farmers because it can withstand harsh conditions. At least 80% of small-holder farmer households in Sub-Saharan Africa grow cassava and viral diseases are major sources of poor yields.              
             

We have taken 105 images for 4 leaf disease categories and a healthy category. Therefore, we have 5 categories of leaves.            
The Cassava Leaf Disease detection system would help the farmers to detect the disease correctly and take preventive measures for the same.       

### Deployment Instructions [ Steps ]     
1.  Create the Custom Vision AI project for training the Cassava Leaf images            
2.  Steps for building the Docker Image [ `docs/01-DockerSteps.md` ]   
3.  Steps for deploying the image as a Container App in Azure [ `docs/2-AzureContainerAppsSteps.md` ]  
4.  Turn the Managed identity [System Assigned] for the deployed Container App     
5.  Create the Storage Account and the Container       
6.  Create the CosmosDB account , database and container. The partition of the container is **category**               
7. Assign Storage Data Blob Contributor Role to the Container App  for the Storage Account so that the Container App can read,write and delete the images in the Storage Account                   
8. Assign Access Policies for the Container App so that the Container App can acess the secrets in the KeyVault
9. Create the secrets in the KeyVault   

## Images of the **Azure Container App**           
|  FileName  |  Description |
|---|---|
| docs\images\ContainerApp\SystemIdentitySetting.png |    Images of the System identity configuration of the Container App which is turned ON            |   
| docs\images\ContainerApp\StorageBlobDataContributorRole.png |     Images of the Storage Account  - Storage Data Blob Contributor Role             |       
| docs\images\ContainerApp\KeyVaultAccess.png |    Key Vault - Access Polices to acess the Key Vault Secrets             |    

### Files     


|  FileName  |  Description |
|---|---|
| Dockerfile |   Docker file for the Container Image        |       
| requirements.txt |   Has the dependencies required for the Container Image        |        
|  app.py | Has the code for running the Flask app |    
| flaskr / cosmosdbwithoutasync.py |   Has the code for connecting the Container App with **CosmosDB**        |        
|  flaskr / kvutils.py | Has the code for reading the secrets from the **KeyVault** by the Container App   |          
|  flaskr / predictions.py | Has the code for getting the **predictions** for the Cassava Leaf by the Container App   |      
|  flaskr / __init__.py | Has the code for initialization for the **Flask** App |      
|  flaskr / templates folder | Folder containing the Views of the Container App   |        
|  flaskr / static folder | Folder containing the CSS file   |     

## Images of the **Cassava Disease Detection Application** 

|  FileName  |  Description |
|---|---|
| docs\images\CassavaDiseaseApplication\Predict.png  |    Prediction UI - Cassava Application          |     
| docs\images\CassavaDiseaseApplication\PredictionResult.png  |    Prediction Result - Cassava Application          |     
| docs\images\CassavaDiseaseApplication\Predict.png  |    All Predictions - Cassava Application          |     
| docs\images\CassavaDiseaseApplication\Predict.png  |    Search Predictions by Filename - Cassava Application          |     
          




