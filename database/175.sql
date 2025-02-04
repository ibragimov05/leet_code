SELECT p.firstName, p.lastName, a.city, a.state
FROm Person p
LEFT JOIN ADDRESS a ON p.personId = a.personId;
