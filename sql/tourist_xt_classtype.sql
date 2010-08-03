-- phpMyAdmin SQL Dump
-- version 2.11.9.5
-- http://www.phpmyadmin.net
--
-- Хост: 193.19.231.254
-- Время создания: Авг 03 2010 г., 19:23
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
-- Структура таблицы `xt_classtype`
--

DROP TABLE IF EXISTS `xt_classtype`;
CREATE TABLE IF NOT EXISTS `xt_classtype` (
  `id` int(11) NOT NULL default '0',
  `nme` varchar(22) collate utf8_bin NOT NULL default '',
  `xtct_desc` varchar(100) collate utf8_bin default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Дамп данных таблицы `xt_classtype`
--

INSERT INTO `xt_classtype` (`id`, `nme`, `xtct_desc`) VALUES
(1, 'napr', '&#1053;&#1072;&#1087;&#1088;&#1072;&#1074;&#1083;&#1077;&#1085;&#1080;&#1077;'),
(2, 'geogr', '&#1043;&#1077;&#1086;&#1075;&#1088;&#1072;&#1092;&#1080;&#1103;'),
(3, 'hrdly', '&#1057;&#1083;&#1086;&#1078;&#1085;&#1086;&#1089;&#1090;&#1100;');
