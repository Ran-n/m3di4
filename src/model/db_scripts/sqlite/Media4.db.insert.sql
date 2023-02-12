BEGIN TRANSACTION;

INSERT INTO "Language" ("id", "name", "description") VALUES (1, "Galician", "A Romance language with roots in medieval Latin, this is spoken by around 2.4 million people primarily in an autonomous community in northwestern Spain. The language is officially recognized by the Spanish government and used in various aspects of daily life including education, media and government communications.");
INSERT INTO "Language" ("id", "name", "description") VALUES (2, "English", "English is a West Germanic language that originated in England and is now the most widely used language in the world for international communication. It is the primary language used in the United Kingdom, the United States, Canada, Australia, and many other countries, and it is also widely spoken as a second language around the world. English is used for business, scientific, and technological purposes and is widely studied as a foreign language.");
INSERT INTO "Language" ("id", "name", "description") VALUES (3, "Spanish", "A Romance language with over 460 million speakers as a first language, Spanish originated in the Castilla region of Spain but is now widely spoken in many countries in the Americas. It has a rich history, evolving from a mix of Latin, Visigothic, and Mozarabic languages, and is now the official language of Spain. Spanish is widely used in various aspects of daily life, including education, media, government and commerce, and is also one of the six official languages of the United Nations.");

INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (1, "Galego", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (2, "Galician", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (3, "Gallego", "", 1);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (4, "English", "", 2);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (5, "Inglés", "", 2);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (6, "Castellano", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (7, "Castelán", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (8, "Castillian", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (9, "Español", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (10, "Espanhol", "", 3);
INSERT INTO "LanguageName" ("id", "name", "description", "id_language") VALUES (11, "Spanish", "", 3);

INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 1, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (2, 2, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (3, 3, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (4, 4, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (5, 5, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (6, 5, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (7, 6, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (8, 7, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (9, 8, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (10, 9, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (11, 9, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (12, 10, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (13, 11, 2);


INSERT INTO "Platform" ("id", "name", "description", "active") VALUES (1, "Telegram", "Telegram is a messaging app with a focus on speed and security, it’s super-fast, simple and free. You can use Telegram on all your devices at the same time — your messages sync seamlessly across any number of your phones, tablets or computers. Telegram has over 700 million monthly active users and is one of the 10 most downloaded apps in the world.\n\nWith Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc), as well as create groups for up to 200,000 people or channels for broadcasting to unlimited audiences. You can write to your phone contacts and find people by their usernames. As a result, Telegram is like SMS and email combined — and can take care of all your personal or business messaging needs. In addition to this, we support end-to-end encrypted voice and video calls, as well as voice chats in groups for thousands of participants.", 1);

INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (1, "Group Chat", "A Telegram chat is a feature within the Telegram app that enables users to communicate with each other in real-time. Chats can be either one-on-one or in a group with up to 200,000 members. In a Telegram chat, users can send text messages, photos, videos, files, and other types of media. The chat interface is user-friendly and supports features such as emoji, stickers, and Gifs to enhance the messaging experience. Telegram chats are encrypted end-to-end, ensuring that only the sender and receiver can access the content of the messages.", 1);
INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (2, "Channel", "A Telegram channel is a broadcast feature within the Telegram app that allows a user, group, or organization to broadcast messages to an unlimited number of subscribers. Unlike Telegram chats which are meant for direct communication between users, Telegram channels are meant for disseminating information to a large audience. Channel subscribers can receive notifications whenever a new message is posted and can also interact with the channel by sending comments and feedback. Channels can be used for various purposes such as sharing news, promoting products or services, or creating communities around a specific topic. Telegram channels are a useful tool for organizations and businesses to reach a large audience quickly and effectively.", 1);
INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (3, "Website", "A collection of web pages and related content, accessible via the internet, used for various purposes including personal, business, educational, and governmental purposes, and identified by a common domain name published on at least one web server.", 1);

COMMIT;