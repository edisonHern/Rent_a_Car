-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 10-12-2024 a las 19:48:01
-- Versión del servidor: 8.0.17
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rentacardb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(4, 'Administrador'),
(5, 'Trabajador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(157, 4, 1),
(158, 4, 2),
(159, 4, 3),
(160, 4, 4),
(161, 4, 5),
(162, 4, 6),
(163, 4, 7),
(164, 4, 8),
(165, 4, 9),
(166, 4, 10),
(167, 4, 11),
(168, 4, 12),
(169, 4, 13),
(170, 4, 14),
(171, 4, 15),
(172, 4, 16),
(173, 4, 17),
(174, 4, 18),
(175, 4, 19),
(176, 4, 20),
(177, 4, 21),
(178, 4, 22),
(179, 4, 23),
(180, 4, 24),
(181, 4, 25),
(182, 4, 26),
(183, 4, 27),
(184, 4, 28),
(185, 4, 29),
(186, 4, 30),
(187, 4, 31),
(188, 4, 32),
(189, 4, 33),
(190, 4, 34),
(191, 4, 35),
(192, 4, 36),
(193, 4, 37),
(194, 4, 38),
(195, 4, 39),
(196, 4, 40),
(197, 4, 41),
(198, 4, 42),
(199, 4, 43),
(200, 4, 44),
(201, 4, 45),
(202, 4, 46),
(203, 4, 47),
(204, 4, 48),
(205, 4, 49),
(206, 4, 50),
(207, 4, 51),
(208, 4, 52),
(237, 5, 1),
(238, 5, 2),
(239, 5, 3),
(240, 5, 4),
(242, 5, 5),
(243, 5, 6),
(244, 5, 7),
(241, 5, 8),
(245, 5, 9),
(246, 5, 10),
(247, 5, 11),
(248, 5, 12),
(209, 5, 13),
(210, 5, 14),
(211, 5, 15),
(212, 5, 16),
(213, 5, 17),
(214, 5, 18),
(215, 5, 19),
(216, 5, 20),
(249, 5, 21),
(250, 5, 22),
(251, 5, 23),
(217, 5, 24),
(218, 5, 25),
(219, 5, 26),
(220, 5, 27),
(221, 5, 28),
(222, 5, 29),
(223, 5, 30),
(224, 5, 31),
(225, 5, 32),
(226, 5, 33),
(227, 5, 34),
(228, 5, 35),
(229, 5, 36),
(230, 5, 37),
(231, 5, 38),
(232, 5, 39),
(233, 5, 40),
(234, 5, 44),
(235, 5, 48),
(236, 5, 52);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add auto', 6, 'add_auto'),
(22, 'Can change auto', 6, 'change_auto'),
(23, 'Can delete auto', 6, 'delete_auto'),
(24, 'Can view auto', 6, 'view_auto'),
(25, 'Can add Usuario', 7, 'add_customuser'),
(26, 'Can change Usuario', 7, 'change_customuser'),
(27, 'Can delete Usuario', 7, 'delete_customuser'),
(28, 'Can view Usuario', 7, 'view_customuser'),
(29, 'Can add cliente', 8, 'add_cliente'),
(30, 'Can change cliente', 8, 'change_cliente'),
(31, 'Can delete cliente', 8, 'delete_cliente'),
(32, 'Can view cliente', 8, 'view_cliente'),
(33, 'Can add reserva', 9, 'add_reserva'),
(34, 'Can change reserva', 9, 'change_reserva'),
(35, 'Can delete reserva', 9, 'delete_reserva'),
(36, 'Can view reserva', 9, 'view_reserva'),
(37, 'Can add factura', 10, 'add_factura'),
(38, 'Can change factura', 10, 'change_factura'),
(39, 'Can delete factura', 10, 'delete_factura'),
(40, 'Can view factura', 10, 'view_factura'),
(41, 'Can add nosotros', 11, 'add_nosotros'),
(42, 'Can change nosotros', 11, 'change_nosotros'),
(43, 'Can delete nosotros', 11, 'delete_nosotros'),
(44, 'Can view nosotros', 11, 'view_nosotros'),
(45, 'Can add politica', 12, 'add_politica'),
(46, 'Can change politica', 12, 'change_politica'),
(47, 'Can delete politica', 12, 'delete_politica'),
(48, 'Can view politica', 12, 'view_politica'),
(49, 'Can add trabajador', 13, 'add_trabajador'),
(50, 'Can change trabajador', 13, 'change_trabajador'),
(51, 'Can delete trabajador', 13, 'delete_trabajador'),
(52, 'Can view trabajador', 13, 'view_trabajador'),
(53, 'Can add seguro basico', 14, 'add_segurobasico'),
(54, 'Can change seguro basico', 14, 'change_segurobasico'),
(55, 'Can delete seguro basico', 14, 'delete_segurobasico'),
(56, 'Can view seguro basico', 14, 'view_segurobasico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_auto`
--

CREATE TABLE `core_auto` (
  `id` bigint(20) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `año` int(10) UNSIGNED NOT NULL,
  `patente` varchar(10) NOT NULL,
  `color` varchar(50) DEFAULT NULL,
  `puertas` int(10) UNSIGNED NOT NULL,
  `precio_dia` int(10) UNSIGNED NOT NULL,
  `kilometraje` int(10) UNSIGNED NOT NULL,
  `estado_auto` varchar(20) NOT NULL,
  `combustible` varchar(50) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `core_auto`
--

INSERT INTO `core_auto` (`id`, `marca`, `modelo`, `año`, `patente`, `color`, `puertas`, `precio_dia`, `kilometraje`, `estado_auto`, `combustible`, `imagen`) VALUES
(3, 'Kia', 'Iberia', 2017, 'LGTH32', 'Verde Musgo', 4, 38000, 65300, 'disponible', 'diesel', 'autos_imagenes/Kia-Iberia.png'),
(4, 'Kia', 'e-Soul', 2018, 'KJTY76', 'Rojo', 2, 34000, 65000, 'disponible', 'electrico', 'autos_imagenes/Kia-eSoul.png'),
(5, 'Kia', 'Niro', 2018, 'HTFG64', 'Azul Petroleo', 4, 41000, 65300, 'disponible', 'gasolina', 'autos_imagenes/kia_niro.png'),
(6, 'Kia', 'Sorento', 2023, 'FFRT66', 'Negro', 4, 39000, 56300, 'reservado', 'gasolina', 'autos_imagenes/Kia-Sorento.png'),
(7, 'Kia', 'EV6', 2019, 'DFTY56', 'Gris', 4, 37000, 47600, 'mantenimiento', 'electrico', 'autos_imagenes/KIA-EV6.png'),
(13, 'Fiat', 'Avanti-500', 2020, 'GR6539', 'Azul grafito', 3, 35000, 38500, 'reservado', 'electrico', 'autos_imagenes/Fiat-500-avanti.png'),
(17, 'Fiat', 'Matehuala', 2019, 'RF2768', 'Rojo', 4, 35000, 45600, 'reservado', 'gasolina', 'autos_imagenes/fiat-matehuala.png'),
(18, 'Fiat', 'Cronos', 2021, 'LI9633', 'Gris', 4, 40000, 38900, 'mantenimiento', 'gasolina', 'autos_imagenes/cronos.png'),
(19, 'Fiat', 'Fastback', 2021, 'PK2903', 'Gris perla', 4, 50000, 38400, 'disponible', 'gasolina', 'autos_imagenes/fiat-fastbackgris.png'),
(20, 'Fiat', 'Fiorino', 2022, 'ST6389', 'Amarillo', 3, 35000, 48000, 'mantenimiento', 'gasolina', 'autos_imagenes/1fiat-fiorino-2.png'),
(21, 'Fiat', 'Pulse', 2018, 'MN5834', 'Gris', 4, 50000, 43900, 'disponible', 'gasolina', 'autos_imagenes/fiat-pulse.png'),
(22, 'Fiat', 'Strada', 2021, 'KL6435', 'Blanco', 4, 38000, 41400, 'mantenimiento', 'gasolina', 'autos_imagenes/fiat-strada.png'),
(24, 'Toyota', 'Corolla', 2022, 'PLIK35', 'Plata', 4, 40000, 54900, 'mantenimiento', 'gasolina', 'autos_imagenes/toyota-corolla-plata.png'),
(25, 'Toyota', 'Tabasco', 2019, 'PJTG70', 'Negro', 4, 43000, 43900, 'disponible', 'diesel', 'autos_imagenes/toyota-tabasco.png'),
(26, 'Toyota', 'Yaris', 2020, 'LKBU56', 'R', 4, 36000, 54000, 'disponible', 'gasolina', 'autos_imagenes/toyota-yaris.png'),
(27, 'Toyota', 'Camry', 2019, 'OKYU38', 'Verde Tiza', 4, 36000, 61400, 'disponible', 'gasolina', 'autos_imagenes/oyota-camry.png'),
(28, 'Toyota', 'Prius', 2020, 'JHUO56', 'Azul', 4, 34000, 55000, 'disponible', 'electrico', 'autos_imagenes/toyota-prius.png'),
(29, 'Toyota', 'Hilux', 2018, 'KYOD03', 'Blanco', 4, 41000, 69000, 'disponible', 'diesel', 'autos_imagenes/toyota-hilux.png'),
(30, 'Toyota', 'Fortune', 2019, 'YGTR32', 'Gris', 4, 42000, 61000, 'disponible', 'diesel', 'autos_imagenes/toyota-fortune.png'),
(31, 'Toyota', 'Laguna', 2019, 'PDRT47', 'Negro', 4, 37000, 57000, 'disponible', 'electrico', 'autos_imagenes/toyota-laguna.png'),
(32, 'Toyota', 'Pachuca', 2024, 'LJUH67', 'Blanco', 4, 37000, 18000, 'disponible', 'electrico', 'autos_imagenes/toyota_pachuca-blanco-perlado.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_cliente`
--

CREATE TABLE `core_cliente` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `fecha_nac` date DEFAULT NULL,
  `ciudad` varchar(50) NOT NULL,
  `licencia_conducir` varchar(20) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `estado_cliente` varchar(12) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `region` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `core_cliente`
--

INSERT INTO `core_cliente` (`id`, `nombre`, `apellido`, `rut`, `fecha_nac`, `ciudad`, `licencia_conducir`, `telefono`, `email`, `direccion`, `estado_cliente`, `imagen`, `user_id`, `region`) VALUES
(22, 'Lucas', 'Vasquez', '156756780', NULL, 'Valdivia', 'A-GTY65-TYH', '956764567', 'pollo@gmail.com', 'Los almendros 1232', 'inactivo', '', NULL, 'XIV'),
(23, 'Pedro', 'Diego', '145678900', '2000-01-01', 'Chileno', 'A-GHY67-Y7U', '956434567', 'pedrovaca@gmil.com', 'correo', 'con_reserva', '', 29, 'Región de Valparaiso'),
(24, 'Pablo', 'Escobar', '63456785', '2000-01-01', 'Chileno', 'A-GTY67-FR5', '956786756', 'pabloe@gmail.com', 'tortolos 45', 'inactivo', '', 30, 'Región de Valparaiso'),
(25, 'Jorge', 'Paco', '56784561', '1997-01-01', 'Chileno', 'A-GTY67-YU7', '956452345', 'paco@gmail.com', 'pacogento', 'inactivo', '', 31, 'Región de Valparaiso'),
(34, 'tigre', 'sanchez', '45677890', '2000-01-01', 'asdasd', 'a-jkilo-lop', '678787878', 'dfsfs@gmail.com', 'sfdsfs', 'inactivo', '', 33, 'Región de Valparaiso'),
(35, 'Pedro Juan', 'Prat', '156785670', '2000-03-20', 'Chileno', 'A-GTY67-TYU', '956785678', 'pedro67@gmail.com', 'carmen 56', 'rentando', '', 34, 'Región de Valparaiso'),
(36, 'Felipe', 'Castillo', '193299490', '1997-03-21', 'Viña del mar', 'B-GTY67-T67', '956565656', 'felipecast@gmail.com', 'galvarino 10', 'inactivo', '', NULL, 'V');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_cliente_historial_alquileres`
--

CREATE TABLE `core_cliente_historial_alquileres` (
  `id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `reserva_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_factura`
--

CREATE TABLE `core_factura` (
  `id` bigint(20) NOT NULL,
  `codigo_factura` varchar(10) NOT NULL,
  `total` int(10) UNSIGNED NOT NULL,
  `fecha_emision` date NOT NULL,
  `metodo_pago` varchar(50) NOT NULL,
  `cliente_id` bigint(20) NOT NULL,
  `reserva_id` bigint(20) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_nosotros`
--

CREATE TABLE `core_nosotros` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `contenido` longtext NOT NULL,
  `mision` longtext NOT NULL,
  `vision` longtext NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_politica`
--

CREATE TABLE `core_politica` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `core_politica`
--

INSERT INTO `core_politica` (`id`, `titulo`, `descripcion`, `fecha_creacion`) VALUES
(3, 'Política de Cancelación de Reservas', 'La plataforma permite a los clientes cancelar sus reservas con la opción de obtener un reembolso, dependiendo de la anticipación con la que se realice la cancelación. Esto busca garantizar tanto la flexibilidad para los usuarios como la estabilidad económica para el negocio.\r\nDetalles:\r\n1.	Reembolso Completo:\r\nSi el cliente realiza la cancelación al menos 24 horas antes del inicio de la reserva, se procesará un reembolso completo del monto pagado.\r\n2.	Reembolso Parcial:\r\nSi la cancelación ocurre con menos de 24 horas de anticipación, se reembolsará solo el 50% del costo total de la reserva.\r\n3.	Sin Reembolso:\r\nSi la cancelación ocurre después del inicio del período de reserva, no se otorgará ningún reembolso.', '2024-12-06 15:05:29.201007'),
(4, 'Política de Daños al Vehículo', 'Los clientes serán responsables de cualquier daño ocasionado al vehículo durante el período de alquiler. Esta responsabilidad incluye cualquier daño físico o mecánico no cubierto por un seguro opcional contratado al momento de la reserva.\r\nDetalles:\r\n1.	Reporte de Daños:\r\nAl devolver el vehículo, cualquier daño debe ser reportado inmediatamente al personal de la plataforma.\r\n2.	Evaluación del Daño:\r\nEl costo del daño será evaluado por un especialista certificado y facturado al cliente.\r\n3.	Seguro Opcional:\r\nLos clientes que hayan contratado un seguro durante el proceso de reserva podrán usarlo para cubrir total o parcialmente los costos, según las condiciones del seguro.', '2024-12-08 16:15:59.288007'),
(5, 'Política de Retrasos en la Devolución', 'Los vehículos alquilados deben ser devueltos en el horario previamente acordado. Los retrasos en la devolución están sujetos a cargos adicionales como compensación por la posible afectación al próximo cliente.\r\nDetalles:\r\n1.	Cargo por Retraso:\r\nSe aplicará un cargo equivalente al 10% del costo diario de alquiler por cada hora de retraso.\r\n2.	Día Adicional:\r\nSi el retraso supera las 6 horas, se considerará como un día adicional de alquiler y se cobrará como tal.\r\n3.	Comunicación:\r\nSe recomienda que los clientes informen con antelación si prevén un retraso, para evaluar posibles soluciones.', '2024-12-08 16:16:18.133383'),
(6, 'Política de Combustible', 'El vehículo alquilado debe devolverse con el mismo nivel de combustible con el que fue entregado al cliente. Esto asegura que no se generen costos inesperados ni inconvenientes operativos para el negocio.\r\nDetalles:\r\n1.	Nivel de Combustible Inicial:\r\nEl nivel de combustible será registrado al momento de entregar el vehículo.\r\n2.	Cobro Adicional:\r\nSi el cliente devuelve el vehículo con menos combustible del registrado, se aplicará un cargo equivalente al costo del combustible faltante, según la tarifa vigente en ese momento.\r\n3.	Excedente de Combustible:\r\nSi el cliente devuelve el vehículo con más combustible del registrado inicialmente, no se hará ninguna compensación adicional.', '2024-12-08 16:16:35.634448'),
(7, 'Política de Edad y Licencia', 'Para alquilar un vehículo, los clientes deben cumplir con ciertos requisitos relacionados con la edad y la experiencia como conductores, asegurando así la seguridad del negocio y el cumplimiento de las regulaciones legales aplicables.\r\nDetalles:\r\n1.	Edad Mínima:\r\nLa edad mínima para alquilar un vehículo es de 21 años.\r\n2.	Tarifa para Conductores Jóvenes:\r\nLos conductores menores de 25 años estarán sujetos a un cargo adicional, denominado \"tarifa joven\", como medida de compensación por los mayores riesgos asociados.\r\n3.	Licencia de Conducir:\r\nLos clientes deben poseer una licencia de conducir válida, emitida al menos un año antes de la fecha del alquiler. No se aceptarán licencias provisionales o temporales.', '2024-12-08 16:16:50.876083'),
(8, 'Política de Pago y Depósitos', 'El proceso de reserva incluye el pago completo del alquiler y el depósito de una garantía reembolsable. Esto protege al negocio frente a posibles inconvenientes durante el uso del vehículo.\r\nDetalles:\r\n1.	Pago Completo:\r\nLos clientes deben pagar el monto total del alquiler al momento de confirmar la reserva.\r\n2.	Depósito Reembolsable:\r\nUn depósito será retenido como garantía y reembolsado dentro de las 48 horas posteriores a la devolución del vehículo, siempre que no se presenten daños o cargos adicionales.\r\n3.	Métodos de Pago Aceptados:\r\nSe aceptan tarjetas de crédito, débito y transferencias bancarias como métodos de pago.', '2024-12-08 16:17:09.990331'),
(9, 'Política de Uso del Vehículo', 'Los vehículos alquilados deben ser utilizados únicamente dentro de las áreas geográficas autorizadas. El uso fuera de estas áreas requiere autorización previa y está sujeto a sanciones en caso de incumplimiento.\r\nDetalles:\r\n1.	Áreas Autorizadas:\r\nLas áreas geográficas permitidas para el uso del vehículo serán definidas al momento de la reserva.\r\n2.	Multa por Infracción:\r\nEl uso fuera de las áreas autorizadas estará sujeto a una multa fija, además del costo del transporte del vehículo de regreso.\r\n3.	Autorización Especial:\r\nLos clientes pueden solicitar autorización previa para utilizar el vehículo fuera de las áreas establecidas.', '2024-12-08 16:17:22.709065'),
(10, 'Política de Notificaciones', 'El sistema enviará notificaciones automatizadas a los clientes para mantenerlos informados sobre eventos importantes relacionados con sus reservas y alquileres.\r\nDetalles:\r\n1.	Recordatorios:\r\nSe enviará un recordatorio 24 horas antes del inicio del alquiler y otro antes del vencimiento de la devolución.\r\n2.	Notificaciones de Retrasos:\r\nLos clientes recibirán alertas si no han devuelto el vehículo en el tiempo acordado.\r\n3.	Actualizaciones:\r\nLas notificaciones incluirán cualquier cambio en las políticas o términos del contrato.', '2024-12-08 16:17:39.548333');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_reserva`
--

CREATE TABLE `core_reserva` (
  `id` bigint(20) NOT NULL,
  `codigo_reserva` varchar(10) NOT NULL,
  `fecha_reserva` datetime(6) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_retorno` date NOT NULL,
  `precio_total` int(10) UNSIGNED DEFAULT NULL,
  `estado_reserva` varchar(20) NOT NULL,
  `auto_id` bigint(20) NOT NULL,
  `cliente_id` bigint(20) NOT NULL
) ;

--
-- Volcado de datos para la tabla `core_reserva`
--

INSERT INTO `core_reserva` (`id`, `codigo_reserva`, `fecha_reserva`, `fecha_inicio`, `fecha_retorno`, `precio_total`, `estado_reserva`, `auto_id`, `cliente_id`) VALUES
(21, '6081556544', '2024-12-01 20:02:45.000000', '2024-01-01', '2024-02-01', 3333, 'completada', 3, 34),
(27, '9127299000', '2024-12-03 20:34:56.000000', '2025-01-01', '2025-01-01', 60000, 'cancelada', 5, 22),
(29, '8456487884', '2024-12-04 04:59:10.000000', '2025-01-01', '2025-02-01', NULL, 'cancelada', 3, 24),
(30, '1339686905', '2024-11-27 19:33:00.000000', '2024-12-03', '2024-12-07', 120000, 'completada', 3, 24),
(31, '6593172253', '2024-12-04 05:16:23.000000', '2025-05-05', '2025-06-05', 60000, 'cancelada', 4, 34),
(32, '5154651630', '2024-12-04 05:22:20.000000', '2025-05-05', '2025-07-05', 6000, 'cancelada', 4, 25),
(33, '9494126740', '2024-12-04 05:23:45.000000', '2025-01-01', '2025-05-03', 60000, 'completada', 4, 25),
(34, '3639828136', '2024-12-04 05:43:12.000000', '2025-01-01', '2025-02-01', 50000, 'cancelada', 4, 25),
(36, '2734776353', '2024-12-05 14:46:44.333422', '2025-01-01', '2025-02-01', NULL, 'pagada', 4, 35),
(37, '7783365223', '2024-12-06 17:57:00.000000', '2024-12-07', '2024-12-08', 60000, 'completada', 4, 36),
(38, '4396043983', '2024-11-28 22:58:00.000000', '2024-12-09', '2024-12-12', 200000, 'activa', 6, 23);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_segurobasico`
--

CREATE TABLE `core_segurobasico` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` int(10) UNSIGNED NOT NULL,
  `deducible` varchar(50) NOT NULL,
  `coberturas` longtext NOT NULL
) ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `core_trabajador`
--

CREATE TABLE `core_trabajador` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `rut` varchar(12) NOT NULL,
  `cargo` varchar(50) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `custom_user`
--

CREATE TABLE `custom_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `tipo_usuario` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `custom_user`
--

INSERT INTO `custom_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`, `tipo_usuario`) VALUES
(5, 'pbkdf2_sha256$870000$zl72obAqvtJnJ1QQdIp0Ri$aYArF6om/lhFvFWX+iG85YF+2bnMrR8T0DYqnbc8U9Q=', '2024-11-29 16:23:38.860674', 0, 'felipe303', '', '', 0, 1, '2024-11-29 16:23:22.761810', 'feliq@gmail.com', 'cliente'),
(21, 'pbkdf2_sha256$870000$rMv5L4aUb1m2vb6Tj20G7U$evpXKWz4QT0MykcrdiKjGYTJSVWCeMmrC8EoNhFQ2cY=', '2024-11-30 04:10:29.000000', 1, 'root', '', '', 1, 1, '2024-11-30 04:09:44.000000', 'root@gmail.com', 'administrador'),
(22, 'pbkdf2_sha256$870000$08DcriSw4AVxcVvN7nQp8Q$JFVyOP9M2d+mZ5qB6TePbL5Ivz17B3ceA3Eksh7kFZ4=', '2024-12-10 17:38:00.463629', 1, 'FelipeCastillo97', 'Felipe', 'Castillo', 1, 1, '2024-11-30 04:15:43.000000', 'felipe.castillo101@inacapmail.cl', 'administrador'),
(23, 'pollo5678', '2024-11-30 04:24:28.000000', 0, 'EdisonHernandez82', 'Edison', 'Hernandez', 1, 1, '2024-11-30 04:24:18.000000', 'enoc@gmail.com', 'cliente'),
(25, 'pbkdf2_sha256$870000$gBaMHihw4FSxtj3HUMqZyu$8gm1GXdWhqIfo6f+CPfsQkfAg+sQ3nLEWin3ms5dD2M=', '2024-12-01 01:31:04.000000', 0, 'FelipeNacho97', 'Felipe', 'Pacheco', 1, 1, '2024-12-01 01:30:45.000000', 'felipenacho@gmail.com', 'Trabajador'),
(27, 'pbkdf2_sha256$870000$LXUS8TeKzQtY8uW8K6Nq0n$o0coF/Qyj3DlHh96J4jc7msgT3ifoFz/LIgCaMQcMOs=', '2024-12-01 06:45:27.628516', 0, 'Pollodrol', '', '', 0, 1, '2024-12-01 04:51:54.782745', 'pollodrol@gmail.com', 'cliente'),
(28, 'pbkdf2_sha256$870000$QwNtL5W6QgoCT4uFATwPz9$ufT0BQbW+ww/Uj/RwjaSce8kUbVLBf5w2K8SPzZ9/ag=', NULL, 0, 'Vacadrol', '', '', 0, 1, '2024-12-01 16:15:21.717602', 'vacadrol@gmail.com', 'cliente'),
(29, 'pbkdf2_sha256$870000$k2qxVvukbWQlEiNO01YKlB$BIUfgFqgGmZHFdYMqiPN/cvUP/RwXYPiuUaQOSZLfZc=', '2024-12-01 17:47:16.996473', 0, 'vacapollo', '', '', 0, 1, '2024-12-01 16:16:40.910836', 'vac@gmail.com', 'cliente'),
(30, 'pbkdf2_sha256$870000$17kSAuWoArz0r4KsuljcmJ$BDLdYYNeaOUgVh2e3QeHYlE96Yx1tzHcHn/M14GhUcg=', '2024-12-10 04:12:17.438606', 0, 'vaca', '', '', 0, 1, '2024-12-01 18:08:35.734688', 'vaca@gmail.com', 'cliente'),
(31, 'pbkdf2_sha256$870000$ZPhuILuXsgTRBLtpqBoJqB$BneRVFCyxSpmo6hCEWn8j/2diQHTkgsrlY2R6dun/lU=', '2024-12-01 18:23:04.308392', 0, 'elefante', '', '', 0, 1, '2024-12-01 18:21:39.610143', 'elefante@gmail.com', 'cliente'),
(32, 'pbkdf2_sha256$870000$6G2YudzuCvQiDh6f4tEdbp$HL+ox157nPZesmfHq3HOaqHUbwcGpiRpAgFdGCiyMdI=', '2024-12-01 19:56:00.543266', 0, 'leon', '', '', 0, 1, '2024-12-01 18:32:09.291699', 'leon@gmail.com', 'cliente'),
(33, 'pbkdf2_sha256$870000$1vRTHCWmG7MgfokXDUftPC$ajrUhU67VYQAK7d0K3YpSTqCetMrkVtk8ChYyCy95oo=', '2024-12-01 19:56:27.472184', 0, 'tigre', '', '', 0, 1, '2024-12-01 19:49:11.412995', 'tigre@gmail.com', 'cliente'),
(34, 'pbkdf2_sha256$870000$9hXzPvNcPOcqU7ebdzgpFT$LII+9EX/oVY/94Lc2WwLTFu8jKMM2o43kJ0pnsDyDxo=', '2024-12-05 14:43:44.260206', 0, 'Pedro67', '', '', 0, 1, '2024-12-05 14:43:16.059712', 'pedro67@gmail.com', 'cliente'),
(35, 'pbkdf2_sha256$870000$ay80PrgD3kc2NkxsvJ2grX$76IpRRM2z5PNBCLtf3G8y65kZGvFFM8yNVQICocvVAY=', '2024-12-06 14:45:15.195700', 0, 'EdisonH', '', '', 0, 1, '2024-12-06 14:45:00.693609', 'edison@rentacar.cl', 'cliente'),
(39, 'pbkdf2_sha256$870000$HwAVigROESSp4s2TquG1JW$89giYy30JyYYU0oNg+YQYZe5VNTowGXdiTIsVDtUJ0E=', '2024-12-10 16:49:21.131426', 1, 'EdisonHer', 'Edison', 'Hernandez', 1, 1, '2024-12-09 15:07:35.000000', 'edisonHer@rentacar.cl', 'administrador'),
(40, 'pbkdf2_sha256$870000$iqOUeADl0NkmKoTDkL00Ss$BXx1ztsshMW0bVQ/Q2+UPztTIkwFxvWsuJyHPzcbMcM=', '2024-12-10 16:05:49.369512', 0, 'FelipePacheco97', 'Felipe', 'Pacheco', 1, 1, '2024-12-09 15:20:50.000000', 'pacheco@rentacar.cl', 'trabajador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `custom_user_groups`
--

CREATE TABLE `custom_user_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `custom_user_groups`
--

INSERT INTO `custom_user_groups` (`id`, `customuser_id`, `group_id`) VALUES
(3, 21, 4),
(1, 22, 4),
(2, 23, 5),
(4, 25, 5),
(7, 39, 4),
(8, 40, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `custom_user_user_permissions`
--

CREATE TABLE `custom_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `custom_user_user_permissions`
--

INSERT INTO `custom_user_user_permissions` (`id`, `customuser_id`, `permission_id`) VALUES
(1, 25, 9),
(2, 39, 1),
(3, 39, 2),
(4, 39, 3),
(5, 39, 4),
(6, 39, 5),
(7, 39, 6),
(8, 39, 7),
(9, 39, 8),
(10, 39, 9),
(11, 39, 10),
(12, 39, 11),
(13, 39, 12),
(14, 39, 13),
(15, 39, 14),
(16, 39, 15),
(17, 39, 16),
(18, 39, 17),
(19, 39, 18),
(20, 39, 19),
(21, 39, 20),
(22, 39, 21),
(23, 39, 22),
(24, 39, 23),
(25, 39, 24),
(26, 39, 25),
(27, 39, 26),
(28, 39, 27),
(29, 39, 28),
(30, 39, 29),
(31, 39, 30),
(32, 39, 31),
(33, 39, 32),
(34, 39, 33),
(35, 39, 34),
(36, 39, 35),
(37, 39, 36),
(38, 39, 37),
(39, 39, 38),
(40, 39, 39),
(41, 39, 40),
(42, 39, 41),
(43, 39, 42),
(44, 39, 43),
(45, 39, 44),
(46, 39, 45),
(47, 39, 46),
(48, 39, 47),
(49, 39, 48),
(50, 39, 49),
(51, 39, 50),
(52, 39, 51),
(53, 39, 52),
(54, 39, 53),
(55, 39, 54),
(56, 39, 55),
(57, 39, 56);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-30 04:17:54.607168', '1', 'Felipe Castillo', 1, '[{\"added\": {}}]', 3, 21),
(2, '2024-11-30 04:18:06.684855', '2', 'Edison Hernandez', 1, '[{\"added\": {}}]', 3, 21),
(3, '2024-11-30 04:18:20.073296', '3', 'Benjamin Gonzalez', 1, '[{\"added\": {}}]', 3, 21),
(4, '2024-11-30 04:18:56.129408', '4', 'Administrador', 1, '[{\"added\": {}}]', 3, 21),
(5, '2024-11-30 04:19:45.981295', '22', 'FelipeCastillo97', 1, '[{\"added\": {}}]', 7, 21),
(6, '2024-11-30 04:25:42.976949', '5', 'Trabajador', 1, '[{\"added\": {}}]', 3, 21),
(7, '2024-11-30 04:27:04.609701', '23', 'EdisonHernandez82', 1, '[{\"added\": {}}]', 7, 21),
(8, '2024-11-30 04:51:25.408261', '22', 'FelipeCastillo97', 2, '[]', 7, 21),
(9, '2024-11-30 04:52:51.441881', '22', 'FelipeCastillo97', 2, '[{\"changed\": {\"fields\": [\"Password\"]}}]', 7, 21),
(10, '2024-11-30 04:55:21.408584', '22', 'FelipeCastillo97', 2, '[]', 7, 21),
(11, '2024-11-30 04:57:26.191292', '22', 'FelipeCastillo97', 2, '[]', 7, 21),
(12, '2024-11-30 05:03:34.663114', '22', 'FelipeCastillo97', 2, '[]', 7, 21),
(13, '2024-11-30 05:09:43.629644', '22', 'FelipeCastillo97', 2, '[]', 7, 22),
(14, '2024-11-30 05:09:53.667430', '23', 'EdisonHernandez82', 2, '[{\"changed\": {\"fields\": [\"Tipo usuario\"]}}]', 7, 22),
(15, '2024-11-30 05:10:32.044302', '3', 'Benjamin Gonzalez', 3, '', 3, 22),
(16, '2024-11-30 05:10:41.029997', '2', 'Edison Hernandez', 3, '', 3, 22),
(17, '2024-11-30 05:10:47.860402', '1', 'Felipe Castillo', 3, '', 3, 22),
(18, '2024-11-30 05:11:21.636509', '21', 'root', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 7, 22),
(19, '2024-12-01 01:31:44.600150', '25', 'FelipeNacho97', 1, '[{\"added\": {}}]', 7, 22),
(20, '2024-12-01 01:33:13.183842', '25', 'FelipeNacho97', 2, '[]', 7, 22),
(21, '2024-12-01 01:33:27.133111', '24', 'FelipePacheco97', 3, '', 7, 22),
(22, '2024-12-01 01:34:18.154819', '25', 'FelipeNacho97', 2, '[]', 7, 22),
(23, '2024-12-01 01:37:46.465834', '5', 'Trabajador', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 22),
(24, '2024-12-01 01:56:09.608620', '5', 'Trabajador', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 22),
(25, '2024-12-01 01:56:34.325429', '25', 'FelipeNacho97', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 7, 22),
(26, '2024-12-01 01:58:13.137424', '26', 'FelipePacheco97', 1, '[{\"added\": {}}]', 7, 22),
(27, '2024-12-01 02:01:24.301015', '5', 'Trabajador', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 22),
(28, '2024-12-01 04:44:57.401246', '26', 'FelipePacheco97', 2, '[{\"changed\": {\"fields\": [\"Tipo usuario\"]}}]', 7, 22),
(29, '2024-12-08 23:58:40.923778', '38', 'FelipePacheco97', 1, '[{\"added\": {}}]', 7, 22),
(30, '2024-12-09 00:05:09.994823', '38', 'FelipePacheco97', 2, '[]', 7, 22),
(31, '2024-12-09 02:04:24.942978', '39', 'EdisonHer', 1, '[{\"added\": {}}]', 7, 22),
(32, '2024-12-09 02:05:44.517259', '38', 'FelipePacheco97', 2, '[]', 7, 22),
(33, '2024-12-09 02:07:17.498781', '38', 'FelipePacheco97', 3, '', 7, 22),
(34, '2024-12-09 14:56:12.503605', '39', 'EdisonHer', 2, '[{\"changed\": {\"fields\": [\"User permissions\", \"Date joined\"]}}]', 7, 22),
(35, '2024-12-09 15:07:59.635069', '39', 'EdisonHer', 2, '[{\"changed\": {\"fields\": [\"Superuser status\", \"Date joined\"]}}]', 7, 22),
(36, '2024-12-09 15:21:12.640814', '40', 'FelipePacheco97', 1, '[{\"added\": {}}]', 7, 39);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'core', 'auto'),
(8, 'core', 'cliente'),
(7, 'core', 'customuser'),
(10, 'core', 'factura'),
(11, 'core', 'nosotros'),
(12, 'core', 'politica'),
(9, 'core', 'reserva'),
(14, 'core', 'segurobasico'),
(13, 'core', 'trabajador'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-29 00:41:16.071549'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-11-29 00:41:16.265787'),
(3, 'auth', '0001_initial', '2024-11-29 00:41:16.972179'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-11-29 00:41:17.098552'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-11-29 00:41:17.109373'),
(6, 'auth', '0004_alter_user_username_opts', '2024-11-29 00:41:17.122227'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-11-29 00:41:17.135441'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-11-29 00:41:17.140952'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-11-29 00:41:17.151258'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-11-29 00:41:17.162831'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-11-29 00:41:17.177222'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-11-29 00:41:17.213983'),
(13, 'auth', '0011_update_proxy_permissions', '2024-11-29 00:41:17.227342'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-11-29 00:41:17.240566'),
(15, 'core', '0001_initial', '2024-11-29 00:41:19.599921'),
(16, 'admin', '0001_initial', '2024-11-29 00:41:19.888337'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-11-29 00:41:19.905757'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-29 00:41:19.926695'),
(19, 'sessions', '0001_initial', '2024-11-29 00:41:20.012494'),
(20, 'templatesApp', '0001_initial', '2024-11-29 00:41:21.388557'),
(21, 'templatesApp', '0002_cliente_imagen_alter_auto_estado_auto_and_more', '2024-11-29 00:41:21.506023'),
(22, 'templatesApp', '0003_remove_reserva_auto_and_more', '2024-11-29 00:41:22.508678'),
(23, 'core', '0002_customuser_tipo_usuario', '2024-11-29 00:43:45.207706'),
(24, 'core', '0003_remove_cliente_user', '2024-11-29 01:06:51.585643'),
(25, 'core', '0004_nosotros_politica_trabajador_cliente_user', '2024-11-29 16:22:41.500877'),
(26, 'core', '0005_alter_customuser_tipo_usuario', '2024-12-01 01:30:36.065225'),
(27, 'core', '0006_alter_cliente_rut_alter_customuser_tipo_usuario_and_more', '2024-12-04 04:56:54.860592'),
(28, 'core', '0007_rename_contenido_politica_descripcion_and_more', '2024-12-06 02:46:00.468649'),
(29, 'core', '0008_remove_auto_fecha_ultimo_mantenimiento_and_more', '2024-12-06 04:50:53.047624'),
(30, 'core', '0009_rename_nacionalidad_cliente_ciudad_cliente_region', '2024-12-06 04:50:53.365342'),
(31, 'core', '0010_remove_cliente_historial_alquileres_and_more', '2024-12-06 14:28:39.287688'),
(32, 'core', '0011_auto_imagen', '2024-12-06 23:39:05.591378'),
(33, 'core', '0012_alter_auto_imagen', '2024-12-07 00:10:13.429315'),
(34, 'core', '0012_segurobasico_alter_auto_imagen', '2024-12-08 04:50:36.209801'),
(35, 'core', '0010_segurobasico_remove_cliente_historial_alquileres_and_more', '2024-12-08 11:58:08.000000'),
(36, 'core', '0011_alter_auto_precio_dia', '2024-12-08 16:58:59.728254'),
(37, 'core', '0012_alter_factura_total_alter_reserva_precio_total', '2024-12-08 17:06:57.486272'),
(38, 'core', '0013_alter_segurobasico_precio', '2024-12-08 17:07:57.986639');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('11jc7farcm6sziklbk6hcd9q1c1jo14y', '.eJxVjDsOwyAQRO9CHSGWxYBTpvcZ0PKLnUQgGbuKcvdgyUVSjTTvzbyZo32b3d7S6pbIrgwFu_yWnsIzlYPEB5V75aGWbV08PxR-0sanGtPrdrp_BzO1ua-9GA16mwINeZAgcPSIJgcFMdsxZDIABB1IkIhK62R1T6VAKzQysM8X8Fs2oA:1tJObu:lqGzTQweXCTBtS_9HxKDZwKpgY-ED44f5aOPDSC3fu8', '2024-12-20 03:02:30.346107'),
('3be43nhqukznophrrnyw3i4zroic5s2p', '.eJxVjDsOwyAQRO9CHSGWxYBTpvcZ0PKLnUQgGbuKcvdgyUVSjTTvzbyZo32b3d7S6pbIrgwFu_yWnsIzlYPEB5V75aGWbV08PxR-0sanGtPrdrp_BzO1ua-9GA16mwINeZAgcPSIJgcFMdsxZDIABB1IkIhK62R1T6VAKzQysM8X8Fs2oA:1tJv6L:hkygddVAx3welQG4mHERG8v4w95W7EAoTOWxdnli9tg', '2024-12-21 13:44:05.736377'),
('5xyw2ukdvtncb3fwkxpv9dxwzo1g53g8', '.eJxVjEEOwiAQRe_C2hBoOxRcuvcMZIaZStVAUtqV8e7apAvd_vfef6mI25rj1mSJM6uzsur0uxGmh5Qd8B3LrepUy7rMpHdFH7Tpa2V5Xg737yBjy9862BAQRgEQR51x1jPS5Dl5CGkiw8JgAP0IvXUJyNnQD4Mllwx77rx6fwDiEjex:1tH3Rz:6hiC4NV-S4vlMe7mRhZW5fFnQ1TYcGqzj8y8Ord_d7k', '2024-12-13 16:02:35.370556'),
('94w7oiwl7b0yzybozi1vq7amq0br99ip', '.eJxVjMsOwiAQRf-FtSGUxwAu3fsNZGBAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hJnZmUrLT7xgxPXLbCd2x3TpPva3LHPmu8IMOfu2Un5fD_TuoOOq3Nr44yICoJ2FIl6J8RnLCFiMcpZS0E2lCjOQBdLYGDFijLJGCokGy9wcW5Dge:1tJjY8:oiaTeWWU8aNrOVRMSkizXLSxFp05O3aT6znCGgDjoZk', '2024-12-21 01:24:00.088656'),
('kskji75u7p4x7pssvwdu81to72x17o15', '.eJxVjDsOwjAQRO_iGln-ZP2hpM8ZrLXXxgHkSHFSIe4OQSmgG817M08WcFtr2HpewkTszAbBTr9lxHTPbSd0w3adeZrbukyR7wo_aOfjTPlxOdy_g4q9ftZCQ6HsrdTCgERnpY8-SgADJbniURn6JkABVklyQ1aasgIgAi3Z6w3t_zeC:1tKfl6:7P6GWRrA4x4JsvhI_A2CV_eqbpnztZaGfNHggWsFcLg', '2024-12-23 15:33:16.515030'),
('ohvn5dzyceo2r3mbzb4pq5i6ms5jqp90', '.eJxVjMsOwiAQRf-FtSGUxwAu3fsNZGBAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hJnZmUrLT7xgxPXLbCd2x3TpPva3LHPmu8IMOfu2Un5fD_TuoOOq3Nr44yICoJ2FIl6J8RnLCFiMcpZS0E2lCjOQBdLYGDFijLJGCokGy9wcW5Dge:1tKmgm:YrfE3kgcFcN6QU3vcCDPNWrx6rlCnIlhHnBSaKEoA1A', '2024-12-23 22:57:16.462484'),
('qj8fxpzrfikj2pih7sz84lbsc209jcbj', 'e30:1tH3Po:i5ZxP183THN2rq_LNey_TPsZFk3yWZrZlpQTLFKGdZE', '2024-12-13 16:00:20.298858');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `core_auto`
--
ALTER TABLE `core_auto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `patente` (`patente`);

--
-- Indices de la tabla `core_cliente`
--
ALTER TABLE `core_cliente`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `core_cliente_historial_alquileres`
--
ALTER TABLE `core_cliente_historial_alquileres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_cliente_historial_a_cliente_id_reserva_id_7031b929_uniq` (`cliente_id`,`reserva_id`),
  ADD KEY `core_cliente_histori_reserva_id_feead6c0_fk_core_rese` (`reserva_id`);

--
-- Indices de la tabla `core_factura`
--
ALTER TABLE `core_factura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_factura` (`codigo_factura`),
  ADD KEY `core_factura_cliente_id_a3d41446_fk_core_cliente_id` (`cliente_id`),
  ADD KEY `core_factura_reserva_id_ba241db6_fk_core_reserva_id` (`reserva_id`);

--
-- Indices de la tabla `core_nosotros`
--
ALTER TABLE `core_nosotros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `core_politica`
--
ALTER TABLE `core_politica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `core_reserva`
--
ALTER TABLE `core_reserva`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_reserva` (`codigo_reserva`),
  ADD KEY `core_reserva_auto_id_3b670659_fk_core_auto_id` (`auto_id`),
  ADD KEY `core_reserva_cliente_id_2ccfdd70_fk_core_cliente_id` (`cliente_id`);

--
-- Indices de la tabla `core_segurobasico`
--
ALTER TABLE `core_segurobasico`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `core_trabajador`
--
ALTER TABLE `core_trabajador`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rut` (`rut`);

--
-- Indices de la tabla `custom_user`
--
ALTER TABLE `custom_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `custom_user_groups`
--
ALTER TABLE `custom_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `custom_user_groups_customuser_id_group_id_ea14f886_uniq` (`customuser_id`,`group_id`),
  ADD KEY `custom_user_groups_group_id_02874f21_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `custom_user_user_permissions`
--
ALTER TABLE `custom_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `custom_user_user_permiss_customuser_id_permission_f9232336_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_custom_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=252;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT de la tabla `core_auto`
--
ALTER TABLE `core_auto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `core_cliente`
--
ALTER TABLE `core_cliente`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `core_factura`
--
ALTER TABLE `core_factura`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `core_nosotros`
--
ALTER TABLE `core_nosotros`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `core_politica`
--
ALTER TABLE `core_politica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `core_reserva`
--
ALTER TABLE `core_reserva`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `core_segurobasico`
--
ALTER TABLE `core_segurobasico`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `core_trabajador`
--
ALTER TABLE `core_trabajador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `custom_user`
--
ALTER TABLE `custom_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `custom_user_groups`
--
ALTER TABLE `custom_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `custom_user_user_permissions`
--
ALTER TABLE `custom_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `core_cliente`
--
ALTER TABLE `core_cliente`
  ADD CONSTRAINT `core_cliente_user_id_d7896daf_fk_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `custom_user` (`id`);

--
-- Filtros para la tabla `core_factura`
--
ALTER TABLE `core_factura`
  ADD CONSTRAINT `core_factura_cliente_id_a3d41446_fk_core_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `core_cliente` (`id`),
  ADD CONSTRAINT `core_factura_reserva_id_ba241db6_fk_core_reserva_id` FOREIGN KEY (`reserva_id`) REFERENCES `core_reserva` (`id`);

--
-- Filtros para la tabla `core_reserva`
--
ALTER TABLE `core_reserva`
  ADD CONSTRAINT `core_reserva_auto_id_3b670659_fk_core_auto_id` FOREIGN KEY (`auto_id`) REFERENCES `core_auto` (`id`),
  ADD CONSTRAINT `core_reserva_cliente_id_2ccfdd70_fk_core_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `core_cliente` (`id`);

--
-- Filtros para la tabla `custom_user_groups`
--
ALTER TABLE `custom_user_groups`
  ADD CONSTRAINT `custom_user_groups_customuser_id_8e3d0338_fk_custom_user_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user` (`id`),
  ADD CONSTRAINT `custom_user_groups_group_id_02874f21_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `custom_user_user_permissions`
--
ALTER TABLE `custom_user_user_permissions`
  ADD CONSTRAINT `custom_user_user_per_customuser_id_ec2da4cb_fk_custom_us` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user` (`id`),
  ADD CONSTRAINT `custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `custom_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
