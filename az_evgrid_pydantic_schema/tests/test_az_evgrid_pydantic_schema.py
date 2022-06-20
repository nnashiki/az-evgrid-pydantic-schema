from az_evgrid_pydantic_schema import __version__, StorageBlobCreatedFull, StorageBlobCreatedBase
import datetime

def test_version():
    assert __version__ == "0.1.0"


def test_parse_storage_blob_created_full_event():
    # ex. from https://docs.microsoft.com/ja-jp/azure/event-grid/event-schema-blob-storage?tabs=event-grid-event-schema
    event = """
{
  "topic": "/subscriptions/{subscription-id}/resourceGroups/Storage/providers/Microsoft.Storage/storageAccounts/my-storage-account",
  "subject": "/blobServices/default/containers/test-container/blobs/new-file.txt",
  "eventType": "Microsoft.Storage.BlobCreated",
  "eventTime": "2017-06-26T18:41:00.9584103Z",
  "id": "831e1650-001e-001b-66ab-eeb76e069631",
  "data": {
    "api": "PutBlockList",
    "clientRequestId": "6d79dbfb-0e37-4fc4-981f-442c9ca65760",
    "requestId": "831e1650-001e-001b-66ab-eeb76e000000",
    "eTag": "0x8D4BCC2E4835CD0",
    "contentType": "text/plain",
    "contentLength": 524288,
    "blobType": "BlockBlob",
    "url": "https://my-storage-account.blob.core.windows.net/testcontainer/new-file.txt",
    "sequencer": "00000000000004420000000000028963",
    "storageDiagnostics": {
      "batchId": "b68529f3-68cd-4744-baa4-3c0498ec19f0"
    }
  },
  "dataVersion": "",
  "metadataVersion": "1"
}
"""

    event = StorageBlobCreatedFull.parse_raw(event)
    assert event.id == "831e1650-001e-001b-66ab-eeb76e069631"
    assert event.eventTime == datetime.datetime(2017, 6, 26, 18, 41, 0, 958410, tzinfo=datetime.timezone.utc)
    assert isinstance(event.data, StorageBlobCreatedBase)
    assert event.data.url == "https://my-storage-account.blob.core.windows.net/testcontainer/new-file.txt"
