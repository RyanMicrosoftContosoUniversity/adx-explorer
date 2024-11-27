param eventHubNamespace string
param eventHubName string
param systemTopicName string
param storageAccountName string 
param eventGridSubscriptionName string

var eventHubResourceId = resourceId('Microsoft.EventHub/namespaces/eventhubs', eventHubNamespace, eventHubName)

resource systemTopic 'Microsoft.EventGrid/systemTopics@2020-04-01-preview' = {
  name: systemTopicName
  location: resourceGroup().location
  properties: {
    source: resourceId('Microsoft.Storage/storageAccounts', storageAccountName)
    topicType: 'Microsoft.Storage.StorageAccounts'
  }
}

resource eventSubscription 'Microsoft.EventGrid/systemTopics/eventSubscriptions@2020-04-01-preview' = {
  name: eventGridSubscriptionName
  parent: systemTopic
  properties: {
    destination: {
      properties: {
        resourceId: eventHubResourceId
      }
      endpointType: 'EventHub'
    }
    filter: {
      includedEventTypes: [
        'Microsoft.Storage.BlobCreated'
      ]
    }
  }
}

output ADXresourceId string = eventHubResourceId
