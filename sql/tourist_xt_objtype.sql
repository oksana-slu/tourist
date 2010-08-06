-- phpMyAdmin SQL Dump
-- version 2.11.9.5
-- http://www.phpmyadmin.net
--
-- Хост: 193.19.231.254
-- Время создания: Авг 06 2010 г., 12:29
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
-- Структура таблицы `xt_objtype`
--

DROP TABLE IF EXISTS `xt_objtype`;
CREATE TABLE IF NOT EXISTS `xt_objtype` (
  `otid` int(11) NOT NULL default '0',
  `otname` varchar(22) collate utf8_bin NOT NULL default '',
  `ot_table_name` varchar(20) collate utf8_bin NOT NULL,
  PRIMARY KEY  (`otid`),
  KEY `ot_table_name` (`ot_table_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Дамп данных таблицы `xt_objtype`
--

INSERT INTO `xt_objtype` (`otid`, `otname`, `ot_table_name`) VALUES
(1, 'article', 'xt_topic'),
(2, 'report', 'xt_topic'),
(3, 'link', 'xt_link'),
(4, 'forum', ''),
(5, 'news', 'xt_news');
