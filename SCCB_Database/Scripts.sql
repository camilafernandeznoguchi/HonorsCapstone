-- root psw=same as always
-- username = camilaferno
-- psw = same as always
BEGIN;

CREATE TABLE USER (
	UID int(12) NOT NULL PRIMARY KEY,
	firstName TEXT NOT NULL,
	lastName TEXT NOT NULL,
	username TEXT,
	userPassword TEXT,
);

CREATE TABLE POINT (
	pointID INTEGER PRIMARY KEY AUTOINCREMENT,
	UID int(12) NOT NULL UNIQUE,
	earnDate TIMESTAMP NOT NULL,
	point int NOT NULL,
	FOREIGN KEY (UID) REFERENCES USER(UID)
);

INSERT INTO USER VALUES (188435878401,"John", "Doe", "jdoe@bentley.edu", MD5("Jdoe22!"));
INSERT INTO USER VALUES (325658432010,"Jacob", "Brown", "jbrown@bentley.edu", MD5("Jbrown22!"));
INSERT INTO USER VALUES (873869103687,"Steven", "Jones", "sjones@bentley.edu", MD5("Sjones22!"));
