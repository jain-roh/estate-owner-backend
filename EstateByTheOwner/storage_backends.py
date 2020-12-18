from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    location = 'private/property'
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False

class PrivateMediaStorage(S3Boto3Storage):
    location = 'private/property'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False

class PrivateMediaProfileStorage(S3Boto3Storage):
    location = 'private/property'
    default_acl = 'private'
    file_overwrite = True
    custom_domain = False

class ThumbnailStorage(S3Boto3Storage):
    location = 'private/thumbnail'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False