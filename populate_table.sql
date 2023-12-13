INSERT INTO financeiro (financeiro_id, gasto_ultimo_mes, ganho_ultimo_mes)VALUES
(1, 30000, 47500),
(2, 55000, 69000),
(3, 40000, 70250);


INSERT INTO cidade (cidade_id, nome, estado, populacao)VALUES 
(1, 'Campo Mourão', 'Paraná', 99488),
(2, 'Londrina', 'Paraná', 575377),
(3, 'Maringá', 'Paraná', 403063);

	
INSERT INTO franquia (franquia_id, cidade_id, proprietario, telefone, bairro, rua, numero, financeiro_id) VALUES
(1, 1, 'Adam Sandler', '(44)99999-9999', 'Jardim Flores', 'Rua Rosa', 123, 1),
(2, 2, 'Beyoncé', '(43)91234-5678', 'Bairro Queen', 'Rua King', 332, 2),
(3, 3, 'Taylor Swift', '(44)99876-5432', 'Bairro Lover', 'Rua Fearless', 13, 3);


INSERT INTO plano (plano_id, preco, duracao, nome) VALUES
(1, 100, 1, 'Mensal'),
(2, 250, 3, 'Trimestral'),
(3, 475, 6, 'Semestral'),
(4, 850, 12, 'Anual');


INSERT INTO treino (treino_id, frequencia, objetivo) VALUES
(1, 3, 'ganhar massa muscular'),
(2, 3, 'perder peso'),
(3, 4, 'recomposicao corporal'),
(4, 3, 'ganhar massa muscular'),
(5, 2, 'perder peso'),
(6, 3, 'recomposicao corporal'),
(7, 5, 'ganhar massa muscular'),
(8, 4, 'recomposicao corporal'),
(9, 3, 'perder peso'),
(10, 4, 'perder peso'),
(11, 5, 'ganhar massa muscular'),
(12, 2, 'perder peso'),
(13, 5, 'perder peso'),
(14, 4, 'perder peso'),
(15, 3, 'perder peso');


INSERT INTO treino_diario (treino_diario_id, cardio) VALUES
(1, true),
(2, false),
(3, true),
(4, false),
(5, true);


INSERT INTO treino_diario_treino (treino_id, treino_diario_id) VALUES
(1, 1), (1, 2), (1, 4),
(2, 1), (2, 2), (2, 3),
(3, 1), (3, 3), (3, 4), (3, 5),
(4, 1), (4, 3), (4, 5),
(5, 1), (5, 4),
(6, 1), (6, 2), (6, 5),
(7, 1), (7, 2), (7, 3), (7, 4), (7, 5),
(8, 1), (8, 2), (8, 3), (8, 5),
(9, 1), (9, 2), (9, 3),
(10, 1), (10, 2), (10, 3), (10, 4),
(11, 1), (11, 2), (11, 3), (11, 4), (11, 5),
(12, 1), (12, 2),
(13, 1), (13, 2), (13, 3), (13, 4),(13, 5),
(14, 1), (14, 3), (14, 4),
(15, 1), (15, 2), (15, 3);


INSERT INTO grupo_muscular (grupo_muscular_id, nome, categoria) VALUES
(1, 'peito', 'superior'),
(2, 'ombro', 'superior'),
(3, 'costas', 'superior'),
(4, 'biceps', 'superior'),
(5, 'triceps', 'superior'),
(6, 'abdomen', 'superior'),
(7, 'antebraco', 'superior'),
(8, 'quadriceps', 'inferior'),
(9, 'posterior de coxa', 'inferior'),
(10, 'gluteos', 'inferior'),
(11, 'panturrilha', 'inferior');


INSERT INTO grupo_treino_diario (grupo_treino_diario_id, treino_diario_id, grupo_muscular_id) VALUES
-- treino 1 (peito e triceps)
(1, 1, 1), 
(2, 1, 5),
-- treino 2 (quadriceps e panturrilha)
(3, 2, 8),
(4, 2, 11),
-- treino 3 (costas, biceps e antebraco)
(5, 3, 3),
(6, 3, 4),
(7, 3, 7),
-- treino 4 (posterior de coxa e gluteos)
(8, 4, 9),
(9, 4, 10),
-- treino 5 (ombro e abdomen)
(10, 5, 2),
(11, 5, 6);


INSERT INTO exercicio (exercicio_id, nome, grupo_muscular_id) VALUES
-- peito --
(1, 'supino reto', 1),
(2, 'supino inclinado', 1),
(3, 'crucifixo', 1),
(4, 'voador', 1),
(5, 'flexão', 1),

