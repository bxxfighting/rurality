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

 Date: 11/11/2020 14:15:31
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of project
-- ----------------------------
BEGIN;
INSERT INTO `project` VALUES (1, '2020-11-06 10:33:10.920210', '2020-11-11 02:19:14.989482', 0, '运维平台', '用于运维');
INSERT INTO `project` VALUES (2, '2020-11-07 10:17:08.967179', '2020-11-11 02:19:23.787115', 0, '权限系统', '用于权限管理');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

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
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4;

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

SET FOREIGN_KEY_CHECKS = 1;
