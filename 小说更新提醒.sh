#!/bin/bash
export LANG=zh_CN.UTF-8
YUANZUN="~E~C~J~O说~[~V~U"
SHENXU="~\~_~O说~[~V~U"
URL1=`curl https://www.xsbiquge.com/78_78513/ | grep -io "<a href=\".*\" target=\"_blank\">" | grep -io "\/.*html"`
URL2=`curl https://www.xsbiquge.com/74_74821/ | grep -io "<a href=\".*\" target=\"_blank\">" | grep -io "\/.*html"`

BIQUGE="https://www.xsbiquge.com"

HIS_Y=`sed -n '1p' log.txt`
HIS_S=`sed -n '2p' log.txt`
FILE=/root/body.html
BODY=""
send(){
        dos2unix -k -f $FILE
        s-nail -s $1 718358058@qq.com < $FILE
}
get_Update()
{
        if [ -z "$HIS_Y" ];then
                sed -i "1c ${URL1}" log.txt
        else
                if [ "$HIS_Y" != "$URL1" ];then
                        sed -i "1c ${URL1}" log.txt
                        echo -n `curl "$BIQUGE$URL1" | grep -io "<div id=\"content\">.*</div>" | tr -d "[:alnum:][:cntrl:][:graph:]"` > body.html
                        send $YUANZUN
                fi
        fi
        if [ -z "$HIS_S" ];then
                sed -i "2c ${URL2}" log.txt
        else
                if [ "$HIS_S" != "$URL2" ];then
                        rm body.html
                        sed -i "2c ${URL2}" log.txt
                        curl "$BIQUGE$URL2" | grep -io "<div id=\"content\">.*</div>" | tr -d "&;<>/abcdefghijklmnopqrstuvwxyz=" >> body.html
                        send $SHENXU
                fi
        fi
}

get_Update
