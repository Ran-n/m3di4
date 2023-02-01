BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Platform" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
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
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "WarehouseType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "CodecType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "CodecType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Code" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Code_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Language" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"description"	TEXT,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Language_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"groupable"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ShareSiteType" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "`ShareSiteType_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaStatus" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaStatus_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Web" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"acronym"		TEXT,
	"link"			TEXT UNIQUE,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Web_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaTypeName" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL,
	"id_media_type"	INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediatypeName_FK1" FOREIGN KEY("id_media_type") REFERENCES "MediaType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaTypeName_NK" UNIQUE("name", "id_media_type"),
	CONSTRAINT "MediaTypeName_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"private"		INTEGER,
	"link"			TEXT,
	"id_type"		INTEGER NOT NULL,
	"id_platform"	INTEGER,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSite_FK1" FOREIGN KEY("id_type") REFERENCES "ShareSiteType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_FK2" FOREIGN KEY("id_platform") REFERENCES "Platform"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSite_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Warehouse" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"size"			INTEGER,
	"filled"		INTEGER,
	"content"		TEXT,
	"id_type"		INTEGER NOT NULL,
	"health"		TEXT,
	"description"	TEXT,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Warehouse_FK1" FOREIGN KEY("id_type") REFERENCES "WarehouseType"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "Warehouse_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
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
	"year_start"	INTEGER NOT NULL,
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
	"name"			TEXT,
	"number"		INTEGER NOT NULL,
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
	"date"				INTEGER,
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
	"writing_app"		TEXT,
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
CREATE TABLE IF NOT EXISTS "Country" (
	"id"			INTEGER NOT NULL UNIQUE,
	"name"			TEXT NOT NULL UNIQUE,
	"kingdom"		INTEGER,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "Country_PK" PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "MediaName" (
	"id"				INTEGER NOT NULL UNIQUE,
	"name"				TEXT NOT NULL,
	"id_media"			INTEGER,
	"id_media_group"	INTEGER,
	"id_media_issue"	INTEGER,
	"active"			INTEGER NOT NULL,
	"added_ts"			TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaName_NN1" CHECK (("id_media" IS NOT NULL AND "id_media_group" IS NULL AND "id_media_issue" IS NULL) OR ("id_media" IS NULL AND "id_media_group" IS NOT NULL AND "id_media_issue" IS NULL) OR ("id_media" IS NULL AND "id_media_group" IS NULL and "id_media_issue" IS NOT NULL)),
	CONSTRAINT "MediaName_FK1" FOREIGN KEY("id_media") REFERENCES "Media"("id"),
	CONSTRAINT "MediaName_FK2" FOREIGN KEY("id_media_group") REFERENCES "MediaGroup"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_FK3" FOREIGN KEY("id_media_issue") REFERENCES "MediaIssue"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaName_NK" UNIQUE("name", "id_media", "id_media_group", "id_media_issue"),
	CONSTRAINT "MediaName_PK" PRIMARY KEY("id" AUTOINCREMENT)
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
CREATE TABLE IF NOT EXISTS "ShareSiteSubs" (
	"id"			INTEGER NOT NULL UNIQUE,
	"id_share_site"	INTEGER NOT NULL,
	"sub_num"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "ShareSiteSubs_FK1" FOREIGN KEY("id_share_site") REFERENCES "ShareSite"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "ShareSiteSubs_NK" UNIQUE("id_share_site", "subs_num", "added_ts"),
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
	"id_media"		INTEGER NOT NULL,
	"id_web"		INTEGER NOT NULL,
	"link"			TEXT NOT NULL,
	"active"		INTEGER NOT NULL,
	"added_ts"		TEXT NOT NULL DEFAULT current_timestamp,
	"modified_ts"	TEXT NOT NULL DEFAULT current_timestamp,
	CONSTRAINT "MediaWeb_FK1" FOREIGN KEY("id_web") REFERENCES "Web"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaWeb_FK2" FOREIGN KEY("id_media") REFERENCES "Media"("id") ON DELETE CASCADE ON UPDATE CASCADE MATCH FULL,
	CONSTRAINT "MediaWeb_PK" PRIMARY KEY("id_media","id_web")
);
COMMIT;