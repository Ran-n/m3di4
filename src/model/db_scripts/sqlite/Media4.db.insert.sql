BEGIN TRANSACTION;

INSERT INTO "Language" ("id", "name", "description") VALUES (1, "Galician", "A Romance language with roots in medieval Latin, this is spoken by around 2.4 million people primarily in an autonomous community in northwestern Spain. The language is officially recognized by the Spanish government and used in various aspects of daily life including education, media and government communications.");
INSERT INTO "Language" ("id", "name", "description") VALUES (2, "English", "A West Germanic language that originated in England and is now the most widely used language in the world for international communication. It is the primary language used in the United Kingdom, the United States, Canada, Australia, and many other countries, and it is also widely spoken as a second language around the world. English is used for business, scientific, and technological purposes and is widely studied as a foreign language.");
INSERT INTO "Language" ("id", "name", "description") VALUES (3, "Spanish", "A Romance language with over 460 million speakers as a first language, Spanish originated in the Castilla region of Spain but is now widely spoken in many countries in the Americas. It has a rich history, evolving from a mix of Latin, Visigothic, and Mozarabic languages, and is now the official language of Spain. Spanish is widely used in various aspects of daily life, including education, media, government and commerce, and is also one of the six official languages of the United Nations.");

INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (1, "Galego", 1);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (2, "Galician", 1);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (3, "Gallego", 1);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (4, "English", 2);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (5, "Inglés", 2);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (6, "Spanish", 3);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (7, "Castillian", 3);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (8, "Español", 3);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (9, "Espanhol", 3);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (10, "Castelán", 3);
INSERT INTO "LanguageName" ("id", "name", "id_language") VALUES (11, "Castellano", 3);

INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (1, "A Romance language with roots in medieval Latin, this is spoken by around 2.4 million people primarily in an autonomous community in northwestern Spain. The language is officially recognized by the Spanish government and used in various aspects of daily life including education, media and government communications.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (2, "Unha lingua romance con raíces no latín medieval, esta é falada por aproximadamente 2,4 millóns de persoas principalmente nunha comunidade autónoma no noroeste de España. A lingua é oficialmente recoñecida polo goberno español e utilizada en varios aspectos da vida diaria, incluíndo educación, medios e comunicacións gubernamentais.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (3, "Un idioma romance con raíces en el latín medieval, se habla por alrededor de 2.4 millones de personas principalmente en una comunidad autónoma en el noroeste de España. El idioma es reconocido oficialmente por el gobierno español y se utiliza en varios aspectos de la vida diaria, incluyendo educación, medios y comunicaciones gubernamentales.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (4, "A West Germanic language that originated in England and is now the most widely used language in the world for international communication. It is the primary language used in the United Kingdom, the United States, Canada, Australia, and many other countries, and it is also widely spoken as a second language around the world. English is used for business, scientific, and technological purposes and is widely studied as a foreign language.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (5, "Idioma xermánico occidental que se originou en Inglaterra e agora é o idioma máis utilizado no mundo para a comunicación internacional. É o idioma principal usado no Reino Unido, Estados Unidos, Canadá, Australia e moitos outros países, e tamén se fala amplamente como segunda lingua en todo o mundo. O inglés usase para fins de negocios, científicos e tecnolóxicos e está amplamente estudado como lingua estranxeira.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (6, "Idioma germánico occidental que se originó en Inglaterra y es ahora el idioma más utilizado en el mundo para la comunicación internacional. Es el idioma principal utilizado en el Reino Unido, los Estados Unidos, Canadá, Australia y muchos otros países, y también se habla ampliamente como segundo idioma en todo el mundo. El inglés se utiliza para fines de negocios, científicos y tecnológicos y está ampliamente estudiado como idioma extranjero.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (7, "Romance language with over 460 million speakers as a first language, Spanish originated in the Castilla region of Spain but is now widely spoken in many countries in the Americas. It has a rich history, evolving from a mix of Latin, Visigothic, and Mozarabic languages, and is now the official language of Spain. Spanish is widely used in various aspects of daily life, including education, media, government and commerce, and is also one of the six official languages of the United Nations.", 3);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (8, "Lingua romance con máis de 460 millóns de falantes como lingua materna, o español originouse na rexión de Castilla de España, pero agora é amplamente falado en moitos países de América. Ten unha rica historia, evoluíndo a partir dunha mistura de latín, visigodo e mozárabe, e é agora a lingua oficial de España. O español é amplamente utilizado en varios aspectos da vida diaria, incluíndo educación, medios, goberno e comercio, e tamén é un dos seis idiomas oficiais das Nacións Unidas.", 3);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (9, "Idioma romance con más de 460 millones de hablantes como lengua materna, el español se originó en la región de Castilla de España, pero ahora se habla ampliamente en muchos países de América. Tiene una rica historia, evolucionando a partir de una mezcla de latín, visigodo y mozárabe, y es ahora el idioma oficial de España. El español se utiliza ampliamente en varios aspectos de la vida diaria, incluyendo educación, medios, gobierno y comercio, y es también uno de los seis idiomas oficiales de las Naciones Unidas.", 3);

INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 1, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 2, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 3, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 4, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 5, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 5, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 6, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 7, 2);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 8, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 8, 3);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 9, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 10, 1);
INSERT INTO "LanguageNameLanguage" ("id", "id_language_name", "id_language") VALUES (1, 11, 3);

INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 1, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 2, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 3, 3);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 4, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 5, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 6, 3);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 7, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 8, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id", "id_language_description", "id_language") VALUES (1, 9, 3);


INSERT INTO "Platform" ("id", "name", "description", "active") VALUES (1, "Telegram", "Telegram is a messaging app with a focus on speed and security, it’s super-fast, simple and free. You can use Telegram on all your devices at the same time — your messages sync seamlessly across any number of your phones, tablets or computers. Telegram has over 700 million monthly active users and is one of the 10 most downloaded apps in the world.\n\nWith Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc), as well as create groups for up to 200,000 people or channels for broadcasting to unlimited audiences. You can write to your phone contacts and find people by their usernames. As a result, Telegram is like SMS and email combined — and can take care of all your personal or business messaging needs. In addition to this, we support end-to-end encrypted voice and video calls, as well as voice chats in groups for thousands of participants.", 1);


INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (1, "Group Chat", "A Telegram chat is a feature within the Telegram app that enables users to communicate with each other in real-time. Chats can be either one-on-one or in a group with up to 200,000 members. In a Telegram chat, users can send text messages, photos, videos, files, and other types of media. The chat interface is user-friendly and supports features such as emoji, stickers, and Gifs to enhance the messaging experience. Telegram chats are encrypted end-to-end, ensuring that only the sender and receiver can access the content of the messages.", 1);
INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (2, "Channel", "A Telegram channel is a broadcast feature within the Telegram app that allows a user, group, or organization to broadcast messages to an unlimited number of subscribers. Unlike Telegram chats which are meant for direct communication between users, Telegram channels are meant for disseminating information to a large audience. Channel subscribers can receive notifications whenever a new message is posted and can also interact with the channel by sending comments and feedback. Channels can be used for various purposes such as sharing news, promoting products or services, or creating communities around a specific topic. Telegram channels are a useful tool for organizations and businesses to reach a large audience quickly and effectively.", 1);
INSERT INTO "ShareSiteType" ("id", "name", "description", "active") VALUES (3, "Website", "A collection of web pages and related content, accessible via the internet, used for various purposes including personal, business, educational, and governmental purposes, and identified by a common domain name published on at least one web server.", 1);

COMMIT;