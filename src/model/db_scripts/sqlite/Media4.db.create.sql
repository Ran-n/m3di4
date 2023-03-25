BEGIN TRANSACTION;
/*** TABLES ***/
/** Without FK **/
CREATE TABLE IF NOT EXISTS "Encoder" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Encoder_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Extension" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"name"				TEXT NOT NULL UNIQUE,
	"format_name"		TEXT NOT NULL UNIQUE,
	"format_name_long"	TEXT NOT NULL UNIQUE,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Extension_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Folder" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"path"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Folder_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Type" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"groupable"		INTEGER,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Type_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Code" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Code_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Status" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Status_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "App" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "App_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Country" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"nation"		INTEGER,
	"state"			INTEGER,
	"kingdom"		INTEGER,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Country_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/***/





/** With FK **/
CREATE TABLE IF NOT EXISTS "Platform" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"acronym"		TEXT,
	"name"			TEXT NOT NULL UNIQUE,
	"name_long"		TEXT UNIQUE,
	"link"			TEXT UNIQUE,
	"id_type"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Platform_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Language" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"id_language"	INTEGER,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Language_FK1" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Language_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodeName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"code_id"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodeName_FK1" FOREIGN KEY("code_id") REFERENCES "Code"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Version_NK" UNIQUE("name", "code_id"),
	CONSTRAINT "CodeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Version" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"id_app"			INTEGER NOT NULL,
	"number"			TEXT NOT NULL,
	"name"				TEXT,
	"num_bit_processor" INTEGER,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Version_FK1" FOREIGN KEY("id_app") REFERENCES "App"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Version_NK" UNIQUE("id_app", "number"),
	CONSTRAINT "Version_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Codec" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"name_long"		TEXT UNIQUE,
	"id_type"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Codec_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Codec_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSite" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"in_platform_id"	TEXT,
	"name"				TEXT NOT NULL,
	"private"			INTEGER,
	"link"				TEXT NOT NULL UNIQUE,
	"id_type"			INTEGER NOT NULL,
	"id_platform"		INTEGER,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSite_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_FK2" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Warehouse" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"size"			INTEGER,
	"filled"		INTEGER,
	"content"		TEXT,
	"id_type"		INTEGER NOT NULL,
	"health"		TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Warehouse_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Warehouse_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "LanguageCode" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"id_code"		INTEGER NOT NULL,
	"codename"		TEXT NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageCode_FK1" FOREIGN KEY("id_code") REFERENCES "Code"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageCode_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageCode_NK" UNIQUE("id_language", "id_code", "codename"),
	CONSTRAINT "LanguageCode_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Media" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"date_start"	TEXT,
	"date_end"		TEXT,
	"id_type"		INTEGER NOT NULL,
	"id_status"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Media_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Media_FK2" FOREIGN KEY("id_status") REFERENCES "Status"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Media_NK" UNIQUE("name", "date_start", "id_type"),
	CONSTRAINT "Media_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Group_" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"number"		INTEGER NOT NULL,
	"name"			TEXT,
	"date_start"	TEXT,
	"date_end"		TEXT,
	"id_media"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Group_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Group_NK" UNIQUE("number", "id_media"),
	CONSTRAINT "Group_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Issue" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"position"			INTEGER NOT NULL,
	"name"				TEXT,
	"date"				TEXT,
	"id_media"			INTEGER NOT NULL,
	"id_group"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Issue_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Issue_FK2" FOREIGN KEY("id_group") REFERENCES "Group_"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Issue_NK" UNIQUE("id_media", "id_group", "position"),
	CONSTRAINT "Issue_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Poster" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"id_extension"	INTEGER NOT NULL,
	"id_media"		INTEGER,
	"id_group"		INTEGER,
	"id_issue"		INTEGER,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Poster_NN1" CHECK (("id_media" IS NOT NULL AND "id_group" IS NULL AND "id_issue" IS NULL) OR ("id_media" IS NULL AND "id_group" IS NOT NULL AND "id_issue" IS NULL) OR ("id_media" IS NULL AND "id_group" IS NULL AND "id_issue" IS NOT NULL)),
	CONSTRAINT "Poster_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Poster_FK2" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Poster_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "File" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"hash"				TEXT NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_extension"		INTEGER NOT NULL,
	"id_warehouse"		INTEGER NOT NULL,
	"id_folder"			INTEGER NOT NULL,
	"id_media"			INTEGER,
	"id_issue"			INTEGER,
	"title"				TEXT,
	"nb_streams"		INTEGER,
	"nb_programs"		INTEGER,
	"start"				REAL,
	"duration"			REAL,
	"size"				INTEGER,
	"bit_rate"			INTEGER,
	"probe_score"		INTEGER,
	"creation_ts"		TEXT,
	"id_version"		INTEGER,
	"id_encoder"		INTEGER,
	"original_name"		TEXT,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "File_NN1" CHECK (("id_media" IS NOT NULL AND "id_issue" IS NULL) OR ("id_media" IS NULL AND "id_issue" IS NOT NULL)),
	CONSTRAINT "File_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK2" FOREIGN KEY("id_warehouse") REFERENCES "Warehouse"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK3" FOREIGN KEY("id_folder") REFERENCES "Folder"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK4" FOREIGN KEY("id_issue") REFERENCES "Issue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK5" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK6" FOREIGN KEY("id_encoder") REFERENCES "Encoder"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK7" FOREIGN KEY("id_version") REFERENCES "Version"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_NK" UNIQUE("name", "id_extension", "id_folder", "id_warehouse"),
	CONSTRAINT "File_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Track" (
	"id"					INTEGER NOT NULL UNIQUE,
	"active"				INTEGER NOT NULL,
	"id_file"				INTEGER NOT NULL,
	"id_codec"				INTEGER NOT NULL,
	"index_"				INTEGER NOT NULL,
	"title"					TEXT,
	"profile"				TEXT,
	"quality"				TEXT,
	"width"					INTEGER,
	"height"				INTEGER,
	"coded_width"			INTEGER,
	"coded_height"			INTEGER,
	"closed_captions"		INTEGER,
	"film_grain"			INTEGER,
	"has_b_frames"			INTEGER,
	"sample_aspect_ratio"	TEXT,
	"display_aspect_ratio"	TEXT,
	"pixel_format"			TEXT,
	"level"					INTEGER,
	"color"					INTEGER,
	"color_range"			TEXT,
	"color_space"			TEXT,
	"color_transfer"		TEXT,
	"color_primaries"		TEXT,
	"chroma_location"		TEXT,
	"field_order"			TEXT,
	"refs"					INTEGER,
	"is_avc"				INTEGER,
	"nal_length_size"		INTEGER,
	"r_frame_rate"			REAL,
	"avg_frame_rate"		REAL,
	"time_base"				REAL,
	"start_pts"				INTEGER,
	"bits_per_raw_sample"	INTEGER,
	"bits_per_sample"		INTEGER,
	"extradata_size"		INTEGER,
	"default_"				INTEGER,
	"dub"					INTEGER,
	"original"				INTEGER,
	"comment"				INTEGER,
	"lyrics"				INTEGER,
	"karaoke"				INTEGER,
	"forced"				INTEGER,
	"hearing_impaired"		INTEGER,
	"visual_impaired"		INTEGER,
	"clean_effects"			INTEGER,
	"attached_pic"			INTEGER,
	"timed_thumbnails"		INTEGER,
	"captions"				INTEGER,
	"descriptions"			INTEGER,
	"metadata"				INTEGER,
	"dependent"				INTEGER,
	"still_image"			INTEGER,
	"start"					REAL,
	"duration"				REAL,
	"size"					INTEGER,
	"bit_rate"				INTEGER,
	"sample_rate"			INTEGER,
	"sample_format"			TEXT,
	"channels"				INTEGER,
	"channel_layout"		TEXT,
	"bps"					INTEGER,
	"frame_number"			INTEGER,
	"dmix_mode"				INTEGER,
	"text_subtitle"			INTEGER,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Track_FK1" FOREIGN KEY("id_file") REFERENCES "File"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Track_FK2" FOREIGN KEY("id_codec") REFERENCES "Codec"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Track_NK" UNIQUE("id_file", "index_"),
	CONSTRAINT "Track_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TrackLanguage" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"id_track"		INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "TrackLanguage_FK1" FOREIGN KEY("id_track") REFERENCES "Track"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TrackLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TrackLanguage_NK" UNIQUE("id_track", "id_language"),
	CONSTRAINT "TrackLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteSubs" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_share_site"	INTEGER NOT NULL,
	"sub_num"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteSubs_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteSubs_NK" UNIQUE("id_share_site", "sub_num", "added_ts"),
	CONSTRAINT "ShareSiteSubs_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FileShareSite" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"id_file"		INTEGER NOT NULL,
	"id_share_site"	INTEGER NOT NULL,
	"link"			TEXT NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "FileShareSite_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileShareSite_FK2" FOREIGN KEY("id_file") REFERENCES "File"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileShareSite_NK" UNIQUE("id_file", "id_share_site", "link"),
	CONSTRAINT "FileShareSite_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaPlatform" (
	"id"				INTEGER UNIQUE NOT NULL,
	"active"			INTEGER NOT NULL,
	"id_media"			INTEGER NOT NULL,
	"id_platform"		INTEGER NOT NULL,
	"in_platform_id"	INTEGER,
	"link"				TEXT NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaPlatform_FK1" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaPlatform_FK2" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaPlatform_NK" UNIQUE("id_media","id_platform", "link"),
	CONSTRAINT "MediaPlatform_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/





/** i18n name **/
CREATE TABLE IF NOT EXISTS "LanguageName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageName_FK1" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageName_NK" UNIQUE("name", "id_language"),
	CONSTRAINT "LanguageName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TypeName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"id_type"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "TypeName_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TypeName_NK" UNIQUE("name", "id_type"),
	CONSTRAINT "TypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "StatusName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"id_status"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "StatusName_FK1" FOREIGN KEY("id_status") REFERENCES "Status"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusName_NK" UNIQUE("name", "id_status"),
	CONSTRAINT "StatusName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CountryName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"id_country"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CountryName_FK1" FOREIGN KEY("id_country") REFERENCES "Country"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryName_NK" UNIQUE("name", "id_country"),
	CONSTRAINT "CountryName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "MediaName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"name"				TEXT NOT NULL,
	"id_media"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id"),
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_media"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GroupName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"name"				TEXT NOT NULL,
	"id_group"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_group") REFERENCES "Group_"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_group"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "IssueName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL,
	"id_issue"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_issue") REFERENCES "Issue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_issue"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/





/** i18n name language **/
CREATE TABLE IF NOT EXISTS "LanguageNameLanguage" (
	"id"				INTEGER NOT NULL UNIQUE,
	"id_language_name"	INTEGER NOT NULL,
	"id_language"		INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageNameLanguage_FK1" FOREIGN KEY("id_language_name") REFERENCES "LanguageName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageNameLanguage_NK" UNIQUE("id_language_name", "id_language"),
	CONSTRAINT "LanguageNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TypeNameLanguage" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_type_name"	INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "TypeNameLanguage_FK1" FOREIGN KEY("id_type_name") REFERENCES "TypeName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TypeNameLanguage_NK" UNIQUE("id_type_name", "id_language"),
	CONSTRAINT "TypeNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "StatusNameLanguage" (
	"id"				INTEGER NOT NULL UNIQUE,
	"id_status_name"	INTEGER NOT NULL,
	"id_language"		INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "StatusNameLanguage_FK1" FOREIGN KEY("id_status_name") REFERENCES "StatusName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusNameLanguage_NK" UNIQUE("id_status_name", "id_language"),
	CONSTRAINT "StatusNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CountryNameLanguage" (
	"id"				INTEGER NOT NULL UNIQUE,
	"id_country_name"	INTEGER NOT NULL,
	"id_language"		INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CountryNameLanguage_FK1" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryNameLanguage_FK2" FOREIGN KEY("id_country_name") REFERENCES "CountryName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryNameLanguage_NK" UNIQUE("id_country_name", "id_language"),
	CONSTRAINT "CountryNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "MediaNameLanguage" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_media_name"	INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaNameLanguage_FK1" FOREIGN KEY("id_media_name") REFERENCES "MediaName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaNameLanguage_NK" UNIQUE("id_media_name", "id_language"),
	CONSTRAINT "MediaNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GroupNameLanguage" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_group_name"	INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "GroupNameLanguage_FK1" FOREIGN KEY("id_group_name") REFERENCES "GroupName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "GroupNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "GroupNameLanguage_NK" UNIQUE("id_group_name", "id_language"),
	CONSTRAINT "GroupNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "IssueNameLanguage" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_issue_name"	INTEGER NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "IssueNameLanguage_FK1" FOREIGN KEY("id_issue_name") REFERENCES "IssueName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "IssueNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "IssueNameLanguage_NK" UNIQUE("id_issue_name", "id_language"),
	CONSTRAINT "IssueNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/





/** i18n description **/
CREATE TABLE IF NOT EXISTS "LanguageDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageDescription_FK1" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageDescription_NK" UNIQUE("description", "id_language"),
	CONSTRAINT "LanguageDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "PlatformDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_platform"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "PlatformDescription_FK1" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescription_NK" UNIQUE("description", "id_platform"),
	CONSTRAINT "PlatformDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "EncoderDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_encoder"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "EncoderDescription_FK1" FOREIGN KEY("id_encoder") REFERENCES "Encoder"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "EncoderDescription_NK" UNIQUE("description", "id_encoder"),
	CONSTRAINT "EncoderDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ExtensionDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_extension"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ExtensionDescription_FK1" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ExtensionDescription_NK" UNIQUE("description", "id_extension"),
	CONSTRAINT "ExtensionDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TypeDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_type"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "TypeDescription_FK1" FOREIGN KEY("id_type") REFERENCES "Type"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TypeDescription_NK" UNIQUE("description", "id_type"),
	CONSTRAINT "TypeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodeDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_code"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodeDescription_FK1" FOREIGN KEY("id_code") REFERENCES "Code"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodeDescription_NK" UNIQUE("description", "id_code"),
	CONSTRAINT "CodeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "StatusDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_status"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "StatusDescription_FK1" FOREIGN KEY("id_status") REFERENCES "Status"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusDescription_NK" UNIQUE("description", "id_status"),
	CONSTRAINT "StatusDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "PlatformDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_platform"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "PlatformDescription_FK1" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescription_NK" UNIQUE("description", "id_platform"),
	CONSTRAINT "PlatformDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AppDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_app"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "AppDescription_FK1" FOREIGN KEY("id_app") REFERENCES "App"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppDescription_NK" UNIQUE("description", "id_app"),
	CONSTRAINT "AppDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CountryDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_country"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CountryDescription_FK1" FOREIGN KEY("id_country") REFERENCES "Country"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryDescription_NK" UNIQUE("description", "id_country"),
	CONSTRAINT "CountryDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "VersionDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_version"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "VersionName_FK1" FOREIGN KEY("id_version") REFERENCES "Version"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "VersionName_NK" UNIQUE("description", "id_version"),
	CONSTRAINT "VersionName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_codec"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecName_FK1" FOREIGN KEY("id_codec") REFERENCES "Codec"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecName_NK" UNIQUE("description", "id_codec"),
	CONSTRAINT "CodecName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_share_site"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteName_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteName_NK" UNIQUE("description", "id_share_site"),
	CONSTRAINT "ShareSiteName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WarehouseDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_warehouse"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseDescription_FK1" FOREIGN KEY("id_warehouse") REFERENCES "Warehouse"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseDescription_NK" UNIQUE("description", "id_warehouse"),
	CONSTRAINT "WarehouseDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_media"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("description", "id_media"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GroupDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_group"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "GroupName_FK1" FOREIGN KEY("id_group") REFERENCES "Group_"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "GroupName_NK" UNIQUE("description", "id_group"),
	CONSTRAINT "GroupName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "IssueDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"id_issue"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "IssueName_FK1" FOREIGN KEY("id_issue") REFERENCES "Issue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "IssueName_NK" UNIQUE("description", "id_issue"),
	CONSTRAINT "IssueName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/***/





/** i18n description language **/
CREATE TABLE IF NOT EXISTS "LanguageDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_language_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageDescriptionLanguage_FK1" FOREIGN KEY("id_language_description") REFERENCES "LanguageDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageDescriptionLanguage_NK" UNIQUE("id_language_description", "id_language"),
	CONSTRAINT "LanguageDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "PlatformDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_platform_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "PlatformDescriptionLanguage_FK1" FOREIGN KEY("id_platform_description") REFERENCES "PlatformDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescriptionLanguage_NK" UNIQUE("id_platform_description", "id_language"),
	CONSTRAINT "PlatformDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "EncoderDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_encoder_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "EncoderDescriptionLanguage_FK1" FOREIGN KEY("id_encoder_description") REFERENCES "EncoderDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "EncoderDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "EncoderDescriptionLanguage_NK" UNIQUE("id_encoder_description", "id_language"),
	CONSTRAINT "EncoderDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ExtensionDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_extension_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ExtensionDescriptionLanguage_FK1" FOREIGN KEY("id_extension_description") REFERENCES "ExtensionDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ExtensionDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ExtensionDescriptionLanguage_NK" UNIQUE("id_extension_description", "id_language"),
	CONSTRAINT "ExtensionDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "TypeDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_type_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "TypeDescriptionLanguage_FK1" FOREIGN KEY("id_type_description") REFERENCES "TypeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TypeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "TypeDescriptionLanguage_NK" UNIQUE("id_type_description", "id_language"),
	CONSTRAINT "TypeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodeDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_code_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodeDescriptionLanguage_FK1" FOREIGN KEY("id_code_description") REFERENCES "CodeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodeDescriptionLanguage_NK" UNIQUE("id_code_description", "id_language"),
	CONSTRAINT "CodeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "StatusDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_status_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "StatusDescriptionLanguage_FK1" FOREIGN KEY("id_status_description") REFERENCES "StatusDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "StatusDescriptionLanguage_NK" UNIQUE("id_status_description", "id_language"),
	CONSTRAINT "StatusDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "PlatformDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_platform_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "PlatformDescriptionLanguage_FK1" FOREIGN KEY("id_platform_description") REFERENCES "PlatformDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "PlatformDescriptionLanguage_NK" UNIQUE("id_platform_description", "id_language"),
	CONSTRAINT "PlatformDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AppDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_app_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "AppDescriptionLanguage_FK1" FOREIGN KEY("id_app_description") REFERENCES "AppDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppDescriptionLanguage_NK" UNIQUE("id_app_description", "id_language"),
	CONSTRAINT "AppDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CountryDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_country_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CountryDescriptionLanguage_FK1" FOREIGN KEY("id_country_description") REFERENCES "CountryDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryDescriptionLanguage_NK" UNIQUE("id_country_description", "id_language"),
	CONSTRAINT "CountryDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "VersionDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_version_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "VersionDescriptionLanguage_FK1" FOREIGN KEY("id_version_description") REFERENCES "VersionDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "VersionDescriptionLanguage_NK" UNIQUE("id_version_description", "id_language"),
	CONSTRAINT "VersionDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_codec_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecDescriptionLanguage_FK1" FOREIGN KEY("id_codec_description") REFERENCES "CodecDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecDescriptionLanguage_NK" UNIQUE("id_codec_description", "id_language"),
	CONSTRAINT "CodecDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_share_site_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteDescriptionLanguage_FK1" FOREIGN KEY("id_share_site_description") REFERENCES "ShareSiteDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteDescriptionLanguage_NK" UNIQUE("id_share_site_description", "id_language"),
	CONSTRAINT "ShareSiteDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WarehouseDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_warehouse_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseDescriptionLanguage_FK1" FOREIGN KEY("id_warehouse_description") REFERENCES "WarehouseDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseDescriptionLanguage_NK" UNIQUE("id_warehouse_description", "id_language"),
	CONSTRAINT "WarehouseDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_media_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaDescriptionLanguage_FK1" FOREIGN KEY("id_media_description") REFERENCES "MediaDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaDescriptionLanguage_NK" UNIQUE("id_media_description", "id_language"),
	CONSTRAINT "MediaDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GroupDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_group_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "GroupDescriptionLanguage_FK1" FOREIGN KEY("id_group_description") REFERENCES "GroupDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "GroupDescriptionLanguage_NK" UNIQUE("id_group_description", "id_language"),
	CONSTRAINT "GroupDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "IssueDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_group_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "IssueDescriptionLanguage_FK1" FOREIGN KEY("id_group_description") REFERENCES "IssueDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "IssueDescriptionLanguage_NK" UNIQUE("id_group_description", "id_language"),
	CONSTRAINT "IssueDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/




/** locale **/
CREATE TABLE IF NOT EXISTS "MediaNameCountry" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_media_name"	INTEGER NOT NULL,
	"id_country"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaNameCountry_FK1" FOREIGN KEY("id_country") REFERENCES "Country"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaNameCountry_FK2" FOREIGN KEY("id_media_name") REFERENCES "MediaName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaNameCountry_NK" UNIQUE("id_media_name", "id_country"),
	CONSTRAINT "MediaNameCountry_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/
/*** ***/





/*** TRIGGERS ***/
/** Without FK **/
CREATE TRIGGER IF NOT EXISTS update_encoder
AFTER UPDATE ON "Encoder" BEGIN
	UPDATE "Encoder"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_extension
AFTER UPDATE ON "Extension" BEGIN
	UPDATE "Extension"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_folder
AFTER UPDATE ON "Folder" BEGIN
	UPDATE "Folder"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_type
AFTER UPDATE ON "Type" BEGIN
	UPDATE "Type"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code
AFTER UPDATE ON "Code" BEGIN
	UPDATE "Code"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_status
AFTER UPDATE ON "Status" BEGIN
	UPDATE "Status"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_app
AFTER UPDATE ON "App" BEGIN
	UPDATE "App"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_country
AFTER UPDATE ON "Country" BEGIN
	UPDATE "Country"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/***/





/** With FK **/
CREATE TRIGGER IF NOT EXISTS update_platform
AFTER UPDATE ON "Platform" BEGIN
	UPDATE "Platform"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_language
AFTER UPDATE ON "Language" BEGIN
	UPDATE "Language"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code_name
AFTER UPDATE ON "CodeName" BEGIN
	UPDATE "CodeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_version
AFTER UPDATE ON "Version" BEGIN
	UPDATE "Version"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec
AFTER UPDATE ON "Codec" BEGIN
	UPDATE "Codec"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site
AFTER UPDATE ON "ShareSite" BEGIN
	UPDATE "ShareSite"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_warehouse
AFTER UPDATE ON "Warehouse" BEGIN
	UPDATE "Warehouse"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_language_code
AFTER UPDATE ON "LanguageCode" BEGIN
	UPDATE "LanguageCode"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media
AFTER UPDATE ON "Media" BEGIN
	UPDATE "Media"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_group
AFTER UPDATE ON "Group_" BEGIN
	UPDATE "Group_"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_issue
AFTER UPDATE ON "Issue" BEGIN
	UPDATE "Issue"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_poster
AFTER UPDATE ON "Poster" BEGIN
	UPDATE "Poster"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_file
AFTER UPDATE ON "File" BEGIN
	UPDATE "File"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_track
AFTER UPDATE ON "Track" BEGIN
	UPDATE "Track"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_track_language
AFTER UPDATE ON "TrackLanguage" BEGIN
	UPDATE "TrackLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_subs
AFTER UPDATE ON "ShareSiteSubs" BEGIN
	UPDATE "ShareSiteSubs"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_file_share_site
AFTER UPDATE ON "FileShareSite" BEGIN
	UPDATE "FileShareSite"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_platform
AFTER UPDATE ON "MediaPlatform" BEGIN
	UPDATE "MediaPlatform"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/** **/





/** i18n name **/
CREATE TRIGGER IF NOT EXISTS update_language_name
AFTER UPDATE ON "LanguageName" BEGIN
	UPDATE "LanguageName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_type_name
AFTER UPDATE ON "TypeName" BEGIN
	UPDATE "TypeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_status_name
AFTER UPDATE ON "StatusName" BEGIN
	UPDATE "StatusName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_country_name
AFTER UPDATE ON "CountryName" BEGIN
	UPDATE "CountryName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;

CREATE TRIGGER IF NOT EXISTS update_media_name
AFTER UPDATE ON "MediaName" BEGIN
	UPDATE "MediaName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_group_name
AFTER UPDATE ON "GroupName" BEGIN
	UPDATE "GroupName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_issue_name
AFTER UPDATE ON "IssueName" BEGIN
	UPDATE "IssueName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/** **/





/** i18n name language **/
CREATE TRIGGER IF NOT EXISTS update_language_name_language
AFTER UPDATE ON "LanguageNameLanguage" BEGIN
	UPDATE "LanguageNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_type_name_language
AFTER UPDATE ON "TypeNameLanguage" BEGIN
	UPDATE "TypeNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_status_name_language
AFTER UPDATE ON "StatusNameLanguage" BEGIN
	UPDATE "StatusNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_country_name_language
AFTER UPDATE ON "CountryNameLanguage" BEGIN
	UPDATE "CountryNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;

CREATE TRIGGER IF NOT EXISTS update_media_name_language
AFTER UPDATE ON "MediaNameLanguage" BEGIN
	UPDATE "MediaNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_group_name_language
AFTER UPDATE ON "GroupNameLanguage" BEGIN
	UPDATE "GroupNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_issue_name_language
AFTER UPDATE ON "IssueNameLanguage" BEGIN
	UPDATE "IssueNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/** **/





/** i18n description **/
CREATE TRIGGER IF NOT EXISTS update_language_description
AFTER UPDATE ON "LanguageDescription" BEGIN
	UPDATE "LanguageDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_platform_description
AFTER UPDATE ON "PlatformDescription" BEGIN
	UPDATE "PlatformDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_encoder_description
AFTER UPDATE ON "EncoderDescription" BEGIN
	UPDATE "EncoderDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_extension_description
AFTER UPDATE ON "ExtensionDescription" BEGIN
	UPDATE "ExtensionDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_type_description
AFTER UPDATE ON "TypeDescription" BEGIN
	UPDATE "TypeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code_description
AFTER UPDATE ON "CodeDescription" BEGIN
	UPDATE "CodeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_status_description
AFTER UPDATE ON "StatusDescription" BEGIN
	UPDATE "StatusDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_platform_description
AFTER UPDATE ON "PlatformDescription" BEGIN
	UPDATE "PlatformDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_app_description
AFTER UPDATE ON "AppDescription" BEGIN
	UPDATE "AppDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_country_description
AFTER UPDATE ON "CountryDescription" BEGIN
	UPDATE "CountryDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;

CREATE TRIGGER IF NOT EXISTS update_version_description
AFTER UPDATE ON "VersionDescription" BEGIN
	UPDATE "VersionDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_description
AFTER UPDATE ON "CodecDescription" BEGIN
	UPDATE "CodecDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_description
AFTER UPDATE ON "ShareSiteDescription" BEGIN
	UPDATE "ShareSiteDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_warehouse_description
AFTER UPDATE ON "WarehouseDescription" BEGIN
	UPDATE "WarehouseDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_description
AFTER UPDATE ON "MediaDescription" BEGIN
	UPDATE "MediaDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_group_description
AFTER UPDATE ON "GroupDescription" BEGIN
	UPDATE "GroupDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_issue_description
AFTER UPDATE ON "IssueDescription" BEGIN
	UPDATE "IssueDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/** **/





/** i18n description language **/
CREATE TRIGGER IF NOT EXISTS update_language_description_language
AFTER UPDATE ON "LanguageDescriptionLanguage" BEGIN
	UPDATE "LanguageDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_platform_description_language
AFTER UPDATE ON "PlatformDescriptionLanguage" BEGIN
	UPDATE "PlatformDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_encoder_description_language
AFTER UPDATE ON "EncoderDescriptionLanguage" BEGIN
	UPDATE "EncoderDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_extension_description_language
AFTER UPDATE ON "ExtensionDescriptionLanguage" BEGIN
	UPDATE "ExtensionDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_type_description_language
AFTER UPDATE ON "TypeDescriptionLanguage" BEGIN
	UPDATE "TypeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code_description_language
AFTER UPDATE ON "CodeDescriptionLanguage" BEGIN
	UPDATE "CodeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_status_description_language
AFTER UPDATE ON "StatusDescriptionLanguage" BEGIN
	UPDATE "StatusDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_platform_description_language
AFTER UPDATE ON "PlatformDescriptionLanguage" BEGIN
	UPDATE "PlatformDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_app_description_language
AFTER UPDATE ON "AppDescriptionLanguage" BEGIN
	UPDATE "AppDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_country_description_language
AFTER UPDATE ON "CountryDescriptionLanguage" BEGIN
	UPDATE "CountryDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;

CREATE TRIGGER IF NOT EXISTS update_version_description_language
AFTER UPDATE ON "VersionDescriptionLanguage" BEGIN
	UPDATE "VersionDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_description_language
AFTER UPDATE ON "CodecDescriptionLanguage" BEGIN
	UPDATE "CodecDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_description_language
AFTER UPDATE ON "ShareSiteDescriptionLanguage" BEGIN
	UPDATE "ShareSiteDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_warehouse_description_language
AFTER UPDATE ON "WarehouseDescriptionLanguage" BEGIN
	UPDATE "WarehouseDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_description_language
AFTER UPDATE ON "MediaDescriptionLanguage" BEGIN
	UPDATE "MediaDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_group_description_language
AFTER UPDATE ON "GroupDescriptionLanguage" BEGIN
	UPDATE "GroupDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_issue_description_language
AFTER UPDATE ON "IssueDescriptionLanguage" BEGIN
	UPDATE "IssueDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/** **/




/** locale **/
/** **/
CREATE TRIGGER IF NOT EXISTS update_media_name_country
AFTER UPDATE ON "MediaNameCountry" BEGIN
	UPDATE "MediaNameCountry"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
/*** ***/
COMMIT;