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

 Date: 05/11/2020 14:31:05
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of mod
-- ----------------------------
BEGIN;
INSERT INTO `mod` VALUES (1, '2020-11-05 06:10:11.031156', '2020-11-05 06:10:11.031271', 0, '模块管理', 'mod', 0);
INSERT INTO `mod` VALUES (2, '2020-11-05 06:10:23.660535', '2020-11-05 06:10:23.660586', 0, '部门管理', 'department', 10);
INSERT INTO `mod` VALUES (3, '2020-11-05 06:10:33.136400', '2020-11-05 06:10:33.136446', 0, '角色管理', 'role', 15);
INSERT INTO `mod` VALUES (4, '2020-11-05 06:10:42.545597', '2020-11-05 06:10:42.545665', 0, '用户管理', 'user', 20);
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of permission
-- ----------------------------
BEGIN;
INSERT INTO `permission` VALUES (1, '2020-11-05 06:15:03.835936', '2020-11-05 06:15:03.835977', 0, '创建模块', 10, '/api/v1/account/mod/create/', 100, 1);
INSERT INTO `permission` VALUES (2, '2020-11-05 06:15:18.800018', '2020-11-05 06:15:18.800065', 0, '编辑模块', 10, '/api/v1/account/mod/update/', 99, 1);
INSERT INTO `permission` VALUES (3, '2020-11-05 06:15:32.934387', '2020-11-05 06:15:32.934466', 0, '删除模块', 10, '/api/v1/account/mod/delete/', 98, 1);
INSERT INTO `permission` VALUES (4, '2020-11-05 06:19:19.130160', '2020-11-05 06:19:19.130239', 0, '创建模块权限', 10, '/api/v1/account/permission/create/', 80, 1);
INSERT INTO `permission` VALUES (5, '2020-11-05 06:19:50.528581', '2020-11-05 06:19:50.528624', 0, '编辑模块权限', 10, '/api/v1/account/permission/update/', 79, 1);
INSERT INTO `permission` VALUES (6, '2020-11-05 06:20:51.754152', '2020-11-05 06:20:51.754196', 0, '删除模块权限', 10, '/api/v1/account/permission/delete/', 78, 1);
INSERT INTO `permission` VALUES (7, '2020-11-05 06:24:01.245629', '2020-11-05 06:24:01.245673', 0, '创建部门', 10, '/api/v1/account/department/create/', 100, 2);
INSERT INTO `permission` VALUES (8, '2020-11-05 06:25:31.359459', '2020-11-05 06:25:31.359511', 0, '编辑部门', 10, '/api/v1/account/department/update/', 99, 2);
INSERT INTO `permission` VALUES (9, '2020-11-05 06:26:06.898016', '2020-11-05 06:26:06.898070', 0, '删除部门', 10, '/api/v1/account/department/delete/', 98, 2);
INSERT INTO `permission` VALUES (10, '2020-11-05 06:26:27.745466', '2020-11-05 06:26:27.745517', 0, '创建部门用户', 10, '/api/v1/account/department/user/create/', 80, 2);
INSERT INTO `permission` VALUES (11, '2020-11-05 06:26:49.670835', '2020-11-05 06:26:49.670926', 0, '编辑部门用户', 10, '/api/v1/account/department/user/update/', 79, 2);
INSERT INTO `permission` VALUES (12, '2020-11-05 06:27:03.539892', '2020-11-05 06:27:03.539938', 0, '删除部门用户', 10, '/api/v1/account/department/user/delete/', 78, 2);
INSERT INTO `permission` VALUES (13, '2020-11-05 06:27:27.508863', '2020-11-05 06:27:27.508901', 0, '创建角色', 10, '/api/v1/account/role/create/', 100, 3);
INSERT INTO `permission` VALUES (14, '2020-11-05 06:27:38.493258', '2020-11-05 06:27:38.493302', 0, '编辑角色', 10, '/api/v1/account/role/update/', 99, 3);
INSERT INTO `permission` VALUES (15, '2020-11-05 06:27:50.836635', '2020-11-05 06:27:50.836680', 0, '删除角色', 10, '/api/v1/account/role/delete/', 98, 3);
INSERT INTO `permission` VALUES (16, '2020-11-05 06:28:28.039050', '2020-11-05 06:28:28.039094', 0, '创建角色用户', 10, '/api/v1/account/role/user/create/', 80, 3);
INSERT INTO `permission` VALUES (17, '2020-11-05 06:28:41.907331', '2020-11-05 06:28:41.907375', 0, '删除角色用户', 10, '/api/v1/account/role/user/delete/', 79, 3);
INSERT INTO `permission` VALUES (18, '2020-11-05 06:29:02.539504', '2020-11-05 06:29:02.539544', 0, '创建用户', 10, '/api/v1/account/user/create/', 100, 4);
INSERT INTO `permission` VALUES (19, '2020-11-05 06:29:20.429143', '2020-11-05 06:29:20.429189', 0, '编辑用户', 10, '/api/v1/account/user/update/', 99, 4);
INSERT INTO `permission` VALUES (20, '2020-11-05 06:29:33.416102', '2020-11-05 06:29:33.416174', 0, '删除用户', 10, '/api/v1/account/user/delete/', 98, 4);
COMMIT;

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
INSERT INTO `user` VALUES (1, '2020-11-05 06:04:04.732877', '2020-11-05 06:04:04.958336', 0, 'admin', 'pbkdf2_sha256$216000$V5XG3BZQLTgW$Tfh/WgIj0slbyElYnZNAiLht9GInAlulqalTrTrDVzs=', '超级管理员', NULL, NULL, 10, 10);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
