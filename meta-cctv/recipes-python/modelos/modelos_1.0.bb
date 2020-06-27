DESCRIPTION = "Modelos entrenados"
SECTION = "cctv"

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/GPL-2.0;md5=801f80980d171dd6425610833a22dbe6"

SRCREV = "${AUTOREV}"
SRC_URI = "file://MobileNetSSD_deploy.caffemodel \
           file://MobileNetSSD_deploy.prototxt.txt"
		

S = "${WORKDIR}"

inherit allarch

do_compile() {
}

do_install() {
        install -d ${D}${sbindir}
        install -d ${D}${sbindir}
        install -m 0755 MobileNetSSD_deploy.caffemodel ${D}${sbindir}
        install -m 0755 MobileNetSSD_deploy.prototxt.txt ${D}${sbindir}
}
