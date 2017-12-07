-- Function #1:
-- Get word from space-delimited phrases
CREATE OR REPLACE FUNCTION get_word (raw_text text, index int) RETURNS text AS $$
	BEGIN
		RETURN SPLIT_PART(LOWER(raw_text), ' ', index);
	END;
$$ LANGUAGE plpgsql;

-- Function #2:
-- Translate date and schedule to day of week.
CREATE OR REPLACE FUNCTION get_day_of_week (first_day date, current_day date) RETURNS int AS $$
  DECLARE week int;
          day_of_week int;
	BEGIN
		day_of_week := EXTRACT(isodow FROM current_day);
    week = ROUND(EXTRACT(days FROM age(current_day, first_day)) / 7)::int % 2;
    CASE day_of_week
      WHEN 5 THEN
        RETURN 5 + week;
      WHEN 6 THEN
        RETURN 7 + week;
      WHEN 7 THEN
        RETURN 9 + week;
      ELSE
        RETURN day_of_week;
    END CASE;
	END;
$$ LANGUAGE plpgsql;

-- Report #1:
-- Replace ids with names in the occurs table to make it more readable
SELECT m.name as manager, s.name as student, w.name as write_up, to_char(o.day, 'DD-Mon-YYYY') as assign_time
FROM occurs o
JOIN managers m ON o.mid = m.id
JOIN students s ON o.sid = s.id
JOIN writeUps w ON o.wid = w.id
ORDER BY o.day;

-- Report #2:
-- Replace ids with names in the works table to make it more readable
SELECT s.name as student, d.name as day, to_char(w.strt, 'HH:MI:SS AM') as start, to_char(w.fnsh, 'HH:MI:SS AM') as finish, a.name as area, j.name as job
FROM works w
JOIN students s ON w.sid = s.id
JOIN days d ON w.did = d.id
JOIN areas a ON w.aid = a.id
JOIN jobs j ON w.jid = j.id
ORDER BY w.did, w.strt;

-- Report #3:
-- Get all write ups for all students that work together
SELECT m.name as manager, s.name as student, wr.name as write_up, to_char(o.day, 'DD-Mon-YYYY') as assign_time, d.name as work_day, a.name as work_area, to_char(o.strt, 'HH:MI:SS AM') as work_time
FROM (SELECT o.mid, w.sid, o.wid, o.day, w.did, w.aid, w.strt
      FROM occurs o
      RIGHT JOIN (SELECT w1.sid, w1.did, w1.aid, w1.strt
                  FROM works w1
                  JOIN works w2 ON w1.aid = w2.aid AND w1.did = w2.did AND w1.strt = w2.strt AND NOT w1.sid = w2.sid) w
      ON o.sid = w.sid) o
LEFT JOIN managers m ON o.mid = m.id
LEFT JOIN students s ON o.sid = s.id
LEFT JOIN writeUps wr ON o.wid = wr.id
LEFT JOIN days d ON o.did = d.id
LEFT JOIN areas a ON o.aid = a.id
ORDER BY o.did, a.name, o.strt;

-- Report #4:
-- Get the schedules of students who have been put on the offenders table
SELECT s.name as student, d.name as day, to_char(w.strt, 'HH:MI:SS AM') as start, to_char(w.fnsh, 'HH:MI:SS AM') as finish, a.name as area, j.name as job, to_char(o.day, 'DD-Mon-YYYY') as strike_date
FROM works w
JOIN offenders o ON w.sid = o.sid
JOIN students s ON w.sid = s.id
JOIN days d ON w.did = d.id
JOIN areas a ON w.aid = a.id
JOIN jobs j ON w.jid = j.id
ORDER BY w.did, w.strt;

-- Report #5:
-- Get the number of strikes on each day of the week
SELECT d.name as day, c.count as count
FROM (SELECT d.id as day, COUNT(*) as count
      FROM occurs o
      JOIN days d ON get_day_of_week('21 Aug 2017', o.day) = d.id
      GROUP BY d.id) c
JOIN days d ON c.day = d.id
ORDER BY c.count DESC;


-- Query #1:
-- Find the name of a specific student
SELECT name
FROM students
WHERE id = {};

-- Query #2:
-- Find the name of a specific writeup
SELECT name
FROM writeUps
WHERE id = {};

-- Query #3:
-- Find the IDs of students with a specific first name
SELECT id
FROM students
WHERE LOWER('{}') like get_word(name, 1);

-- Query #4:
-- Get the number of writeups for students with a specific first name
SELECT s.id as student, COUNT(*)
FROM students s
JOIN occurs o ON s.id = o.sid
WHERE LOWER('{}') like get_word(s.name, 1)
GROUP BY s.id;

-- Query #5:
-- Validate a manager's login credentials
SELECT id
FROM managers
WHERE username = '{}' AND password = '{}';

-- Query #6:
-- Which write ups a manager uses and how many times
SELECT o.mid as manager, o.wid as write_up, COUNT(*)
FROM occurs
WHERE o.mid = {}
GROUP BY o.mid, o.wid
ORDER BY o.wid;

-- Query #7:
-- Which students a manager has written up and how many times
SELECT o.mid as manager, o.sid as student, COUNT(*)
FROM occurs o
WHERE o.mid = {}
GROUP BY o.mid, o.sid
ORDER BY o.sid;

-- Query #8:
-- Which write ups a student receives and how many times
SELECT o.sid as student, o.wid as write_up, COUNT(*)
FROM occurs o
WHERE o.sid = {}
GROUP BY o.sid, o.wid
ORDER BY s.name;

-- Query #9:
-- Get all the students with a certain number of strikes
SELECT c.sid as student
FROM (
    SELECT sid, COUNT(*) as count
    FROM occurs
    GROUP BY sid
) c
WHERE c.count = {}

-- Query 10:
-- Get all the write ups given to a student on the day they work
SELECT o.mid AS manager, o.sid AS student, o.wid AS write_up, o.day AS assign_date, w.did AS assign_day, w.strt AS start, w.fnsh AS finish, w.aid AS area, w.jid AS job
FROM occurs o
JOIN works w ON o.sid = w.sid AND get_day_of_week('21 Aug 2017', o.day) = w.did
WHERE o.sid = {};

-- Query Extra:
-- Get all the write ups assigned to a student with a specific first name on the day they work
SELECT m.name AS manager, s.name AS student, w.name AS write_up, to_char(o.day, 'DD Mon YYYY') AS assignwork_date, d.name AS assignwork_day, to_char(o.strt, 'HH:MI:SS AM') AS start, to_char(o.fnsh, 'HH:MI:SS AM') AS finish, a.name AS area, j.name AS job
FROM (SELECT o.mid, o.sid, o.wid, o.day, w.did, w.strt, w.fnsh, w.aid, w.jid
      FROM occurs o
      JOIN works w ON o.sid = w.sid AND get_day_of_week('21 Aug 2017', o.day) = w.did
      JOIN students s ON o.sid = s.id
      WHERE LOWER('{}') like get_word(s.name, 1)) o
JOIN managers m ON o.mid = m.id
JOIN students s ON o.sid = s.id
JOIN writeUps w ON o.wid = w.id
JOIN days d ON o.did = d.id
JOIN areas a ON o.aid = a.id
JOIN jobs j ON o.jid = j.id;
