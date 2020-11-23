#!/usr/bin/env bash
# Script to autogenerate screenshots for x3270.nice by soldier of fortran
# license gpl3
# requires: x3270, xfce4-screenshooter
# Download Xresources from https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/Xresources
# Then use this USSTABLE: https://github.com/mainframed/usstable/blob/master/demo_screen.jcl

############
# Config Options
SLEEPY=1            # How long to wait to take screenshot
README=../README.MD # README location
pro=~/.x3270pro     #.x3270pro file for x3270

############
# Arguments
echo "[+] Xresources folder:" $1 # e.g. ~/iTerm2-Color-Schemes/tree/master/Xresources
echo "[+] Output folder    :" $2 # e.g. ../schemes
echo "[+] Server string    :" $3 # e.g. L:mainframed:992
echo "[+] Screenshot folder:" $4 # e.g. ./

############
# Let's go

if test -f "$pro"; then
    echo "[+] Backing up current x3270pro file to ~/.x3270pro_backup"
    mv $pro "$pro"_backup
fi

if test -f $README; then
    rm $README
fi

cat << 'EOF' > $README
# x3270 themes!

No longer does your x3270 screen need to use the default colors that come with it! This repo contains all the themes from terminal.sexy in `.x3270pro` format, *over 157 themes!* Take your favorite theme and put it in your `.x3270pro` file: `cat schemes/<x3270pro> >> ~/.x3270pro`

## Make Your Own

Don't like the themes included here? Just go to [terminal.sexy](http://terminal.sexy) or [https://ciembor.github.io/4bit/#](https://ciembor.github.io/4bit/#) pick your favorite colors and save it as an `.Xresources` file, then convert it to x3270pro format with `x3270_pro_generator.py <.Xresources file> >> ~/.x3270pro`

## Color Schemes

These themes have been converted using this script from https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/Xresources
EOF


for i in $1/*
do
    echo "[+] Processing : $i"
    f=$(basename "$i")
    echo "! model  (-model)" > $pro
    echo "x3270.model: 2" >> $pro
    echo "x3270.scrollBar:	false" >> $pro
    #echo "[+] Theme name :" $f
    python3 ../x3270.nice.py "$i" > $2/"$f".x3270pro
    cat $2/"$f".x3270pro >> $pro
    x3270 -title "$f" $3&
    last_pid=$!
    sleep $SLEEPY
    echo "" >> $README
    echo "### $f" >> $README
    echo "" >> $README
    echo "![$f](./screenshots/${f// /%20}.png?raw=true)" >> $README
    xfce4-screenshooter -w -s $4/"$f".png
    disown $last_pid
    kill -KILL $last_pid

done

if test -f "$pro"_backup; then
    echo "[+] Restoring x3270pro file to ~/.x3270pro"
    mv "$pro"_backup $pro
fi

echo "[+] Done"