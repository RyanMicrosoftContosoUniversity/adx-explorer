# adx-explorer
Note that this project is for POC purposes only.  Please see DISCLAIMER.md for more details


This Sample Code is provided for the purpose of illustration only and is not intended to be used in a production environment.
THIS SAMPLE CODE AND ANY RELATED INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, 
EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY 
AND/OR FITNESS FOR A PARTICULAR PURPOSE.  We grant You a nonexclusive, royalty-free right to use and 
modify the Sample Code and to reproduce and distribute the object code form of the Sample Code, provided that 
You agree: (i) to not use Our name, logo, or trademarks to market Your software product in which the Sample Code
is embedded; (ii) to include a valid copyright notice on Your software product in which the Sample Code is embedded;
and (iii) to indemnify, hold harmless, and defend Us and Our suppliers from and against any claims or lawsuits, 
including attorneys’ fees, that arise or result from the use or distribution of the Sample Code.



Examples for working with ADX

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Sample codebase for working with ADX

## Features

- **Event Grid Ingestion**: Easily setup an event grid subscription to automatically ingest data into an ADX table

## Steps


Navigate to Portal.azure.com and launch cloud portal
![Alt text](images\App_Registration_1.png)


Ensure you are in bash
Git clone github file
![Alt text](images/git-clone-repo.png)


Change RESOURCE_GROUP in create-event-grid.infra.sh file
![Alt text](images/change-rg-name.png)

Adjust parameter names in bicepparam files to desired values
![Alt text](images/change-biccepparam-values.png)

Change permissions for cloud shell to allow script to be run
![Alt text](images/elevate-permissions-for-script.png)

From root, run ./event-grid-ingestion/.bash/create-event-grid-infra.sh
![Alt text](images/run-create-infra.png)

Deployment in Progress
![Alt text](images/deployment-in-progress.png)

Post Deployment Results
![Alt text](images/post-deployment-results.png)



## Create Data Connection for Event Grid
Create a new ADX table, this can be done either via the UI or using the script in this repo (as an example)

In your ADX Database, create a new data connection for the Event Grid created earlier
![Alt text](images/create-event-grid-connection.png)
![Alt text](images/create-event-grid-connection-details.png)

Missed from the earlier screenshot, be sure to add the correct mapping file as well
![Alt text](images/add-missing-mapping-file-image.png)

Upload the second file and the Event Grid should load the data for the ADX DB
![Alt text](images/upload-second-file.png)

Wait five minutes and you should see traffic against the event hub
![Alt text](images/traffic-check.png)

Check the table you created and you should see more data in the table now
![Alt text](images/additional-data-in-table.png)
