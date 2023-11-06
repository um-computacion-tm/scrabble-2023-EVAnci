#!bin/bash

docker_status=$(systemctl status docker | awk 'NR==3 {print $2}')
if [ "$docker_status" = "inactive" ]; then
	echo "El servicio docker está inactivo. Activándolo..."
	systemctl start docker
fi

read -p "Realizó una instalación con el script play.sh? [Y/n]: " automated

if [ -z "$automated" ]; then
  automated="Y"
fi

if [[ "$automated" == "Y" || "$automated" == "y" ]]; then
  docker_image="scrabble"
  gost_name="scrabble"
else
  docker images
  read -p "Nombre de la imagen a eliminar: " docker_image
  docker ps -a
  read -p "Nombre de la ejecución del contenedor a eliminar: " ghost_name
fi

if [[ "$(docker images -q $docker_image 2> /dev/null)" == "" ]]; then
  echo "La imagen $docker_image no está presente."
else
  echo "Borrando la imagen $docker_image."
  docker rm scrabble && docker image rm scrabble
fi