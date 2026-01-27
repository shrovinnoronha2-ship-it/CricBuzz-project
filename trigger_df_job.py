from googleapiclient.discovery import build

def trigger_dataflow(event, context):
    """Start Dataflow job when CSV is uploaded to GCS"""
    
    service = build('dataflow', 'v1b3')
    project = "prj-poc-001"
    
    config = {
        "jobName": "cricket-pipeline",
        "parameters": {
            "javascriptTextTransformGcsPath": "gs://bkt-dataflow-metadata/udf.js",
            "JSONPath": "gs://bkt-dataflow-metadata/bq.json",
            "javascriptTextTransformFunctionName": "transform",
            "outputTable": "prj-poc-001:cricket_dataset.icc_odi_batsman_ranking",
            "inputFilePattern": "gs://bkt-dataflow-metadata/batsmen_rankings_cleaned.jsonl",
            "bigQueryLoadingTemporaryDirectory": "gs://bkt-dataflow-metadata/temp",
        }
    }
    
    # Start Dataflow job
    request = service.projects().templates().launch(
        projectId=project,
        gcsPath="gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery",
        body=config
    )
    
    return request.execute()
