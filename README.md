# Cassava Leaf Disease Detection         

## Problem Statement
We would implement a Cassava Leaf Disease detection system.
Cassava is a rich, affordable source of carbohydrates. It can provide more calories per acre of the crop than cereal grain crops, which makes it a very useful crop in developing nations.          
              

As the 2nd largest provider of carbohydrates in Africa, cassava is a key food security crop grown by small-holder farmers because it can withstand harsh conditions. At least 80% of small-holder farmer households in Sub-Saharan Africa grow cassava and viral diseases are major sources of poor yields.              
             

We have taken 105 images for 4 leaf disease categories and a healthy category. Therefore, we have 5 categories of leaves.            
The Cassava Leaf Disease detection system would help the farmers to detect the disease correctly and take preventive measures for the same.       

### Deployment Instructions     


|  FileName  |  Description |
|---|---|
| 01-DockerSteps.md |   Steps for building the Docker Image        |
|  02-AzureContainerAppsSteps.md | Steps for deploying the image as a Container App in Azure   |         

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
          




