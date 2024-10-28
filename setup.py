from setuptools import setup, find_packages

setup(
    name='confirma',
    version='0.2.3',
    packages=find_packages(),
    url='https://github.com/gisce/confirma',
    license='MIT',
    author='GISCE-TI, S.L.',
    long_description='''Send Documents to ConFirma service package''',
    author_email='devel@gisce.net',
    description='Send Documents to ConFirma service',
    install_requires=[
        'requests'
    ],
)
