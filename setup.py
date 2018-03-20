from setuptools import setup, find_packages

with open('README.MD',encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backup locally or to AWS S3',
    long_description=readme,
    author='Drew',
    author_email='ripa.andrew@gmail.com',
    install_requires=[],
    package=find_packages('src'),
    package_dir={'': 'src'}
)