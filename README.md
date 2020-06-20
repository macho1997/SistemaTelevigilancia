# SistemaTelevigilancia
Proyecto 1 - Taller de Sistemas Embebidos

Dependencias

Para hacer uso de este repositorio se requiere seguir los siguientes pasos:

1. Clonar poky zeus: git clone -b zeus git://git.yoctoproject.org/poky
2. Clonar layer meta-raspberrypi: git clone -b zeus git://git.yoctoproject.org/meta-raspberrypi
3. Clonar el master de este repositorio en el mismo nivel que poky-zeus.
4. Ejecutar en terminal al mismo nivel de poke-zeus: source poky-zeus/oe-init-build-env SistemaTelevigilancia/build
5. Ejecutar: bitbake core-image-minimal

Consideraciones:
  Hacer las cambios correspondientes al archivo bblayer.bb para darle la dirección correspondiente de los layers.
