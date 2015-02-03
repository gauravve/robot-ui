from setuptools import setup

setup(
    name='robot-ui',
    version='0.1',
    author='Gaurav Verma',
    author_email='to.gaurav.verma@gmail.com',
    url='https://bitbucket.org/gauravve/robot-ui',
    keywords='robotframework',
    license='Apache License 2.0',
    description='Web UI for Robot Framework test reports',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['django==1.7.3',
                      'djangorestframework',
                      'django-rest-swagger',
                      'gunicorn'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Intended Audience :: Testers, BA, Developers",
    ],
    scripts=[],
)