from setuptools import setup

setup(
        name='qrcode',
        version='0.0.1',
        keywords='Qrcode animated',
        description='Generator for Qr Codes.',
        author='umut',
        author_email='umutdrsn34@gmail.com',
        url='https://github.com/onur55-tr/Qrcode',
        download_url='https://github.com/onur55-tr/Qrcode',
        install_requires=[
            'image >= 1.5.33',
            'pyqrcode >= 1.2.1',
            'pypng >= 0.0.21'],
        packages=['qrcode'],
        license='GPLv3',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
            ],
        entry_points={
            'console_scripts': [
                'qrcode=qrcode:generate',
                ],
        },
        python_requires=">=3"
)
        
