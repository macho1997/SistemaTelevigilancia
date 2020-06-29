# Recipe created by recipetool
# This is the basis of a recipe and may need further editing in order to be fully functional.
# (Feel free to remove these comments when editing.)

SUMMARY = "Python Game Development"
HOMEPAGE = "https://www.pygame.org"
# WARNING: the following LICENSE and LIC_FILES_CHKSUM values are best guesses - it is
# your responsibility to verify that the values are complete and correct.
# NOTE: Original package / source metadata indicates license is: LGPL
#
# NOTE: multiple licenses have been detected; they have been separated with &
# in the LICENSE value for now since it is a reasonable assumption that all
# of the licenses apply. If instead there is a choice between the multiple
# licenses then you should change the value to separate the licenses with |
# instead of &. If there is any doubt, check the accompanying documentation
# to determine which situation is applicable.
LICENSE = "LGPLv2.1 & LGPL"
LIC_FILES_CHKSUM = "file://docs/LGPL;md5=7fbc338309ac38fefcd64b04bb903e34"

SRC_URI = "https://files.pythonhosted.org/packages/0f/9c/78626be04e193c0624842090fe5555b3805c050dfaa81c8094d6441db2be/pygame-${PV}.tar.gz"
SRC_URI[md5sum] = "36f8817874f9e63acdf12914340b60e9"
SRC_URI[sha256sum] = "301c6428c0880ecd4a9e3951b80e539c33863b6ff356a443db1758de4f297957"

inherit setuptools3

# WARNING: the following rdepends are determined through basic analysis of the
# python sources, and might not be 100% accurate.
RDEPENDS_${PN} += "python3-core"


