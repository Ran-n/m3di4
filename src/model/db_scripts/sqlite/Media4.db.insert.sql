BEGIN TRANSACTION;

INSERT INTO "Language" ("id", "name") VALUES (1, "Galician");
INSERT INTO "Language" ("id", "name") VALUES (2, "English");
INSERT INTO "Language" ("id", "name") VALUES (3, "Spanish");

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

INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (1, 1);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (2, 2);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (3, 3);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (4, 2);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (5, 1);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (5, 3);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (6, 2);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (7, 2);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (8, 1);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (8, 3);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (9, 1);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (10, 1);
INSERT INTO "LanguageNameLanguage" ("id_language_name", "id_language") VALUES (11, 3);

INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (1, "A Romance language with roots in medieval Latin, this is spoken by around 2.4 million people primarily in an autonomous community in northwestern Spain. The language is officially recognized by the Spanish government and used in various aspects of daily life including education, media and government communications.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (2, "Unha lingua romance con raíces no latín medieval, esta é falada por aproximadamente 2,4 millóns de persoas principalmente nunha comunidade autónoma no noroeste de España. A lingua é oficialmente recoñecida polo goberno español e utilizada en varios aspectos da vida diaria, incluíndo educación, medios e comunicacións gubernamentais.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (3, "Un idioma romance con raíces en el latín medieval, se habla por alrededor de 2.4 millones de personas principalmente en una comunidad autónoma en el noroeste de España. El idioma es reconocido oficialmente por el gobierno español y se utiliza en varios aspectos de la vida diaria, incluyendo educación, medios y comunicaciones gubernamentales.", 1);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (4, "A West Germanic language that originated in England and is now the most widely used language in the world for international communication. It is the primary language used in the United Kingdom, the United States, Canada, Australia, and many other countries, and it is also widely spoken as a second language around the world. English is used for business, scientific, and technological purposes and is widely studied as a foreign language.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (5, "Idioma xermánico occidental que se originou en Inglaterra e agora é o idioma máis utilizado no mundo para a comunicación internacional. É o idioma principal usado no Reino Unido, Estados Unidos, Canadá, Australia e moitos outros países, e tamén se fala amplamente como segunda lingua en todo o mundo. O inglés usase para fins de negocios, científicos e tecnolóxicos e está amplamente estudado como lingua estranxeira.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (6, "Idioma germánico occidental que se originó en Inglaterra y es ahora el idioma más utilizado en el mundo para la comunicación internacional. Es el idioma principal utilizado en el Reino Unido, los Estados Unidos, Canadá, Australia y muchos otros países, y también se habla ampliamente como segundo idioma en todo el mundo. El inglés se utiliza para fines de negocios, científicos y tecnológicos y está ampliamente estudiado como idioma extranjero.", 2);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (7, "Romance language with over 460 million speakers as a first language, Spanish originated in the Castilla region of Spain but is now widely spoken in many countries in the Americas. It has a rich history, evolving from a mix of Latin, Visigothic, and Mozarabic languages, and is now the official language of Spain. Spanish is widely used in various aspects of daily life, including education, media, government and commerce, and is also one of the six official languages of the United Nations.", 3);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (8, "Lingua romance con máis de 460 millóns de falantes como lingua materna, o español originouse na rexión de Castilla de España, pero agora é amplamente falado en moitos países de América. Ten unha rica historia, evoluíndo a partir dunha mistura de latín, visigodo e mozárabe, e é agora a lingua oficial de España. O español é amplamente utilizado en varios aspectos da vida diaria, incluíndo educación, medios, goberno e comercio, e tamén é un dos seis idiomas oficiais das Nacións Unidas.", 3);
INSERT INTO "LanguageDescription" ("id", "description", "id_language") VALUES (9, "Idioma romance con más de 460 millones de hablantes como lengua materna, el español se originó en la región de Castilla de España, pero ahora se habla ampliamente en muchos países de América. Tiene una rica historia, evolucionando a partir de una mezcla de latín, visigodo y mozárabe, y es ahora el idioma oficial de España. El español se utiliza ampliamente en varios aspectos de la vida diaria, incluyendo educación, medios, gobierno y comercio, y es también uno de los seis idiomas oficiales de las Naciones Unidas.", 3);

INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (1, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (2, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (3, 3);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (4, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (5, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (6, 3);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (7, 2);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (8, 1);
INSERT INTO "LanguageDescriptionLanguage" ("id_language_description", "id_language") VALUES (9, 3);





INSERT INTO "Platform" ("id", "active", "name") VALUES (1, 1, "Telegram");

INSERT INTO "PlatformDescription" ("id", "description", "id_platform") VALUES (1, "Telegram is a messaging app with a focus on speed and security, it’s super-fast, simple and free. You can use Telegram on all your devices at the same time — your messages sync seamlessly across any number of your phones, tablets or computers. Telegram has over 700 million monthly active users and is one of the 10 most downloaded apps in the world.\n\nWith Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc), as well as create groups for up to 200,000 people or channels for broadcasting to unlimited audiences. You can write to your phone contacts and find people by their usernames. As a result, Telegram is like SMS and email combined — and can take care of all your personal or business messaging needs. In addition to this, we support end-to-end encrypted voice and video calls, as well as voice chats in groups for thousands of participants.", 1);
INSERT INTO "PlatformDescription" ("id", "description", "id_platform") VALUES (2, "Telegram é unha aplicación de mensaxería con enfoque na velocidade e seguridade, é super rápida, simple e de balde. Podes usar Telegram en todos os teus dispositivos ao mesmo tempo, as túas mensaxes sincronízanse perfectamente en calquera número dos teus teléfonos, tablets ou ordenadores. Telegram ten máis de 700 millóns de usuarios activos mensuais e é unha das 10 aplicacións máis descargadas do mundo.\n\nCon Telegram, podes enviar mensaxes, fotos, vídeos e arquivos de calquera tipo (doc, zip, mp3, etc), así como crear grupos de ata 200.000 persoas ou canles para emitir para audiencias ilimitadas. Podes escribir aos teus contactos do teléfono e atopar xente polos seus nomes de usuario. Como resultado, Telegram é como se combinan as mensaxes de SMS e correo electrónico e pode encargarse de todas as túas necesidades de mensaxería persoais ou comerciais. Ademais, compatibilizamos chamadas de voz e vídeo cifradas de extremo a extremo, así como conversas de voz en grupos de miles de participantes.", 1);
INSERT INTO "PlatformDescription" ("id", "description", "id_platform") VALUES (3, "Telegram es una aplicación de mensajería con un enfoque en la velocidad y la seguridad, es súper rápida, simple y gratuita. Puedes usar Telegram en todos tus dispositivos al mismo tiempo: tus mensajes se sincronizan perfectamente en cualquier número de tus teléfonos, tabletas o computadoras. Telegram cuenta con más de 700 millones de usuarios activos mensuales y es una de las 10 aplicaciones más descargadas del mundo.\n\nCon Telegram, puedes enviar mensajes, fotos, videos y archivos de cualquier tipo (doc, zip, mp3, etc.), así como crear grupos de hasta 200.000 personas o canales para transmitir a audiencias ilimitadas. Puedes escribir a tus contactos del teléfono y encontrar personas por sus nombres de usuario. Como resultado, Telegram es como si se combinan los mensajes de SMS y correo electrónico y puede encargarse de todas tus necesidades de mensajería personales o comerciales. Además, admitimos llamadas de voz y video cifradas de extremo a extremo, así como chats de voz en grupos para miles de participantes.", 1);

INSERT INTO "PlatformDescriptionLanguage" ("id_platform_description", "id_language") VALUES (1, 2);
INSERT INTO "PlatformDescriptionLanguage" ("id_platform_description", "id_language") VALUES (2, 1);
INSERT INTO "PlatformDescriptionLanguage" ("id_platform_description", "id_language") VALUES (3, 3);





INSERT INTO "ShareSiteType" ("id", "active", "name") VALUES (1, 1, "Group Chat");
INSERT INTO "ShareSiteType" ("id", "active", "name") VALUES (2, 1, "Channel");
INSERT INTO "ShareSiteType" ("id", "active", "name") VALUES (3, 1, "Website");

INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (1, "Group Chat", 1);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (2, "Chat grupal", 1);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (3, "Chat de grupo", 1);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (4, "Channel", 2);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (5, "Canle", 2);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (6, "Canal", 2);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (7, "Website", 3);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (8, "Páxina web", 3);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (9, "Web", 3);
INSERT INTO "ShareSiteTypeName" ("id", "name", "id_share_site_type") VALUES (10, "Página web", 3);

INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (1, 2);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (2, 1);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (2, 3);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (3, 2);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (3, 3);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (4, 2);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (5, 1);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (6, 3);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (7, 2);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (8, 1);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (9, 1);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (9, 3);
INSERT INTO "ShareSiteTypeNameLanguage" ("id_share_site_type_name", "id_language") VALUES (10, 3);


INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (1, "A Telegram chat is a feature within the Telegram app that enables users to communicate with each other in real-time. Chats can be either one-on-one or in a group with up to 200,000 members. In a Telegram chat, users can send text messages, photos, videos, files, and other types of media. The chat interface is user-friendly and supports features such as emoji, stickers, and Gifs to enhance the messaging experience. Telegram chats are encrypted end-to-end, ensuring that only the sender and receiver can access the content of the messages.", 1);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (2, "Unha conversa ou 'chat' de Telegram é unha función dentro da aplicación Telegram que permite aos usuarios comunicarse en tempo real. As conversas poden ser individuais ou en grupo con ata 200.000 membros. Nunha conversa de Telegram, os usuarios poden enviar mensaxes de texto, fotos, vídeos, ficheiros e outros tipos de contido multimedia. A interface da conversa é fácil de usar e admite características como emoticonos, pegatinas e GIFs para mellorar a experiencia de mensaxería. As conversas de Telegram están cifradas de extremo a extremo, garantindo que só o emisor e o receptor poidan acceder ao contido das mensaxes.", 1);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (3, "Un chat de Telegram es una función dentro de la aplicación de Telegram que permite a los usuarios comunicarse en tiempo real. Los chats pueden ser individuales o en grupo con hasta 200.000 miembros. En un chat de Telegram, los usuarios pueden enviar mensajes de texto, fotos, videos, archivos y otros tipos de contenido multimedia. La interfaz del chat es fácil de usar y admite características como emojis, pegatinas y GIF para mejorar la experiencia de mensajería. Los chats de Telegram están cifrados de extremo a extremo, garantizando que solo el emisor y el receptor puedan acceder al contenido de los mensajes.", 1);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (4, "A Telegram channel is a broadcast feature within the Telegram app that allows a user, group, or organization to broadcast messages to an unlimited number of subscribers. Unlike Telegram chats which are meant for direct communication between users, Telegram channels are meant for disseminating information to a large audience. Channel subscribers can receive notifications whenever a new message is posted and can also interact with the channel by sending comments and feedback. Channels can be used for various purposes such as sharing news, promoting products or services, or creating communities around a specific topic. Telegram channels are a useful tool for organizations and businesses to reach a large audience quickly and effectively.", 2);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (5, "Un canal de Telegram é unha función de difusión dentro da aplicación de Telegram que permite a un usuario, grupo ou organización transmitir mensaxes a un número ilimitado de subscritores. Ao contrario dos chats de Telegram, que están destinados á comunicación directa entre usuarios, os canais de Telegram están destinados a difundir información a unha gran audiencia. Os subscritores do canal poden recibir notificacións cada vez que se publique unha nova mensaxe e tamén poden interactuar co canal enviando comentarios e feedback. Os canais poden ser utilizados para diversos fins, como compartir noticias, promocionar produtos ou servizos ou crear comunidades en torno a un tema específico. Os canais de Telegram son unha ferramenta útil para organizacións e empresas para chegar a unha gran audiencia de forma rápida e eficaz.", 2);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (6, "Un canal de Telegram es una función de difusión dentro de la aplicación de Telegram que permite a un usuario, grupo u organización transmitir mensajes a un número ilimitado de suscriptores. A diferencia de los chats de Telegram, que están destinados a la comunicación directa entre usuarios, los canales de Telegram están destinados a difundir información a una gran audiencia. Los suscriptores del canal pueden recibir notificaciones cada vez que se publique un nuevo mensaje y también pueden interactuar con el canal enviando comentarios y feedback. Los canales pueden ser utilizados para diversos fines, como compartir noticias, promocionar productos o servicios o crear comunidades en torno a un tema específico. Los canales de Telegram son una herramienta útil para organizaciones y empresas para llegar a una gran audiencia de forma rápida y efectiva.", 2);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (7, "A collection of web pages and related content, accessible via the internet, used for various purposes including personal, business, educational, and governmental purposes, and identified by a common domain name published on at least one web server.", 3);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (8, "Unha colección de páxinas web e contido relacionado, accesible a través de internet, usado para diversos fins, incluíndo persoais, empresariais, educativos e gobernamentais, e identificado por un nome de dominio común publicado en polo menos un servidor web.", 3);
INSERT INTO "ShareSiteTypeDescription" ("id", "description", "id_share_site_type") VALUES (9, "Una colección de páginas web y contenido relacionado, accesible a través de internet, utilizado para diversos fines, incluyendo personales, empresariales, educativos y gubernamentales, e identificado por un nombre de dominio común publicado en al menos un servidor web.", 3);

INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (1, 2);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (2, 1);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (3, 3);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (4, 2);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (5, 1);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (6, 3);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (7, 2);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (8, 1);
INSERT INTO "ShareSiteTypeDescriptionLanguage" ("id_share_site_type_description", "id_language") VALUES (9, 3);





INSERT INTO "Web" ("id", "active", "acronym", "name", "name_long", "link") VALUES (1, 1, "tmdb", "TMDB", "The Movie Database", "https://www.themoviedb.org/");
INSERT INTO "Web" ("id", "active", "acronym", "name", "name_long", "link") VALUES (2, 1, "imdb", "IMDb", "Internet Movie Database", "https://www.imdb.com/");
INSERT INTO "Web" ("id", "active", "acronym", "name", "name_long", "link") VALUES (3, 1, "tvdb", "TheTVDB", "The TV Database", "https://thetvdb.com/");
INSERT INTO "Web" ("id", "active", "acronym", "name", "name_long", "link") VALUES (4, 1, "omdb", "OMDb", "The Open Movie Database", "https://www.omdbapi.com/");

INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (1, "Community built movie and TV database. Every piece of data has been added by our amazing community dating back to 2008. TMDB's strong international focus and breadth of data is largely unmatched and something we're incredibly proud of. Put simply, we live and breathe community and that's precisely what makes us different.", 1);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (2, "Unha base de datos de cine e televisión construída pola comunidade. Cada peza de datos foi engadida pola nosa sorprendente comunidade desde 2008. O enfoque internacional sólido de TMDB e a ampla cobertura de datos é en gran parte sen igual, e é algo do que estamos moi orgullosos. En resumo, vivimos e respiramos a comunidade, e é precisamente iso o que nos fai diferentes.", 1);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (3, "Una base de datos de películas y televisión construida por la comunidad. Cada pieza de datos ha sido agregada por nuestra increíble comunidad desde 2008. El sólido enfoque internacional y la amplitud de datos de TMDB son en gran parte inigualables y es algo de lo que estamos muy orgullosos. En resumen, vivimos y respiramos la comunidad, y eso es precisamente lo que nos hace diferentes.", 1);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (4, "Launched online in 1990 and a subsidiary of Amazon.com since 1998, IMDb is the world's most popular and authoritative source for movie, TV and celebrity content, designed to help fans explore the world of movies and shows and decide what to watch.\nOur searchable database includes millions of movies, TV and entertainment programs and cast and crew members.", 2);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (5, "Lanzada en liña en 1990 e filial de Amazon.com desde 1998, IMDb é a fonte de contido de cine, televisión e celebridades máis popular e autorizada do mundo, deseñada para axudar aos fans a explorar o mundo dos filmes e programas e decidir que ver. A nosa base de datos buscable inclúe millóns de películas, programas de televisión e entretemento e membros do elenco e equipo técnico.", 2);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (6, "Lanzada en línea en 1990 y subsidiaria de Amazon.com desde 1998, IMDb es la fuente de contenido de cine, televisión y celebridades más popular y autorizada del mundo, diseñada para ayudar a los fans a explorar el mundo de las películas y programas y decidir qué ver. Nuestra base de datos buscable incluye millones de películas, programas de televisión y entretenimiento y miembros del elenco y equipo técnico.", 2);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (7, "Founded in 2006, TheTVDB is one of the longest-running community-driven TV and Movie databases. With content metadata available for 138,000+ TV Series and 330,000+ movies, TheTVDB is a complete and accurate, yet affordable entertainment metadata solution.\n\nThousands of developers use our digital media metadata API to power their apps, utilities, and projects, generating over 1 billion API calls per day on average.", 3);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (8, "Fundada en 2006, TheTVDB é unha das bases de datos de televisión e cine impulsadas pola comunidade máis antigas. Con metadatos de contido dispoñibles para máis de 138.000 series de televisión e 330.000 películas, TheTVDB é unha solución de metadatos de entretemento completa, precisa e asequible.\n\nMiles de desenvolvedores utilizan a nosa API de metadatos de medios dixitais para alimentar as súas aplicacións, utilidades e proxectos, xerando en promedio máis de 1 billón de chamadas de API por día.", 3);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (9, "Fundada en 2006, TheTVDB es una de las bases de datos de televisión y cine impulsadas por la comunidad más antiguas. Con metadatos de contenido disponibles para más de 138,000 series de televisión y 330,000 películas, TheTVDB es una solución de metadatos de entretenimiento completa, precisa y asequible.\n\nMiles de desarrolladores utilizan nuestra API de metadatos de medios digitales para alimentar sus aplicaciones, utilidades y proyectos, generando en promedio más de 1 billón de llamadas de API por día.", 3);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (10, "The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.", 4);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (11, "La API de OMDb é un servizo web RESTful para obter información de películas, todo o contido e imaxes no sitio son contribuídos e mantidos polos nosos usuarios.", 4);
INSERT INTO "WebDescription" ("id", "description", "id_web") VALUES (12, "La API de OMDb es un servicio web RESTful para obtener información de películas, todo el contenido e imágenes en el sitio son contribuidos y mantenidos por nuestros usuarios.", 4);

INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (1, 2);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (2, 1);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (3, 3);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (4, 2);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (5, 1);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (6, 3);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (7, 2);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (8, 1);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (9, 3);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (10, 2);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (11, 1);
INSERT INTO "WebDescriptionLanguage" ("id_web_description", "id_language") VALUES (12, 3);

COMMIT;