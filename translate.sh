#! /bin/sh
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/29 16:25:34.134764
#+ Editado:	2023/01/29 17:04:52.046750
# ------------------------------------------------------------------------------

add=0
update=0
compile=0

folder_i18n="media/i18n/"
filename="media"

while getopts "acul:" o; do
    case ${o} in
        a)
            add=1
            ;;
        u)
            update=1
            ;;
        l)
            language="$OPTARG"
            ;;
        c)
            compile=1
            ;;

xgettext -d media4 -o "$folder_i18n""$filename".pot $(find . -name "*.py")

if [[ "$add" -eq 1 ]]; then
    # copy the pot file to all language folder as a po one
    for folder in $(find "folder_i18n" -type d -name "*LC_MESSAGES"); do
        cp "$folder_i18n""$filename".pot "$folder"/"$filename".po
        #msgfmt "$folder"/"$filename".po -o "$folder"/"$filename".mo
    done
fi

if [[ "$update" -eq 1 ]]; then
    msgmerge --update "folder_i18n""$lang"/LC_MESSAGES/"$filename".po "$folder_i18n""$filename".pot
    #msgfmt "$folder_i18n""$lang"/LC_MESSAGES/"$filename".po -o "$folder_i18n""$lang"/LC_MESSAGES/"$filename".mo
fi

if [[ "$compile" -eq 1 ]]; then
    msgfmt "$folder_i18n""$lang"/LC_MESSAGES/"$filename".po -o "$folder_i18n""$lang"/LC_MESSAGES/"$filename".mo
fi
