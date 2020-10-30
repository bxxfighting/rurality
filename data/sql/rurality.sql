/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50643
 Source Host           : localhost:3306
 Source Schema         : rurality

 Target Server Type    : MySQL
 Target Server Version : 50643
 File Encoding         : 65001

 Date: 30/10/2020 19:16:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(32) NOT NULL,
  `sign` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for department_user
-- ----------------------------
DROP TABLE IF EXISTS `department_user`;
CREATE TABLE `department_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `typ` smallint(6) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `department_user_department_id_c869a6ca_fk_department_id` (`department_id`),
  KEY `department_user_user_id_522743e1_fk_user_id` (`user_id`),
  CONSTRAINT `department_user_department_id_c869a6ca_fk_department_id` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`),
  CONSTRAINT `department_user_user_id_522743e1_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for mod
-- ----------------------------
DROP TABLE IF EXISTS `mod`;
CREATE TABLE `mod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(32) NOT NULL,
  `sign` varchar(32) NOT NULL,
  `rank` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `typ` smallint(6) NOT NULL,
  `sign` varchar(128) NOT NULL,
  `rank` int(11) NOT NULL,
  `mod_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `permission_mod_id_f75289cc_fk_mod_id` (`mod_id`),
  CONSTRAINT `permission_mod_id_f75289cc_fk_mod_id` FOREIGN KEY (`mod_id`) REFERENCES `mod` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(32) NOT NULL,
  `typ` int(11) NOT NULL,
  `sign` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for role_mod
-- ----------------------------
DROP TABLE IF EXISTS `role_mod`;
CREATE TABLE `role_mod` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `mod_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `role_mod_mod_id_053ffcd7_fk_mod_id` (`mod_id`),
  KEY `role_mod_role_id_827d1e5a_fk_role_id` (`role_id`),
  CONSTRAINT `role_mod_mod_id_053ffcd7_fk_mod_id` FOREIGN KEY (`mod_id`) REFERENCES `mod` (`id`),
  CONSTRAINT `role_mod_role_id_827d1e5a_fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for role_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `role_permission_permission_id_ee9c5982_fk_permission_id` (`permission_id`),
  KEY `role_permission_role_id_877a80a4_fk_role_id` (`role_id`),
  CONSTRAINT `role_permission_permission_id_ee9c5982_fk_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`id`),
  CONSTRAINT `role_permission_role_id_877a80a4_fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for role_user
-- ----------------------------
DROP TABLE IF EXISTS `role_user`;
CREATE TABLE `role_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `role_user_role_id_3b7811a1_fk_role_id` (`role_id`),
  KEY `role_user_user_id_c9245d4a_fk_user_id` (`user_id`),
  CONSTRAINT `role_user_role_id_3b7811a1_fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  CONSTRAINT `role_user_user_id_c9245d4a_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(256) NOT NULL,
  `name` varchar(128) NOT NULL,
  `email` varchar(128) DEFAULT NULL,
  `phone` varchar(64) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `typ` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, '2020-10-30 11:12:53.911958', '2020-10-30 11:12:54.143970', 0, 'admin', 'pbkdf2_sha256$216000$9axLwBleCSuZ$Octlph66wPXCU5H0ilyS9SLHe1/QY+DaJr+MHbMMJW8=', '超级管理员', NULL, NULL, 10, 10);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
