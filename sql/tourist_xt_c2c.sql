-- phpMyAdmin SQL Dump
-- version 2.11.9.5
-- http://www.phpmyadmin.net
--
-- Хост: 193.19.231.254
-- Время создания: Авг 03 2010 г., 19:25
-- Версия сервера: 5.0.91
-- Версия PHP: 5.2.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `tourist2`
--

-- --------------------------------------------------------

--
-- Структура таблицы `xt_c2c`
--

DROP TABLE IF EXISTS `xt_c2c`;
CREATE TABLE IF NOT EXISTS `xt_c2c` (
  `c2c_parent` int(11) NOT NULL default '0',
  `c2c_child` int(11) NOT NULL default '0',
  KEY `c2c_parent` (`c2c_parent`,`c2c_child`),
  KEY `c2c_child` (`c2c_child`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Дамп данных таблицы `xt_c2c`
--

INSERT INTO `xt_c2c` (`c2c_parent`, `c2c_child`) VALUES
(0, 2),
(0, 14),
(0, 16),
(0, 17),
(0, 18),
(0, 19),
(0, 22),
(0, 23),
(0, 29),
(0, 38),
(0, 44),
(0, 50),
(0, 51),
(0, 53),
(0, 54),
(0, 55),
(0, 59),
(0, 63),
(0, 70),
(0, 84),
(2, 69),
(2, 91),
(14, 27),
(14, 32),
(14, 35),
(14, 36),
(16, 30),
(16, 34),
(16, 83),
(17, 45),
(18, 26),
(18, 40),
(18, 43),
(18, 49),
(19, 20),
(19, 21),
(19, 24),
(19, 25),
(19, 58),
(19, 77),
(19, 78),
(19, 79),
(19, 80),
(19, 90),
(20, 73),
(26, 31),
(26, 39),
(26, 41),
(26, 82),
(29, 89),
(38, 67),
(38, 68),
(38, 87),
(50, 65),
(50, 66),
(50, 86),
(51, 52),
(51, 57),
(51, 88),
(53, 1),
(53, 47),
(53, 48),
(53, 75),
(54, 4),
(54, 5),
(54, 7),
(54, 76),
(55, 37),
(55, 42),
(55, 56),
(59, 60),
(59, 61),
(59, 62),
(63, 3),
(63, 64),
(70, 71),
(70, 72),
(77, 74),
(84, 81),
(84, 85);
