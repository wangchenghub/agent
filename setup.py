import setuptools

requirements = [
    "gunicorn==20.1.0",
    "flask==2.0.1",
    "gevent==21.1.2"
    "flask-restful==0.3.9",

]


setuptools.setup(
    name="agent",
    version="1.0",
    author="admin",
    author_email="cheng.wang.vaddsoft.com",
    description="Dsm Agent Pre",
    packages=setuptools.find_packages(where='.', exclude=(), include=('*',)),
    py_modules=["main", "gunicorn"],
    include_package_data=True,
    install_requires=requirements
)
