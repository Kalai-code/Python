create Database LMS

USE LMS;
delimiter $$

CREATE TABLE `lms_md_lookup` (
  `serialNo` int(11) NOT NULL AUTO_INCREMENT,
  `cs_start` int(11) DEFAULT NULL,
  `cs_end` int(11) DEFAULT NULL,
  `loan_amt_start` int(11) DEFAULT NULL,
  `loan_amt_end` int(11) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `interest` float DEFAULT NULL,
  PRIMARY KEY (`serialNo`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (100,199,10000,19999,72,9);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (200,299,10000,19999,72,8.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (300,399,10000,19999,72,8);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (400,499,10000,19999,72,7.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (100,199,20000,29999,72,9);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (200,299,20000,29999,72,8.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (300,399,20000,29999,65,8.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (400,499,20000,29999,72,7.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (100,199,30000,39999,72,9);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (200,299,30000,39999,72,8.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (300,399,30000,39999,72,8);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (400,499,30000,39999,72,7.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (100,199,40000,50000,72,9);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (200,299,40000,50000,72,8.5);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (300,399,40000,50000,72,8);
INSERT INTO `lms`.`lms_md_lookup`(`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES (400,499,40000,50000,72,7.5);


INSERT INTO `lms`.`lms_md_lookup`(`serialNo`,`cs_start`,`cs_end`,`loan_amt_start`,`loan_amt_end`,`duration`,`interest`)
VALUES
(
<{serialNo: }>,
<{cs_start: }>,
<{cs_end: }>,
<{loan_amt_start: }>,
<{loan_amt_end: }>,
<{duration: }>,
<{interest: }>
);

SELECT 
    *
FROM
    lms_md_lookup;

