#! /bin/bash
echo "#################################################"
echo "#    Verificando o estatus do Git - git status  #"
echo "#################################################"
echo
git status;
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

echo "#################################################"
echo "#            Git Pull - Atualizando             #"
echo "#################################################"
git pull;
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

echo
echo "#################################################"
echo "#   Verificando o estatus do Git - git status   #"
echo "#################################################"
echo
git status;
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

echo "#################################################"
echo "#                 FNALIZANDO!                   #"
echo "#################################################"
echo 
echo "*************************************************"
echo “Aperte ENTER para sair ”
read pause;


