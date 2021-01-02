-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 30, 2020 at 08:52 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `daycare`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_detailtransaksi`
--

CREATE TABLE `tb_detailtransaksi` (
  `idDetailTransaksi` bigint(20) NOT NULL,
  `idTransaksi` bigint(20) DEFAULT NULL,
  `idKategori` bigint(20) DEFAULT NULL,
  `namaPeliharaan` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_detailtransaksi`
--

INSERT INTO `tb_detailtransaksi` (`idDetailTransaksi`, `idTransaksi`, `idKategori`, `namaPeliharaan`) VALUES
(1, 1, 1, 'Pusi'),
(2, 1, 2, 'Ciko'),
(3, 2, 4, 'Delon'),
(4, 3, 3, 'Sena'),
(5, 4, 2, 'Rusaa'),
(6, 5, 4, 'tuturu'),
(7, 6, 3, 'Senorita'),
(8, 7, 2, 'Yui'),
(9, 7, 1, 'Susano');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kategorihewan`
--

CREATE TABLE `tb_kategorihewan` (
  `idKategori` bigint(20) NOT NULL,
  `namaKategori` varchar(255) DEFAULT NULL,
  `biaya` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_kategorihewan`
--

INSERT INTO `tb_kategorihewan` (`idKategori`, `namaKategori`, `biaya`) VALUES
(1, 'Kucing', 30000),
(2, 'Anjing', 50000),
(3, 'Burung Beo', 26000),
(4, 'Musang', 70000);

-- --------------------------------------------------------

--
-- Table structure for table `tb_pelanggan`
--

CREATE TABLE `tb_pelanggan` (
  `usernamePelanggan` varchar(15) NOT NULL,
  `nama` varchar(40) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_pelanggan`
--

INSERT INTO `tb_pelanggan` (`usernamePelanggan`, `nama`, `password`) VALUES
('bagoesnayoko', 'Bagus Nayoko', 'bagoezz'),
('dindaptr', 'Dinda Putri', 'dindamzz'),
('rarasdw', 'Raras Dwistian', 'rarass'),
('riannn', 'Yusrian', 'riannyavio'),
('suprakuning', 'Gavril', 'ddd');

-- --------------------------------------------------------

--
-- Table structure for table `tb_petugas`
--

CREATE TABLE `tb_petugas` (
  `usernamePetugas` varchar(15) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_petugas`
--

INSERT INTO `tb_petugas` (`usernamePetugas`, `nama`, `password`) VALUES
('jeje1702', 'Jessica Maya', '1702ivan');

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `idTransaksi` bigint(20) NOT NULL,
  `waktuTransaksi` datetime NOT NULL,
  `waktuPengembalian` datetime DEFAULT NULL,
  `usernamePetugas` varchar(15) DEFAULT NULL,
  `usernamePelanggan` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`idTransaksi`, `waktuTransaksi`, `waktuPengembalian`, `usernamePetugas`, `usernamePelanggan`) VALUES
(1, '2020-12-20 12:00:30', '2020-12-23 11:30:00', 'jeje1702', 'rarasdw'),
(2, '2020-12-23 16:20:00', '2020-12-30 00:27:24', 'jeje1702', 'bagoesnayoko'),
(3, '2020-12-28 23:03:28', NULL, 'jeje1702', 'rarasdw'),
(4, '2020-12-28 23:23:45', '2020-12-30 00:27:48', 'jeje1702', 'bagoesnayoko'),
(5, '2020-12-28 23:26:02', NULL, 'jeje1702', 'dindaptr'),
(6, '2020-12-30 00:40:39', NULL, 'jeje1702', 'suprakuning'),
(7, '2020-12-30 01:04:55', NULL, 'jeje1702', 'riannn');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  ADD PRIMARY KEY (`idDetailTransaksi`),
  ADD KEY `idTransaksi` (`idTransaksi`),
  ADD KEY `idKategori` (`idKategori`);

--
-- Indexes for table `tb_kategorihewan`
--
ALTER TABLE `tb_kategorihewan`
  ADD PRIMARY KEY (`idKategori`);

--
-- Indexes for table `tb_pelanggan`
--
ALTER TABLE `tb_pelanggan`
  ADD PRIMARY KEY (`usernamePelanggan`);

--
-- Indexes for table `tb_petugas`
--
ALTER TABLE `tb_petugas`
  ADD PRIMARY KEY (`usernamePetugas`);

--
-- Indexes for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`idTransaksi`),
  ADD KEY `usernamePetugas` (`usernamePetugas`),
  ADD KEY `usernamePelanggan` (`usernamePelanggan`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  MODIFY `idDetailTransaksi` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tb_kategorihewan`
--
ALTER TABLE `tb_kategorihewan`
  MODIFY `idKategori` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `idTransaksi` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_detailtransaksi`
--
ALTER TABLE `tb_detailtransaksi`
  ADD CONSTRAINT `tb_detailtransaksi_ibfk_1` FOREIGN KEY (`idTransaksi`) REFERENCES `tb_transaksi` (`idTransaksi`),
  ADD CONSTRAINT `tb_detailtransaksi_ibfk_2` FOREIGN KEY (`idKategori`) REFERENCES `tb_kategorihewan` (`idKategori`);

--
-- Constraints for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`usernamePetugas`) REFERENCES `tb_petugas` (`usernamePetugas`),
  ADD CONSTRAINT `tb_transaksi_ibfk_2` FOREIGN KEY (`usernamePelanggan`) REFERENCES `tb_pelanggan` (`usernamePelanggan`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
