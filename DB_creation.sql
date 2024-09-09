CREATE DATABASE if NOT EXISTS food_distribuitor;

USE food_distribuitor;

CREATE TABLE `food_distribuitor`.`vendors` (`ID` INT(150) NOT NULL , `Nombre` VARCHAR(250) NULL , `Zona` VARCHAR(50) NULL , `Telefono` VARCHAR(100) NULL , `Correo` VARCHAR(150) NULL , `Meta` INT(150) NULL , `Ventas` INT(150) NULL , `Comisiones` INT(150) NULL , `Clientes` INT(150) NULL , `Estado` VARCHAR(50) NULL , `Comentarios` VARCHAR(200) NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `vendors` CHANGE `ID` `ID` INT(150) NOT NULL AUTO_INCREMENT;
