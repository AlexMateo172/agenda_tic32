CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

INSERT INTO contactos(nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES
('Dejah','Thoris','Barsoomn','dejah@email.com','11111111'),
('John','Carter','Eath','john@email.com','22222222'),
('Miles', 'Tails', 'Prower', 'tails@workshop.com', '33333333'),
('Shadow', 'The', 'Hedgehog', 'shadow@gun.net', '44444444');

SELECT * FROM contactos;