-- ombros -- 
(6, 'Desenvolvimento militar com barra', 2),
(7, 'Desenvolvimento com halteres', 2),
(8, 'Elevação lateral com halteres', 2),
(9, 'Elevação frontal com halteres', 2),
(10, 'Encolhimento de ombros com barra', 2),

-- costas -- 
(11, 'remada baixa', 3),
(12, 'puxada alta', 3),
(13, 'pull-down', 3),
(14, 'cavalinho', 3),
(15, 'remada unilateral', 3),

-- biceps -- 
(16, 'Rosca direta com barra', 4),
(17, 'Rosca alternada com halteres', 4),
(18, 'Rosca martelo', 4),
(19, 'Rosca Scott (concentrada)', 4),
(20, 'Rosca inversa (curl inverso)', 4),

-- triceps -- 
(21, 'Tríceps na polia alta (pushdown)', 5),
(22, 'Tríceps na polia com corda', 5),
(23, 'Extensão de tríceps com halter', 5),
(24, 'Tríceps mergulho (dips)', 5),
(25, 'Tríceps testa com barra', 5),

-- abdomen --
(26, 'Abdominais', 6),
(27, 'Prancha', 6),
(28, 'Elevação de pernas', 6),
(29, 'Torção russa', 6),
(30, 'Abdominal com rotação', 6),

-- antebracos -- 
(31, 'Rosca de punho com barra', 7),
(32, 'Rosca de punho com halteres', 7),
(33, 'Rotação de punho com barra', 7),
(34, 'Rotação de punho com halteres', 7),
(35, 'Pegada pronada na barra fixa', 7),

-- Pernas (Quadríceps) --
(36, 'Agachamento (squats)', 8),
(37, 'Leg press', 8),
(38, 'Extensão de pernas na máquina', 8),
(39, 'Agachamento frontal', 8),
(40, 'Cadeira extensora', 8),

-- Pernas (Posterior da coxa) -- 
(41, 'Flexão de pernas (leg curl)', 9),
(42, 'Stiff', 9),
(43, 'Afundo reverso', 9),
(44, 'Puxada no glúteo na máquina', 9),
(45, 'Bom dia', 9),

-- glúteos -- 
(46, 'Elevação de quadril com barra', 10),
(47, 'Elevação de quadril com halteres', 10),
(48, 'Agachamento sumô', 10),
(49, 'Cadeira abdutora', 10),
(50, 'Agachamento búlgaro', 10),

-- panturrilhas -- 
(51, 'Elevação de panturrilha em pé', 11),
(52, 'Elevação de panturrilha sentado', 11),
(53, 'Elevação de panturrilha com barra', 11),
(54, 'Elevação de panturrilha unilateral', 11),
(55, 'Pulldown na polia baixa com pés', 11);


INSERT INTO series_repeticoes (grupo_treino_diario_id, exercicio_id, series, repeticoes)
VALUES
	(1, 1, 4, 15),
	(1, 2, 4, 12),
	(1, 3, 3, 12),
	(1, 4, 4, 12),
	(2, 16, 4, 12),
	(2, 18, 3, 15),
	(2, 19, 3, 12),
	(3, 36, 4, 12),
	(3, 37, 4, 8),
	(3, 38, 4, 12),
	(3, 40, 3, 12),
	(4, 51, 4, 8),
	(4, 52, 3, 12),
	(5, 11, 4, 12),
	(5, 12, 3, 15),
	(5, 13, 3, 12),
	(5, 14, 4, 8),
	(6, 16, 4, 12),
	(6, 18, 3, 8),
	(6, 19, 4, 12),
	(7, 31, 4, 12),
	(7, 33, 3, 15),
	(8, 41, 4, 8),
	(8, 42, 4, 12),
	(9, 48, 3, 12),
	(9, 50, 4, 15),
	(10, 7, 3, 12),
	(10, 8, 4, 15),
	(10, 9, 4, 8),
	(10, 10, 3, 12),
	(11, 26, 4, 8),
	(11, 27, 4, 15);


