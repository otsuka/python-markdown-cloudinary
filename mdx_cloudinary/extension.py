# vim:fileencoding=utf-8
import logging
import re
import cloudinary

from markdown import Extension
from markdown.inlinepatterns import Pattern

logger = logging.getLogger(__name__)

IMG_RE = r'{%\s+cloudinary ' \
         r'("|\')(?P<public_id>[a-zA-Z0-9]+?\.(\w{3}))("|\')' \
         r'(?P<options>(\s+\w+?=("|\')?[a-zA-Z0-9_\-]+?("|\')?)*)' \
         r'\s+%}'


class CloudinaryImagePattern(Pattern):
    def handleMatch(self, m):
        public_id_with_ext = m.group('public_id')
        logger.debug("public_id: %s", public_id_with_ext)
        opt_str = m.group('options')
        logger.debug("opt_str: %s", opt_str)
        options = self._parse_options(opt_str)

        if 'format' in options:
            public_id_with_ext = self._strip_extension(public_id_with_ext)

        img_tag = cloudinary.CloudinaryImage(public_id_with_ext).image(**options)
        return self.markdown.htmlStash.store(img_tag)

    def _strip_extension(self, public_id_with_ext):
        return public_id_with_ext.split('.')[0]

    def _parse_options(self, opt_str):
        if not opt_str:
            return {}

        options = re.split(r'\s+', opt_str.strip())
        options = [opt for opt in options if opt]
        logger.debug("options: %s", options)
        d = {}
        for key, val in [opt.split('=') for opt in options]:
            val = val[1:-1]
            d[key] = val
        return d


class CloudinaryImageExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        cloudinary = CloudinaryImagePattern(IMG_RE, md)
        md.inlinePatterns['cloudinary'] = cloudinary
