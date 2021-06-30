
-- Dumping database structure for db_knit
USE `db_knit`;

-- Dumping structure for table db_knit.tblprod
CREATE TABLE IF NOT EXISTS `tblprod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(100) DEFAULT NULL,
  `desc` varchar(2000) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `category` char(50) DEFAULT NULL,
  `enable` int(1) DEFAULT NULL,
  `picture` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

-- Dumping data for table db_knit.tblprod: ~6 rows (approximately)
/*!40000 ALTER TABLE `tblprod` DISABLE KEYS */;
REPLACE INTO `tblprod` (`id`, `name`, `desc`, `price`, `category`, `enable`, `picture`) VALUES
	(5, 'Gryffindor House Hat', 'Harry Potter inspired knitted hat made with 100% acrylic', 35, 'hat', 1, '1.JPG'),
	(6, 'Braided Purple Hat', 'Knitted hat in braided style made with 100% acrylic\r\n', 25, 'hat', 1, '2.JPG'),
	(7, 'Braided  Grey hat', 'Knitted hat in braided style made with 100% acrylic\r\n', 25, 'hat', 1, '3.JPG'),
	(8, 'Snowflake Hat', 'Winter Style knitted hat made with 100% acrylic', 25, 'hat', 1, '4.JPG\r\n'),
	(10, 'Chunky Grey and Pink Hat', 'Handmade chunky hat made with 60% acrylic and 40% wool', 40, 'hat', 1, '5.JPG'),
	(11, 'Chunky White Hat', 'Chunky knitted hat made with 100% wool', 50, 'hat', 1, '6.JPG'),
	(12, 'Gold and Red Knitted Gloves', 'Handmade knitted gloves made with 100% acrylic\r\n\r\n', 25, 'gloves', 1, '1.JPG'),
	(13, 'Purple Knitted Gloves', 'Handmade knitted gloves made with 100% acrylic', 25, 'gloves', 1, '2.JPG'),
	(14, 'Grey Knitted Gloves', 'Handmade knitted gloves made with 100% acrylic', 25, 'gloves', 1, '3.JPG'),
	(15, 'Gryffindor Knitted Sweater', 'Handmade Gryffindor knitted sweater made with 100% acrylic', 300, 'sweaters', 1, '1.JPG'),
	(16, 'Multicolour Knitted Sweater', 'Handmade knitted sweater made with 40% wool and 60% acrylic', 300, 'sweaters', 1, '2.JPG'),
	(17, 'Multicolour Knitted Sweater', 'Handmade knitted sweater made with 100% merino wool', 300, 'sweaters', 1, '3.JPG'),
	(18, 'Multicolour Knitted Sweater', 'Handmade knitted sweater made with 40% wool and 60% acrylic', 300, 'sweaters', 1, '4.JPG'),
	(19, 'White Knitted Blanket', 'Handmade knitted chunky blanket made with  40% wool and 60% acrylic', 400, 'blankets', 1, '1.JPG'),
	(20, 'Grey Knitted Blanket', 'Handmade knitted chunky blanket made with  40% wool and 60% acrylic', 400, 'blankets', 1, '2.JPG'),
	(21, 'Mustard Knitted Blanket', 'Handmade knitted chunky blanket made\r\n with  40% wool and 60% acrylic', 400, 'blankets', 1, '4.JPG'),
	(22, 'Braided Purple Scarf', 'Handmade knitted scarf made with 100% acrylic', 70, 'scarves', 1, '1.JPG'),
	(23, 'Gryffindor House Scarf', 'Handmade knitted Gryffindor House made with 100% acrylic', 60, 'scarves', 1, '2.JPG'),
	(24, 'Pink Ombre Scarf', 'Handmade knitted chunky scarf 40% wool and 60% acrylic', 50, 'scarves', 1, '3.JPG');
/*!40000 ALTER TABLE `tblprod` ENABLE KEYS */;

