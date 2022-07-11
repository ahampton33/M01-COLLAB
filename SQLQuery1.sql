CREATE table Books2
(Title varchar(50),
Author varchar(50),
Yr int
);


Alter table Books
add Yr_released int;

select * from Books2

insert into Books2 (Title, Author, Yr)
Values ('Small Gods','Terry Pratchett',1992);

select Title from Books2 order by Title ASC;