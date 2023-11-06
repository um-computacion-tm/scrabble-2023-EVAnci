#!bin/bash

docker_status=$(systemctl status docker | awk 'NR==3 {print $2}')
if [ "$docker_status" = "inactive" ]; then
	echo "El servicio docker está inactivo. Activándolo..."
	systemctl start docker
fi

docker_image="scrabble"               
if [[ "$(docker images -q $docker_image 2> /dev/null)" == "" ]]; then
  echo "La imagen $docker_image no está presente. Compilándola..."
  docker build -t $docker_image .
else
  echo "La imagen $docker_image ya está compilada."
fi

docker run -it --name scrabble -p 5000:5000 $docker_image:latest