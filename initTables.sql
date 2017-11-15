BEGIN TRANSACTION;

ALTER SEQUENCE managers_id_seq RESTART WITH 1;
INSERT INTO managers VALUES(DEFAULT, 'Jill');

ALTER SEQUENCE students_id_seq RESTART WITH 1;
INSERT INTO students VALUES(DEFAULT, 'Bob');

ALTER SEQUENCE writeUps_id_seq RESTART WITH 1;
INSERT INTO writeUps VALUES(DEFAULT, 'Beard', 'Did not shave.');
INSERT INTO writeUps VALUES(DEFAULT, 'sWoLiOsIs', 'Too big.');
INSERT INTO writeUps VALUES(DEFAULT, 'Jewelry', 'Too shiny');
INSERT INTO writeUps VALUES(DEFAULT, 'Nails', 'Too long.');

INSERT INTO occurs VALUES(1, 1, 1, to_date('2 Nov 2017', 'DD Mon YYYY'));
INSERT INTO occurs VALUES(1, 1, 2, to_date('2 Nov 2017', 'DD Mon YYYY'));
INSERT INTO occurs VALUES(1, 1, 3, to_date('2 Nov 2017', 'DD Mon YYYY'));

ALTER SEQUENCE jobs_id_seq RESTART WITH 1;
INSERT INTO jobs VALUES(DEFAULT, 'server', 'Serves food');

ALTER SEQUENCE areas_id_seq RESTART WITH 1;
INSERT INTO areas VALUES(DEFAULT, 'Wok', 'Bad Asian Food');

ALTER SEQUENCE days_id_seq RESTART WITH 1;
INSERT INTO days VALUES(DEFAULT, 'Monday');
INSERT INTO days VALUES(DEFAULT, 'Tuesday');
INSERT INTO days VALUES(DEFAULT, 'Wednesday');
INSERT INTO days VALUES(DEFAULT, 'Thursday');
INSERT INTO days VALUES(DEFAULT, 'Friday1');
INSERT INTO days VALUES(DEFAULT, 'Friday2');
INSERT INTO days VALUES(DEFAULT, 'Saturday1');
INSERT INTO days VALUES(DEFAULT, 'Saturday2');
INSERT INTO days VALUES(DEFAULT, 'Sunday1');
INSERT INTO days VALUES(DEFAULT, 'Sunday2');

INSERT INTO works VALUES(1, 4, '01:00 PM'::time, 1, 1);

COMMIT;