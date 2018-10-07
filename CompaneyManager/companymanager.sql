-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 24, 2018 at 05:34 AM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `companymanager`
--

-- --------------------------------------------------------

--
-- Table structure for table `executive`
--

CREATE TABLE `executive` (
  `executive_id` int(11) NOT NULL,
  `executive_fname` varchar(255) NOT NULL,
  `executive_lname` varchar(255) NOT NULL,
  `executive_dob` varchar(255) NOT NULL,
  `executive_contact` varchar(255) NOT NULL,
  `executive_basicpay` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `executive`
--

INSERT INTO `executive` (`executive_id`, `executive_fname`, `executive_lname`, `executive_dob`, `executive_contact`, `executive_basicpay`, `created_at`) VALUES
(2, 'Mike', 'Forde', '12/07/1985', '5632145563', '100000', '2018-09-22 09:40:13'),
(3, 'Sandeep', 'Sandhu', '12/18/1995', '123652145', '26532', '2018-09-22 10:46:31');

-- --------------------------------------------------------

--
-- Table structure for table `hourly`
--

CREATE TABLE `hourly` (
  `hourEmp_id` int(11) NOT NULL,
  `hourEmp_fname` varchar(255) NOT NULL,
  `hourEmp_lname` varchar(255) NOT NULL,
  `hourEmp_dob` varchar(255) NOT NULL,
  `hourEmp_contact` varchar(255) NOT NULL,
  `hourEmp_basicpay` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `manager_id` int(11) NOT NULL,
  `manager_fname` varchar(255) NOT NULL,
  `manager_lname` varchar(255) NOT NULL,
  `manager_dob` varchar(255) NOT NULL,
  `manager_contact` varchar(255) NOT NULL,
  `manager_basicpay` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `salaried`
--

CREATE TABLE `salaried` (
  `salaried_id` int(11) NOT NULL,
  `salaried_fname` varchar(255) NOT NULL,
  `salaried_lname` varchar(255) NOT NULL,
  `salaried_dob` varchar(255) NOT NULL,
  `salaried_contact` varchar(255) NOT NULL,
  `salaried_basicpay` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `executive`
--
ALTER TABLE `executive`
  ADD PRIMARY KEY (`executive_id`);

--
-- Indexes for table `hourly`
--
ALTER TABLE `hourly`
  ADD PRIMARY KEY (`hourEmp_id`);

--
-- Indexes for table `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`manager_id`);

--
-- Indexes for table `salaried`
--
ALTER TABLE `salaried`
  ADD PRIMARY KEY (`salaried_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `executive`
--
ALTER TABLE `executive`
  MODIFY `executive_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `hourly`
--
ALTER TABLE `hourly`
  MODIFY `hourEmp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `manager`
--
ALTER TABLE `manager`
  MODIFY `manager_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `salaried`
--
ALTER TABLE `salaried`
  MODIFY `salaried_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
