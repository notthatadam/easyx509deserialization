from setuptools import setup

setup(
    name='easyx509deserialization',
    version='0.2.0',
    description='A simple front-end to call cryptography x509 functions',
    url='https://github.com/notthatadam/easyx509deserialization',
    author='Adam Peterson',
    author_email='adampeterson@gmail.com',
    license='GNU General Public License v3.0',
    packages=['easyx509deserialization'],
    install_requires=['cryptography>=3.4',
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
