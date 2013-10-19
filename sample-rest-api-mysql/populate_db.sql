-- MySQL dump 10.14  Distrib 5.5.33a-MariaDB, for Win64 (x86)
--
-- Host: localhost    Database: upout_test
-- ------------------------------------------------------
-- Server version	5.5.33a-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `upout_test`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `upout_test` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `upout_test`;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lon` double NOT NULL,
  `lat` double NOT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `start` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (6,37.3226,-122.054,'white tie DC 3',5,'birthday\'s party 3','2013-10-15 23:01:46','2013-10-16 02:09:44'),(8,37.322125,-122.053528,'white tie DC 25',5,'birthday\'s 25 party','2013-10-15 23:00:05','2013-10-15 23:01:45'),(9,37.322125,-122.053528,'white tie DC 25',5,'birthday\'s 25 party','2013-10-15 23:00:05','2013-10-15 23:01:45'),(10,37.322125,-122.053528,'white tie DC 25',5,'birthday\'s 25 party','2013-10-15 23:00:05','2013-10-15 23:01:45'),(11,37.322125,-122.053528,'white tie DC 25',5,'birthday\'s 25 party','2013-10-15 23:00:05','2013-10-15 23:01:45'),(12,37.322125,-122.053528,'white tie DC 25',5,'birthday\'s 25 party','2013-10-15 23:00:05','2013-10-15 23:01:45');
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt`
--

DROP TABLE IF EXISTS `tt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tt` (
  `t` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt`
--

LOCK TABLES `tt` WRITE;
/*!40000 ALTER TABLE `tt` DISABLE KEYS */;
INSERT INTO `tt` VALUES ('2013-10-15 23:00:05'),('2013-10-15 23:00:05');
/*!40000 ALTER TABLE `tt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` char(41) NOT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,NULL,'petrichenko@gmail.com','*23AE809DDACAF96AF0FD78ED04B6A265E05AA257',NULL),(3,'Ivane','petrichenko+e@gmail.com','*A4B6157319038724E3560894F7F932C8886EBFCF','Petrychenkoe'),(5,'Ivanf','petrichenko+f@gmail.com','*1ED0756FC28EDD73C2AA727F25A9177CD9910C79','Petrychenkof');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-10-15 23:31:30
