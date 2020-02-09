#! /bin/bash

git config --global credential.helper cache;

echo "#################################################"
echo "#            Git Pull - Atualizando             #"
echo "#################################################"
echo
git pull;
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

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
echo "#       Adicionando arquivos - git add *        #"
echo "#################################################"
echo
git add *;
echo 
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

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
echo "#             Comitando Alterações              #"
echo "#             git commit -m 'texto'             #"
echo "#################################################"
echo
echo "Digite o texto do commit:"
read commit;
echo
git commit -m "$commit";
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

echo "#################################################"
echo "#              Subindo para a nuvem             #"
echo "#################################################"
echo
git push;
echo
echo "*************************************************"
echo “Aperte ENTER para continuar...... ”
read pause;

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


