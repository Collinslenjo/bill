-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 12, 2018 at 10:07 AM
-- Server version: 5.7.21
-- PHP Version: 7.0.25-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pizza`
--

CREATE TABLE `pizza` (
  `id` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pizza`
--

INSERT INTO `pizza` (`id`, `name`, `size`, `price`, `created_on`, `updated_on`) VALUES
(1, 'Pizza', 'Small', 1200, '2018-03-05 13:46:51', '2018-03-05 13:46:51'),
(2, 'Pizza', 'Medium', 1400, '2018-03-05 13:47:03', '2018-03-05 13:47:03'),
(3, 'Pizza', 'Large', 1600, '2018-03-05 13:47:14', '2018-03-05 13:47:14'),
(4, 'None', 'None', 0, '2018-03-12 10:57:08', '2018-03-12 10:57:08');

-- --------------------------------------------------------

--
-- Table structure for table `pizza_order_items`
--

CREATE TABLE `pizza_order_items` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `pizza_id` int(11) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `topping`
--

CREATE TABLE `topping` (
  `id` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `category` varchar(36) DEFAULT NULL,
  `type` varchar(36) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `topping`
--

INSERT INTO `topping` (`id`, `name`, `category`, `type`, `price`, `created_on`, `updated_on`) VALUES
(1, 'pepperoni', 'Basic', 'small', 50, '2018-03-05 17:08:37', '2018-03-05 17:08:37'),
(2, 'pepperoni', 'Basic', 'medium', 75, '2018-03-05 17:10:18', '2018-03-05 17:10:18'),
(3, 'pepperoni', 'Basic', 'large', 100, '2018-03-05 17:11:27', '2018-03-05 17:11:27'),
(4, 'Cheese', 'Basic', 'small', 50, '2018-03-05 17:11:57', '2018-03-05 17:11:57'),
(5, 'Cheese', 'Basic', 'medium', 75, '2018-03-05 17:12:10', '2018-03-05 17:12:10'),
(6, 'Cheese', 'Basic', 'large', 100, '2018-03-05 17:13:27', '2018-03-05 17:13:27'),
(7, 'Ham', 'Basic', 'small', 50, '2018-03-05 17:14:18', '2018-03-05 17:14:18'),
(8, 'Ham', 'Basic', 'medium', 75, '2018-03-05 17:14:33', '2018-03-05 17:14:33'),
(9, 'Ham', 'Basic', 'large', 100, '2018-03-05 17:14:44', '2018-03-05 17:14:44'),
(10, 'pineapple', 'Basic', 'small', 50, '2018-03-05 17:15:11', '2018-03-05 17:15:11'),
(11, 'pineapple', 'Basic', 'medium', 75, '2018-03-05 17:15:21', '2018-03-05 17:15:21'),
(12, 'pineapple', 'Basic', 'large', 100, '2018-03-05 17:15:33', '2018-03-05 17:15:33'),
(13, 'Sausage', 'Deluxe', 'small', 200, '2018-03-05 17:16:20', '2018-03-05 17:16:20'),
(14, 'Sausage', 'Deluxe', 'medium', 300, '2018-03-05 17:16:33', '2018-03-05 17:16:33'),
(15, 'Sausage', 'Deluxe', 'large', 400, '2018-03-05 17:16:49', '2018-03-05 17:16:49'),
(16, 'Feta Cheese', 'Deluxe', 'small', 200, '2018-03-05 17:17:16', '2018-03-05 17:17:16'),
(17, 'Feta Cheese', 'Deluxe', 'medium', 300, '2018-03-05 17:17:31', '2018-03-05 17:17:31'),
(18, 'Feta Cheese', 'Deluxe', 'large', 400, '2018-03-05 17:17:47', '2018-03-05 17:17:47'),
(19, 'Tomatoes', 'Deluxe', 'small', 200, '2018-03-05 17:18:12', '2018-03-05 17:18:12'),
(20, 'Tomatoes', 'Deluxe', 'medium', 300, '2018-03-05 17:18:22', '2018-03-05 17:18:22'),
(21, 'Tomatoes', 'Deluxe', 'large', 400, '2018-03-05 17:18:38', '2018-03-05 17:18:38'),
(22, 'Olives', 'Deluxe', 'small', 200, '2018-03-05 17:19:08', '2018-03-05 17:19:08'),
(23, 'Olives', 'Deluxe', 'medium', 300, '2018-03-05 17:19:19', '2018-03-05 17:19:19'),
(24, 'Olives', 'Deluxe', 'large', 400, '2018-03-05 17:19:32', '2018-03-05 17:19:32'),
(25, 'None', 'None', 'None', 0, '2018-03-12 11:03:06', '2018-03-12 11:03:06');

-- --------------------------------------------------------

--
-- Table structure for table `topping_order_items`
--

CREATE TABLE `topping_order_items` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `topping_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `created_on` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_on` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `password`, `created_on`, `updated_on`) VALUES
(1, 'Admin', 'admin@example.com', 'pbkdf2:sha256:50000$6JTVQHZg$056676a25db53d5c4e71e22c479ecfd7419dc99ab0125f67d554612ef94a093b', '2018-03-12 11:07:24', '2018-03-12 11:07:24');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `size` (`size`);

--
-- Indexes for table `pizza_order_items`
--
ALTER TABLE `pizza_order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `pizza_id` (`pizza_id`);

--
-- Indexes for table `topping`
--
ALTER TABLE `topping`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `topping_order_items`
--
ALTER TABLE `topping_order_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `topping_id` (`topping_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `pizza`
--
ALTER TABLE `pizza`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `pizza_order_items`
--
ALTER TABLE `pizza_order_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `topping`
--
ALTER TABLE `topping`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `topping_order_items`
--
ALTER TABLE `topping_order_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `pizza_order_items`
--
ALTER TABLE `pizza_order_items`
  ADD CONSTRAINT `pizza_order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `pizza_order_items_ibfk_2` FOREIGN KEY (`pizza_id`) REFERENCES `pizza` (`id`);

--
-- Constraints for table `topping_order_items`
--
ALTER TABLE `topping_order_items`
  ADD CONSTRAINT `topping_order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`),
  ADD CONSTRAINT `topping_order_items_ibfk_2` FOREIGN KEY (`topping_id`) REFERENCES `topping` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
