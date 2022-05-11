delimiter $$

CREATE TABLE `dept` (
  `deptid` int(11) NOT NULL,
  `dname` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `emp` (
  `EmpID` int(11) NOT NULL,
  `Ename` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sal` decimal(7,2) DEFAULT NULL,
  `deptid` int(11) DEFAULT NULL,
  PRIMARY KEY (`EmpID`),
  KEY `FK_emp_deptid` (`deptid`),
  CONSTRAINT `FK_emp_deptid` FOREIGN KEY (`deptid`) REFERENCES `dept` (`deptid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `empprojects` (
  `EP_ID` int(11) NOT NULL,
  `EmpID` int(11) DEFAULT NULL,
  `ProjectID` int(11) DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  PRIMARY KEY (`EP_ID`),
  KEY `FK_ep_emp` (`EmpID`),
  KEY `FK_ep_projects` (`ProjectID`),
  CONSTRAINT `FK_ep_emp` FOREIGN KEY (`EmpID`) REFERENCES `emp` (`EmpID`),
  CONSTRAINT `FK_ep_projects` FOREIGN KEY (`ProjectID`) REFERENCES `projects` (`ProjectID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `projects` (
  `ProjectID` int(11) NOT NULL,
  `ProjectName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ProjectBudget` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`ProjectID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

delimiter $$

CREATE TABLE `ti_test` (
  `col1` int(11) NOT NULL,
  `col2` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `col3` date DEFAULT NULL,
  `col4` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`col1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci$$

