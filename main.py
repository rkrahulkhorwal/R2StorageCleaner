import boto3
from botocore.config import Config
from datetime import datetime

def clean_r2_storage(account_id, access_key_id, secret_access_key, bucket_name):
    """
    Clean objects from Cloudflare R2 storage bucket
    
    Parameters:
    account_id (str): Your Cloudflare account ID
    access_key_id (str): R2 access key ID
    secret_access_key (str): R2 secret access key
    bucket_name (str): Name of the R2 bucket to clean
    """
    try:
        # Configure the S3 client for Cloudflare R2 with specific config
        config = Config(
            signature_version='s3v4',
            region_name='auto',
            # Disable checksum which causes the NotImplemented error
            s3={
                "payload_signing_enabled": False,
                "use_accelerate_endpoint": False,
                "checksums_algorithm": None
            }
        )

        s3_client = boto3.client(
            's3',
            endpoint_url=f'https://{account_id}.r2.cloudflarestorage.com',
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            config=config
        )

        # List all objects in the bucket
        print(f"Starting cleanup of bucket: {bucket_name}")
        print(f"Current UTC time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
        
        paginator = s3_client.get_paginator('list_objects_v2')
        deleted_count = 0
        error_count = 0

        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    try:
                        # Delete individual objects instead of batch deletion
                        s3_client.delete_object(
                            Bucket=bucket_name,
                            Key=obj['Key']
                        )
                        deleted_count += 1
                        if deleted_count % 10 == 0:  # Progress update every 10 deletions
                            print(f"Successfully deleted {deleted_count} objects...")
                            
                    except Exception as delete_error:
                        error_count += 1
                        print(f"Error deleting {obj['Key']}: {str(delete_error)}")

        print(f"\nCleanup Summary:")
        print(f"Successfully deleted: {deleted_count} objects")
        print(f"Failed deletions: {error_count} objects")
        print(f"Operation completed at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Replace these with your actual credentials and bucket information
    ACCOUNT_ID = "your_account_id"
    ACCESS_KEY_ID = "your_access_key_id"
    SECRET_ACCESS_KEY = "your_secret_access_key"
    BUCKET_NAME = "your_bucket_name"

    # Run the cleaning function
    clean_r2_storage(ACCOUNT_ID, ACCESS_KEY_ID, SECRET_ACCESS_KEY, BUCKET_NAME)
