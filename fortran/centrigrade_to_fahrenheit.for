* columns matter in fortran
* to compile:
* gfortran centrigrade_to_fahrenheit.for -o centrigrade_to_fahrenheit
      PROGRAM CENTIGRADE_TO_FAHRENHEIT
      INTEGER C, Z
      REAL R
      PARAMETER (Z = 32)
      PARAMETER (R = 9.0 / 5.0)
      DO 10, C = 0, 40
         F = (C * R) + Z
         WRITE (*, 99) C, F
 99      FORMAT (I2, F6.1)
 10   CONTINUE
      STOP
      END
