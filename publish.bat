git add .
git commit -a -m %1
git push -u origin pelican
REM pelican content -o output -s pelicanconf.py
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout pelican
timeout /t 5
START chrome "http://m-zakeri.github.io"