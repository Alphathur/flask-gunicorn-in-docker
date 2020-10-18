from setuptools import setup

setup(
    name='DataAPI',
    version='1.0',
    description="data access api for yyhy card",
    author="CMBNetworkers",
    packages=['data_service'],
    include_package_data=True,
    install_requires=[
        'flask>=1.0',
        'py2neo>=4.2.0',
        'elasticsearch>=6.3.1' 
    ],
    zip_safe=False,
    entry_points={"console_scripts":["data_service=data_service.__main__:main"]},
)

