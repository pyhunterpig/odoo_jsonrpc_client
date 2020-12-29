from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='odoo_jsonrpc_client',
    version=version,
    description="Another python json-rpc client",
    author="Pyhunterpig",
    license='LGPL v3',
    author_email="hunterpig75@qq.com",
    python_requires='>=3.6',
    packages=['odooClient'],
    platforms = 'any',
    install_requires = [
       'requests>=2.0',
    ],
    url = "https://github.com/pyhunterpig/odoo_jsonrpc_client",
)