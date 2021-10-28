-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.3.31-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para proyecto
CREATE DATABASE IF NOT EXISTS `proyecto` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `proyecto`;

-- Volcando estructura para tabla proyecto.categories
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.categories: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;

-- Volcando estructura de base de datos para proyecto
CREATE DATABASE IF NOT EXISTS `proyecto` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `proyecto`;

-- Volcando estructura para tabla proyecto.colores
CREATE TABLE IF NOT EXISTS `colores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.colores: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `colores` DISABLE KEYS */;
/*!40000 ALTER TABLE `colores` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.elementos
CREATE TABLE IF NOT EXISTS `elementos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cant` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.elementos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `elementos` DISABLE KEYS */;
-- Volcando estructura para tabla proyecto.issues
CREATE TABLE IF NOT EXISTS `issues` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(30) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `description` (`description`),
  KEY `category_id` (`category_id`),
  KEY `status_id` (`status_id`),
  CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `issues_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `statuses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.issues: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `issues` DISABLE KEYS */;
-- Volcando estructura para tabla proyecto.ordenacion
CREATE TABLE IF NOT EXISTS `ordenacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_orden` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.ordenacion: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `ordenacion` DISABLE KEYS */;
INSERT INTO `ordenacion` (`id`, `id_orden`) VALUES
	(1, 1);
/*!40000 ALTER TABLE `ordenacion` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.permisos
CREATE TABLE IF NOT EXISTS `permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.permisos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.puntosdeencuentro
CREATE TABLE IF NOT EXISTS `puntosdeencuentro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `coordenadas` varchar(80) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `direccion` (`direccion`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `puntosdeencuentro_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `statuses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.puntosdeencuentro: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `puntosdeencuentro` DISABLE KEYS */;
/*!40000 ALTER TABLE `puntosdeencuentro` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.roles
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.roles: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.roles_permisos
CREATE TABLE IF NOT EXISTS `roles_permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rol_id` int(11) DEFAULT NULL,
  `permiso_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rol_id` (`rol_id`),
  KEY `permiso_id` (`permiso_id`),
  CONSTRAINT `roles_permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `roles_permisos_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.roles_permisos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `roles_permisos` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles_permisos` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.statuses
CREATE TABLE IF NOT EXISTS `statuses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.statuses: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `statuses` DISABLE KEYS */;
INSERT INTO `statuses` (`id`, `name`) VALUES
	(1, 'active'),
	(2, 'inactive');
/*!40000 ALTER TABLE `statuses` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(300) DEFAULT NULL,
  `bloqueado` tinyint(1) DEFAULT NULL,
  `username` varchar(39) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.users: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Volcando estructura para tabla proyecto.users_roles
CREATE TABLE IF NOT EXISTS `users_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `rol_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `rol_id` (`rol_id`),
  CONSTRAINT `users_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_roles_ibfk_2` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla proyecto.users_roles: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `users_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_roles` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;