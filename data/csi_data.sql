-- INSERTS USADOS PARA POPULAR BANCO DE DADOS


-- PRODUTO TABLE INSERTS

INSERT INTO public."Produto"(
            id, descricao, preco)
    VALUES (1, 'computador', 599.90);

INSERT INTO public."Produto"(
            id, descricao, preco)
    VALUES (2, 'mouse', 15.90);

INSERT INTO public."Produto"(
            id, descricao, preco)
    VALUES (3, 'teclado', 20.99);

INSERT INTO public."Produto"(
            id, descricao, preco)
    VALUES (4, 'monitor', 140.99);

INSERT INTO public."Produto"(
            id, descricao, preco)
    VALUES (5, 'fone de ouvido', 12.90);


-- CLIENTE TABLE INSERTS

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (1, 'Jose');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (2, 'Pedro');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (3, 'Maria');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (4, 'Camila');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (5, 'Junior');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (6, 'Davi');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (7, 'Luisa');

INSERT INTO public."Cliente"(
            id, nome)
    VALUES (8, 'Cristiano');


-- VENDA TABLE INSERTS

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (1, 1, '2018-01-10', 'Zacarias');

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (2, 2, '2018-01-11', 'Carlos');

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (3, 3, '2018-01-12', 'Marcelo');

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (4, 4, '2018-01-13', 'Denise');

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (5, 1, '2018-02-14', 'Denise');

INSERT INTO public."Venda"(
            id, "clienteId", data, vendedor)
    VALUES (6, 7, '2018-03-20', 'Matheus');


-- VENDA_DETALHE TABLE INSERTS


INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (1, 1, 2);

INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (2, 2, 5);

INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (3, 3, 10);

INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (4, 4, 20);

INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (5, 2, 17);

INSERT INTO public."VendaDetalhe"(
            "vendaId", "produtoId", quantidade)
    VALUES (6, 5, 30);