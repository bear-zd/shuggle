/*
 Navicat Premium Data Transfer

 Source Server         : chin_local
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : citylife

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 07/06/2021 09:31:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `article_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_title` varchar(100) NOT NULL,
  `article_summary` varchar(3000) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `article_read_cnt` int(11) NOT NULL DEFAULT '0',
  `article_pl` int(11) NOT NULL DEFAULT '0',
  `article_sc` int(11) NOT NULL DEFAULT '0',
  `article_date` varchar(255) DEFAULT NULL,
  `article_url` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '/static/upload/top_img/none.png',
  `article_type` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for article_sc
-- ----------------------------
DROP TABLE IF EXISTS `article_sc`;
CREATE TABLE `article_sc` (
  `sc_id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL DEFAULT '0',
  `user_id` int(11) NOT NULL DEFAULT '0',
  `sc_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`sc_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_text` text,
  `comment_date` datetime DEFAULT NULL,
  `article_id` varchar(20) NOT NULL,
  `comment_name` varchar(30) DEFAULT NULL,
  `comment_support` int(11) DEFAULT '0',
  `comment_oppose` int(11) DEFAULT '0',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for count
-- ----------------------------
DROP TABLE IF EXISTS `count`;
CREATE TABLE `count` (
  `dbname` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dbvalue` int(11) DEFAULT '1',
  PRIMARY KEY (`dbname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for follow
-- ----------------------------
DROP TABLE IF EXISTS `follow`;
CREATE TABLE `follow` (
  `follow_id` int(11) NOT NULL AUTO_INCREMENT,
  `send_id` int(11) NOT NULL DEFAULT '0',
  `receive_id` int(11) NOT NULL DEFAULT '0',
  `foolow_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`follow_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for login_log
-- ----------------------------
DROP TABLE IF EXISTS `login_log`;
CREATE TABLE `login_log` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `login_ip` varchar(255) DEFAULT NULL,
  `login_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `mess_id` int(11) NOT NULL AUTO_INCREMENT,
  `send_type` int(11) DEFAULT '0',
  `send_id` int(11) NOT NULL DEFAULT '0',
  `receive_id` int(11) NOT NULL DEFAULT '0',
  `send_time` varchar(255) NOT NULL,
  `mess_content` varchar(255) DEFAULT NULL,
  `read_state` int(11) NOT NULL DEFAULT '1' COMMENT '1?????????0?????????-1??????',
  PRIMARY KEY (`mess_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(255) DEFAULT NULL,
  `tx_link` varchar(15000) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '/static/tx_upload/tx.png' COMMENT '??????',
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '??????',
  `birthday` varchar(255) DEFAULT NULL COMMENT '????????????',
  `now_address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '?????????',
  `home_address` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '??????',
  `qq` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'QQ',
  `wechat` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '??????',
  `weibo` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '??????',
  `readme` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '????????????',
  `money` double(255,0) DEFAULT NULL COMMENT '??????',
  `register_date` varchar(255) DEFAULT NULL COMMENT '????????????',
  `following_cnt` int(11) NOT NULL DEFAULT '0' COMMENT '????????????',
  `follower_cnt` int(11) NOT NULL DEFAULT '0' COMMENT '????????????',
  `mess_cnt` int(11) NOT NULL DEFAULT '0' COMMENT '?????????',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for user_login
-- ----------------------------
DROP TABLE IF EXISTS `user_login`;
CREATE TABLE `user_login` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '??????( ???????????????',
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '?????? ??????',
  `phone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '?????? ??????',
  `password_hash` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '??????',
  `is_admin` int(2) NOT NULL DEFAULT '0' COMMENT '???????????????,0???1???',
  `is_enable` int(2) NOT NULL DEFAULT '0' COMMENT '????????????,????????????',
  `lastlogin` varchar(255) NOT NULL COMMENT '??????????????????',
  `pay_password_hash` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '????????????',
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for verify
-- ----------------------------
DROP TABLE IF EXISTS `verify`;
CREATE TABLE `verify` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `yzm` varchar(255) DEFAULT NULL,
  `sendtime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Triggers structure for table user_login
-- ----------------------------
DROP TRIGGER IF EXISTS `update_count`;
delimiter ;;
CREATE TRIGGER `update_count` AFTER INSERT ON `user_login` FOR EACH ROW begin -- ?????????????????????
	-- ?????????????????????????????????????????????
	UPDATE count SET dbvalue=dbvalue+1 WHERE dbname='user';
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user_login
-- ----------------------------
DROP TRIGGER IF EXISTS `update_count2`;
delimiter ;;
CREATE TRIGGER `update_count2` AFTER DELETE ON `user_login` FOR EACH ROW begin -- ?????????????????????
	-- ?????????????????????????????????????????????
	UPDATE count SET dbvalue=dbvalue-1 WHERE dbname='user';
end
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user_login
-- ----------------------------
DROP TRIGGER IF EXISTS `after_insert`;
delimiter ;;
CREATE TRIGGER `after_insert` AFTER INSERT ON `user_login` FOR EACH ROW begin -- ?????????????????????
	-- ?????????????????????????????????????????????
	insert into user(uid,account,register_date) values(new.uid,new.account,new.lastlogin);
end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
