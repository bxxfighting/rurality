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

 Date: 01/12/2020 11:29:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for aliyun_key
-- ----------------------------
DROP TABLE IF EXISTS `aliyun_key`;
CREATE TABLE `aliyun_key` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `key` varchar(128) NOT NULL,
  `secret` varchar(128) NOT NULL,
  `status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of aliyun_key
-- ----------------------------
BEGIN;
INSERT INTO `aliyun_key` VALUES (4, '2020-11-25 10:30:11.658145', '2020-11-25 10:40:28.479968', 1, '333', '332', 20);
INSERT INTO `aliyun_key` VALUES (5, '2020-11-25 10:44:37.056989', '2020-11-25 10:44:46.909587', 1, '33', '444', 20);
COMMIT;

-- ----------------------------
-- Table structure for asset
-- ----------------------------
DROP TABLE IF EXISTS `asset`;
CREATE TABLE `asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `sign` varchar(128) NOT NULL,
  `rank` int(11) NOT NULL,
  `remark` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of asset
-- ----------------------------
BEGIN;
INSERT INTO `asset` VALUES (1, '2020-11-25 12:19:52.697156', '2020-11-25 12:20:01.468287', 0, 'ECS', 'ecs', 100, '阿里云ECS模块');
INSERT INTO `asset` VALUES (2, '2020-11-25 12:20:14.068730', '2020-11-25 12:21:03.584707', 1, 'SLB', 'slb', 90, '阿里云SLB模块');
INSERT INTO `asset` VALUES (3, '2020-12-01 03:11:37.112352', '2020-12-01 03:11:37.112405', 0, 'SLB', 'slb', 96, '');
INSERT INTO `asset` VALUES (4, '2020-12-01 03:11:46.209042', '2020-12-01 03:11:46.209111', 0, 'RDS', 'rds', 93, '');
INSERT INTO `asset` VALUES (5, '2020-12-01 03:11:56.487127', '2020-12-01 03:11:56.487428', 0, 'Redis', 'redis', 89, '');
INSERT INTO `asset` VALUES (6, '2020-12-01 03:12:09.098221', '2020-12-01 03:12:09.098283', 0, 'Mongo', 'mongo', 85, '');
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of department
-- ----------------------------
BEGIN;
INSERT INTO `department` VALUES (1, '2020-11-05 08:48:37.362642', '2020-11-05 08:48:37.362725', 0, '运维部', 'ops');
INSERT INTO `department` VALUES (2, '2020-11-10 10:05:35.502089', '2020-11-10 10:05:35.502131', 0, '前端开发组', 'frontend');
INSERT INTO `department` VALUES (3, '2020-11-10 10:05:50.540234', '2020-11-10 10:05:50.540326', 0, '移动开发组', 'mobile');
COMMIT;

-- ----------------------------
-- Table structure for department_service
-- ----------------------------
DROP TABLE IF EXISTS `department_service`;
CREATE TABLE `department_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `department_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `department_service_department_id_8a798ac7_fk_department_id` (`department_id`),
  KEY `department_service_service_id_b86a666f_fk_service_id` (`service_id`),
  CONSTRAINT `department_service_department_id_8a798ac7_fk_department_id` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`),
  CONSTRAINT `department_service_service_id_b86a666f_fk_service_id` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of department_service
-- ----------------------------
BEGIN;
INSERT INTO `department_service` VALUES (1, '2020-11-10 10:05:15.039312', '2020-11-10 10:06:04.151615', 1, 1, 1);
INSERT INTO `department_service` VALUES (2, '2020-11-10 10:05:59.074737', '2020-11-10 10:06:01.946124', 1, 2, 1);
INSERT INTO `department_service` VALUES (3, '2020-11-10 10:06:07.711059', '2020-11-10 10:06:07.711119', 0, 2, 1);
INSERT INTO `department_service` VALUES (4, '2020-11-10 10:06:11.069409', '2020-11-10 10:06:11.069449', 0, 3, 1);
INSERT INTO `department_service` VALUES (5, '2020-11-11 02:45:14.984173', '2020-11-11 02:45:14.984214', 0, 1, 1);
INSERT INTO `department_service` VALUES (6, '2020-11-11 02:45:26.036309', '2020-11-11 02:45:26.036364', 0, 1, 2);
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of department_user
-- ----------------------------
BEGIN;
INSERT INTO `department_user` VALUES (1, '2020-11-06 07:18:31.200259', '2020-11-06 07:18:31.200298', 0, 10, 1, 2);
INSERT INTO `department_user` VALUES (2, '2020-11-10 11:10:01.248574', '2020-11-10 11:10:01.248631', 0, 20, 2, 2);
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES (1, 'account', '0001_initial', '2020-11-05 06:03:55.209143');
INSERT INTO `django_migrations` VALUES (2, 'project', '0001_initial', '2020-11-06 02:14:37.498351');
INSERT INTO `django_migrations` VALUES (3, 'project', '0002_auto_20201106_1455', '2020-11-06 06:56:00.788403');
INSERT INTO `django_migrations` VALUES (4, 'service', '0001_initial', '2020-11-06 07:00:36.872850');
INSERT INTO `django_migrations` VALUES (5, 'service', '0002_auto_20201106_1650', '2020-11-06 08:50:39.837503');
INSERT INTO `django_migrations` VALUES (6, 'account', '0002_auto_20201106_1947', '2020-11-06 11:47:18.621301');
INSERT INTO `django_migrations` VALUES (7, 'project', '0003_auto_20201110_1611', '2020-11-10 08:11:29.116684');
INSERT INTO `django_migrations` VALUES (8, 'service', '0003_auto_20201110_1611', '2020-11-10 08:11:52.785341');
INSERT INTO `django_migrations` VALUES (9, 'project', '0004_remove_projectmodel_sign', '2020-11-10 09:30:56.298798');
INSERT INTO `django_migrations` VALUES (10, 'manager', '0001_initial', '2020-11-25 07:24:57.541805');
INSERT INTO `django_migrations` VALUES (11, 'service', '0004_environmentmodel_serviceenvironmentmodel', '2020-11-27 05:57:36.937384');
INSERT INTO `django_migrations` VALUES (12, 'service', '0005_auto_20201127_1610', '2020-11-27 08:10:32.261804');
INSERT INTO `django_migrations` VALUES (13, 'ecs', '0001_initial', '2020-11-27 12:22:07.219712');
INSERT INTO `django_migrations` VALUES (14, 'service', '0006_serviceassetmodel', '2020-12-01 03:25:52.397268');
COMMIT;

-- ----------------------------
-- Table structure for ecs
-- ----------------------------
DROP TABLE IF EXISTS `ecs`;
CREATE TABLE `ecs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `region_id` varchar(128) NOT NULL,
  `zone_id` varchar(128) NOT NULL,
  `name` varchar(128) NOT NULL,
  `instance_id` varchar(128) NOT NULL,
  `hostname` varchar(128) NOT NULL,
  `inner_ip` varchar(128) NOT NULL,
  `outer_ip` varchar(128) NOT NULL,
  `cpu` int(11) NOT NULL,
  `os` varchar(128) NOT NULL,
  `memory` int(11) NOT NULL,
  `dt_buy` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of ecs
-- ----------------------------
BEGIN;
INSERT INTO `ecs` VALUES (1, '2020-11-27 12:27:10.525321', '2020-11-27 12:27:10.525373', 0, 'cn-zhangjiakou', 'cn-zhangjiakou-a', '量量', 'i-8vb19kumx22v0hxpzqni', 'iZ8vb19kumx22v0hxpzqniZ', '172.26.106.158', '47.92.71.110', 1, 'Ubuntu  16.04 64位', 1024, '2017-03-27 00:15:00.000000');
INSERT INTO `ecs` VALUES (2, '2020-11-27 12:30:44.048351', '2020-11-27 12:30:44.048397', 0, 'cn-beijing', 'cn-beijing-a', 'yike', 'i-2zedsuhv55oquitw5pqw', 'yike', '172.17.16.167', '39.105.71.60', 1, 'Ubuntu  16.04 64位', 1024, '2018-10-10 17:56:00.000000');
COMMIT;

