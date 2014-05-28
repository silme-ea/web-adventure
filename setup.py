from setuptools import setup, find_packages

setup(
    name='Web Adventure',
    version='0.0.1',
    url='https://github.com/silme-ea/web-adventure',
    license='BSD',
    author='Yuri Shakalov, Anton Al-Houry-Hanna',
    description='Web port of Collosal Cave adventure game',
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
