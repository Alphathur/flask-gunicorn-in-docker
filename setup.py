from setuptools import setup

setup(
    name='DataAPI',
    version='1.0',
    description="A Restful application using flask and fetching data from mysql",
    author="Alphathur",
    packages=['service', 'common', 'config'],
    include_package_data=True,
    install_requires=[
        'flask>=1.0'
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["data-api=service:main"]},
)
