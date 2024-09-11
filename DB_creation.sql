CREATE DATABASE if NOT EXISTS food_distribuitor;

USE food_distribuitor;

CREATE TABLE `food_distribuitor`.`vendors` (`ID` INT(150) NOT NULL , `Nombre` VARCHAR(250) NULL , `Zona` VARCHAR(50) NULL , `Telefono` VARCHAR(100) NULL , `Correo` VARCHAR(150) NULL , `Meta` INT(150) NULL , `Ventas` INT(150) NULL , `Comisiones` INT(150) NULL , `Clientes` INT(150) NULL , `Estado` VARCHAR(50) NULL , `Comentarios` VARCHAR(200) NULL , PRIMARY KEY (`ID`)) ENGINE = InnoDB;
ALTER TABLE `vendors` CHANGE `ID` `ID` INT(150) NOT NULL AUTO_INCREMENT;

CREATE TABLE `food_distribuitor`.`sales` (`ID` INT(150) NOT NULL AUTO_INCREMENT , `Id_vendor` INT(150) NULL , `Name_client` VARCHAR(250) NULL , `Product` VARCHAR(250) NULL , `Quantity` INT(150) NULL , `P/u` INT(150) NULL , `Tot_sale` INT(150) NULL , `Payment` VARCHAR(250) NULL , `Status` VARCHAR(150) NULL ) ENGINE = InnoDB;
ALTER TABLE `sales` CHANGE `P/u` `Unitary_p` INT(150) NULL DEFAULT NULL;