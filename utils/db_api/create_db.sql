create table category
(
    codename        varchar(255) primary key,
    name            varchar(255),
    aliases         text
);

create table expense
(
    id                integer primary key,
    amount            integer,
    created           datetime,
    category_codename integer,
    raw_text          text,
    FOREIGN KEY (category_codename) REFERENCES category (codename)
);

insert into category (codename, name, aliases)
values ("products", "продукти", "їда, продукти"),
       ("coffee", "кава", "кава"),
       ("cafe", "кафе", "ресторан, мак, макдональдс, макдак, kfc"),
       ("transport", "громадський транспорт", "метро, автобус,тролейбус, трамвай, фонікулер"),
       ("taxi", "таксі", "таксі"),
       ("phone", "телефон", "телефон, звязок, рахунок, київстар, водафон, лайф, 4g"),
       ("utilities", "комунальні послуги", "комуналка, комунальні послуги, світло, рахунки, газ, вода, хородна вода, гаряча вода, тепло, опалення, домофон, квартплата"),
       ("pets", "домашні тварини", "собака, домашні тварини, корм, ветеренарка, вет клініка, кіт"),
       ("other", "інше","");


