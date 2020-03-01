CREATE TABLE `Data` (
  `Run_id` int(11) NOT NULL AUTO_INCREMENT,
  `Config_UID` int(11) DEFAULT NULL,
  `Generation` int(11) DEFAULT NULL,
  `Fitness` float DEFAULT NULL,
  `Trial` int(11) DEFAULT NULL,
  `Chromosome` varchar(255) DEFAULT NULL,
  `Robot_UID` varchar(255) NOT NULL,
   PRIMARY KEY (Run_id)
);