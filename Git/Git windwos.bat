@Echo off
echo Inicinado
echo ##############################################
echo Baixando arquivos do Git
git pull
echo ##############################################
echo Adicionando arquivo - git add *
git add *
echo ##############################################
set /p comit=Digite o texto do seu commit: 
git commit -m '%comit%'
echo ##############################################
echo enviando arquivo para o Github
git push
echo ##############################################
echo Fim!
pause