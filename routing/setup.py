from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name="alerta-routing",
    version=version,
    description='Alerta routing rules for plugins',
    url='https://github.com/rosskouk/docker-image-alerta',
    license='Apache License 2.0',
    author='Ross Stewart',
    author_email='rosskouk@gmail.com',
    packages=find_packages(),
    py_modules=['routing'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.routing': [
          'rules = routing:rules'
        ]
    }
)