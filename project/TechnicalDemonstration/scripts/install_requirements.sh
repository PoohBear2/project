# Note: this is for container
# (https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch)
# Changes:
#   - remove pytorch installation as it should come with containers
#   - use pip only for package installement
#   - additional packages that could be missing in container 

pip install pandas
pip install matplotlib
pip install scikit-learn
pip install scikit-image
pip install numpy
pip install imageio
pip install pillow
pip install opencv-python
pip install openslide-python
pip install Jinja2
pip install imagecodecs
