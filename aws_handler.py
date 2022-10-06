import boto3
import time
import urllib
import json
import os
    
transcribe_client = boto3.client('transcribe')
upload_client = boto3.client('s3')

def start_transcribe(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='fr-CA'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']
                print("========== below is output of speech-to-text ========================")
                print(text)
                print("=====================================================================")
                return text
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def upload_and_transcribe(filedir,filename):
    upload_client.upload_file(filedir,"bucketveille",filename)
    file_uri = 's3://bucketveille/'+filename
    return start_transcribe('Example-job', file_uri, transcribe_client)


def clean():
    transcribe_client.delete_transcription_job(TranscriptionJobName='Example-job')


if __name__ == '__main__':
    try:
        upload_and_transcribe()
    except:
        clean()