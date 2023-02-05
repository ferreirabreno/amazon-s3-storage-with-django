# What is Amazon S3?

# What is Django?

Django is a high-level Python web framework that enables the rapid development of secure and maintainable websites. It follows the Model-View-Template (MVT) architectural pattern and provides a rich set of tools and libraries to simplify the development of dynamic web applications. Django comes with built-in features such as URL routing, template engine, ORM, and more, that help developers build complex web applications in less time and with less code. It also follows a strict security model and provides robust features for user authentication and authorization, making it an ideal choice for building secure web applications.

# What is Amazon S3?

Amazon S3 (Simple Storage Service) is a cloud-based object storage service provided by Amazon Web Services (AWS). It allows you to store, retrieve, and manage large amounts of data, such as images, videos, and other files, in the cloud. S3 provides high durability and availability, as well as scalability, making it a popular choice for storing and serving large amounts of data for websites and applications. S3 also offers various features such as versioning, access control, and data management, allowing you to easily manage and control your data. S3 is accessible through APIs and can be used through the AWS Management Console, AWS SDKs, and the AWS CLI, making it easy to integrate with other AWS services and third-party applications.

## Configuring django project step-by-step
1. Install Django:
```shell
pip3 install django
```

2. Create a new Django project:
```shell
django-admin startproject storage_in_cloud
```

3. Navigate to the project directory:
```shell
cd storage_in_cloud
```

4. Install the required packages:
```shell
pip3 install boto3
pip3 install django-storages
```

5. Create a new Django app:
```shell
python3 manage.py startapp amazon_s3_poc
```

6. Add `storages` to your INSTALLED_APPS in settings.py:
```py
INSTALLED_APPS = [    ...    'storages']
```

7. Create a storage backend in settings.py:
```py
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

8. Configure AWS credentials:
```txt
AWS_ACCESS_KEY_ID = <YOUR_ACCESS_KEY_ID>
AWS_SECRET_ACCESS_KEY = <YOUR_SECRET_ACCESS_KEY>
AWS_STORAGE_BUCKET_NAME = <YOUR_BUCKET_NAME>
AWS_S3_REGION_NAME = <YOUR_REGION_NAME>
```

# TODO

- [ ] Configure django project
- [ ] Configure django application
- [ ] Install AWS python SDK Boto3 dependency
- [ ] Install django storages dependency
- [ ] Create a docker-compose.yml with localstack
- [ ] Make an view for receive file and save
