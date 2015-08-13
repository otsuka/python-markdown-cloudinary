# vim:fileencoding=utf-8
from unittest import TestCase
import cloudinary
import markdown
from mdx_cloudinary.extension import CloudinaryImageExtension
import logging

logging.basicConfig(level=logging.DEBUG)


class CloudinaryImageExtensionTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cloudinary.config(
            cloud_name="demo",
        )

    def test_md_cloudinary_image(self):
        text = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" %}'
        expected = '<p>' \
                   '<img ' \
                   'src="http://res.cloudinary.com/demo/image/upload/b9sulehz2ehiqe9r6xdq.jpg"/>' \
                   '</p>'

        html = markdown.markdown(text, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

    def test_md_cloudinary_image_with_single_option(self):
        text = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" width="auto" %}'
        expected = '<p>' \
                   '<img ' \
                   'class="cld-responsive" ' \
                   'data-src="http://res.cloudinary.com/demo/image/upload/w_auto/b9sulehz2ehiqe9r6xdq.jpg"/>' \
                   '</p>'

        html = markdown.markdown(text, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

    def test_md_cloudinary_image_with_multiple_options(self):
        text = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" width="auto" dpr="auto" %}'
        expected = '<p>' \
                   '<img ' \
                   'class="cld-responsive" ' \
                   'data-src="http://res.cloudinary.com/demo/image/upload/dpr_auto,w_auto/b9sulehz2ehiqe9r6xdq.jpg"/>' \
                   '</p>'

        html = markdown.markdown(text, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

    def test_md_cloudinary_image_with_format(self):
        text = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" format="png" %}'
        expected = '<p>' \
                   '<img ' \
                   'src="http://res.cloudinary.com/demo/image/upload/b9sulehz2ehiqe9r6xdq.png"/>' \
                   '</p>'

        html = markdown.markdown(text, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

    def test_md_cloudinary_image_secure(self):
        text1 = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" secure="True" %}'
        text2 = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" secure="true" %}'
        text3 = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" secure="1" %}'
        text4 = '{% cloudinary "b9sulehz2ehiqe9r6xdq.jpg" secure=True %}'
        expected = '<p>' \
                   '<img ' \
                   'src="https://res.cloudinary.com/demo/image/upload/b9sulehz2ehiqe9r6xdq.jpg"/>' \
                   '</p>'

        html = markdown.markdown(text1, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

        html = markdown.markdown(text2, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

        html = markdown.markdown(text3, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))

        html = markdown.markdown(text4, extensions=[CloudinaryImageExtension()])
        self.assertEqual(expected, html.replace('\n', ''))
