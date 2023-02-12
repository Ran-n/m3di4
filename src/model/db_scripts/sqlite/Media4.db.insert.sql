BEGIN TRANSACTION;

INSERT INTO "Language" ("id", "name", "description") VALUES (1, "Galego", "");
INSERT INTO "Language" ("id", "name", "description") VALUES (2, "English", "");
INSERT INTO "Language" ("id", "name", "description") VALUES (3, "Castellano", "");
INSERT INTO "Language" ("id", "name", "description") VALUES (4, "Español", "");

INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (1, "Galego", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (2, "Galician", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (3, "Gallego", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (4, "English", "", 2);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (5, "Inglés", "", 2);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (6, "Castellano", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (7, "Castelán", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (8, "Castillian", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (9, "Español", "", 4);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (10, "Espanhol", "", 4);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (11, "Spanish", "", 4);

INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 1, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (2, 2, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (3, 3, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (4, 3, 4);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (5, 4, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (6, 5, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (7, 5, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (8, 5, 4);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (9, 6, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (10, 6, 4);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (11, 7, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (12, 8, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (13, 9, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (14, 9, 4);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (15, 9, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (16, 10, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (17, 11, 2);


INSERT INTO "Platform" ("id", "name", "description", "active") VALUES (1, "Telegram", "Messaging platform", 1);

COMMIT;