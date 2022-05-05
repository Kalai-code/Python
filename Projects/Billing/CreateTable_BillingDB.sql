delimiter $$

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_category` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `unit_price` float DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `billdetails` (
  `bill_detail_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` bigint(20) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `line_total` float DEFAULT NULL,
  PRIMARY KEY (`bill_detail_id`),
  KEY `FK_billdetails` (`bill_id`),
  KEY `FK_billdetails_prodid` (`product_id`),
  CONSTRAINT `FK_billdetails` FOREIGN KEY (`bill_id`) REFERENCES `bills` (`bill_id`),
  CONSTRAINT `FK_billdetails_prodid` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1260 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `bills` (
  `bill_id` bigint(20) NOT NULL,
  `bill_date` datetime DEFAULT NULL,
  `store_id` bigint(20) DEFAULT NULL,
  `bill_total` float DEFAULT NULL,
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

