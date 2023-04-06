-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 18, 2021 at 10:10 AM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `authorization_policy`
--
CREATE DATABASE IF NOT EXISTS `authorization_policy` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `authorization_policy`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=34 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add upload_product1', 7, 'add_upload_product1'),
(20, 'Can change upload_product1', 7, 'change_upload_product1'),
(21, 'Can delete upload_product1', 7, 'delete_upload_product1'),
(22, 'Can add employee_reg', 8, 'add_employee_reg'),
(23, 'Can change employee_reg', 8, 'change_employee_reg'),
(24, 'Can delete employee_reg', 8, 'delete_employee_reg'),
(25, 'Can add dkey_request1', 9, 'add_dkey_request1'),
(26, 'Can change dkey_request1', 9, 'change_dkey_request1'),
(27, 'Can delete dkey_request1', 9, 'delete_dkey_request1'),
(28, 'Can add payment1', 10, 'add_payment1'),
(29, 'Can change payment1', 10, 'change_payment1'),
(30, 'Can delete payment1', 10, 'delete_payment1'),
(31, 'Can add transportation1', 11, 'add_transportation1'),
(32, 'Can change transportation1', 11, 'change_transportation1'),
(33, 'Can delete transportation1', 11, 'delete_transportation1');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'employee', 'dkey_request1'),
(8, 'employee', 'employee_reg'),
(10, 'employee', 'payment1'),
(11, 'employee', 'transportation1'),
(7, 'managing_director', 'upload_product1'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-27 11:58:39.686179'),
(2, 'auth', '0001_initial', '2021-01-27 12:01:13.656986'),
(3, 'admin', '0001_initial', '2021-01-27 12:01:26.083696'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-27 12:01:26.194703'),
(5, 'contenttypes', '0002_remove_content_type_name', '2021-01-27 12:01:31.506007'),
(6, 'auth', '0002_alter_permission_name_max_length', '2021-01-27 12:01:36.577297'),
(7, 'auth', '0003_alter_user_email_max_length', '2021-01-27 12:01:41.976605'),
(8, 'auth', '0004_alter_user_username_opts', '2021-01-27 12:01:42.117614'),
(9, 'auth', '0005_alter_user_last_login_null', '2021-01-27 12:01:47.409916'),
(10, 'auth', '0006_require_contenttypes_0002', '2021-01-27 12:01:47.531923'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2021-01-27 12:01:47.637929'),
(12, 'auth', '0008_alter_user_username_max_length', '2021-01-27 12:01:55.066354'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2021-01-27 12:01:59.526609'),
(14, 'managing_director', '0001_initial', '2021-01-27 12:02:02.035753'),
(15, 'sessions', '0001_initial', '2021-01-27 12:02:08.649131'),
(16, 'employee', '0001_initial', '2021-01-27 12:16:58.226012'),
(17, 'employee', '0002_auto_20210213_1345', '2021-02-13 08:16:32.120147'),
(18, 'managing_director', '0002_auto_20210215_1346', '2021-02-15 08:16:38.284221'),
(19, 'managing_director', '0003_upload_product1_fcontent', '2021-02-16 05:17:15.980131'),
(20, 'managing_director', '0004_auto_20210216_1128', '2021-02-16 06:00:06.091398'),
(21, 'managing_director', '0005_upload_product1_enc_content', '2021-02-16 12:26:50.319607'),
(22, 'employee', '0003_employee_reg_group_password1', '2021-02-16 14:27:32.382939'),
(23, 'employee', '0004_dkey_request1', '2021-02-22 10:10:05.659891'),
(24, 'employee', '0005_payment1_transportation1', '2021-02-22 13:53:41.187326');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2qcftmtiokhu6sqlmgyuyce6ypmrb6z2', 'YmRmODgwYWNkM2MyODQxOTA5ODhkNjNmMDI5ZTliNWMxOGQ5OWNhYTp7ImVpZCI6NSwiZW5hbWUiOiJyYW15YSIsImVtcF9lbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJkZXNpZ25hdGlvbiI6InN1YmNvbnRyYWN0b3JzIn0=', '2021-03-04 13:47:22.848992'),
('e7wmh0tgyl0l9z6b227zkm647cymyg4g', 'MTk0NGVkMjhjNWMyMGZjODkzYmZiYWUzMWM2OWI4YTJmMTA1MmYyMzp7ImVpZCI6NSwiZW5hbWUiOiJyYW15YSIsImVtcF9lbWFpbCI6ImNoZW5uYWlzdW5kYXlyYW15YUBnbWFpbC5jb20iLCJkZXNpZ25hdGlvbiI6InN1YmNvbnRyYWN0b3JzIiwiZmlkMSI6M30=', '2021-03-08 13:54:17.607124');

-- --------------------------------------------------------

--
-- Table structure for table `employee_dkey_request1`
--

CREATE TABLE IF NOT EXISTS `employee_dkey_request1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empid` varchar(300) NOT NULL,
  `empname` varchar(300) NOT NULL,
  `empemail` varchar(300) NOT NULL,
  `emp_designation` varchar(300) NOT NULL,
  `fileid` varchar(300) NOT NULL,
  `stauts` varchar(300) NOT NULL,
  `dkey` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- Table structure for table `employee_employee_reg`
--

CREATE TABLE IF NOT EXISTS `employee_employee_reg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(300) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(300) NOT NULL,
  `designation` varchar(300) NOT NULL,
  `gender` varchar(300) NOT NULL,
  `lname` varchar(300) NOT NULL,
  `uname` varchar(300) NOT NULL,
  `group_password1` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

-- --------------------------------------------------------

--
-- Table structure for table `employee_payment1`
--

CREATE TABLE IF NOT EXISTS `employee_payment1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(300) NOT NULL,
  `payment` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Table structure for table `employee_transportation1`
--

CREATE TABLE IF NOT EXISTS `employee_transportation1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transport_no` varchar(300) NOT NULL,
  `project_name` varchar(300) NOT NULL,
  `send_place` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Table structure for table `managing_director_upload_product1`
--

CREATE TABLE IF NOT EXISTS `managing_director_upload_product1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(200) NOT NULL,
  `duration` varchar(300) NOT NULL,
  `designation` varchar(200) NOT NULL,
  `work_requirements` varchar(100) NOT NULL,
  `file_path` varchar(300) NOT NULL,
  `fcontent` longtext NOT NULL,
  `enc_content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
