#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/04 23:17:25.456829
#+ Editado:	2023/01/04 23:55:27.468994
# ------------------------------------------------------------------------------
from src.dtos.MediaDTO import MediaDTO
from src.dtos.MediaNomesDTO import MediaNomesDTO
# ------------------------------------------------------------------------------
media = MediaDTO(
        nome = 'Proba',
        ano_ini = 2000,
        ano_fin = 2000,
        id_tipo = 'serie',
        id_situacion = 'rematada',
)
print(media)
media.nome = 'cambio'
print(media)
media_nomes = MediaNomesDTO(nome='a', id_media=1)
print(media_nomes)
# ------------------------------------------------------------------------------
