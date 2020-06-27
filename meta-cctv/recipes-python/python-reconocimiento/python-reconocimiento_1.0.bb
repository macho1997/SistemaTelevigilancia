DESCRIPTION = "Aplicacion de reconocimiento facial con red neuronal entrenada"
SECTION = "cctv"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://setup.py \
           file://python-reconocimiento.py \
           file://__init__.py"

S = "${WORKDIR}"

inherit setuptools3

DEPENDS += "python3-setuptools-native"

#RDEPENDS_${PN} += "python3-core"


do_install_append () {
    install -d ${D}${bindir}
    install -m 0755 python-reconocimiento.py ${D}${bindir}
}
