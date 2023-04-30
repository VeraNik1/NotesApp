# Задание 1. Приложение заметки (Python)

## Информация о проекте

Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.

## Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.

## Задание

Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.

# Project description

## The application has several options:

1. Add a new note
2. Show all notes
3. Update note's title or description
4. Delete the note 
5. Find the note (by id or by text from title or description)

## Class Menu

Class menu has the method show() which shows all possible options for work with the notes and asks users option choice. 

Every option calls the conforming method from class NotesApp

## Class Note

It's a note which has 5 properties (fields): identificator (id), title, description (body), date and time of creation (created_at), date and time of last update (updated_at).
Also it has method edit() for note's title and description updating.

## Class NotesApp

It is the application for work with notes.
It has 10 following methods:

- init(): initial method which takes file's name (*.csv) to make or find file for saving and loading notes. (For example notes.csv); 
- load_notes(): method which loads notes from csv-file;
- save_notes(): method which saves notes to csv-file; 
- add_note(): method which adds a new note to self.notes list from class NotesApp and to csv-file; 
- show_notes(): method which shows all notes from self.notes list;
- find_note_by_id(): method which helps to find note by id in self.notes list;
- find_note_by_text(): method which helps to find note by text from title or description in self.notes list;
- edit_note_by_id(): method which helps to change note title and note description by note id in self.notes list and then rewrite csv-file;
- delete_note_by_id(): method which helps to delete note by id from self.notes list and then rewrite csv-file;
- get_max_id(): method which helps to find maximum id in the list self.notes in class NotesApp. 

