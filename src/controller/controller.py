#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/01/11 18:38:56.570892
#+ Editado:	2023/03/18 12:45:31.509257
# ------------------------------------------------------------------------------
import sys
import logging
from datetime import datetime
from threading import Thread

from src.model import iModel
from src.view import iView

from src.service import MemberCountService, FileInfoService

from src.model.dao import FileDao, TrackDao, TrackLanguageDao
from src.model.entity import ShareSite, ShareSiteSubs, Platform
# ------------------------------------------------------------------------------
class Controller:
    def __init__(self, model: iModel, view: iView):
        self.model = model
        self.view = view
        self.view.controller = self
        self.view.strategy.controller = self

        self.update_member_count(show_user=False)

        self.view.start()


    def save(self) -> None:
        logging.info(_('Starting the saving process'))
        self.view.save()
        self.model.save_db()
        logging.info(_('The saving process was finished'))

    def exit_no_save(self) -> None:
        self.__exit(False)

    def exit_save(self) -> None:
        self.__exit(True)

    def __exit(self, commit: bool) -> None:
        logging.info(_('Starting the exit process'))
        self.model.disconnect_db(commit= commit)
        self.view.exit()
        logging.info(_('Exiting the program'))
        sys.exit()

    def update_member_count(self, show_user: bool = True) -> None:
        logging.info(_('Starting the "Update Member Count" process'))
        Thread(target=self.__update_member_count_aux).start()
        if show_user: self.view.update_member_count()
        logging.info(_('The "Update Member Count" process was finished'))

    def __update_member_count_aux(self) -> None:
        logging.info(_('Starting the thread for the "Update Member Count"'))
        share_sites = self.model.get_all(ShareSite.table_name)
        if len(share_sites) > 0:
            chat_ids = {}
            platform_share_sites = {}
            platforms = [ele.name.lower() for ele in self.model.get_all(Platform.table_name)]
            for platform in platforms:
                chat_ids[platform] = []
                platform_share_sites[platform] = []

            # sort the ids by platform
            for ele in share_sites:
                if ele.in_platform_id is not None:
                    chat_ids[ele.platform.name.lower()].append(ele.in_platform_id)
                    platform_share_sites[ele.platform.name.lower()].append(ele)

            members = MemberCountService().run(chat_ids.copy())

            for share_site, sub_num in zip(*platform_share_sites.values(), *members.values()):
                ss = ShareSiteSubs(
                        share_site=share_site,
                        sub_num=sub_num,
                        added_ts=datetime.now().strftime("%Y-%m-%d")
                        )
                if sub_num and not self.model.exists(ss):
                    self.model.insert(ss)
        else:
            logging.info(_('The member count was not updated since there \
                    are no ShareSites'))
        logging.info(_('Finishing the thread for the "Update Member Count"'))

    def add_type(self) -> None:
        logging.info(_('Starting the "Add Type" process'))
        self.model.insert(self.view.add_type())
        logging.info(_('The "Add Type" process was finished'))

    def add_status(self) -> None:
        logging.info(_('Starting the "Add Media Status" process'))
        self.model.insert(self.view.add_status())
        logging.info(_('The "Add Media Status" process was finished'))

    def add_media(self) -> None:
        logging.info(_('Starting the "Add Media" process'))
        self.model.insert(self.view.add_media())
        logging.info(_('The "Add Media" process was finished'))

    def add_group(self, id_media: int = None) -> None:
        logging.info(_('Starting the "Add Group" process'))
        self.model.insert(self.view.add_group(id_media))
        logging.info(_('The "Add Group" process was finished'))

    def add_issue(self) -> None:
        logging.info(_('Starting the "Add Media Issue" process'))
        self.model.insert(self.view.add_issue())
        logging.info(_('The "Add Media Issue" process was finished'))

    def add_platform(self) -> None:
        logging.info(_('Starting the "Add Platform" process'))
        self.model.insert(self.view.add_platform())
        logging.info(_('The "Add Platform" process was finished'))

    def add_sharesite(self) -> None:
        """
        """
        logging.info(_('Starting the "Add ShareSite" process'))
        self.model.insert(self.view.add_sharesite())
        logging.info(_('The "Add ShareSite" process was finished'))

    def add_warehouse(self) -> None:
        """
        """
        logging.info(_('Starting the "Add Warehouse" process'))
        self.model.insert(self.view.add_warehouse())
        logging.info(_('The "Add Warehouse" process was finished'))

    def add_file(self) -> None:
        """
        """
        logging.info(_('Starting the "Add File" process'))

        fis = FileInfoService(self.view.add_file())
        files_data = fis.run()

        for file_data in files_data:
            # file
            file_data.file=FileDao(model=self.model).save(file=file_data.file)
            # track
            for track, track_langs in file_data.tracks:
                track.file=file_data.file
                track=TrackDao(model=self.model).save(track=track)
                for lang in track_langs:
                    lang.track=track
                    TrackLanguageDao(model=self.model).save(track_language=lang)

        logging.info(_('The "Add File" process was finished'))

# ------------------------------------------------------------------------------
