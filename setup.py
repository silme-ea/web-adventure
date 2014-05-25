from setuptools import setup, find_packages

setup(
    name='filmtemecula',
    version='0.0.1',
    url='https://bitbucket.org/joes/',
    license='BSD',
    author='Serge S. Koval, Yuri Shakalov',
    description='Film Temecula site',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=open('requirements.txt').readlines(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
