from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

setup(
    name='confirma',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/gisce/confirma',
    license='MIT',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    description='Send Documents to ConFirma service',
    install_requires=INSTALL_REQUIRES
)