INSERT INTO cliente (cpf, nome, sobrenome, telefone, data_nasc, peso, email, senha, plano_id, franquia_id, treino_id)
VALUES
	('11111111111', 'Luan', 'Santana', '(45)96629-9891', '1984-10-25', 54, 'luancity@gmail.com', 'amanda123', 1, 2, NULL),
	('22222222222', 'Brad', 'Pitt', '(77)35934-4581', '1963-12-18', 74, 'brad.pitt@example.com', 'bradpass123', 2, 3, NULL),
	('33333333333', 'Miley', 'Cyrus', '(99)87667-7777', '1992-11-23', 44, 'miley.cyrus@example.com', 'miley1234', 3, 3, NULL),
	('97859859859', 'Tom', 'Cruise', '(44)44344-9494', '1972-07-03', 92, 'tom.cruise@example.com', 'tomcruise456', 2, 1, NULL),
	('55555555555', 'Jennifer', 'Aniston', '(88)37729-9891', '1994-11-30', 50, 'jennifer.aniston@example.com', 'jen_pass', 1, 3, 11),
	('66666666666', 'Lady', 'Gaga', '(39)73912-8235', '1988-05-12', 48, 'lady.gaga@example.com', 'gaga123', 1, 1, 2),
	('77777777777', 'Al', 'Pacino', '(74)97652-1762', '1968-07-24', 79, 'al.pacino@example.com', 'al1234', 3, 2, 9),
	('88888888888', 'Bruce', 'Willis', '(69)34234-9641', '1982-09-11', 89, 'bruce.willis@example.com', 'brucepass', 3, 1, 13),
	('99999999999', 'Nicole', 'Kidman', '(57)82132-3261', '1977-12-03', 77, 'nicole.kidman@example.com', 'nicole123', 2, 2, 1),
	('10110110110', 'Will', 'Smith', '(55)96175-8237', '1977-02-02', 72, 'will.smith@example.com', 'willsmithpass', 2, 3, 2),
	('12112112112', 'Johnny', 'Depp', '(81)98346-3481', '1999-07-30', 73, 'johnny.depp@example.com', 'depp_pass', 2, 3, 5),
	('13113113113', 'Leonardo', 'DiCaprio', '(88)53269-7473', '1979-12-18', 85, 'leonardo.dicaprio@example.com', 'leo_pass', 1, 1, 15),
	('14114114114', 'Angelina', 'Jolie', '(45)11487-1313', '1986-03-19', 63, 'angelina.jolie@example.com', 'angelina123', 1, 1, 1),
	('15115115115', 'Robert', 'De Niro', '(53)91266-2227', '1954-03-13', 69, 'robert.deniro@example.com', 'robertd123', 2, 3, 12),
	('16116116116', 'Robert', 'Downey Jr.', '(44)55563-1421', '1983-04-22', 75, 'robert.downey@example.com', 'rdjr_pass', 3, 2, 4),
	('17117117117', 'Jackie', 'Chan', '(89)66266-3136', '1982-12-25', 58, 'jackie.chan@example.com', 'jackie123', 3, 2, 4),
	('18118118118', 'Nicole', 'Kidman', '(33)56378-1587', '1981-09-26', 58, 'nicole.kidman2@example.com', 'nicole456', 2, 1, 10),
	('19119119119', 'Nicolas', 'Cage', '(44)45783-7246', '1980-06-11', 52, 'nicolas.cage@example.com', 'cage_pass', 2, 1, 4),
	('20220220220', 'Sandra', 'Bullock', '(69)92756-8135', '1979-03-08', 51, 'sandra.bullock@example.com', 'sandra_pass', 2, 3, 1),
	('21221221221', 'Scarlett', 'Johansson', '(45)89894-5370', '1992-05-08', 50, 'scarlett.johansson@example.com', 'scarlett123', 2, 3, 11),
	('36336336336', 'Sylvester', 'Stallone', '(45)15134-1412', '1980-11-19', 55, 'sylvester.stallone@example.com', 'sylvester123', 3, 3, 7),
	('23223223223', 'Julia', 'Roberts', '(77)74257-5577', '1979-05-29', 74, 'julia.roberts@example.com', 'julia_pass', 1, 1, 3),
	('24224224224', 'The', 'Rock', '(48)14825-8289', '1983-05-22', 89, 'the.rock@example.com', 'therock123', 1, 1, 4),
	('25225225225', 'Ben', 'Stiller', '(69)24639-1718', '1999-09-09', 85, 'ben.stiller@example.com', 'benstiller123', 2, 1, 4),
	('26226226226', 'Owen', 'Wilson', '(49)00045-2037', '1981-11-11', 67, 'owen.wilson@example.com', 'owenwilson_pass', 2, 1, 2),
	('27227227227', 'Edward', 'Norton', '(42)77843-1619', '1967-08-25', 87, 'edward.norton@example.com', 'edwardnorton123', 3, 2, 2),
	('28228228228', 'Robert', 'Pattinson', '(50)53683-1368', '1987-01-21', 88, 'robert.pattinson@example.com', 'rpattinson_pass', 3, 3, 12),
	('29229229229', 'Kristen', 'Stewart', '(65)83659-1473', '1989-12-22', 67, 'kristen.stewart@example.com', 'kstewart_pass', 3, 2, 1),
	('30330330330', 'Taylor', 'Lautner', '(62)47824-4424', '1982-02-22', 72, 'taylor.lautner@example.com', 'taylorl_pass', 3, 3, 1),
	('31331331331', 'Ashley', 'Greene', '(22)73677-1350', '1988-08-08', 53, 'ashley.greene@example.com', 'ashleyg_pass', 3, 2, 1),
	('76776776776', 'Dwayne', 'Johnson', '(45)76534-1234', '1972-05-02', 120, 'dwayne.johnson@example.com', 'dwayne_pass', 1, 2, 1),
	('34334334334', 'Emma', 'Watson', '(44)98765-4321', '1990-04-15', 57, 'emma.watson@example.com', 'emma123', 2, 3, 2),
	('79779779779', 'Chris', 'Hemsworth', '(55)87654-9876', '1983-08-11', 85, 'chris.hemsworth@example.com', 'chrish123', 3, 1, 8),
	('37337337337', 'Natalie', 'Portman', '(44)76543-2109', '1981-06-09', 55, 'natalie.portman@example.com', 'natalie123', 1, 2, 4),
	('38338338338', 'Hugh', 'Jackman', '(55)12345-6789', '1968-10-12', 80, 'hugh.jackman@example.com', 'hugh123', 2, 1, 5),
	('39339339339', 'Anne', 'Hathaway', '(44)67890-1234', '1982-11-12', 63, 'anne.hathaway@example.com', 'anne123', 3, 3, 1),
	('40440440440', 'Chris', 'Evans', '(55)23456-7890', '1981-06-13', 88, 'chris.evans@example.com', 'chrisevans_pass', 1, 2, 2),
	('41441441441', 'Jennifer', 'Lawrence', '(44)56789-0123', '1990-08-15', 58, 'jennifer.lawrence@example.com', 'jlaw123', 2, 1, 3),
	('42442442442', 'Matthew', 'McConaughey', '(55)34567-8901', '1969-11-04', 75, 'matthew.mcconaughey@example.com', 'matthew123', 3, 3, 4),
	('43443443443', 'Charlize', 'Theron', '(44)67890-1234', '1975-08-07', 63, 'charlize.theron@example.com', 'charlize123', 1, 2, 5),
	('44444444444', 'George', 'Clooney', '(77)98765-4321', '1961-05-06', 75, 'george.clooney@example.com', 'george123', 1, 1, 1),
	('45445445445', 'Cate', 'Blanchett', '(44)87654-3210', '1969-05-14', 62, 'cate.blanchett@example.com', 'cate123', 2, 2, 9),
	('46446446446', 'Daniel', 'Craig', '(44)76543-2109', '1968-03-02', 80, 'daniel.craig@example.com', 'danielc123', 3, 3, 3),
	('47447447447', 'Natalie', 'Dormer', '(44)12345-6789', '1982-02-11', 58, 'natalie.dormer@example.com', 'natalied_pass', 1, 1, 14),
	('48448448448', 'Idris', 'Elba', '(55)23456-7890', '1972-09-06', 92, 'idris.elba@example.com', 'idris123', 2, 2, 5),
	('49449449449', 'Amy', 'Adams', '(44)56789-0123', '1974-08-20', 63, 'amy.adams@example.com', 'amyadams123', 3, 1, 1),
	('50550550550', 'Ryan', 'Reynolds', '(55)34567-8901', '1976-10-23', 88, 'ryan.reynolds@example.com', 'ryanr_pass', 1, 3, 2),
	('51551551551', 'Emma', 'Stone', '(44)67890-1234', '1988-11-06', 54, 'emma.stone@example.com', 'emmastone_pass', 2, 2, 3),
	('52552552552', 'Chris', 'Pratt', '(55)87654-4321', '1979-06-21', 82, 'chris.pratt@example.com', 'chrisp123', 3, 1, 7),
	('53553553553', 'Jessica', 'Chastain', '(44)76543-2109', '1977-03-24', 61, 'jessica.chastain@example.com', 'jessicac_pass', 1, 3, 6);