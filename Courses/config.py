from django.template.defaultfilters import slugify


def generate_slug(text):
    new_slug = slugify(text)
    return new_slug