-- ----------------------------
-- Table structure for environment
-- ----------------------------
DROP TABLE IF EXISTS `environment`;
CREATE TABLE `environment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `sign` varchar(128) NOT NULL,
  `rank` int(11) NOT NULL,
  `remark` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of environment
-- ----------------------------
BEGIN;
INSERT INTO `environment` VALUES (1, '2020-11-27 08:11:09.071451', '2020-11-27 08:11:18.147764', 1, '线上环境', 'prod', 100, '用于线上环境');
INSERT INTO `environment` VALUES (2, '2020-11-27 08:11:31.618363', '2020-11-27 08:11:37.917759', 0, '生产环境', 'prod', 100, '生产环境');
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of mod
-- ----------------------------
BEGIN;
INSERT INTO `mod` VALUES (1, '2020-11-05 06:10:11.031156', '2020-11-05 06:10:11.031271', 0, '模块管理', 'mod', 0);
INSERT INTO `mod` VALUES (2, '2020-11-05 06:10:23.660535', '2020-11-05 06:10:23.660586', 0, '部门管理', 'department', 10);
INSERT INTO `mod` VALUES (3, '2020-11-05 06:10:33.136400', '2020-11-05 06:10:33.136446', 0, '角色管理', 'role', 15);
INSERT INTO `mod` VALUES (4, '2020-11-05 06:10:42.545597', '2020-11-05 06:10:42.545665', 0, '用户管理', 'user', 20);
INSERT INTO `mod` VALUES (5, '2020-11-10 06:02:59.689214', '2020-11-10 06:02:59.689266', 0, '项目管理', 'project', 50);
INSERT INTO `mod` VALUES (6, '2020-11-10 06:06:17.629788', '2020-11-10 06:06:17.629874', 0, '服务管理', 'service', 48);
INSERT INTO `mod` VALUES (7, '2020-11-27 08:36:39.506846', '2020-11-27 08:36:39.506887', 0, '环境管理', 'environment', 30);
INSERT INTO `mod` VALUES (8, '2020-11-28 10:23:27.332670', '2020-11-28 10:23:27.332722', 0, 'ECS管理', 'ecs', 80);
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
  `mod_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `permission_mod_id_f75289cc_fk_mod_id` (`mod_id`),
  CONSTRAINT `permission_mod_id_f75289cc_fk_mod_id` FOREIGN KEY (`mod_id`) REFERENCES `mod` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4;

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
INSERT INTO `permission` VALUES (21, '2020-11-06 07:23:07.702264', '2020-11-06 07:23:07.702327', 0, '设置角色模块', 10, '/api/v1/account/role/mod/set/', 70, 3);
INSERT INTO `permission` VALUES (22, '2020-11-06 07:23:25.016743', '2020-11-06 07:23:25.016908', 0, '设置角色权限', 10, '/api/v1/account/role/permission/set/', 69, 3);
INSERT INTO `permission` VALUES (23, '2020-11-06 07:26:53.581617', '2020-11-06 07:27:02.901177', 1, '测试权限', 10, 'test', 0, 3);
INSERT INTO `permission` VALUES (24, '2020-11-06 11:50:13.439763', '2020-11-06 11:50:13.439841', 0, 'name', 10, '/api/v1/business/project/', 0, NULL);
INSERT INTO `permission` VALUES (25, '2020-11-06 11:50:13.439942', '2020-11-06 11:50:13.439967', 0, 'name', 10, '/api/v1/business/project/list/', 0, NULL);
INSERT INTO `permission` VALUES (26, '2020-11-06 11:50:13.440001', '2020-11-06 11:50:13.440016', 0, '创建项目', 10, '/api/v1/business/project/create/', 100, 5);
INSERT INTO `permission` VALUES (27, '2020-11-06 11:50:13.440045', '2020-11-06 11:50:13.440059', 0, '编辑项目', 10, '/api/v1/business/project/update/', 99, 5);
INSERT INTO `permission` VALUES (28, '2020-11-06 11:50:13.440087', '2020-11-06 11:50:13.440100', 0, '删除项目', 10, '/api/v1/business/project/delete/', 98, 5);
INSERT INTO `permission` VALUES (29, '2020-11-06 11:50:13.440128', '2020-11-06 11:50:13.440141', 0, '创建项目关联部门', 10, '/api/v1/business/project/department/create/', 80, 5);
INSERT INTO `permission` VALUES (30, '2020-11-06 11:50:13.440168', '2020-11-06 11:50:13.440182', 0, '删除项目关联部门', 10, '/api/v1/business/project/department/delete/', 79, 5);
INSERT INTO `permission` VALUES (31, '2020-11-06 11:50:13.440209', '2020-11-06 11:50:13.440222', 0, '创建项目关联用户', 10, '/api/v1/business/project/user/create/', 70, 5);
INSERT INTO `permission` VALUES (32, '2020-11-06 11:50:13.440249', '2020-11-06 11:50:13.440263', 0, '编辑项目关联用户', 10, '/api/v1/business/project/user/update/', 69, 5);
INSERT INTO `permission` VALUES (33, '2020-11-06 11:50:13.440291', '2020-11-06 11:50:13.440304', 0, '删除项目关联用户', 10, '/api/v1/business/project/user/delete/', 68, 5);
INSERT INTO `permission` VALUES (34, '2020-11-06 11:50:13.440331', '2020-11-06 11:50:13.440344', 0, 'name', 10, '/api/v1/business/project/user/list/', 0, NULL);
INSERT INTO `permission` VALUES (35, '2020-11-06 11:50:13.440370', '2020-11-06 11:50:13.440384', 0, 'name', 10, '/api/v1/business/service/', 0, NULL);
INSERT INTO `permission` VALUES (36, '2020-11-06 11:50:13.440410', '2020-11-06 11:50:13.440424', 0, 'name', 10, '/api/v1/business/service/list/', 0, NULL);
INSERT INTO `permission` VALUES (37, '2020-11-06 11:50:13.440451', '2020-11-06 11:50:13.440464', 0, '创建服务', 10, '/api/v1/business/service/create/', 100, 6);
INSERT INTO `permission` VALUES (38, '2020-11-06 11:50:13.440491', '2020-11-06 11:50:13.440504', 0, '编辑服务', 10, '/api/v1/business/service/update/', 99, 6);
INSERT INTO `permission` VALUES (39, '2020-11-06 11:50:13.440531', '2020-11-06 11:50:13.440544', 0, '删除服务', 10, '/api/v1/business/service/delete/', 98, 6);
INSERT INTO `permission` VALUES (40, '2020-11-06 11:50:13.440571', '2020-11-06 11:50:13.440584', 0, '创建服务关联用户', 10, '/api/v1/business/service/user/create/', 80, 6);
INSERT INTO `permission` VALUES (41, '2020-11-06 11:50:13.440611', '2020-11-06 11:50:13.440624', 0, '编辑服务关联用户', 10, '/api/v1/business/service/user/update/', 79, 6);
INSERT INTO `permission` VALUES (42, '2020-11-06 11:50:13.440651', '2020-11-06 11:50:13.440664', 0, '删除服务关联用户', 10, '/api/v1/business/service/user/delete/', 78, 6);
INSERT INTO `permission` VALUES (43, '2020-11-06 11:50:13.440691', '2020-11-06 11:50:13.440704', 0, 'name', 10, '/api/v1/business/service/user/list/', 0, NULL);
INSERT INTO `permission` VALUES (44, '2020-11-06 11:50:13.440731', '2020-11-06 11:50:13.440744', 0, 'name', 10, '/api/v1/account/user/login/', 0, NULL);
INSERT INTO `permission` VALUES (45, '2020-11-06 11:50:13.440770', '2020-11-06 11:50:13.440783', 0, 'name', 10, '/api/v1/account/user/logout/', 0, NULL);
INSERT INTO `permission` VALUES (46, '2020-11-06 11:50:13.440810', '2020-11-06 11:50:13.440823', 0, 'name', 10, '/api/v1/account/user/', 0, NULL);
INSERT INTO `permission` VALUES (47, '2020-11-06 11:50:13.440850', '2020-11-06 11:50:13.440864', 0, 'name', 10, '/api/v1/account/user/current/', 0, NULL);
INSERT INTO `permission` VALUES (48, '2020-11-06 11:50:13.440890', '2020-11-06 11:50:13.440904', 0, 'name', 10, '/api/v1/account/user/list/', 0, NULL);
INSERT INTO `permission` VALUES (49, '2020-11-06 11:50:13.440931', '2020-11-06 11:50:13.440944', 0, 'name', 10, '/api/v1/account/user/role/list/', 0, NULL);
INSERT INTO `permission` VALUES (50, '2020-11-06 11:50:13.440971', '2020-11-06 11:50:13.440985', 0, 'name', 10, '/api/v1/account/user/department/list/', 0, NULL);
INSERT INTO `permission` VALUES (51, '2020-11-06 11:50:13.441012', '2020-11-06 11:50:13.441026', 0, 'name', 10, '/api/v1/account/role/', 0, NULL);
INSERT INTO `permission` VALUES (52, '2020-11-06 11:50:13.441053', '2020-11-06 11:50:13.441066', 0, 'name', 10, '/api/v1/account/role/list/', 0, NULL);
INSERT INTO `permission` VALUES (53, '2020-11-06 11:50:13.441093', '2020-11-06 11:50:13.441106', 0, 'name', 10, '/api/v1/account/role/user/list/', 0, NULL);
INSERT INTO `permission` VALUES (54, '2020-11-06 11:50:13.441133', '2020-11-06 11:50:13.441146', 0, 'name', 10, '/api/v1/account/role/mod/list/', 0, NULL);
INSERT INTO `permission` VALUES (55, '2020-11-06 11:50:13.441173', '2020-11-06 11:50:13.441186', 0, 'name', 10, '/api/v1/account/role/permission/list/', 0, NULL);
INSERT INTO `permission` VALUES (56, '2020-11-06 11:50:13.441213', '2020-11-06 11:50:13.441226', 0, 'name', 10, '/api/v1/account/role/mod/permission/', 0, NULL);
INSERT INTO `permission` VALUES (57, '2020-11-06 11:50:13.441253', '2020-11-06 11:50:13.441267', 0, 'name', 10, '/api/v1/account/mod/', 0, NULL);
INSERT INTO `permission` VALUES (58, '2020-11-06 11:50:13.441294', '2020-11-06 11:50:13.441307', 0, 'name', 10, '/api/v1/account/mod/list/', 0, NULL);
INSERT INTO `permission` VALUES (59, '2020-11-06 11:50:13.441334', '2020-11-06 11:50:13.441347', 0, 'name', 10, '/api/v1/account/department/', 0, NULL);
INSERT INTO `permission` VALUES (60, '2020-11-06 11:50:13.441374', '2020-11-06 11:50:13.441387', 0, 'name', 10, '/api/v1/account/department/list/', 0, NULL);
INSERT INTO `permission` VALUES (61, '2020-11-06 11:50:13.441414', '2020-11-06 11:50:13.441428', 0, 'name', 10, '/api/v1/account/department/user/list/', 0, NULL);
INSERT INTO `permission` VALUES (62, '2020-11-06 11:50:13.441455', '2020-11-06 11:50:13.441468', 0, 'name', 10, '/api/v1/account/permission/', 0, NULL);
INSERT INTO `permission` VALUES (63, '2020-11-06 11:50:13.441495', '2020-11-06 11:50:13.441508', 0, 'name', 10, '/api/v1/account/permission/list/', 0, NULL);
INSERT INTO `permission` VALUES (64, '2020-11-10 06:44:15.585198', '2020-11-10 06:44:15.585257', 0, 'name', 10, '/api/v1/business/project/department/list/', 0, NULL);
INSERT INTO `permission` VALUES (65, '2020-11-10 06:44:15.585304', '2020-11-10 06:44:15.585320', 0, 'name', 10, '/api/v1/business/project/service/list/', 0, NULL);
INSERT INTO `permission` VALUES (66, '2020-11-10 06:44:15.585349', '2020-11-10 06:44:15.585363', 0, '创建服务关联部门', 10, '/api/v1/business/service/department/create/', 70, 6);
INSERT INTO `permission` VALUES (67, '2020-11-10 06:44:15.585392', '2020-11-10 06:44:15.585405', 0, '删除服务关联部门', 10, '/api/v1/business/service/department/delete/', 69, 6);
INSERT INTO `permission` VALUES (68, '2020-11-10 06:44:15.585433', '2020-11-10 06:44:15.585447', 0, 'name', 10, '/api/v1/business/service/department/list/', 0, NULL);
INSERT INTO `permission` VALUES (69, '2020-11-27 08:34:43.328551', '2020-11-27 08:34:43.328609', 0, '创建服务关联环境', 10, '/api/v1/business/service/environment/create/', 60, 6);
INSERT INTO `permission` VALUES (70, '2020-11-27 08:34:58.347496', '2020-11-27 08:34:58.347549', 0, '删除服务关联环境', 10, '/api/v1/business/service/environment/delete/', 59, 6);
INSERT INTO `permission` VALUES (71, '2020-11-27 08:37:07.390971', '2020-11-27 08:37:07.391019', 0, '创建环境', 10, '/api/v1/business/environment/create/', 100, 7);
INSERT INTO `permission` VALUES (72, '2020-11-27 08:37:19.315751', '2020-11-27 08:37:19.315797', 0, '编辑环境', 10, '/api/v1/business/environment/update/', 90, 7);
INSERT INTO `permission` VALUES (73, '2020-11-27 08:37:32.801874', '2020-11-27 08:37:32.801936', 0, '删除环境', 10, '/api/v1/business/environment/delete/', 80, 7);
INSERT INTO `permission` VALUES (74, '2020-12-01 03:26:47.000402', '2020-12-01 03:26:47.000469', 0, '创建服务关联资产模块', 10, '/api/v1/business/service/asset/create/', 30, 6);
INSERT INTO `permission` VALUES (75, '2020-12-01 03:27:06.514420', '2020-12-01 03:27:06.514461', 0, '删除服务关联资产模块', 10, '/api/v1/business/service/asset/delete/', 29, 6);
COMMIT;

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `remark` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of project
-- ----------------------------
BEGIN;
INSERT INTO `project` VALUES (1, '2020-11-06 10:33:10.920210', '2020-11-11 02:19:14.989482', 0, '运维平台', '用于运维');
INSERT INTO `project` VALUES (2, '2020-11-07 10:17:08.967179', '2020-11-11 02:19:23.787115', 0, '权限系统', '用于权限管理');
INSERT INTO `project` VALUES (3, '2020-11-25 06:15:58.064205', '2020-11-25 06:15:58.064707', 0, '工单系统', '用于流程审批');
COMMIT;

