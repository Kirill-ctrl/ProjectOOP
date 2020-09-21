CREATE TABLE question_list(
    id SERIAL PRIMARY KEY,
    code SMALLINT UNIQUE NOT NULL
)

CREATE TABLE question(
    id SERIAL PRIMARY KEY,
    quest_text TEXT NOT NULL,
    question_list_id BIGINT REFERENCES question_list(id)
)

INSERT INTO question_list(code) VALUES
	(100),
	(200),
	(300),
    (400)

INSERT INTO question(quest_text, question_list_id) VALUES
('Python - интерпретируемый язык?', 1)
('В чем отличие Flask от Django?', 1)
('Как называются хеш-таблицы в Python?', 1),
('Как работает асинхронность в Python?', 1),
('Как осуществляется тестирование в Python?', 1),
('Как осуществляется отладка в Python?', 1)

INSERT INTO question(quest_text, question_list_id) VALUES
('Знания HTML', 2),
('Знания CSS', 2),
('Знания JS', 2),
('Фремфорки JS и для чего они нужны?', 2)

INSERT INTO question(quest_text, question_list_id) VALUES
('Основные методы HTTP', 3),
('Протокол FTP', 3),
('Для чего нужен Postman?', 3),
('Как осуществляется работа приложения через Ajax', 3),
('Что такое SPA?', 3)

INSERT INTO question(quest_text, question_list_id) VALUES
('Для чего нужен GIT?', 4),
('Отслеживаемая и неотслеживаемые зоны', 4),
('Какие бывают виды конфликтов?', 4),
('Как скопировать к себе сразу все содержимое с удаленного источника?', 4)


CREATE TABLE employer(
	id SERIAL PRIMARY KEY,
	employer_name varchar(32) NOT NULL,
	city varchar(32) NOT NULL
)

INSERT INTO employer(employer_name, city)
VALUES
('Dmitry', 'Kazan'),
('Maria', 'Kazan'),
('Nasty', 'Perm'),
('Clavdia', 'Dobryanka'),
('Stella', 'Omsk'),
('Darya', 'Sochi')


CREATE TABLE applicant(
	id SERIAL PRIMARY KEY,
	applicant_name varchar(32) NOT NULL,
	city varchar(32) NOT NULL,
	age INTEGER NOT NULL,
	email text NOT NULL,
	question_list_code SMALLINT REFERENCES question_list(code),
	employer_id BIGINT REFERENCES employer(id)
	accept BOOL NOT NULL DEFAULT FALSE
)


INSERT INTO applicant(applicant_name, city, age, email)
VALUES
('Kirill', 'Kazan', 18, 'k.pechurin02@mail.ru'),
('Sasha', 'Kazan', 18, 'sasha@mail.ru'),
('Danil', 'Perm', 20, 'danil@mail.ru'),
('Dmitry', 'Sochi', 40, 'dmitry@mail.ru'),
('Tanya', 'Moscow', 27, 'tanya@mail.ru')


CREATE TABLE answer(
    user_id INTEGER REFERENCES applicant(id),
    text_answer text,
    id_quest INTEGER REFERENCES question(id)
)


CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	name text NOT NULL,
	email text UNIQUE NOT NULL,
	psw text NOT NULL,
	status text NOT NULL,
	login BOOL NOT NULL DEFAULT FALSE
)

CREATE TABLE token(
	id SERIAL PRIMARY KEY,
	token_text text NOT NULL,
	user_id BIGINT REFERENCES users(id)
)



ALTER TABLE applicant
ADD COLUMN users_id REFERENCES users(id)


ALTER TABLE employer
ADD COLUMN users_id REFERENCES users(id)

ALTER TABLE token
ADD COLUMN token_status boolean;
ADD COLUMN token_time timestamp;
ADD COLUMN save_temp date;

