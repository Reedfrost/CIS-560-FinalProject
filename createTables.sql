BEGIN TRANSACTION;

DROP TABLE IF EXISTS works;
DROP TABLE IF EXISTS occurs;
DROP TABLE IF EXISTS offenders;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS managers;
DROP TABLE IF EXISTS writeUps;
DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS areas;
DROP TABLE IF EXISTS days;

CREATE TABLE students(
	id		serial PRIMARY KEY,
	name	text NOT NULL
);

CREATE TABLE managers(
	id			serial PRIMARY KEY,
	name		text NOT NULL,
	username	text NOT NULL,
	password	text NOT NULL,
	CONSTRAINT username_uq UNIQUE(username)
);

CREATE TABLE writeUps(
	id		serial PRIMARY KEY,
	name	text NOT NULL,
	descr	text,
	CONSTRAINT names_uq2 UNIQUE (name)
);

CREATE TABLE offenders(
	sID		int NOT NULL,
	dTime	timestamp NOT NULL,
	CONSTRAINT sID_uq1 UNIQUE(sID),
	CONSTRAINT sID_fk1 FOREIGN KEY(sID) REFERENCES students(id) ON DELETE CASCADE
);

CREATE TABLE occurs(
	mID		int NOT NULL,
	sID		int NOT NULL,
	wID		int NOT NULL,
	dTime	date NOT NULL,
	CONSTRAINT all_uq1 UNIQUE (mID, sID, wID, dTime),
	CONSTRAINT mID_fk1 FOREIGN KEY (mID) REFERENCES managers(id),
	CONSTRAINT sID_fk2 FOREIGN KEY (sID) REFERENCES students(id) ON DELETE CASCADE,
	CONSTRAINT wID_fk2 FOREIGN KEY (wID) REFERENCES writeUps(id)
);

CREATE TABLE jobs(
	id     serial PRIMARY KEY,
	name   text NOT NULL,
	descr  text,
	CONSTRAINT names_uq3 UNIQUE(name)
);

CREATE TABLE areas(
	id     serial PRIMARY KEY,
	name   text NOT NULL,
	descr  text,
	CONSTRAINT names_uq4 UNIQUE(name)
);

CREATE TABLE days(
	id     serial PRIMARY KEY,
	name   text NOT NULL,
	CONSTRAINT name_uq5 UNIQUE(name)
);

CREATE TABLE works(
	sID    int NOT NULL,
	dID    int NOT NULL,
	strt   time NOT NULL,
	fnsh   time NOT NULL,
	aID    int NOT NULL,
	jID    int NOT NULL,
	CONSTRAINT all_uq2 UNIQUE(sID, dID, strt, fnsh),
	CONSTRAINT sID_fk3 FOREIGN KEY(sID) REFERENCES students(id) ON DELETE CASCADE,
	CONSTRAINT dID_fk1 FOREIGN KEY(dID) REFERENCES days(id),
	CONSTRAINT aID_fk1 FOREIGN KEY(aID) REFERENCES areas(id),
	CONSTRAINT jID_fk1 FOREIGN KEY(jID) REFERENCES jobs(id)
);

COMMIT;





BEGIN TRANSACTION;

DROP TRIGGER IF EXISTS trig_sani_writeUp ON writeUps;
DROP TRIGGER IF EXISTS trig_sani_job ON jobs;
DROP TRIGGER IF EXISTS trig_sani_area ON areas;
DROP TRIGGER IF EXISTS trig_sani_day ON days;
DROP TRIGGER IF EXISTS trig_occurs ON occurs;

CREATE OR REPLACE FUNCTION sanitize_text (rawWriteUp text) RETURNS text AS $$
	DECLARE newString text;
	BEGIN
		newString := LOWER(rawWriteUp);
		newString := regexp_replace(newString, '[^a-zA-Z0123456789]', '', 'g');
		RETURN  newString;
	END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION sanitize_name() RETURNS trigger AS $$
	BEGIN
		NEW.name = sanitize_text(NEW.name);
		RETURN NEW;
	END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_sani_writeUp
BEFORE INSERT ON writeUps
FOR EACH ROW EXECUTE PROCEDURE sanitize_name();

CREATE TRIGGER trig_sani_job
BEFORE INSERT ON jobs
FOR EACH ROW EXECUTE PROCEDURE sanitize_name();

CREATE TRIGGER trig_sani_area
BEFORE INSERT ON areas
FOR EACH ROW EXECUTE PROCEDURE sanitize_name();

CREATE TRIGGER trig_sani_day
BEFORE INSERT ON days
FOR EACH ROW EXECUTE PROCEDURE sanitize_name();

CREATE OR REPLACE FUNCTION count_strikes (id int) RETURNS int AS $$
	BEGIN
		RETURN (SELECT COUNT(*) FROM occurs WHERE sID=id GROUP BY sID);
	END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_strikes () RETURNS trigger AS $$
	BEGIN
		IF (count_strikes(NEW.sID) = 3) THEN
			INSERT INTO offenders VALUES (NEW.sID, NEW.dTime);
		END IF;
		RETURN NEW;
	END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_occurs
AFTER INSERT ON occurs
FOR EACH ROW EXECUTE PROCEDURE check_strikes();

COMMIT;
