# 20200515, WA_Hyperloop

## Laptop CMD

docker pull continuumio/anaconda2
docker run -it continuumio/anaconda2 bash

## Docker container

git clone https://github.com/wateraccounting/WA_Hyperloop.git
cp WA_Hyperloop/hyperloop_example.py /

apt-get update

apt-get install vim

### rpy2==2.8.0
apt-get install r-base
apt-get install r-base-dev

### CairoSVG==1.0.22
apt-get install libcairo2-dev
apt-get install libffi-dev

### GDAL, [install](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html)
apt-get install gdal-bin
apt-get install libgdal-dev

ls /usr/include
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal

ogrinfo --version
gdalinfo --version
>>GDAL 2.4.0, released 2018/12/14

>>pip install GDAL==<GDAL VERSION FROM OGRINFO>
pip install GDAL==2.4.0

### netCDF4
pip install netCDF4==1.5.3


### PyPis
pip install rpy2==2.8.0
pip install CairoSVG==1.0.22
pip install geopy==1.22.0

### Python
python hyperloop_example.py

