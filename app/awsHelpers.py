import boto3, botocore
from flask import current_app




class S3:

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
        else:
            self.client = None


    def init_app(self, app):
        self.app = app
        self.client =  boto3.client(
            "s3",
            aws_access_key_id=self.app.config['S3_ACCESS_KEY'],
            aws_secret_access_key=self.app.config['S3_SECRET_KEY']
        )


    def __getattr__(self, name):
        return getattr(self.client, name, None)


    def get_presigned_url(self, filename, expires_in=500):
    	url = self.client.generate_presigned_url(
    			ClientMethod='get_object', 
    			Params={
    			'Bucket' : self.app.config['S3_BUCKET'], 
    			'Key' : filename,
    		}, ExpiresIn=expires_in)
    	return url




    def upload_file_to_s3(self, file):

        try:
            self.client.upload_fileobj(
                file,
                self.app.config['S3_BUCKET'],
                file.filename,
                ExtraArgs={
                    "ContentType": file.content_type
                }
            )

        except Exception as e:
            print("Something Happened: ", e)
            return e

        return file.filename