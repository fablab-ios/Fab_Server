CREATE TABLE notifications (
  id int NOT NULL AUTO_INCREMENT,
  email varchar(100) NOT NULL,
  title varchar(1000) NOT NULL,
  message varchar(1000) NOT NULL,
  PRIMARY KEY(id)
);