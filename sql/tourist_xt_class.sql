-- phpMyAdmin SQL Dump
-- version 2.11.9.5
-- http://www.phpmyadmin.net
--
-- Хост: 193.19.231.254
-- Время создания: Авг 03 2010 г., 19:22
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
-- Структура таблицы `xt_class`
--

DROP TABLE IF EXISTS `xt_class`;
CREATE TABLE IF NOT EXISTS `xt_class` (
  `nid` int(11) NOT NULL auto_increment,
  `vname` varchar(88) collate utf8_bin NOT NULL,
  `vcode` varchar(88) collate utf8_bin NOT NULL,
  `xtcdescription` varchar(80) collate utf8_bin NOT NULL default '',
  `nclasstype` int(11) NOT NULL default '0',
  `nshablon` int(11) NOT NULL default '0',
  `xtcconst` varchar(30) collate utf8_bin NOT NULL default '',
  `class_order` int(3) NOT NULL default '0',
  PRIMARY KEY  (`nid`),
  KEY `vcode` (`vcode`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=92 ;

--
-- Дамп данных таблицы `xt_class`
--

INSERT INTO `xt_class` (`nid`, `vname`, `vcode`, `xtcdescription`, `nclasstype`, `nshablon`, `xtcconst`, `class_order`) VALUES
(1, 'ВЕЛОСИПЕДЫ', 'velo', 'Велосипеды байки велопоходы велоспорт', 1, 1, 'velo_topics_const.html', 3),
(2, 'Активный отдых', 'active', 'Активное время препровождение', 1, 0, '', 0),
(3, 'Авто-мото', 'automoto', 'Все у чего есть ДВС', 1, 0, '', 0),
(4, 'Архитектура', 'castles', 'Архитектурные памятники и сооружения', 1, 0, '', 5),
(5, 'История', 'history', 'Городища и другие места, связанные с историей', 1, 0, '', 4),
(59, 'Экстрим', 'extremes', 'Экстремальные виды', 1, 0, '', 0),
(7, 'Живописные места', 'niceplaces', 'Живописные места и замечательные маршруты', 1, 0, '', 2),
(8, 'Общей сложности', 'forall', 'Общей сложности доступно для всех', 3, 0, '', 0),
(9, 'Украина', 'ukr', 'Украина - р_дна ненька', 2, 0, '', 0),
(11, 'Для матрасников', 'matras', 'Попсовые почти походы', 3, 0, '', 0),
(12, 'Походы 1-2', 'poh12', 'Походы на 2-5 дней без благ цивилизации', 3, 0, '', 0),
(17, 'Америка', 'america', 'Континент Америка и все что близко', 2, 0, '', 0),
(14, 'Европа', 'europe', 'Европа', 2, 0, '', 0),
(16, 'Азия', 'asia', 'Азия как часть света и все что близко', 2, 0, '', 0),
(18, 'СНГ', 'sng', 'Страны СНГ кроме Украины', 2, 0, '', 0),
(19, 'Украина', 'ukraine', 'Украина', 2, 0, '', 0),
(20, 'Харьков', 'kharkov', 'Харьковская область', 2, 0, '', 33),
(21, 'Киев', 'kiev', 'Киевская область', 2, 0, '', 0),
(22, 'Спортивные отчеты', 'sportrep', 'Категорийные выше третьей', 3, 0, '', 0),
(23, 'Матрасные отчеты', 'matrac', 'Совсем матрасные бухаловки', 3, 0, '', 0),
(24, 'Крым', 'crimea', 'Благодатный Крым', 2, 0, '', 22),
(25, 'Карпаты', 'carpathian', 'Карпаты в широком смысле', 2, 0, '', 0),
(26, 'Россия', 'russia', 'Россия', 2, 0, '', 0),
(27, 'Венгрия', 'hungary', 'Угорщина', 2, 0, '', 0),
(29, 'Африка', 'africa', 'Африка', 2, 0, '', 0),
(30, 'Турция', 'turkey', 'турция', 2, 0, '', 0),
(31, 'Карелия', 'karel', 'Карелия', 2, 0, '', 0),
(32, 'Польша', 'poland', 'Польша', 2, 0, '', 0),
(34, 'Камбоджа', 'cambodja', 'Камбоджа', 2, 0, '', 0),
(35, 'Германия', 'gemany', 'германия', 2, 0, '', 0),
(36, 'Австрия', 'austria', 'австрия', 2, 0, '', 0),
(37, 'Спелео', 'speleo', 'Пещеры', 1, 0, '', 0),
(38, 'Вода', 'water', 'Байдарки, паруса, акваланги, и пр.', 1, 0, '', 0),
(39, 'Алтай', 'altay', 'алтай', 2, 0, '', 0),
(40, 'Грузия', 'georgia', 'грузия', 2, 0, '', 0),
(41, 'Урал', 'ural', 'Урал', 2, 0, '', 0),
(42, 'Диггерство', 'diggers', 'Диггерство и сталкер', 1, 0, '', 0),
(43, 'Прибалтика', 'baltic', 'Прибалтика', 2, 0, '', 0),
(44, 'Обычные походы', 'normaltr', 'Обычные походы 0-2 сложностей', 3, 0, '', 0),
(45, 'Куба', 'kuba', 'Вива Куба!', 2, 0, '', 0),
(49, 'Кавказ', 'caucasus', 'Российская часть Кавказа', 2, 0, '', 0),
(47, 'Пеший туризм', 'foot', 'Пешие походы', 1, 0, '', 2),
(48, 'Мультиспорт', 'multisport', 'Приключенческие гонки (экстрим-марафоны)', 1, 0, '', 0),
(50, 'Зима', 'winter', 'Лыжные походы, горные лыжи, сноуборд...', 1, 0, '', 0),
(51, 'Горы', 'mount', 'Горы', 1, 0, '', 0),
(52, 'Альпинизм', 'alpinism', 'восхождения на труднодоступные вершины', 1, 0, '', 0),
(53, 'Земля', 'ground', 'Мать сыра земля', 1, 0, '', 5),
(54, 'Краеведение', 'etnografia', 'Достопримечательности Харькова', 1, 0, '', 5),
(55, 'Под землей', 'underground', 'Под землей', 1, 0, '', 4),
(56, 'МД', 'md', 'Металлодетекторы', 1, 0, '', 0),
(57, 'Горный туризм', 'footmount', 'Пешком до 3000', 1, 0, '', 0),
(58, 'Азов', 'azov', 'Азовское море и побережье', 2, 0, '', 31),
(60, 'Ролики, Скейты', 'roll', 'Ролики, скейтбоард', 1, 0, '', 0),
(61, 'Паркур', 'parkour', 'Паркур', 1, 0, '', 0),
(62, 'Дёрт и Триал', 'veloaxtremes', 'Дертджампинг и велотриал', 1, 0, '', 0),
(63, 'Мужской отдых', 'mans', 'Мужской отдых', 1, 0, '', 0),
(64, 'Рыбалка', 'fishing', 'Рыбалка', 1, 0, '', 0),
(65, 'Лыжи', 'ski', 'Лыжный туризм и беговые лыжи', 1, 0, '', 0),
(66, 'Горные лыжи', 'mski', 'Горные лыжи и сноуборды', 1, 0, '', 0),
(67, 'Байдарки', 'kayak', 'Байдарки и каяки', 1, 0, '', 0),
(68, 'Дайвинг', 'diving', 'Дайвинг', 1, 0, '', 0),
(69, 'Квесты', 'quests', 'квесты', 1, 0, '', 0),
(70, 'Небо', 'sky', 'Небо', 1, 0, '', 0),
(71, 'Парапланы', 'paraplan', 'Парапланы', 1, 0, '', 0),
(72, 'Парашюты', 'parashut', 'Парашюты', 1, 0, '', 0),
(73, 'Чугуев', 'chuguev', 'Чугуев', 2, 0, '', 0),
(74, 'Сорочинцы', 'sorochinci', 'Сорочинцы', 2, 0, '', 0),
(75, 'Лошади', 'horses', 'Верховая езда', 1, 0, '', 0),
(76, 'Флора', 'flora', 'Растения в походе', 1, 0, '', 0),
(77, 'Полтава', 'poltava', 'Полтава', 2, 0, '', 0),
(78, 'Запорожье', 'zaporogie', 'Запорожье', 2, 0, '', 0),
(79, 'Ивано-франковск', 'ivanofrankovsk', 'Ивано-франковск', 2, 0, '', 0),
(80, 'Ужгород', 'uzhgorod', 'Ужгород', 2, 0, '', 0),
(81, 'Путешествия', 'travels', 'Путешествия и путешественники', 1, 0, '', 1),
(82, 'Дальний Восток', 'fareast', 'Дальний восток', 2, 0, '', 0),
(83, 'Израиль', 'israel', 'Израиль', 2, 0, '', 0),
(84, 'Другое', 'others', 'Разное', 1, 0, '', -1),
(85, 'Туры', 'tours', 'Туры, путевки', 1, 0, '', 0),
(86, 'Сноуборд', 'snowbord', 'Сноуборд', 1, 0, '', -1),
(87, 'Виндсерфинг', 'windserfing', 'Виндсерфинг', 1, 0, '', -1),
(88, 'Скалолазание', 'climbing', 'Скалолазание', 1, 0, '', 0),
(89, 'Египет', 'egypt', 'Египет', 2, 0, '', 0),
(90, 'Одесса', 'odessa', 'Одесса', 2, 0, '', 0),
(91, 'Пейнтбол', 'paintball', 'Пейнтбол в Харькове', 1, 0, '', 0);
