Interfaz de bajo nivel
===================

La comunicación entre la api y el dispositivo fuelsensor ocurre mediante intercambio de paquetes de bytes. La api genera solicitudes para el dispositivo fuelSensor mediante un `paquete query`. El dispositivo fuelsensor procesa el paquete y responde con el `paquete response`. 


Paquete Query
-------------

El formato del `paquete query` es:

`cmd (2 bytes), params(4 bytes), CRC(2 bytes)`




