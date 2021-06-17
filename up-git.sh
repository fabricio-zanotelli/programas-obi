#! /bin/bash

clear
echo "*************************************"
echo " Subindo todas as alterações no GIT "
echo "*************************************"

echo " "
echo "Status GIT: "
echo " "
git status
echo " "
echo "Adding GIT: "
echo " "
git add .
echo " "
echo "GIT Commit: "
echo " "
git commit -m "New modification"
echo " "
echo "GIT PUSH: "
echo " "
git push


