from setuptools import setup
import os

def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read();

setup(
        name = 'ScreenShot',
        version = '0.0.1',
        description = 'ScreenShot',
        author = 'Janarthanan Rasakanthan',
        author_email = 'Janarthanan.Rasakanthan@perkinelmer.com',
        include_package_data=True,
        packages = ['ScreenShot'],
        install_requires=[
            'Desktopmagic>=14.3.11',
            'Pillow>=3.4.2',
            'pypiwin32>=219',
            'ScreenShot>=0.0.1',
            'ParseTime>=0.0.1',
        ],
        zip_safe = False,
    )


