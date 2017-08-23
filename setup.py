from setuptools import find_packages, setup

setup(
    name='todo_api',
    version='0.1',
    description='A ToDo List API built with Django Rest Framework',
    author='Michael Washburn Jr',
    author_email='michael@michaelwashburnjr.com',
    url='https://github.com/mdw7326/DjangoRestApiExample',
    packages=find_packages(),
    install_requires=[
        'Django==1.11.4',
        'djangorestframework==3.6.3',
        'pytz==2017.2',
    ]
)