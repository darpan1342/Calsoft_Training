#!/bin/bash

echo "Git clone repo shell script"
read -p "Repo Links File name: " File

if [ ! -d "projects_cloned/" ]
then
mkdir projects_cloned
else
rm -rf projects_cloned
mkdir projects_cloned
fi
t=$(pwd)
t+="/$File"
cd projects_cloned
while read line; do
git clone $line
done <$t

rec=$(ls)
for i in `ls`; do 
cd $i
git branch practice
cd ..
done
