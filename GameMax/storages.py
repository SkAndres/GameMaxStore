from storages.backends.s3boto3 import S3Boto3Storage


class MediaStore(S3Boto3Storage):
    location = 'static/media'
    file_overwrite = False


class JsStore(S3Boto3Storage):
    location = 'static/js/'
    file_overwrite = False

