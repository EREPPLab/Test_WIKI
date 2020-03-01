CREATE TABLE Config (
  `Uid` int(11) NOT NULL AUTO_INCREMENT,
  `Selection` varchar(255) DEFAULT NULL,
  `Crossover` varchar(255) DEFAULT NULL,
  `Mutation` varchar(255) DEFAULT NULL,
  `Evaluation` varchar(255) DEFAULT NULL,
  `Termination` varchar(255) DEFAULT NULL,
  `Elitism` varchar(5) DEFAULT NULL,
  PRIMARY KEY (Uid)
)