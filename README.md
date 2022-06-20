# az-evgrid-pydantic-schema
Azure Event Grid の event schema を Pydantic Model で提供

## 使い方

Azure Event Grid の event データ(json形式) を Pydantic Model Object にパースできます。  
現段階では以下のイベントに対応しています。

- 実装済みのイベント
    - Microsoft.Storage.BlobCreated イベント
         - https://docs.microsoft.com/ja-jp/azure/event-grid/event-schema-blob-storage?tabs=event-grid-event-schema#microsoftstorageblobcreated-event


## 開発方法

以下手順を実行して、ローカルソースを利用したテストができます。

```shell
$ cd az_evgrid_pydantic_schema
$ poetry shell
$ poetry run task test
```

## publish

- `poetry build`
- `poetry publish` 
    - `poetry publish` すると user と password の確認が求められます。
- https://cocoatomo.github.io/poetry-ja/repositories/
