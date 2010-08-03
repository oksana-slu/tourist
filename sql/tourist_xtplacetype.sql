-- phpMyAdmin SQL Dump
-- version 2.11.9.5
-- http://www.phpmyadmin.net
--
-- Хост: 193.19.231.254
-- Время создания: Авг 03 2010 г., 19:19
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
-- Структура таблицы `xtplacetype`
--

DROP TABLE IF EXISTS `xtplacetype`;
CREATE TABLE IF NOT EXISTS `xtplacetype` (
  `id` tinyint(4) default NULL,
  `vname` char(36) character set utf8 collate utf8_bin default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `xtplacetype`
--

INSERT INTO `xtplacetype` (`id`, `vname`) VALUES
(7, 'государство'),
(34, 'группа государств'),
(10, 'континент'),
(8, 'область'),
(6, 'город'),
(37, 'блок'),
(12, 'столица'),
(47, 'республика'),
(31, 'край'),
(30, 'штат'),
(32, 'округ'),
(11, 'субконтинент'),
(17, 'пгт'),
(56, 'поселок'),
(19, 'село'),
(41, 'бульвар'),
(40, 'проспект'),
(61, 'проезд'),
(59, 'станция'),
(14, 'район'),
(67, 'масив'),
(20, 'хутор'),
(127, 'урочище'),
(127, 'парк'),
(127, 'санаторий'),
(127, 'проселок'),
(42, 'шоcсе'),
(50, 'квартал'),
(127, 'спуск');
