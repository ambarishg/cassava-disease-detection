from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

import os
from . import kvutils
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials


bp = Blueprint('predictions', __name__)

@bp.route('/predict', methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        local_file_name =  request.files["filename"].filename
        bytes_data = request.files["filename"].read()
        
        credential = kvutils.credential
        account_url = kvutils.account_url 
        container_name = kvutils.container_name 
        blob_service_client = BlobServiceClient(account_url, 
    credential=credential)
        blob_client = blob_service_client.get_blob_client(container=container_name, 
        blob=local_file_name)
        blob_client.upload_blob(bytes_data)

        ENDPOINT = kvutils.ENDPOINT
        prediction_key = kvutils.prediction_key
        prediction_resource_id = "paddy"
        project_id = kvutils.project_id
        publish_iteration_name = kvutils.publish_iteration_name

         # Now there is a trained endpoint that can be used to make a prediction
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

        results = predictor.classify_image(
                project_id, publish_iteration_name, bytes_data)
        

        return render_template('predictions/index.html',
        filename = local_file_name,predictionresults = results.predictions)

    return render_template('predictions/predict.html')

@bp.route('/')
def index():
    return render_template('predictions/index.html')