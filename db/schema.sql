-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.3.31-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for proyecto
CREATE DATABASE IF NOT EXISTS `proyecto` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `proyecto`;

-- Dumping structure for table proyecto.categories
CREATE TABLE IF NOT EXISTS `categories` (
  `id` smallint(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.categories: ~3 rows (approximately)
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` (`id`, `name`) VALUES
	(2, 'Advertencia'),
	(3, 'Poco probable'),
	(1, 'Urgente');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;

-- Dumping structure for table proyecto.colores
CREATE TABLE IF NOT EXISTS `colores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `publico` varchar(50) DEFAULT NULL,
  `privado` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.colores: ~0 rows (approximately)
/*!40000 ALTER TABLE `colores` DISABLE KEYS */;
/*!40000 ALTER TABLE `colores` ENABLE KEYS */;

-- Dumping structure for table proyecto.denuncias
CREATE TABLE IF NOT EXISTS `denuncias` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(40) NOT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_cierre` datetime DEFAULT NULL,
  `descripcion` varchar(80) NOT NULL,
  `coordenadas` varchar(200) NOT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `asignado_a` int(11) DEFAULT NULL,
  `apellido_denunciante` varchar(20) NOT NULL,
  `nombre_denunciante` varchar(20) NOT NULL,
  `telefono_denunciante` int(11) NOT NULL,
  `email_denunciante` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `titulo` (`titulo`),
  KEY `categoria_id` (`categoria_id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `denuncias_ibfk_1` FOREIGN KEY (`categoria_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `denuncias_ibfk_2` FOREIGN KEY (`estado_id`) REFERENCES `statuses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.denuncias: ~2 rows (approximately)
/*!40000 ALTER TABLE `denuncias` DISABLE KEYS */;
INSERT INTO `denuncias` (`id`, `titulo`, `fecha_creacion`, `fecha_cierre`, `descripcion`, `coordenadas`, `categoria_id`, `estado_id`, `asignado_a`, `apellido_denunciante`, `nombre_denunciante`, `telefono_denunciante`, `email_denunciante`) VALUES
	(2, 'Alcantarilla tapada', '2021-10-29 15:37:39', NULL, 'La alcantarilla de la esquina esta tapada por hojas', '324,423.432,432', 3, 4, 1, 'Fulanito', 'Jorge', 2147483647, 'jorge@gmail.com'),
	(3, 'Cloaca', '2021-11-02 15:50:45', NULL, 'Cloaca con hojas', '345,763.23,65', 2, 4, 1, 'Perez', 'Luis', 324324234, 'Luis@gmail.com');
/*!40000 ALTER TABLE `denuncias` ENABLE KEYS */;

-- Dumping structure for table proyecto.elementos
CREATE TABLE IF NOT EXISTS `elementos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cant` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.elementos: ~0 rows (approximately)
/*!40000 ALTER TABLE `elementos` DISABLE KEYS */;
/*!40000 ALTER TABLE `elementos` ENABLE KEYS */;

-- Dumping structure for table proyecto.issues
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

-- Dumping data for table proyecto.issues: ~0 rows (approximately)
/*!40000 ALTER TABLE `issues` DISABLE KEYS */;
/*!40000 ALTER TABLE `issues` ENABLE KEYS */;

-- Dumping structure for table proyecto.ordenacion
CREATE TABLE IF NOT EXISTS `ordenacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderBy` varchar(50) DEFAULT NULL,
  `lista` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.ordenacion: ~0 rows (approximately)
/*!40000 ALTER TABLE `ordenacion` DISABLE KEYS */;
INSERT INTO `ordenacion` (`id`, `orderBy`, `lista`) VALUES
	(1, 'titulo', 'denuncias');
/*!40000 ALTER TABLE `ordenacion` ENABLE KEYS */;

-- Dumping structure for table proyecto.permisos
CREATE TABLE IF NOT EXISTS `permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.permisos: ~13 rows (approximately)
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
INSERT INTO `permisos` (`id`, `name`) VALUES
	(13, 'denuncia_cerrar'),
	(10, 'denuncia_confirmar'),
	(11, 'denuncia_create'),
	(4, 'denuncia_destroy'),
	(1, 'denuncia_index'),
	(12, 'denuncia_new'),
	(3, 'denuncia_resuelta'),
	(5, 'denuncia_sinConfirmar'),
	(2, 'denuncia_update'),
	(7, 'user_create'),
	(9, 'user_destroy'),
	(6, 'user_index'),
	(8, 'user_update');
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;

-- Dumping structure for table proyecto.puntosdeencuentro
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

-- Dumping data for table proyecto.puntosdeencuentro: ~0 rows (approximately)
/*!40000 ALTER TABLE `puntosdeencuentro` DISABLE KEYS */;
/*!40000 ALTER TABLE `puntosdeencuentro` ENABLE KEYS */;

-- Dumping structure for table proyecto.puntos_de_encuentro
CREATE TABLE IF NOT EXISTS `puntos_de_encuentro` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `direccion` varchar(30) NOT NULL,
  `coordenadas` varchar(80) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `direccion` (`direccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.puntos_de_encuentro: ~0 rows (approximately)
/*!40000 ALTER TABLE `puntos_de_encuentro` DISABLE KEYS */;
/*!40000 ALTER TABLE `puntos_de_encuentro` ENABLE KEYS */;

-- Dumping structure for table proyecto.roles
CREATE TABLE IF NOT EXISTS `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.roles: ~2 rows (approximately)
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` (`id`, `name`) VALUES
	(1, 'admin'),
	(2, 'operador');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;

-- Dumping structure for table proyecto.roles_permisos
CREATE TABLE IF NOT EXISTS `roles_permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rol_id` int(11) DEFAULT NULL,
  `permiso_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rol_id` (`rol_id`),
  KEY `permiso_id` (`permiso_id`),
  CONSTRAINT `roles_permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `roles_permisos_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.roles_permisos: ~13 rows (approximately)
/*!40000 ALTER TABLE `roles_permisos` DISABLE KEYS */;
INSERT INTO `roles_permisos` (`id`, `rol_id`, `permiso_id`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 1, 3),
	(4, 1, 4),
	(5, 1, 5),
	(6, 1, 6),
	(7, 1, 7),
	(8, 1, 8),
	(9, 1, 9),
	(10, 1, 10),
	(11, 1, 11),
	(12, 1, 12),
	(13, 1, 13);
/*!40000 ALTER TABLE `roles_permisos` ENABLE KEYS */;

-- Dumping structure for table proyecto.seguimientos
CREATE TABLE IF NOT EXISTS `seguimientos` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(80) DEFAULT NULL,
  `autor` varchar(20) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `denuncia_id` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `seguimiento_ibfk_1` (`denuncia_id`),
  CONSTRAINT `seguimiento_ibfk_1` FOREIGN KEY (`denuncia_id`) REFERENCES `denuncias` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.seguimientos: ~0 rows (approximately)
/*!40000 ALTER TABLE `seguimientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimientos` ENABLE KEYS */;

-- Dumping structure for table proyecto.statuses
CREATE TABLE IF NOT EXISTS `statuses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.statuses: ~6 rows (approximately)
/*!40000 ALTER TABLE `statuses` DISABLE KEYS */;
INSERT INTO `statuses` (`id`, `name`) VALUES
	(1, 'active'),
	(6, 'Cerrada'),
	(4, 'En curso'),
	(2, 'inactive'),
	(5, 'Resuelta'),
	(3, 'Sin confirmar');
/*!40000 ALTER TABLE `statuses` ENABLE KEYS */;

-- Dumping structure for table proyecto.users
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.users: ~3 rows (approximately)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `password`, `bloqueado`, `username`) VALUES
	(1, 'cosme', 'fulanito', 'admin@gmail.com', '123123', 0, 'admin'),
	(2, 'martin', 'Lopez', 'martin99@hotmail.com', 'pbkdf2:sha256:260000$U8sakHFEiHozGTDl$94bbd87ea23d4c142b1c105faedbc626974b1b7dd0cb2d73991e88609b64b1a7', 0, 'martin99'),
	(3, 'Pedro', 'perez', 'pedro88@hotmail.com', 'pbkdf2:sha256:260000$bLfNn71DYMtUIVQp$fe6ddfc0f6e15de99b40d053c68188e988ee90dd6a5d17f6a300f1926213a889', 0, 'pedro88');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

-- Dumping structure for table proyecto.users_roles
CREATE TABLE IF NOT EXISTS `users_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `rol_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `rol_id` (`rol_id`),
  CONSTRAINT `users_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_roles_ibfk_2` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.users_roles: ~2 rows (approximately)
/*!40000 ALTER TABLE `users_roles` DISABLE KEYS */;
INSERT INTO `users_roles` (`id`, `user_id`, `rol_id`) VALUES
	(1, 1, 1),
	(2, 2, 1);
/*!40000 ALTER TABLE `users_roles` ENABLE KEYS */;

-- Dumping structure for table proyecto.zonas_inundables
CREATE TABLE IF NOT EXISTS `zonas_inundables` (
  `id` smallint(6) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `coordenadas` text NOT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  `color` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table proyecto.zonas_inundables: ~0 rows (approximately)
/*!40000 ALTER TABLE `zonas_inundables` DISABLE KEYS */;
/*!40000 ALTER TABLE `zonas_inundables` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