-- ----------------------------
-- Table structure for project_user
-- ----------------------------
DROP TABLE IF EXISTS `project_user`;
CREATE TABLE `project_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `typ` smallint(6) NOT NULL,
  `project_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `project_user_project_id_ebbcc526_fk_project_id` (`project_id`),
  KEY `project_user_user_id_fd20b2f6_fk_user_id` (`user_id`),
  CONSTRAINT `project_user_project_id_ebbcc526_fk_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `project_user_user_id_fd20b2f6_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of project_user
-- ----------------------------
BEGIN;
INSERT INTO `project_user` VALUES (1, '2020-11-06 10:48:08.177234', '2020-11-06 10:48:08.177275', 0, 20, 1, 2);
COMMIT;

-- ----------------------------
-- Table structure for region
-- ----------------------------
DROP TABLE IF EXISTS `region`;
CREATE TABLE `region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `instance_id` varchar(128) NOT NULL,
  `endpoint` varchar(128) NOT NULL,
  `status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of region
-- ----------------------------
BEGIN;
INSERT INTO `region` VALUES (47, '2020-11-26 12:22:20.685658', '2020-11-26 12:22:20.685775', 0, '华北 1', 'cn-qingdao', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (48, '2020-11-26 12:22:20.685818', '2020-11-26 12:22:38.212399', 0, '华北 2', 'cn-beijing', 'ecs.aliyuncs.com', 10);
INSERT INTO `region` VALUES (49, '2020-11-26 12:22:20.685861', '2020-11-26 12:22:43.591381', 0, '华北 3', 'cn-zhangjiakou', 'ecs.cn-zhangjiakou.aliyuncs.com', 10);
INSERT INTO `region` VALUES (50, '2020-11-26 12:22:20.685900', '2020-11-26 12:22:20.685914', 0, '华北 5', 'cn-huhehaote', 'ecs.cn-huhehaote.aliyuncs.com', 20);
INSERT INTO `region` VALUES (51, '2020-11-26 12:22:20.685939', '2020-11-26 12:22:20.685952', 0, '华北6（乌兰察布）', 'cn-wulanchabu', 'ecs.cn-wulanchabu.aliyuncs.com', 20);
INSERT INTO `region` VALUES (52, '2020-11-26 12:22:20.685978', '2020-11-26 12:22:20.685995', 0, '华东 1', 'cn-hangzhou', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (53, '2020-11-26 12:22:20.686022', '2020-11-26 12:22:20.686035', 0, '华东 2', 'cn-shanghai', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (54, '2020-11-26 12:22:20.686061', '2020-11-26 12:22:20.686074', 0, '华南 1', 'cn-shenzhen', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (55, '2020-11-26 12:22:20.686100', '2020-11-26 12:22:20.686113', 0, '华南2（河源）', 'cn-heyuan', 'ecs.cn-heyuan.aliyuncs.com', 20);
INSERT INTO `region` VALUES (56, '2020-11-26 12:22:20.686139', '2020-11-26 12:22:20.686155', 0, '华南3（广州）', 'cn-guangzhou', 'ecs.cn-guangzhou.aliyuncs.com', 20);
INSERT INTO `region` VALUES (57, '2020-11-26 12:22:20.686181', '2020-11-26 12:22:20.686194', 0, '西南1（成都）', 'cn-chengdu', 'ecs.cn-chengdu.aliyuncs.com', 20);
INSERT INTO `region` VALUES (58, '2020-11-26 12:22:20.686220', '2020-11-26 12:22:20.686233', 0, '香港', 'cn-hongkong', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (59, '2020-11-26 12:22:20.686259', '2020-11-26 12:22:20.686272', 0, '亚太东北 1 (东京)', 'ap-northeast-1', 'ecs.ap-northeast-1.aliyuncs.com', 20);
INSERT INTO `region` VALUES (60, '2020-11-26 12:22:20.686298', '2020-11-26 12:22:20.686311', 0, '亚太东南 1 (新加坡)', 'ap-southeast-1', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (61, '2020-11-26 12:22:20.686336', '2020-11-26 12:22:20.686350', 0, '亚太东南 2 (悉尼)', 'ap-southeast-2', 'ecs.ap-southeast-2.aliyuncs.com', 20);
INSERT INTO `region` VALUES (62, '2020-11-26 12:22:20.686375', '2020-11-26 12:22:20.686388', 0, '亚太东南 3 (吉隆坡)', 'ap-southeast-3', 'ecs.ap-southeast-3.aliyuncs.com', 20);
INSERT INTO `region` VALUES (63, '2020-11-26 12:22:20.686414', '2020-11-26 12:22:20.686427', 0, '亚太东南 5 (雅加达)', 'ap-southeast-5', 'ecs.ap-southeast-5.aliyuncs.com', 20);
INSERT INTO `region` VALUES (64, '2020-11-26 12:22:20.686453', '2020-11-26 12:22:20.686466', 0, '亚太南部 1 (孟买)', 'ap-south-1', 'ecs.ap-south-1.aliyuncs.com', 20);
INSERT INTO `region` VALUES (65, '2020-11-26 12:22:20.686492', '2020-11-26 12:22:20.686505', 0, '美国东部 1 (弗吉尼亚)', 'us-east-1', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (66, '2020-11-26 12:22:20.686531', '2020-11-26 12:22:20.686544', 0, '美国西部 1 (硅谷)', 'us-west-1', 'ecs.aliyuncs.com', 20);
INSERT INTO `region` VALUES (67, '2020-11-26 12:22:20.686570', '2020-11-26 12:22:20.686583', 0, '英国 (伦敦)', 'eu-west-1', 'ecs.eu-west-1.aliyuncs.com', 20);
INSERT INTO `region` VALUES (68, '2020-11-26 12:22:20.686608', '2020-11-26 12:22:20.686621', 0, '中东东部 1 (迪拜)', 'me-east-1', 'ecs.me-east-1.aliyuncs.com', 20);
INSERT INTO `region` VALUES (69, '2020-11-26 12:22:20.686647', '2020-11-26 12:22:20.686660', 0, '欧洲中部 1 (法兰克福)', 'eu-central-1', 'ecs.eu-central-1.aliyuncs.com', 20);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role
-- ----------------------------
BEGIN;
INSERT INTO `role` VALUES (1, '2020-11-05 08:45:46.766031', '2020-11-05 08:45:46.766175', 0, '开发工程师', 20, 'dev');
INSERT INTO `role` VALUES (2, '2020-11-06 07:17:57.943663', '2020-11-06 07:17:57.943704', 0, '管理员', 20, 'manager');
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role_mod
-- ----------------------------
BEGIN;
INSERT INTO `role_mod` VALUES (1, '2020-11-05 10:31:00.541293', '2020-11-05 10:34:57.198019', 1, 4, 1);
INSERT INTO `role_mod` VALUES (2, '2020-11-05 10:31:04.564458', '2020-11-05 10:31:19.042445', 1, 3, 1);
INSERT INTO `role_mod` VALUES (3, '2020-11-05 10:31:07.020837', '2020-11-05 10:31:08.781066', 1, 2, 1);
INSERT INTO `role_mod` VALUES (4, '2020-11-05 10:31:20.049692', '2020-11-05 10:31:22.912970', 1, 3, 1);
INSERT INTO `role_mod` VALUES (5, '2020-11-05 10:31:27.043018', '2020-11-05 10:34:54.018489', 1, 3, 1);
INSERT INTO `role_mod` VALUES (6, '2020-11-05 10:34:58.026271', '2020-11-05 10:34:58.026544', 0, 3, 1);
INSERT INTO `role_mod` VALUES (7, '2020-11-06 07:18:00.880961', '2020-11-06 07:18:00.881021', 0, 4, 2);
INSERT INTO `role_mod` VALUES (8, '2020-11-06 07:18:02.682295', '2020-11-06 07:18:02.682433', 0, 3, 2);
INSERT INTO `role_mod` VALUES (9, '2020-11-06 07:18:07.336387', '2020-11-06 07:18:07.336446', 0, 2, 2);
INSERT INTO `role_mod` VALUES (10, '2020-11-10 06:08:09.095080', '2020-11-10 06:08:09.095123', 0, 5, 2);
INSERT INTO `role_mod` VALUES (11, '2020-11-10 06:08:15.207004', '2020-11-10 09:59:22.143137', 1, 6, 2);
INSERT INTO `role_mod` VALUES (12, '2020-11-10 09:59:55.159388', '2020-11-10 09:59:55.159732', 0, 6, 2);
INSERT INTO `role_mod` VALUES (13, '2020-11-27 08:37:40.118063', '2020-11-27 08:37:40.118103', 0, 7, 2);
INSERT INTO `role_mod` VALUES (14, '2020-11-28 10:23:37.035079', '2020-11-28 10:23:37.035126', 0, 8, 2);
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role_permission
-- ----------------------------
BEGIN;
INSERT INTO `role_permission` VALUES (1, '2020-11-05 10:31:00.522597', '2020-11-05 10:31:15.553982', 1, 18, 1);
INSERT INTO `role_permission` VALUES (2, '2020-11-05 10:31:02.621587', '2020-11-05 10:31:16.336795', 1, 19, 1);
INSERT INTO `role_permission` VALUES (3, '2020-11-05 10:31:03.442850', '2020-11-05 10:31:17.129070', 1, 20, 1);
INSERT INTO `role_permission` VALUES (4, '2020-11-05 10:31:04.549044', '2020-11-05 10:31:13.032910', 1, 13, 1);
INSERT INTO `role_permission` VALUES (5, '2020-11-05 10:31:05.715638', '2020-11-05 10:31:14.062393', 1, 14, 1);
INSERT INTO `role_permission` VALUES (6, '2020-11-05 10:31:07.838535', '2020-11-05 10:31:11.595288', 1, 12, 1);
INSERT INTO `role_permission` VALUES (7, '2020-11-05 10:31:20.927144', '2020-11-05 10:34:54.028257', 1, 13, 1);
INSERT INTO `role_permission` VALUES (8, '2020-11-05 10:31:21.945541', '2020-11-05 10:34:54.028257', 1, 14, 1);
INSERT INTO `role_permission` VALUES (9, '2020-11-05 10:34:55.871197', '2020-11-05 10:34:57.208557', 1, 18, 1);
INSERT INTO `role_permission` VALUES (10, '2020-11-05 10:34:56.435799', '2020-11-05 10:34:57.208557', 1, 19, 1);
INSERT INTO `role_permission` VALUES (11, '2020-11-05 10:34:58.004780', '2020-11-05 10:34:58.004836', 0, 13, 1);
INSERT INTO `role_permission` VALUES (12, '2020-11-05 10:34:58.489812', '2020-11-05 10:34:58.489892', 0, 14, 1);
INSERT INTO `role_permission` VALUES (13, '2020-11-06 07:18:00.869205', '2020-11-06 07:18:00.869248', 0, 18, 2);
INSERT INTO `role_permission` VALUES (14, '2020-11-06 07:18:01.452497', '2020-11-06 07:18:01.452544', 0, 19, 2);
INSERT INTO `role_permission` VALUES (15, '2020-11-06 07:18:01.973920', '2020-11-06 07:18:01.973960', 0, 20, 2);
INSERT INTO `role_permission` VALUES (16, '2020-11-06 07:18:02.669546', '2020-11-06 07:18:02.669602', 0, 15, 2);
INSERT INTO `role_permission` VALUES (17, '2020-11-06 07:18:04.015526', '2020-11-06 07:18:04.015585', 0, 13, 2);
INSERT INTO `role_permission` VALUES (18, '2020-11-06 07:18:04.585716', '2020-11-06 07:18:04.585758', 0, 14, 2);
INSERT INTO `role_permission` VALUES (19, '2020-11-06 07:18:05.540527', '2020-11-06 07:18:05.540566', 0, 16, 2);
INSERT INTO `role_permission` VALUES (20, '2020-11-06 07:18:06.296457', '2020-11-06 07:18:06.296501', 0, 17, 2);
INSERT INTO `role_permission` VALUES (21, '2020-11-06 07:18:07.323346', '2020-11-06 07:18:07.323397', 0, 7, 2);
INSERT INTO `role_permission` VALUES (22, '2020-11-06 07:18:07.927562', '2020-11-06 07:18:07.927602', 0, 8, 2);
INSERT INTO `role_permission` VALUES (23, '2020-11-06 07:18:08.625044', '2020-11-06 07:18:08.625106', 0, 9, 2);
INSERT INTO `role_permission` VALUES (24, '2020-11-06 07:18:09.353280', '2020-11-06 07:18:09.353330', 0, 10, 2);
INSERT INTO `role_permission` VALUES (25, '2020-11-06 07:18:10.001470', '2020-11-06 07:18:10.001532', 0, 11, 2);
INSERT INTO `role_permission` VALUES (26, '2020-11-06 07:18:11.325284', '2020-11-06 07:18:11.325346', 0, 12, 2);
INSERT INTO `role_permission` VALUES (27, '2020-11-06 07:24:05.453487', '2020-11-06 07:24:05.453529', 0, 21, 2);
INSERT INTO `role_permission` VALUES (28, '2020-11-06 07:24:06.291906', '2020-11-06 07:24:06.291947', 0, 22, 2);
INSERT INTO `role_permission` VALUES (29, '2020-11-10 06:08:09.077233', '2020-11-10 06:08:09.077274', 0, 26, 2);
INSERT INTO `role_permission` VALUES (30, '2020-11-10 06:08:09.811513', '2020-11-10 06:08:09.811621', 0, 27, 2);
INSERT INTO `role_permission` VALUES (31, '2020-11-10 06:08:10.493897', '2020-11-10 06:08:10.493935', 0, 28, 2);
INSERT INTO `role_permission` VALUES (32, '2020-11-10 06:08:11.192069', '2020-11-10 06:08:11.192109', 0, 29, 2);
INSERT INTO `role_permission` VALUES (33, '2020-11-10 06:08:11.819231', '2020-11-10 06:08:11.819339', 0, 30, 2);
INSERT INTO `role_permission` VALUES (34, '2020-11-10 06:08:12.421448', '2020-11-10 06:08:12.421488', 0, 31, 2);
INSERT INTO `role_permission` VALUES (35, '2020-11-10 06:08:13.109717', '2020-11-10 06:08:13.109859', 0, 32, 2);
INSERT INTO `role_permission` VALUES (36, '2020-11-10 06:08:13.829533', '2020-11-10 06:08:13.829576', 0, 33, 2);
INSERT INTO `role_permission` VALUES (37, '2020-11-10 06:08:15.181413', '2020-11-10 09:59:22.155676', 1, 37, 2);
INSERT INTO `role_permission` VALUES (38, '2020-11-10 06:08:15.958203', '2020-11-10 09:59:22.155676', 1, 38, 2);
INSERT INTO `role_permission` VALUES (39, '2020-11-10 06:08:16.663434', '2020-11-10 09:59:22.155676', 1, 39, 2);
INSERT INTO `role_permission` VALUES (40, '2020-11-10 06:08:17.204208', '2020-11-10 09:59:22.155676', 1, 40, 2);
INSERT INTO `role_permission` VALUES (41, '2020-11-10 06:08:17.870139', '2020-11-10 09:59:22.155676', 1, 41, 2);
INSERT INTO `role_permission` VALUES (42, '2020-11-10 06:08:18.611246', '2020-11-10 09:59:22.155676', 1, 42, 2);
INSERT INTO `role_permission` VALUES (43, '2020-11-10 09:42:41.508322', '2020-11-10 09:54:21.920192', 1, 66, 2);
INSERT INTO `role_permission` VALUES (44, '2020-11-10 09:42:42.265233', '2020-11-10 09:54:20.753024', 1, 67, 2);
INSERT INTO `role_permission` VALUES (45, '2020-11-10 09:54:57.939693', '2020-11-10 09:58:54.468836', 1, 66, 2);
INSERT INTO `role_permission` VALUES (46, '2020-11-10 09:54:59.535734', '2020-11-10 09:59:05.984541', 1, 67, 2);
INSERT INTO `role_permission` VALUES (47, '2020-11-10 09:59:55.139915', '2020-11-10 09:59:55.139956', 0, 37, 2);
INSERT INTO `role_permission` VALUES (48, '2020-11-10 09:59:55.715479', '2020-11-10 09:59:55.715537', 0, 38, 2);
INSERT INTO `role_permission` VALUES (49, '2020-11-10 09:59:56.617616', '2020-11-10 09:59:56.617674', 0, 39, 2);
INSERT INTO `role_permission` VALUES (50, '2020-11-10 09:59:57.282143', '2020-11-10 09:59:57.282206', 0, 40, 2);
INSERT INTO `role_permission` VALUES (51, '2020-11-10 09:59:58.586125', '2020-11-10 09:59:58.586167', 0, 41, 2);
INSERT INTO `role_permission` VALUES (52, '2020-11-10 09:59:59.521815', '2020-11-10 09:59:59.521854', 0, 42, 2);
INSERT INTO `role_permission` VALUES (53, '2020-11-10 10:00:02.229650', '2020-11-10 10:00:02.229980', 0, 66, 2);
INSERT INTO `role_permission` VALUES (54, '2020-11-10 10:00:03.735617', '2020-11-10 10:00:48.341374', 1, 67, 2);
INSERT INTO `role_permission` VALUES (55, '2020-11-10 10:01:03.693578', '2020-11-10 10:01:03.693691', 0, 67, 2);
INSERT INTO `role_permission` VALUES (56, '2020-11-27 08:35:05.680695', '2020-11-27 08:35:05.680741', 0, 69, 2);
INSERT INTO `role_permission` VALUES (57, '2020-11-27 08:35:06.400507', '2020-11-27 08:35:06.400609', 0, 70, 2);
INSERT INTO `role_permission` VALUES (58, '2020-11-27 08:37:41.069126', '2020-11-27 08:37:41.069165', 0, 71, 2);
INSERT INTO `role_permission` VALUES (59, '2020-11-27 08:37:41.678468', '2020-11-27 08:37:53.992781', 1, 72, 2);
INSERT INTO `role_permission` VALUES (60, '2020-11-27 08:37:42.292193', '2020-11-27 08:37:53.040048', 1, 73, 2);
INSERT INTO `role_permission` VALUES (61, '2020-12-01 03:27:19.000342', '2020-12-01 03:27:19.000386', 0, 74, 2);
INSERT INTO `role_permission` VALUES (62, '2020-12-01 03:27:19.854893', '2020-12-01 03:27:19.854939', 0, 75, 2);
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of role_user
-- ----------------------------
BEGIN;
INSERT INTO `role_user` VALUES (1, '2020-11-06 07:18:23.928603', '2020-11-06 07:18:23.928671', 0, 2, 2);
COMMIT;

-- ----------------------------
-- Table structure for service
-- ----------------------------
DROP TABLE IF EXISTS `service`;
CREATE TABLE `service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `sign` varchar(128) NOT NULL,
  `remark` longtext,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `service_project_id_6e6d0821_fk_project_id` (`project_id`),
  CONSTRAINT `service_project_id_6e6d0821_fk_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of service
-- ----------------------------
BEGIN;
INSERT INTO `service` VALUES (1, '2020-11-07 10:17:30.413472', '2020-11-07 10:52:11.582977', 0, '运维系统前端', 'enjoy', NULL, 1);
INSERT INTO `service` VALUES (2, '2020-11-07 10:45:01.293950', '2020-11-07 10:52:20.488689', 0, '运维系统后端', 'rurality', NULL, 1);
COMMIT;

-- ----------------------------
-- Table structure for service_asset
-- ----------------------------
DROP TABLE IF EXISTS `service_asset`;
CREATE TABLE `service_asset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `asset_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `service_asset_asset_id_a00b7f13_fk_asset_id` (`asset_id`),
  KEY `service_asset_service_id_2805134d_fk_service_id` (`service_id`),
  CONSTRAINT `service_asset_asset_id_a00b7f13_fk_asset_id` FOREIGN KEY (`asset_id`) REFERENCES `asset` (`id`),
  CONSTRAINT `service_asset_service_id_2805134d_fk_service_id` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of service_asset
-- ----------------------------
BEGIN;
INSERT INTO `service_asset` VALUES (1, '2020-12-01 03:27:43.783912', '2020-12-01 03:27:43.783956', 0, 1, 1);
INSERT INTO `service_asset` VALUES (2, '2020-12-01 03:27:49.322467', '2020-12-01 03:27:49.322532', 0, 3, 1);
INSERT INTO `service_asset` VALUES (3, '2020-12-01 03:27:53.259204', '2020-12-01 03:27:53.259265', 0, 4, 1);
COMMIT;

-- ----------------------------
-- Table structure for service_environment
-- ----------------------------
DROP TABLE IF EXISTS `service_environment`;
CREATE TABLE `service_environment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `environment_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `service_environment_environment_id_9cbd560e_fk_environment_id` (`environment_id`),
  KEY `service_environment_service_id_c6f2006f_fk_service_id` (`service_id`),
  CONSTRAINT `service_environment_environment_id_9cbd560e_fk_environment_id` FOREIGN KEY (`environment_id`) REFERENCES `environment` (`id`),
  CONSTRAINT `service_environment_service_id_c6f2006f_fk_service_id` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of service_environment
-- ----------------------------
BEGIN;
INSERT INTO `service_environment` VALUES (1, '2020-11-27 08:35:23.610069', '2020-11-27 08:35:26.457864', 1, 2, 1);
INSERT INTO `service_environment` VALUES (2, '2020-11-27 08:35:30.507815', '2020-11-27 08:35:30.507885', 0, 2, 1);
COMMIT;

-- ----------------------------
-- Table structure for service_user
-- ----------------------------
DROP TABLE IF EXISTS `service_user`;
CREATE TABLE `service_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `typ` smallint(6) NOT NULL,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `service_user_service_id_841bc91a_fk_service_id` (`service_id`),
  KEY `service_user_user_id_c30338c4_fk_user_id` (`user_id`),
  CONSTRAINT `service_user_service_id_841bc91a_fk_service_id` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`),
  CONSTRAINT `service_user_user_id_c30338c4_fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of service_user
-- ----------------------------
BEGIN;
INSERT INTO `service_user` VALUES (1, '2020-11-07 10:21:38.487791', '2020-11-10 09:35:21.906763', 1, 10, 1, 2);
INSERT INTO `service_user` VALUES (2, '2020-11-07 10:22:23.302933', '2020-11-10 09:35:19.484129', 1, 20, 1, 3);
INSERT INTO `service_user` VALUES (3, '2020-11-07 10:54:27.332821', '2020-11-07 10:54:27.332863', 0, 20, 2, 2);
INSERT INTO `service_user` VALUES (4, '2020-11-07 10:54:41.238474', '2020-11-07 10:54:41.238520', 0, 10, 2, 3);
INSERT INTO `service_user` VALUES (5, '2020-11-10 09:35:28.016470', '2020-11-10 09:35:28.016512', 0, 10, 1, 2);
INSERT INTO `service_user` VALUES (6, '2020-11-10 09:35:45.275634', '2020-11-10 09:35:45.275743', 0, 20, 1, 3);
COMMIT;

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, '2020-11-05 06:04:04.732877', '2020-11-05 06:04:04.958336', 0, 'admin', 'pbkdf2_sha256$216000$V5XG3BZQLTgW$Tfh/WgIj0slbyElYnZNAiLht9GInAlulqalTrTrDVzs=', '超级管理员', NULL, NULL, 10, 10);
INSERT INTO `user` VALUES (2, '2020-11-06 07:17:47.936792', '2020-11-06 07:17:48.206010', 0, 'buxingxing', 'pbkdf2_sha256$216000$Vk8DCMr9YoSi$jftHttrQOfc5LwUsN0LvFYKubJ3sl8FlM8F9ak4fRHI=', '卜星星', '', '', 10, 10);
INSERT INTO `user` VALUES (3, '2020-11-07 10:21:53.576676', '2020-11-07 10:21:53.865161', 0, 'wanger', 'pbkdf2_sha256$216000$K2nt1VoivRWL$0rFCNADRwwnsjJzE/PPLmP8MXoT9bqaVEqLFgFFQTsY=', '王二', '', '', 10, 10);
COMMIT;

-- ----------------------------
-- Table structure for zone
-- ----------------------------
DROP TABLE IF EXISTS `zone`;
CREATE TABLE `zone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_create` datetime(6) NOT NULL,
  `dt_update` datetime(6) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `name` varchar(128) NOT NULL,
  `instance_id` varchar(128) NOT NULL,
  `region_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `zone_region_id_d806a9c4_fk_region_id` (`region_id`),
  CONSTRAINT `zone_region_id_d806a9c4_fk_region_id` FOREIGN KEY (`region_id`) REFERENCES `region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of zone
-- ----------------------------
BEGIN;
INSERT INTO `zone` VALUES (1, '2020-11-26 12:29:44.565805', '2020-11-26 12:29:44.565866', 0, '华北 1 可用区 C', 'cn-qingdao-c', 47);
INSERT INTO `zone` VALUES (2, '2020-11-26 12:29:44.565915', '2020-11-26 12:29:44.565931', 0, '华北 1 可用区 C', 'cn-qingdao-c', 47);
INSERT INTO `zone` VALUES (3, '2020-11-26 12:29:44.565960', '2020-11-26 12:29:44.565975', 0, '华北 1 可用区 B', 'cn-qingdao-b', 47);
INSERT INTO `zone` VALUES (4, '2020-11-26 12:29:44.566002', '2020-11-26 12:29:44.566017', 0, '华北 1 可用区 B', 'cn-qingdao-b', 47);
INSERT INTO `zone` VALUES (5, '2020-11-26 12:29:44.566044', '2020-11-26 12:29:44.566059', 0, '华北 2 可用区 H', 'cn-beijing-h', 48);
INSERT INTO `zone` VALUES (6, '2020-11-26 12:29:44.566086', '2020-11-26 12:29:44.566100', 0, '华北 2 可用区 H', 'cn-beijing-h', 48);
INSERT INTO `zone` VALUES (7, '2020-11-26 12:29:44.566127', '2020-11-26 12:29:44.566141', 0, '华北 2 可用区 G', 'cn-beijing-g', 48);
INSERT INTO `zone` VALUES (8, '2020-11-26 12:29:44.566168', '2020-11-26 12:29:44.566183', 0, '华北 2 可用区 G', 'cn-beijing-g', 48);
INSERT INTO `zone` VALUES (9, '2020-11-26 12:29:44.566209', '2020-11-26 12:29:44.566224', 0, '华北 2 可用区 F', 'cn-beijing-f', 48);
INSERT INTO `zone` VALUES (10, '2020-11-26 12:29:44.566259', '2020-11-26 12:29:44.566274', 0, '华北 2 可用区 F', 'cn-beijing-f', 48);
INSERT INTO `zone` VALUES (11, '2020-11-26 12:29:44.566301', '2020-11-26 12:29:44.566318', 0, '华北 2 可用区 C', 'cn-beijing-c', 48);
INSERT INTO `zone` VALUES (12, '2020-11-26 12:29:44.566347', '2020-11-26 12:29:44.566362', 0, '华北 2 可用区 C', 'cn-beijing-c', 48);
INSERT INTO `zone` VALUES (13, '2020-11-26 12:29:44.566404', '2020-11-26 12:29:44.566418', 0, '华北 2 可用区 E', 'cn-beijing-e', 48);
INSERT INTO `zone` VALUES (14, '2020-11-26 12:29:44.566445', '2020-11-26 12:29:44.566462', 0, '华北 2 可用区 E', 'cn-beijing-e', 48);
INSERT INTO `zone` VALUES (15, '2020-11-26 12:29:44.566491', '2020-11-26 12:29:44.566505', 0, '华北 2 可用区 D', 'cn-beijing-d', 48);
INSERT INTO `zone` VALUES (16, '2020-11-26 12:29:44.566531', '2020-11-26 12:29:44.566544', 0, '华北 2 可用区 D', 'cn-beijing-d', 48);
INSERT INTO `zone` VALUES (17, '2020-11-26 12:29:44.566570', '2020-11-26 12:29:44.566606', 0, '华北 2 可用区 A', 'cn-beijing-a', 48);
INSERT INTO `zone` VALUES (18, '2020-11-26 12:29:44.566665', '2020-11-26 12:29:44.566683', 0, '华北 2 可用区 A', 'cn-beijing-a', 48);
INSERT INTO `zone` VALUES (19, '2020-11-26 12:29:44.566711', '2020-11-26 12:29:44.566725', 0, '华北 2 可用区 B', 'cn-beijing-b', 48);
INSERT INTO `zone` VALUES (20, '2020-11-26 12:29:44.566750', '2020-11-26 12:29:44.566764', 0, '华北 2 可用区 B', 'cn-beijing-b', 48);
INSERT INTO `zone` VALUES (21, '2020-11-26 12:29:44.566789', '2020-11-26 12:29:44.566803', 0, '华北 2 可用区 J', 'cn-beijing-j', 48);
INSERT INTO `zone` VALUES (22, '2020-11-26 12:29:44.566828', '2020-11-26 12:29:44.566842', 0, '华北 2 可用区 J', 'cn-beijing-j', 48);
INSERT INTO `zone` VALUES (23, '2020-11-26 12:29:44.566867', '2020-11-26 12:29:44.566880', 0, '华北 3 可用区 A', 'cn-zhangjiakou-a', 49);
INSERT INTO `zone` VALUES (24, '2020-11-26 12:29:44.566906', '2020-11-26 12:29:44.566919', 0, '华北 3 可用区 A', 'cn-zhangjiakou-a', 49);
INSERT INTO `zone` VALUES (25, '2020-11-26 12:29:44.566944', '2020-11-26 12:29:44.566958', 0, '华北 3 可用区 C', 'cn-zhangjiakou-c', 49);
INSERT INTO `zone` VALUES (26, '2020-11-26 12:29:44.566983', '2020-11-26 12:29:44.566997', 0, '华北 3 可用区 C', 'cn-zhangjiakou-c', 49);
INSERT INTO `zone` VALUES (27, '2020-11-26 12:29:44.567022', '2020-11-26 12:29:44.567036', 0, '华北 3 可用区 B', 'cn-zhangjiakou-b', 49);
INSERT INTO `zone` VALUES (28, '2020-11-26 12:29:44.567062', '2020-11-26 12:29:44.567076', 0, '华北 3 可用区 B', 'cn-zhangjiakou-b', 49);
INSERT INTO `zone` VALUES (29, '2020-11-26 12:29:44.567101', '2020-11-26 12:29:44.567114', 0, '华北5 可用区A', 'cn-huhehaote-a', 50);
INSERT INTO `zone` VALUES (30, '2020-11-26 12:29:44.567139', '2020-11-26 12:29:44.567153', 0, '华北5 可用区A', 'cn-huhehaote-a', 50);
INSERT INTO `zone` VALUES (31, '2020-11-26 12:29:44.567178', '2020-11-26 12:29:44.567192', 0, '华北5 可用区B', 'cn-huhehaote-b', 50);
INSERT INTO `zone` VALUES (32, '2020-11-26 12:29:44.567217', '2020-11-26 12:29:44.567231', 0, '华北5 可用区B', 'cn-huhehaote-b', 50);
INSERT INTO `zone` VALUES (33, '2020-11-26 12:29:44.567256', '2020-11-26 12:29:44.567270', 0, '乌兰察布 可用区B', 'cn-wulanchabu-b', 51);
INSERT INTO `zone` VALUES (34, '2020-11-26 12:29:44.567295', '2020-11-26 12:29:44.567309', 0, '乌兰察布 可用区B', 'cn-wulanchabu-b', 51);
INSERT INTO `zone` VALUES (35, '2020-11-26 12:29:44.567334', '2020-11-26 12:29:44.567347', 0, '乌兰察布 可用区A', 'cn-wulanchabu-a', 51);
INSERT INTO `zone` VALUES (36, '2020-11-26 12:29:44.567372', '2020-11-26 12:29:44.567386', 0, '乌兰察布 可用区A', 'cn-wulanchabu-a', 51);
INSERT INTO `zone` VALUES (37, '2020-11-26 12:29:44.567411', '2020-11-26 12:29:44.567424', 0, '乌兰察布 可用区C', 'cn-wulanchabu-c', 51);
INSERT INTO `zone` VALUES (38, '2020-11-26 12:29:44.567450', '2020-11-26 12:29:44.567463', 0, '乌兰察布 可用区C', 'cn-wulanchabu-c', 51);
INSERT INTO `zone` VALUES (39, '2020-11-26 12:29:44.567488', '2020-11-26 12:29:44.567502', 0, '华东 1 可用区 I', 'cn-hangzhou-i', 52);
INSERT INTO `zone` VALUES (40, '2020-11-26 12:29:44.567532', '2020-11-26 12:29:44.567546', 0, '华东 1 可用区 I', 'cn-hangzhou-i', 52);
INSERT INTO `zone` VALUES (41, '2020-11-26 12:29:44.567572', '2020-11-26 12:29:44.567585', 0, '华东 1 可用区 H', 'cn-hangzhou-h', 52);
INSERT INTO `zone` VALUES (42, '2020-11-26 12:29:44.567611', '2020-11-26 12:29:44.567624', 0, '华东 1 可用区 H', 'cn-hangzhou-h', 52);
INSERT INTO `zone` VALUES (43, '2020-11-26 12:29:44.567649', '2020-11-26 12:29:44.567663', 0, '华东 1 可用区 G', 'cn-hangzhou-g', 52);
INSERT INTO `zone` VALUES (44, '2020-11-26 12:29:44.567688', '2020-11-26 12:29:44.567701', 0, '华东 1 可用区 G', 'cn-hangzhou-g', 52);
INSERT INTO `zone` VALUES (45, '2020-11-26 12:29:44.567726', '2020-11-26 12:29:44.567740', 0, '华东 1 可用区 F', 'cn-hangzhou-f', 52);
INSERT INTO `zone` VALUES (46, '2020-11-26 12:29:44.567765', '2020-11-26 12:29:44.567779', 0, '华东 1 可用区 F', 'cn-hangzhou-f', 52);
INSERT INTO `zone` VALUES (47, '2020-11-26 12:29:44.567804', '2020-11-26 12:29:44.567818', 0, '华东 1 可用区 B', 'cn-hangzhou-b', 52);
INSERT INTO `zone` VALUES (48, '2020-11-26 12:29:44.567843', '2020-11-26 12:29:44.567857', 0, '华东 1 可用区 B', 'cn-hangzhou-b', 52);
INSERT INTO `zone` VALUES (49, '2020-11-26 12:29:44.567882', '2020-11-26 12:29:44.567895', 0, '华东 1 可用区 E', 'cn-hangzhou-e', 52);
INSERT INTO `zone` VALUES (50, '2020-11-26 12:29:44.567920', '2020-11-26 12:29:44.567934', 0, '华东 1 可用区 E', 'cn-hangzhou-e', 52);
INSERT INTO `zone` VALUES (51, '2020-11-26 12:29:44.567959', '2020-11-26 12:29:44.567972', 0, '华东 1 可用区 D', 'cn-hangzhou-d', 52);
INSERT INTO `zone` VALUES (52, '2020-11-26 12:29:44.567997', '2020-11-26 12:29:44.568011', 0, '华东 1 可用区 D', 'cn-hangzhou-d', 52);
INSERT INTO `zone` VALUES (53, '2020-11-26 12:29:44.568036', '2020-11-26 12:29:44.568049', 0, '华东 1 可用区 C', 'cn-hangzhou-c', 52);
INSERT INTO `zone` VALUES (54, '2020-11-26 12:29:44.568074', '2020-11-26 12:29:44.568088', 0, '华东 1 可用区 C', 'cn-hangzhou-c', 52);
INSERT INTO `zone` VALUES (55, '2020-11-26 12:29:44.568112', '2020-11-26 12:29:44.568126', 0, '华东 1 可用区 J', 'cn-hangzhou-j', 52);
INSERT INTO `zone` VALUES (56, '2020-11-26 12:29:44.568151', '2020-11-26 12:29:44.568168', 0, '华东 1 可用区 J', 'cn-hangzhou-j', 52);
INSERT INTO `zone` VALUES (57, '2020-11-26 12:29:44.568194', '2020-11-26 12:29:44.568208', 0, '华东 2 可用区 G', 'cn-shanghai-g', 53);
INSERT INTO `zone` VALUES (58, '2020-11-26 12:29:44.568233', '2020-11-26 12:29:44.568247', 0, '华东 2 可用区 G', 'cn-shanghai-g', 53);
INSERT INTO `zone` VALUES (59, '2020-11-26 12:29:44.568272', '2020-11-26 12:29:44.568285', 0, '华东 2 可用区 F', 'cn-shanghai-f', 53);
INSERT INTO `zone` VALUES (60, '2020-11-26 12:29:44.568311', '2020-11-26 12:29:44.568325', 0, '华东 2 可用区 F', 'cn-shanghai-f', 53);
INSERT INTO `zone` VALUES (61, '2020-11-26 12:29:44.568350', '2020-11-26 12:29:44.568364', 0, '华东 2 可用区 E', 'cn-shanghai-e', 53);
INSERT INTO `zone` VALUES (62, '2020-11-26 12:29:44.568389', '2020-11-26 12:29:44.568402', 0, '华东 2 可用区 E', 'cn-shanghai-e', 53);
INSERT INTO `zone` VALUES (63, '2020-11-26 12:29:44.568427', '2020-11-26 12:29:44.568441', 0, '华东 2 可用区 D', 'cn-shanghai-d', 53);
INSERT INTO `zone` VALUES (64, '2020-11-26 12:29:44.568466', '2020-11-26 12:29:44.568480', 0, '华东 2 可用区 D', 'cn-shanghai-d', 53);
INSERT INTO `zone` VALUES (65, '2020-11-26 12:29:44.568507', '2020-11-26 12:29:44.568521', 0, '华东 2 可用区 C', 'cn-shanghai-c', 53);
INSERT INTO `zone` VALUES (66, '2020-11-26 12:29:44.568546', '2020-11-26 12:29:44.568560', 0, '华东 2 可用区 C', 'cn-shanghai-c', 53);
INSERT INTO `zone` VALUES (67, '2020-11-26 12:29:44.568585', '2020-11-26 12:29:44.568599', 0, '华东 2 可用区 B', 'cn-shanghai-b', 53);
INSERT INTO `zone` VALUES (68, '2020-11-26 12:29:44.568624', '2020-11-26 12:29:44.568637', 0, '华东 2 可用区 B', 'cn-shanghai-b', 53);
INSERT INTO `zone` VALUES (69, '2020-11-26 12:29:44.568662', '2020-11-26 12:29:44.568676', 0, '华东 2 可用区 A', 'cn-shanghai-a', 53);
INSERT INTO `zone` VALUES (70, '2020-11-26 12:29:44.568701', '2020-11-26 12:29:44.568715', 0, '华东 2 可用区 A', 'cn-shanghai-a', 53);
INSERT INTO `zone` VALUES (71, '2020-11-26 12:29:44.568740', '2020-11-26 12:29:44.568753', 0, '华南1 可用区 E', 'cn-shenzhen-e', 54);
INSERT INTO `zone` VALUES (72, '2020-11-26 12:29:44.568779', '2020-11-26 12:29:44.568792', 0, '华南1 可用区 E', 'cn-shenzhen-e', 54);
INSERT INTO `zone` VALUES (73, '2020-11-26 12:29:44.568817', '2020-11-26 12:29:44.568834', 0, '华南 1 可用区 D', 'cn-shenzhen-d', 54);
INSERT INTO `zone` VALUES (74, '2020-11-26 12:29:44.568861', '2020-11-26 12:29:44.568875', 0, '华南 1 可用区 D', 'cn-shenzhen-d', 54);
INSERT INTO `zone` VALUES (75, '2020-11-26 12:29:44.568900', '2020-11-26 12:29:44.568914', 0, '华南 1 可用区 C', 'cn-shenzhen-c', 54);
INSERT INTO `zone` VALUES (76, '2020-11-26 12:29:44.568939', '2020-11-26 12:29:44.568953', 0, '华南 1 可用区 C', 'cn-shenzhen-c', 54);
INSERT INTO `zone` VALUES (77, '2020-11-26 12:29:44.568978', '2020-11-26 12:29:44.568991', 0, '华南 1 可用区 A', 'cn-shenzhen-a', 54);
INSERT INTO `zone` VALUES (78, '2020-11-26 12:29:44.569016', '2020-11-26 12:29:44.569030', 0, '华南 1 可用区 A', 'cn-shenzhen-a', 54);
INSERT INTO `zone` VALUES (79, '2020-11-26 12:29:44.569055', '2020-11-26 12:29:44.569069', 0, '华南 1 可用区 B', 'cn-shenzhen-b', 54);
INSERT INTO `zone` VALUES (80, '2020-11-26 12:29:44.569094', '2020-11-26 12:29:44.569107', 0, '华南 1 可用区 B', 'cn-shenzhen-b', 54);
INSERT INTO `zone` VALUES (81, '2020-11-26 12:29:44.569132', '2020-11-26 12:29:44.569145', 0, '华南1 可用区 F', 'cn-shenzhen-f', 54);
INSERT INTO `zone` VALUES (82, '2020-11-26 12:29:44.569171', '2020-11-26 12:29:44.569184', 0, '华南1 可用区 F', 'cn-shenzhen-f', 54);
INSERT INTO `zone` VALUES (83, '2020-11-26 12:29:44.569209', '2020-11-26 12:29:44.569223', 0, '河源 可用区B', 'cn-heyuan-b', 55);
INSERT INTO `zone` VALUES (84, '2020-11-26 12:29:44.569248', '2020-11-26 12:29:44.569261', 0, '河源 可用区B', 'cn-heyuan-b', 55);
INSERT INTO `zone` VALUES (85, '2020-11-26 12:29:44.569286', '2020-11-26 12:29:44.569300', 0, '河源 可用区A', 'cn-heyuan-a', 55);
INSERT INTO `zone` VALUES (86, '2020-11-26 12:29:44.569325', '2020-11-26 12:29:44.569339', 0, '河源 可用区A', 'cn-heyuan-a', 55);
INSERT INTO `zone` VALUES (87, '2020-11-26 12:29:44.569364', '2020-11-26 12:29:44.569377', 0, '广州 可用区A', 'cn-guangzhou-a', 56);
INSERT INTO `zone` VALUES (88, '2020-11-26 12:29:44.569403', '2020-11-26 12:29:44.569416', 0, '广州 可用区A', 'cn-guangzhou-a', 56);
INSERT INTO `zone` VALUES (89, '2020-11-26 12:29:44.569441', '2020-11-26 12:29:44.569455', 0, '广州 可用区B', 'cn-guangzhou-b', 56);
INSERT INTO `zone` VALUES (90, '2020-11-26 12:29:44.569483', '2020-11-26 12:29:44.569497', 0, '广州 可用区B', 'cn-guangzhou-b', 56);
INSERT INTO `zone` VALUES (91, '2020-11-26 12:29:44.569523', '2020-11-26 12:29:44.569536', 0, '成都 可用区 A', 'cn-chengdu-a', 57);
INSERT INTO `zone` VALUES (92, '2020-11-26 12:29:44.569562', '2020-11-26 12:29:44.569575', 0, '成都 可用区 A', 'cn-chengdu-a', 57);
INSERT INTO `zone` VALUES (93, '2020-11-26 12:29:44.569600', '2020-11-26 12:29:44.569614', 0, '成都 可用区 B', 'cn-chengdu-b', 57);
INSERT INTO `zone` VALUES (94, '2020-11-26 12:29:44.569639', '2020-11-26 12:29:44.569652', 0, '成都 可用区 B', 'cn-chengdu-b', 57);
INSERT INTO `zone` VALUES (95, '2020-11-26 12:29:44.569678', '2020-11-26 12:29:44.569691', 0, '香港可用区 B', 'cn-hongkong-b', 58);
INSERT INTO `zone` VALUES (96, '2020-11-26 12:29:44.569716', '2020-11-26 12:29:44.569730', 0, '香港可用区 B', 'cn-hongkong-b', 58);
INSERT INTO `zone` VALUES (97, '2020-11-26 12:29:44.569755', '2020-11-26 12:29:44.569768', 0, '香港可用区 C', 'cn-hongkong-c', 58);
INSERT INTO `zone` VALUES (98, '2020-11-26 12:29:44.569794', '2020-11-26 12:29:44.569810', 0, '香港可用区 C', 'cn-hongkong-c', 58);
INSERT INTO `zone` VALUES (99, '2020-11-26 12:29:44.569836', '2020-11-26 12:29:44.569849', 0, '香港可用区 A', 'cn-hongkong-a', 58);
INSERT INTO `zone` VALUES (100, '2020-11-26 12:29:44.569875', '2020-11-26 12:29:44.569888', 0, '香港可用区 A', 'cn-hongkong-a', 58);
INSERT INTO `zone` VALUES (101, '2020-11-26 12:29:44.569914', '2020-11-26 12:29:44.569927', 0, '香港可用区 D', 'cn-hongkong-d', 58);
INSERT INTO `zone` VALUES (102, '2020-11-26 12:29:44.569952', '2020-11-26 12:29:44.569966', 0, '香港可用区 D', 'cn-hongkong-d', 58);
INSERT INTO `zone` VALUES (103, '2020-11-26 12:29:44.569991', '2020-11-26 12:29:44.570005', 0, '亚太东北1 可用区B', 'ap-northeast-1b', 59);
INSERT INTO `zone` VALUES (104, '2020-11-26 12:29:44.570030', '2020-11-26 12:29:44.570043', 0, '亚太东北1 可用区B', 'ap-northeast-1b', 59);
INSERT INTO `zone` VALUES (105, '2020-11-26 12:29:44.570071', '2020-11-26 12:29:44.570085', 0, '亚太东北1 可用区A', 'ap-northeast-1a', 59);
INSERT INTO `zone` VALUES (106, '2020-11-26 12:29:44.570110', '2020-11-26 12:29:44.570124', 0, '亚太东北1 可用区A', 'ap-northeast-1a', 59);
INSERT INTO `zone` VALUES (107, '2020-11-26 12:29:44.570149', '2020-11-26 12:29:44.570163', 0, '亚太东南1 可用区C', 'ap-southeast-1c', 60);
INSERT INTO `zone` VALUES (108, '2020-11-26 12:29:44.570188', '2020-11-26 12:29:44.570202', 0, '亚太东南1 可用区C', 'ap-southeast-1c', 60);
INSERT INTO `zone` VALUES (109, '2020-11-26 12:29:44.570227', '2020-11-26 12:29:44.570240', 0, '亚太东南1 可用区B', 'ap-southeast-1b', 60);
INSERT INTO `zone` VALUES (110, '2020-11-26 12:29:44.570266', '2020-11-26 12:29:44.570279', 0, '亚太东南1 可用区B', 'ap-southeast-1b', 60);
INSERT INTO `zone` VALUES (111, '2020-11-26 12:29:44.570304', '2020-11-26 12:29:44.570318', 0, '亚太东南1 可用区A', 'ap-southeast-1a', 60);
INSERT INTO `zone` VALUES (112, '2020-11-26 12:29:44.570343', '2020-11-26 12:29:44.570357', 0, '亚太东南1 可用区A', 'ap-southeast-1a', 60);
INSERT INTO `zone` VALUES (113, '2020-11-26 12:29:44.570382', '2020-11-26 12:29:44.570396', 0, '亚太东南 2 可用区B', 'ap-southeast-2b', 61);
INSERT INTO `zone` VALUES (114, '2020-11-26 12:29:44.570421', '2020-11-26 12:29:44.570435', 0, '亚太东南 2 可用区B', 'ap-southeast-2b', 61);
INSERT INTO `zone` VALUES (115, '2020-11-26 12:29:44.570472', '2020-11-26 12:29:44.570487', 0, '亚太东南 2 可用区A', 'ap-southeast-2a', 61);
INSERT INTO `zone` VALUES (116, '2020-11-26 12:29:44.570512', '2020-11-26 12:29:44.570526', 0, '亚太东南 2 可用区A', 'ap-southeast-2a', 61);
INSERT INTO `zone` VALUES (117, '2020-11-26 12:29:44.570551', '2020-11-26 12:29:44.570564', 0, '亚太东南3 可用区A', 'ap-southeast-3a', 62);
INSERT INTO `zone` VALUES (118, '2020-11-26 12:29:44.570590', '2020-11-26 12:29:44.570604', 0, '亚太东南3 可用区A', 'ap-southeast-3a', 62);
INSERT INTO `zone` VALUES (119, '2020-11-26 12:29:44.570629', '2020-11-26 12:29:44.570642', 0, '亚太东南3 可用区B', 'ap-southeast-3b', 62);
INSERT INTO `zone` VALUES (120, '2020-11-26 12:29:44.570667', '2020-11-26 12:29:44.570681', 0, '亚太东南3 可用区B', 'ap-southeast-3b', 62);
INSERT INTO `zone` VALUES (121, '2020-11-26 12:29:44.570706', '2020-11-26 12:29:44.570720', 0, '亚太东南 5 可用区A', 'ap-southeast-5a', 63);
INSERT INTO `zone` VALUES (122, '2020-11-26 12:29:44.570745', '2020-11-26 12:29:44.570759', 0, '亚太东南 5 可用区A', 'ap-southeast-5a', 63);
INSERT INTO `zone` VALUES (123, '2020-11-26 12:29:44.570784', '2020-11-26 12:29:44.570798', 0, '亚太东南 5 可用区B', 'ap-southeast-5b', 63);
INSERT INTO `zone` VALUES (124, '2020-11-26 12:29:44.570823', '2020-11-26 12:29:44.570836', 0, '亚太东南 5 可用区B', 'ap-southeast-5b', 63);
INSERT INTO `zone` VALUES (125, '2020-11-26 12:29:44.570860', '2020-11-26 12:29:44.570874', 0, '亚太南部1 可用区B', 'ap-south-1b', 64);
INSERT INTO `zone` VALUES (126, '2020-11-26 12:29:44.570898', '2020-11-26 12:29:44.570912', 0, '亚太南部1 可用区B', 'ap-south-1b', 64);
INSERT INTO `zone` VALUES (127, '2020-11-26 12:29:44.570936', '2020-11-26 12:29:44.570950', 0, '亚太南部1 可用区A', 'ap-south-1a', 64);
INSERT INTO `zone` VALUES (128, '2020-11-26 12:29:44.570975', '2020-11-26 12:29:44.570989', 0, '亚太南部1 可用区A', 'ap-south-1a', 64);
INSERT INTO `zone` VALUES (129, '2020-11-26 12:29:44.571014', '2020-11-26 12:29:44.571027', 0, '美国东部1 可用区B', 'us-east-1b', 65);
INSERT INTO `zone` VALUES (130, '2020-11-26 12:29:44.571052', '2020-11-26 12:29:44.571065', 0, '美国东部1 可用区B', 'us-east-1b', 65);
INSERT INTO `zone` VALUES (131, '2020-11-26 12:29:44.571091', '2020-11-26 12:29:44.571104', 0, '美国东部1 可用区A', 'us-east-1a', 65);
INSERT INTO `zone` VALUES (132, '2020-11-26 12:29:44.571129', '2020-11-26 12:29:44.571142', 0, '美国东部1 可用区A', 'us-east-1a', 65);
INSERT INTO `zone` VALUES (133, '2020-11-26 12:29:44.571167', '2020-11-26 12:29:44.571180', 0, '美国西部1 可用区B', 'us-west-1b', 66);
INSERT INTO `zone` VALUES (134, '2020-11-26 12:29:44.571205', '2020-11-26 12:29:44.571219', 0, '美国西部1 可用区B', 'us-west-1b', 66);
INSERT INTO `zone` VALUES (135, '2020-11-26 12:29:44.571243', '2020-11-26 12:29:44.571257', 0, '美国西部1 可用区A', 'us-west-1a', 66);
INSERT INTO `zone` VALUES (136, '2020-11-26 12:29:44.571286', '2020-11-26 12:29:44.571300', 0, '美国西部1 可用区A', 'us-west-1a', 66);
INSERT INTO `zone` VALUES (137, '2020-11-26 12:29:44.571325', '2020-11-26 12:29:44.571338', 0, '伦敦 可用区B', 'eu-west-1b', 67);
INSERT INTO `zone` VALUES (138, '2020-11-26 12:29:44.571363', '2020-11-26 12:29:44.571376', 0, '伦敦 可用区B', 'eu-west-1b', 67);
INSERT INTO `zone` VALUES (139, '2020-11-26 12:29:44.571401', '2020-11-26 12:29:44.571415', 0, '伦敦 可用区A', 'eu-west-1a', 67);
INSERT INTO `zone` VALUES (140, '2020-11-26 12:29:44.571443', '2020-11-26 12:29:44.571459', 0, '伦敦 可用区A', 'eu-west-1a', 67);
INSERT INTO `zone` VALUES (141, '2020-11-26 12:29:44.571484', '2020-11-26 12:29:44.571498', 0, '中东东部1 可用区A', 'me-east-1a', 68);
INSERT INTO `zone` VALUES (142, '2020-11-26 12:29:44.571523', '2020-11-26 12:29:44.571536', 0, '中东东部1 可用区A', 'me-east-1a', 68);
INSERT INTO `zone` VALUES (143, '2020-11-26 12:29:44.571561', '2020-11-26 12:29:44.571575', 0, '欧洲中部1 可用区B', 'eu-central-1b', 69);
INSERT INTO `zone` VALUES (144, '2020-11-26 12:29:44.571600', '2020-11-26 12:29:44.571613', 0, '欧洲中部1 可用区B', 'eu-central-1b', 69);
INSERT INTO `zone` VALUES (145, '2020-11-26 12:29:44.571639', '2020-11-26 12:29:44.571652', 0, '欧洲中部1 可用区A', 'eu-central-1a', 69);
INSERT INTO `zone` VALUES (146, '2020-11-26 12:29:44.571677', '2020-11-26 12:29:44.571690', 0, '欧洲中部1 可用区A', 'eu-central-1a', 69);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
