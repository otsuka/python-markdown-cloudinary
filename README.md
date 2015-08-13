# Markdown extension for Cloudinary

This is a 3rd party extension for [Python Markdown library](https://pythonhosted.org/Markdown/).<br>
Enabling this extension, you can generate `<img>` tags that display images uploaded on [Cloudinary](http://cloudinary.com/).

## Syntax

[The cloudinary template tag](http://cloudinary.com/documentation/django_image_manipulation#template_tags) can be used in markdown text.

###### Markdown

```md
{% cloudinary "sample.jpg" %}
```

###### HTML

```html
<img src="http://res.cloudinary.com/demo/image/upload/sample.jpg"/>
```

Transformation options are supported. Quotations around number value are necessary.

###### Markdown

```md
{% cloudinary "sample.jpg" width="100" height="150" crop="fill" %}
```

###### HTML

```html
<img src="http://res.cloudinary.com/otsuka/image/upload/c_fill,h_150,w_100/sample.jpg" width="100" height="150"/>
```

The given options are directly passed to [CloudinaryImage.image()](http://cloudinary.com/documentation/django_image_manipulation#display_images) method. 
The extension does not check given options are valid or not.

## Installation

You can install the extesion and its dependencies via pip.

```sh
pip install python-markdown-extesion
```

## Usage

Python code to convert markdown text to HTML text using this extension.

```py
import cloudinary
import markdown
from mdx_cloudinary.extension import CloudinaryImageExtension

cloudinary.config(
    cloud_name="demo"
)

markdown_text = '{% cloudinary "sample.jpg" %}'

html = markdown.markdown(markdown_text, extensions=[CloudinaryImageExtension()])
```

### Django Template Tag

If you need a Django template filter to convert markdown text to HTML, the template tag code is as follows:

```py
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown
from mdx_cloudinary.extension import CloudinaryImageExtension

register = template.Library()

md = markdown.Markdown(extensions=[CloudinaryImageExtension()])

@register.filter()
@stringfilter
def md2html(value):
    html = md.convert(value)
    return mark_safe(html)
```

Loading the template tag, you can use `md2html` filter in your template.

```
{{ markdown_text_variable|md2html }}
```

Note: Your cloud name must be configured in settings.py or via environment variable.<br>
See http://cloudinary.com/documentation/django_integration#configuration

