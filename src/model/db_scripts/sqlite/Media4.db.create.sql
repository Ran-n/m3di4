BEGIN TRANSACTION;
/*** TABLES ***/
/** Without FK **/
CREATE TABLE IF NOT EXISTS "Language" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Language_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Platform" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Platform_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Encoder" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Encoder_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Extension" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL UNIQUE,
	"format_name"		TEXT NOT NULL UNIQUE,
	"format_name_long"	TEXT NOT NULL UNIQUE,
	"description"		TEXT,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Extension_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FolderName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "FolderName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WarehouseType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Code" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Code_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"groupable"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "`ShareSiteType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatus" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatus_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Web" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"acronym"		TEXT,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"link"			TEXT UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Web_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "App" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "App_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Country" (
	"id"			INTEGER NOT NULL UNIQUE,
	"active"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"kingdom"		INTEGER,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Country_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/***/





/** With FK **/
CREATE TABLE IF NOT EXISTS "AppVersion" (
	"id"				INTEGER NOT NULL UNIQUE,
	"active"			INTEGER NOT NULL,
	"id_app"			INTEGER NOT NULL,
	"number"			TEXT NOT NULL,
	"name"				TEXT,
	"num_bit_processor" INTEGER,
	"description"		TEXT,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "AppVersion_FK1" FOREIGN KEY("id_app") REFERENCES "App"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppVersion_NK" UNIQUE("id_app", "number"),
	CONSTRAINT "AppVersion_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Codec" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"name_long"		TEXT UNIQUE,
	"id_type"		INTEGER NOT NULL,
	"description"	TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Codec_FK1" FOREIGN KEY("id_type") REFERENCES "CodecType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Codec_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSite" (
	"id"				INTEGER NOT NULL UNIQUE,
	"in_platform_id"	TEXT,
	"name"				TEXT NOT NULL,
	"private"			INTEGER,
	"link"				TEXT NOT NULL UNIQUE,
	"id_type"			INTEGER NOT NULL,
	"id_platform"		INTEGER,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSite_FK1" FOREIGN KEY("id_type") REFERENCES "ShareSiteType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_FK2" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Warehouse" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"size"			INTEGER,
	"filled"		INTEGER,
	"content"		TEXT,
	"id_type"		INTEGER NOT NULL,
	"health"		TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Warehouse_FK1" FOREIGN KEY("id_type") REFERENCES "WarehouseType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Warehouse_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "LanguageCode" (
	"id"			INTEGER NOT NULL UNIQUE,
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
	"name"			TEXT NOT NULL,
	"description"	TEXT,
	"year_start"	INTEGER,
	"year_end"		INTEGER,
	"id_type"		INTEGER NOT NULL,
	"id_status"		INTEGER NOT NULL,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Media_FK1" FOREIGN KEY("id_type") REFERENCES "MediaType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Media_FK2" FOREIGN KEY("id_status") REFERENCES "MediaStatus"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Media_NK" UNIQUE("name", "year_start", "id_type"),
	CONSTRAINT "Media_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaGroup" (
	"id"			INTEGER NOT NULL UNIQUE,
	"number"		INTEGER NOT NULL,
	"name"			TEXT,
	"description"	TEXT,
	"year_start"	INTEGER,
	"year_end"		INTEGER,
	"id_media"		INTEGER NOT NULL,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaGroup_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaGroup_NK" UNIQUE("number", "id_media"),
	CONSTRAINT "MediaGroup_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaIssue" (
	"id"				INTEGER NOT NULL UNIQUE,
	"position"			INTEGER NOT NULL,
	"name"				TEXT,
	"description"		TEXT,
	"date"				TEXT,
	"id_media"			INTEGER NOT NULL,
	"id_media_group"	INTEGER NOT NULL,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaIssue_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssue_FK2" FOREIGN KEY("id_media_group") REFERENCES "MediaGroup"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssue_NK" UNIQUE("id_media", "id_media_group", "position"),
	CONSTRAINT "MediaIssue_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaPoster" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_media"		INTEGER NOT NULL,
	"name"			TEXT NOT NULL UNIQUE,
	"id_extension"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaPoster_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaPoster_FK2" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaPoster_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "File" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_extension"		INTEGER NOT NULL,
	"id_warehouse"		INTEGER NOT NULL,
	"id_folder"			INTEGER NOT NULL,
	"id_media"			INTEGER,
	"id_media_issue"	INTEGER,
	"title"				TEXT,
	"nb_streams"		INTEGER,
	"nb_programs"		INTEGER,
	"start"				REAL,
	"duration"			REAL,
	"size"				INTEGER,
	"bit_rate"			INTEGER,
	"probe_score"		INTEGER,
	"creation_ts"		TEXT,
	"id_app_version"	INTEGER,
	"id_encoder"		INTEGER,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "File_NN1" CHECK (("id_media" IS NOT NULL AND "id_media_issue" IS NULL) OR ("id_media" IS NULL AND "id_media_issue" IS NOT NULL)),
	CONSTRAINT "File_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK2" FOREIGN KEY("id_warehouse") REFERENCES "Warehouse"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK3" FOREIGN KEY("id_folder") REFERENCES "FolderName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK4" FOREIGN KEY("id_media_issue") REFERENCES "MediaIssue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK5" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK6" FOREIGN KEY("id_encoder") REFERENCES "Encoder"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_FK7" FOREIGN KEY("id_app_version") REFERENCES "AppVersion"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "File_NK" UNIQUE("name", "id_extension", "id_folder", "id_warehouse"),
	CONSTRAINT "File_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FileStream" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_file"				INTEGER NOT NULL,
	"id_codec"				INTEGER NOT NULL,
	"id_language"			INTEGER,
	"index"					INTEGER NOT NULL,
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
	"default"				INTEGER,
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
	"active"				INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "FileStream_FK1" FOREIGN KEY("id_file") REFERENCES "File"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileStream_FK2" FOREIGN KEY("id_codec") REFERENCES "Codec"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileStream_FK3" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileStream_NK" UNIQUE("id_file", "index"),
	CONSTRAINT "FileStream_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteSubs" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_share_site"	INTEGER NOT NULL,
	"sub_num"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteSubs_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteSubs_NK" UNIQUE("id_share_site", "sub_num", "added_ts"),
	CONSTRAINT "ShareSiteSubs_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "FileShareSite" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_file"		INTEGER NOT NULL,
	"id_share_site"	INTEGER NOT NULL,
	"link"			TEXT NOT NULL,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "FileShareSite_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileShareSite_FK2" FOREIGN KEY("id_file") REFERENCES "File"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "FileShareSite_NK" UNIQUE("id_file", "id_share_site", "link"),
	CONSTRAINT "FileShareSite_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaWeb" (
	"id"			INTEGER UNIQUE NOT NULL,
	"id_media"		INTEGER NOT NULL,
	"id_web"		INTEGER NOT NULL,
	"link"			TEXT NOT NULL,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaWeb_FK1" FOREIGN KEY("id_web") REFERENCES "Web"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaWeb_FK2" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaWeb_NK" UNIQUE("id_media","id_web", "link"),
	CONSTRAINT "MediaWeb_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/





/** i18n name **/
CREATE TABLE IF NOT EXISTS "LanguageName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL,
	"id_language"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "LanguageName_FK1" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "LanguageName_NK" UNIQUE("name", "id_language"),
	CONSTRAINT "LanguageName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WarehouseTypeName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_warehouse_type"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseTypeName_FK1" FOREIGN KEY("id_warehouse_type") REFERENCES "WarehouseType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseTypeName_NK" UNIQUE("name", "id_warehouse_type"),
	CONSTRAINT "WarehouseTypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecTypeName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL,
	"id_codec_type"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecTypeName_FK1" FOREIGN KEY("id_codec_type") REFERENCES "CodecType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecTypeName_NK" UNIQUE("name", "id_codec_type"),
	CONSTRAINT "CodecTypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaTypeName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL,
	"id_media_type"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaTypeName_FK1" FOREIGN KEY("id_media_type") REFERENCES "MediaType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeName_NK" UNIQUE("name", "id_media_type"),
	CONSTRAINT "MediaTypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteTypeName" (
	"id"					INTEGER NOT NULL UNIQUE,
	"name"					TEXT NOT NULL,
	"id_share_site_type"	INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteTypeName_FK1" FOREIGN KEY("id_share_site_type") REFERENCES "ShareSiteType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeName_NK" UNIQUE("name", "id_share_site_type"),
	CONSTRAINT "ShareSiteTypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatusName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_media_status"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatusName_FK1" FOREIGN KEY("id_media_status") REFERENCES "MediaStatus"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusName_NK" UNIQUE("name", "id_media_status"),
	CONSTRAINT "MediaStatusName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CountryName" (
	"id"			INTEGER NOT NULL UNIQUE,
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
	"name"				TEXT NOT NULL,
	"id_media"			INTEGER NOT NULL,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id"),
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_media"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaGroupName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_media_group"	INTEGER NOT NULL,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media_group") REFERENCES "MediaGroup"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_media_group"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaIssueName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_media_issue"	INTEGER NOT NULL,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media_issue") REFERENCES "MediaIssue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_media_issue"),
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
CREATE TABLE IF NOT EXISTS "WarehouseTypeNameLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_warehouse_type_name"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseTypeNameLanguage_FK1" FOREIGN KEY("id_warehouse_type_name") REFERENCES "WarehouseTypeName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseTypeNameLanguage_NK" UNIQUE("id_warehouse_type_name", "id_language"),
	CONSTRAINT "WarehouseTypeNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecTypeNameLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_codec_type_name"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecTypeNameLanguage_FK1" FOREIGN KEY("id_codec_type_name") REFERENCES "CodecTypeName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecTypeNameLanguage_NK" UNIQUE("id_codec_type_name", "id_language"),
	CONSTRAINT "CodecTypeNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaTypeNameLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_media_type_name"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediatypeNameLanguage_FK1" FOREIGN KEY("id_media_type_name") REFERENCES "MediaTypeName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediatypeNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeNameLanguage_NK" UNIQUE("id_media_type_name", "id_language"),
	CONSTRAINT "MediaTypeNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteTypeNameLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_share_site_type_name"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteTypeNameLanguage_FK1" FOREIGN KEY("id_share_site_type_name") REFERENCES "ShareSiteTypeName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeNameLanguage_NK" UNIQUE("id_share_site_type_name", "id_language"),
	CONSTRAINT "ShareSiteTypeNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatusNameLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_media_status_name"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatusNameLanguage_FK1" FOREIGN KEY("id_media_status_name") REFERENCES "MediaStatusName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusNameLanguage_NK" UNIQUE("id_media_status_name", "id_language"),
	CONSTRAINT "MediaStatusNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TABLE IF NOT EXISTS "MediaGroupNameLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_media_group_name"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaGroupNameLanguage_FK1" FOREIGN KEY("id_media_group_name") REFERENCES "MediaGroupName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaGroupNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaGroupNameLanguage_NK" UNIQUE("id_media_group_name", "id_language"),
	CONSTRAINT "MediaGroupNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaIssueNameLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_media_issue_name"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaIssueNameLanguage_FK1" FOREIGN KEY("id_media_issue_name") REFERENCES "MediaIssueName"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssueNameLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssueNameLanguage_NK" UNIQUE("id_media_issue_name", "id_language"),
	CONSTRAINT "MediaIssueNameLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
/** **/





/** i18n description **/
CREATE TABLE IF NOT EXISTS "LanguageDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
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
	"description"	TEXT NOT NULL,
	"id_extension"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ExtensionDescription_FK1" FOREIGN KEY("id_extension") REFERENCES "Extension"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ExtensionDescription_NK" UNIQUE("description", "id_extension"),
	CONSTRAINT "ExtensionDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WarehouseTypeDescription" (
	"id"				INTEGER NOT NULL UNIQUE,
	"description"		TEXT NOT NULL,
	"id_warehouse_type"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseTypeDescription_FK1" FOREIGN KEY("id_warehouse_type") REFERENCES "WarehouseType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseTypeDescription_NK" UNIQUE("description", "id_warehouse_type"),
	CONSTRAINT "WarehouseTypeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecTypeDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL,
	"id_codec_type"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecTypeDescription_FK1" FOREIGN KEY("id_codec_type") REFERENCES "CodecType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecTypeDescription_NK" UNIQUE("description", "id_codec_type"),
	CONSTRAINT "CodecTypeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodeDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL,
	"id_code"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodeDescription_FK1" FOREIGN KEY("id_code") REFERENCES "Code"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodeDescription_NK" UNIQUE("description", "id_code"),
	CONSTRAINT "CodeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaTypeDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL,
	"id_media_type"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaTypeDescription_FK1" FOREIGN KEY("id_media_type") REFERENCES "MediaType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeDescription_NK" UNIQUE("description", "id_media_type"),
	CONSTRAINT "MediaTypeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteTypeDescription" (
	"id"					INTEGER NOT NULL UNIQUE,
	"description"			TEXT NOT NULL,
	"id_share_site_type"	INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteTypeDescription_FK1" FOREIGN KEY("id_share_site_type") REFERENCES "ShareSiteType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeDescription_NK" UNIQUE("description", "id_share_site_type"),
	CONSTRAINT "ShareSiteTypeDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatusDescription" (
	"id"				INTEGER NOT NULL UNIQUE,
	"description"		TEXT NOT NULL,
	"id_media_status"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatusDescription_FK1" FOREIGN KEY("id_media_status") REFERENCES "MediaStatus"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusDescription_NK" UNIQUE("description", "id_media_status"),
	CONSTRAINT "MediaStatusDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WebDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
	"description"	TEXT NOT NULL,
	"id_web"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WebDescription_FK1" FOREIGN KEY("id_web") REFERENCES "Web"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WebDescription_NK" UNIQUE("description", "id_web"),
	CONSTRAINT "WebDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "AppDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
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
	"description"	TEXT NOT NULL,
	"id_country"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CountryDescription_FK1" FOREIGN KEY("id_country") REFERENCES "Country"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CountryDescription_NK" UNIQUE("description", "id_country"),
	CONSTRAINT "CountryDescription_PK" PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "AppVersionDescription" (
	"id"				INTEGER NOT NULL UNIQUE,
	"description"		TEXT NOT NULL,
	"id_app_version"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "AppVersionName_FK1" FOREIGN KEY("id_app_version") REFERENCES "AppVersion"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppVersionName_NK" UNIQUE("description", "id_app_version"),
	CONSTRAINT "AppVersionName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecDescription" (
	"id"			INTEGER NOT NULL UNIQUE,
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
	"description"	TEXT NOT NULL,
	"id_media"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("description", "id_media"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaGroupDescription" (
	"id"				INTEGER NOT NULL UNIQUE,
	"description"		TEXT NOT NULL,
	"id_media_group"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaGroupName_FK1" FOREIGN KEY("id_media_group") REFERENCES "MediaGroup"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaGroupName_NK" UNIQUE("description", "id_media_group"),
	CONSTRAINT "MediaGroupName_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaIssueDescription" (
	"id"				INTEGER NOT NULL UNIQUE,
	"description"		TEXT NOT NULL,
	"id_media_issue"	INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaIssueName_FK1" FOREIGN KEY("id_media_issue") REFERENCES "MediaIssue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssueName_NK" UNIQUE("description", "id_media_issue"),
	CONSTRAINT "MediaIssueName_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TABLE IF NOT EXISTS "WarehouseTypeDescriptionLanguage" (
	"id"							INTEGER NOT NULL UNIQUE,
	"id_warehouse_type_description"	INTEGER NOT NULL,
	"id_language"					INTEGER NOT NULL,
	"added_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseTypeDescriptionLanguage_FK1" FOREIGN KEY("id_warehouse_type_description") REFERENCES "WarehouseTypeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseTypeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WarehouseTypeDescriptionLanguage_NK" UNIQUE("id_warehouse_type_description", "id_language"),
	CONSTRAINT "WarehouseTypeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecTypeDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_codec_type_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecTypeDescriptionLanguage_FK1" FOREIGN KEY("id_codec_type_description") REFERENCES "CodecTypeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecTypeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "CodecTypeDescriptionLanguage_NK" UNIQUE("id_codec_type_description", "id_language"),
	CONSTRAINT "CodecTypeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TABLE IF NOT EXISTS "MediaTypeDescriptionLanguage" (
	"id"						INTEGER NOT NULL UNIQUE,
	"id_media_type_description"	INTEGER NOT NULL,
	"id_language"				INTEGER NOT NULL,
	"added_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaTypeDescriptionLanguage_FK1" FOREIGN KEY("id_media_type_description") REFERENCES "MediaTypeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeDescriptionLanguage_NK" UNIQUE("id_media_type_description", "id_language"),
	CONSTRAINT "MediaTypeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteTypeDescriptionLanguage" (
	"id"								INTEGER NOT NULL UNIQUE,
	"id_share_site_type_description"	INTEGER NOT NULL,
	"id_language"						INTEGER NOT NULL,
	"added_ts"							TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteTypeDescriptionLanguage_FK1" FOREIGN KEY("id_share_site_type_description") REFERENCES "ShareSiteTypeDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteTypeDescriptionLanguage_NK" UNIQUE("id_share_site_type_description", "id_language"),
	CONSTRAINT "ShareSiteTypeDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatusDescriptionLanguage" (
	"id"							INTEGER NOT NULL UNIQUE,
	"id_media_status_description"	INTEGER NOT NULL,
	"id_language"					INTEGER NOT NULL,
	"added_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatusDescriptionLanguage_FK1" FOREIGN KEY("id_media_status_description") REFERENCES "MediaStatusDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaStatusDescriptionLanguage_NK" UNIQUE("id_media_status_description", "id_language"),
	CONSTRAINT "MediaStatusDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "WebDescriptionLanguage" (
	"id"					INTEGER NOT NULL UNIQUE,
	"id_web_description"	INTEGER NOT NULL,
	"id_language"			INTEGER NOT NULL,
	"added_ts"				TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WebDescriptionLanguage_FK1" FOREIGN KEY("id_web_description") REFERENCES "WebDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WebDescriptionLanguage_FK2" FOREIGN KEY("id_language") REFERENCES "Language"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "WebDescriptionLanguage_NK" UNIQUE("id_web_description", "id_language"),
	CONSTRAINT "WebDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
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

CREATE TABLE IF NOT EXISTS "AppVersionDescriptionLanguage" (
	"id"							INTEGER NOT NULL UNIQUE,
	"id_app_version_description"	INTEGER NOT NULL,
	"id_language"					INTEGER NOT NULL,
	"added_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "AppVersionDescriptionLanguage_FK1" FOREIGN KEY("id_app_version_description") REFERENCES "AppVersionDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "AppVersionDescriptionLanguage_NK" UNIQUE("id_app_version_description", "id_language"),
	CONSTRAINT "AppVersionDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TABLE IF NOT EXISTS "MediaGroupDescriptionLanguage" (
	"id"							INTEGER NOT NULL UNIQUE,
	"id_media_group_description"	INTEGER NOT NULL,
	"id_language"					INTEGER NOT NULL,
	"added_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaGroupDescriptionLanguage_FK1" FOREIGN KEY("id_media_group_description") REFERENCES "MediaGroupDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaGroupDescriptionLanguage_NK" UNIQUE("id_media_group_description", "id_language"),
	CONSTRAINT "MediaGroupDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaIssueDescriptionLanguage" (
	"id"							INTEGER NOT NULL UNIQUE,
	"id_media_group_description"	INTEGER NOT NULL,
	"id_language"					INTEGER NOT NULL,
	"added_ts"						TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"					TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaIssueDescriptionLanguage_FK1" FOREIGN KEY("id_media_group_description") REFERENCES "MediaIssueDescription"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaIssueDescriptionLanguage_NK" UNIQUE("id_media_group_description", "id_language"),
	CONSTRAINT "MediaIssueDescriptionLanguage_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TRIGGER IF NOT EXISTS update_language
AFTER UPDATE ON "Language" BEGIN
	UPDATE "Language"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_platform
AFTER UPDATE ON "Platform" BEGIN
	UPDATE "Platform"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
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
CREATE TRIGGER IF NOT EXISTS update_folder_name
AFTER UPDATE ON "FolderName" BEGIN
	UPDATE "FolderName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_warehouse_type
AFTER UPDATE ON "WarehouseType" BEGIN
	UPDATE "WarehouseType"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_type
AFTER UPDATE ON "CodecType" BEGIN
	UPDATE "CodecType"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code
AFTER UPDATE ON "Code" BEGIN
	UPDATE "Code"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_type
AFTER UPDATE ON "MediaType" BEGIN
	UPDATE "MediaType"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_type
AFTER UPDATE ON "ShareSiteType" BEGIN
	UPDATE "ShareSiteType"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_status
AFTER UPDATE ON "MediaStatus" BEGIN
	UPDATE "MediaStatus"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_web
AFTER UPDATE ON "Web" BEGIN
	UPDATE "Web"
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
CREATE TRIGGER IF NOT EXISTS update_app_version
AFTER UPDATE ON "AppVersion" BEGIN
	UPDATE "AppVersion"
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
CREATE TRIGGER IF NOT EXISTS update_media_group
AFTER UPDATE ON "MediaGroup" BEGIN
	UPDATE "MediaGroup"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_issue
AFTER UPDATE ON "MediaIssue" BEGIN
	UPDATE "MediaIssue"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_poster
AFTER UPDATE ON "MediaPoster" BEGIN
	UPDATE "MediaPoster"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_file
AFTER UPDATE ON "File" BEGIN
	UPDATE "File"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_file_stream
AFTER UPDATE ON "FileStream" BEGIN
	UPDATE "FileStream"
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
CREATE TRIGGER IF NOT EXISTS update_media_web
AFTER UPDATE ON "MediaWeb" BEGIN
	UPDATE "MediaWeb"
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
CREATE TRIGGER IF NOT EXISTS update_warehouse_type_name
AFTER UPDATE ON "WarehouseTypeName" BEGIN
	UPDATE "WarehouseTypeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_type_name
AFTER UPDATE ON "CodecTypeName" BEGIN
	UPDATE "CodecTypeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_type_name
AFTER UPDATE ON "MediaTypeName" BEGIN
	UPDATE "MediaTypeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_type_name
AFTER UPDATE ON "ShareSiteTypeName" BEGIN
	UPDATE "ShareSiteTypeName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_status_name
AFTER UPDATE ON "MediaStatusName" BEGIN
	UPDATE "MediaStatusName"
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
CREATE TRIGGER IF NOT EXISTS update_media_group_name
AFTER UPDATE ON "MediaGroupName" BEGIN
	UPDATE "MediaGroupName"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_issue_name
AFTER UPDATE ON "MediaIssueName" BEGIN
	UPDATE "MediaIssueName"
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
CREATE TRIGGER IF NOT EXISTS update_warehouse_type_name_language
AFTER UPDATE ON "WarehouseTypeNameLanguage" BEGIN
	UPDATE "WarehouseTypeNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_type_name_language
AFTER UPDATE ON "CodecTypeNameLanguage" BEGIN
	UPDATE "CodecTypeNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_type_name_language
AFTER UPDATE ON "MediaTypeNameLanguage" BEGIN
	UPDATE "MediaTypeNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_type_name_language
AFTER UPDATE ON "ShareSiteTypeNameLanguage" BEGIN
	UPDATE "ShareSiteTypeNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_status_name_language
AFTER UPDATE ON "MediaStatusNameLanguage" BEGIN
	UPDATE "MediaStatusNameLanguage"
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
CREATE TRIGGER IF NOT EXISTS update_media_group_name_language
AFTER UPDATE ON "MediaGroupNameLanguage" BEGIN
	UPDATE "MediaGroupNameLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_issue_name_language
AFTER UPDATE ON "MediaIssueNameLanguage" BEGIN
	UPDATE "MediaIssueNameLanguage"
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
CREATE TRIGGER IF NOT EXISTS update_warehouse_type_description
AFTER UPDATE ON "WarehouseTypeDescription" BEGIN
	UPDATE "WarehouseTypeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_type_description
AFTER UPDATE ON "CodecTypeDescription" BEGIN
	UPDATE "CodecTypeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code_description
AFTER UPDATE ON "CodeDescription" BEGIN
	UPDATE "CodeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_type_description
AFTER UPDATE ON "MediaTypeDescription" BEGIN
	UPDATE "MediaTypeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_type_description
AFTER UPDATE ON "ShareSiteTypeDescription" BEGIN
	UPDATE "ShareSiteTypeDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_status_description
AFTER UPDATE ON "MediaStatusDescription" BEGIN
	UPDATE "MediaStatusDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_web_description
AFTER UPDATE ON "WebDescription" BEGIN
	UPDATE "WebDescription"
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

CREATE TRIGGER IF NOT EXISTS update_app_version_description
AFTER UPDATE ON "AppVersionDescription" BEGIN
	UPDATE "AppVersionDescription"
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
CREATE TRIGGER IF NOT EXISTS update_media_group_description
AFTER UPDATE ON "MediaGroupDescription" BEGIN
	UPDATE "MediaGroupDescription"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_issue_description
AFTER UPDATE ON "MediaIssueDescription" BEGIN
	UPDATE "MediaIssueDescription"
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
CREATE TRIGGER IF NOT EXISTS update_warehouse_type_description_language
AFTER UPDATE ON "WarehouseTypeDescriptionLanguage" BEGIN
	UPDATE "WarehouseTypeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_type_description_language
AFTER UPDATE ON "MediaTypeDescriptionLanguage" BEGIN
	UPDATE "MediaTypeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_codec_type_description_language
AFTER UPDATE ON "CodecTypeDescriptionLanguage" BEGIN
	UPDATE "CodecTypeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_code_description_language
AFTER UPDATE ON "CodeDescriptionLanguage" BEGIN
	UPDATE "CodeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_share_site_type_description_language
AFTER UPDATE ON "ShareSiteTypeDescriptionLanguage" BEGIN
	UPDATE "ShareSiteTypeDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_status_description_language
AFTER UPDATE ON "MediaStatusDescriptionLanguage" BEGIN
	UPDATE "MediaStatusDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_web_description_language
AFTER UPDATE ON "WebDescriptionLanguage" BEGIN
	UPDATE "WebDescriptionLanguage"
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

CREATE TRIGGER IF NOT EXISTS update_app_version_description_language
AFTER UPDATE ON "AppVersionDescriptionLanguage" BEGIN
	UPDATE "AppVersionDescriptionLanguage"
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
CREATE TRIGGER IF NOT EXISTS update_media_group_description_language
AFTER UPDATE ON "MediaGroupDescriptionLanguage" BEGIN
	UPDATE "MediaGroupDescriptionLanguage"
	SET modified_ts = current_timestamp
	WHERE rowid = new.rowid;
END;
CREATE TRIGGER IF NOT EXISTS update_media_issue_description_language
AFTER UPDATE ON "MediaIssueDescriptionLanguage" BEGIN
	UPDATE "MediaIssueDescriptionLanguage"
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