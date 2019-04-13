CREATE TABLE tickets (
  ticket_number int(10) NOT NULL,
  date varchar(50) NOT NULL,
  time varchar(50) NOT NULL,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  status varchar(100) NOT NULL,
  notes varchar(1000) NOT NULL,
  PRIMARY KEY(ticket_number)
);