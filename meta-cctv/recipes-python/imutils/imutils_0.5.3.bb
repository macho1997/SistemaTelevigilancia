# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

SUMMARY = "A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, displaying Matplotlib images, sorting contours, detecting edges, and much more easier with OpenCV and both Python 2.7 and Python 3."
HOMEPAGE = "https://github.com/jrosebr1/imutils"
# Unable to find any files that looked like license statements. Check the accompanying
# documentation and source headers and set LICENSE and LIC_FILES_CHKSUM accordingly.
#
# NOTE: LICENSE is being set to "CLOSED" to allow you to at least start building - if
# this is not accurate with respect to the licensing of the software being built (it
# will not be in most cases) you must specify the correct value before using this
# recipe for anything other than initial testing/development!
LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

SRC_URI = "https://files.pythonhosted.org/packages/b5/94/46dcae8c061e28be31bcaa55c560cb30ee9403c9a4bb2659768ec1b9eb7d/imutils-${PV}.tar.gz"
SRC_URI[md5sum] = "8c2a1cbf774f35fbb9dffd26df0c4bff"
SRC_URI[sha256sum] = "857af6169d90e4a0a814130b9b107f5d611150ce440107e1c1233521c6fb1e2b"

inherit setuptools3 pypi distutils3

# WARNING: the following rdepends are determined through basic analysis of the
# python sources, and might not be 100% accurate.
RDEPENDS_${PN} += "python3-core"

# WARNING: We were unable to map the following python package/module
# dependencies to the bitbake packages which include them:
#    Queue
#    __future__
#    argparse
#    base64
#    collections
#    cv2
#    datetime
#    json
#    numpy
#    operator
#    os
#    picamera
#    picamera.array
#    queue
#    re
#    scipy.spatial
#    threading
#    urllib
#    urllib.request
#    uuid
#    warnings


