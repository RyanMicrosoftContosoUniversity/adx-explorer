#!/bin/bash

# Array of Bicep files and their corresponding parameter files
declare -A deployments=(
    ["event-grid-ingestion/bicep/storage-account.bicep"]="event-grid-ingestion/bicep/storage-account.params.bicepparam"
    ["event-grid-ingestion/bicep/event-hub.bicep"]="event-grid-ingestion/bicep/event-hub.params.bicepparam"
    ["event-grid-ingestion/bicep/event-grid.bicep"]="event-grid-ingestion/bicep/event-grid.params.bicepparam"
)

RESOURCE_GROUP="adx-rg"

# Loop through the deployments array and deploy each Bicep file with its parameters
for bicep_file in "${!deployments[@]}"; do
    param_file=${deployments[$bicep_file]}
    
    echo "Deploying $bicep_file with parameters from $param_file..."
    
    echo "bicep file is $bicep_file"
    echo "param file is $param_file"

    az deployment group create \
        --resource-group $RESOURCE_GROUP \
        --template-file $bicep_file \
        --parameters $param_file
    
done

