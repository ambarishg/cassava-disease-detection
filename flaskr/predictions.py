from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

import os
from . import kvutils
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

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

        return render_template('predictions/index.html',
        filename = local_file_name)

    return render_template('predictions/predict.html')

@bp.route('/')
def index():
    return render_template('predictions/index.html')