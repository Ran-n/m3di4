[//]: # ( -*- coding: utf-8 -*- )
[//]: # ( ---------------------------------------------------------------------- )
[//]: # (+ Autor:  	Ran# )
[//]: # (+ Creado: 	2023/02/24 19:09:59.057007 )
[//]: # (+ Editado:	2023/02/24 19:19:40.953329 )
[//]: # ( ---------------------------------------------------------------------- )

[↩️](index.md#documentation)

# Design Choices

## Index
- [Why are i18n description tables they way they are?](#why-are-i18n-description-tables-they-way-they-are?)

## Why are i18n description tables they way they are?
A typical i18n tableset for translating a description of a element "Element" would be: "ElementDescription", "ElementDescriptionLanguage".
But why does the [Language](tables.md#language) table have to be referenced in the second table, couldn't the foreign key be listed in the first one?

Tecnically, given a long enough text a description would be 100% in one language only.
Hence removing the need for the second table.
However, that is not the case, a description -though not typically- can be as short as one word long.
And this is to remain the same as per not compell verbosity, save useless data and confuse the user.

Nevertheless, it is true -and can be confirmed looking at the insert script- that in the real world use case the relationship between these two i18n tables is 1:1.
