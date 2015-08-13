# vim:fileencoding=utf-8

from setuptools import setup, find_packages

setup(name='python-markdown-cloudinary',
      version='1.0.0',
      description='Markdown extension to display and manipulate images on Cloudinary.',
      url='https://github.com/otsuka/python-markdown-cloudinary',
      license='BSD License',
      author='Tomohiro Otsuka',
      author_email='t.otsuka@gmail.com',
      packages=find_packages(
          exclude=['*tests*', 'testproj']
      ),
      package_data={
      },
      install_requires=['cloudinary', 'Markdown'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Filters',
          'Topic :: Text Processing :: Markup :: HTML',
      ],
      keywords=['python', 'markdown', 'cloudinary'],
      )
