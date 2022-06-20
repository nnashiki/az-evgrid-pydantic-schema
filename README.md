# az-evgrid-pydantic-schema
Azure Event Grid の event schema  を Pydantic Model で提供


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
