import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


@app.blob_trigger(arg_name="myblob", path="images",
                               connection="AzureWebJobsStorage") 
def HelloBlob(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    



@app.queue_trigger(arg_name="azqueue", queue_name="cnammessages",
                               connection="AzureWebJobsStorage") 
def helloazure(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
