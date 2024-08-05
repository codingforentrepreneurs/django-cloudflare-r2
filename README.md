# Django x Cloudflare R2 with Django Storages
Example project using Cloudflare R2 for Django Static Files and Media Uploads


## TLDR:


### 1. Create a bucket on Cloudflare R2



### 2. Add `.env`
As you can see on this repo, my django project is at `django-r2/src/` and my `.env` file is at `django-r2/.env`. Ensure that `.env` is one level above the root of your Django project (e.g. `src`) otherwise you need to customize how `python-decouple` loads the `.env` file.

```bash
CLOUDFLARE_R2_BUCKET=""
CLOUDFLARE_R2_BUCKET_ENDPOINT=""
CLOUDFLARE_R2_ACCESS_KEY=""
CLOUDFLARE_R2_SECRET_KEY=""
```
> These all come directly from Cloudflare R2 under "Manage R2 API Tokens"

### 3. Install requirements (in addition to Django)
```bash
pip install "django-storages[s3]" python-decouple
```
> If you replace `python-decouple`, you need a way to load `.env` files.


### Update `settings.py` for Storages

```python
try:
    from decouple import config
except ImportError:
    import os
    config = os.environ.get

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name": config("CLOUDFLARE_R2_BUCKET"),
    "default_acl": "public-read",  # or "private"
    "signature_version": "s3v4",
    "endpoint_url": config("CLOUDFLARE_R2_BUCKET_ENDPOINT"),
    "access_key": config("CLOUDFLARE_R2_ACCESS_KEY"),
    "secret_key": config("CLOUDFLARE_R2_SECRET_KEY"),
}

# Introduced in Django 4.2
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
}
```

Review the [Storages](https://docs.djangoproject.com/en/5.0/ref/settings/#storages) section of the Django docs if the 👆 looks new to you. 

## In depth setup? Wath the [tutorial](https://youtu.be/VU3MAN1gs1s).
