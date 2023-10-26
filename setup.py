#!/usr/bin/env python
from setuptools import setup



setup(
    name='cms',
    version=__version__,
    author='Django CMS Association and contributors',
    author_email='info@django-cms.org',
    url='https://www.django-cms.org/',
    license='BSD-3-Clause',
    description='Lean enterprise content management powered by Django.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    packages=find_packages(exclude=['project', 'project.*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='runtests.main',
)

