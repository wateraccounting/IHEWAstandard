# IHEWAstandard.Data

Define the **Data standard** of WaterAccounting Tools.

Data type

| C              | Python  | Numpy         | NetCDF    | Decsription      | Bits | Min                  | Max                  |
| -------------- | ------  | ------------- | --------- | ---------------- | ---- | -------------------- | -------------------- |
| signed char    |         | byte          | NC_BYTE   | Byte             | 8    | -128                 | 127                  |
| unsigned char  |         | ubyte         | NC_UBYTE  | Unsigned byte    | 8    | 0                    | 255                  |
| int8_t         |         | int8          | NC_UBYTE  | Byte             | 8    | -128                 | 127                  |
| int16_t        |         | int16         | NC_SHORT  | Integer          | 16   | -32768               | 32767                |
| int32_t        |         | int32         | NC_INT    | Integer          | 32   | -2147483648          | 2147483647           |
| int64_t        |         | int64         | NC_INT64  | Integer          | 64   | -9223372036854775808 | 9223372036854775807  |
| uint8_t        |         | uint8         | NC_UBYTE  | Unsigned integer | 8    | 0                    | 255                  |
| uint16_t       |         | uint16        | NC_USHORT | Unsigned integer | 16   | 0                    | 65535                |
| uint32_t       |         | uint32        | NC_UINT   | Unsigned integer | 32   | 0                    | 4294967295           |
| uint64_t       |         | uint64        | NC_UINT64 | Unsigned integer | 64   | 0                    | 18446744073709551615 |
| float          |         | float32       | NC_FLOAT  | Float            | 32   | 1.17549e-38          | 3.40282e+38          |
| double         | float   | float64       | NC_DOUBLE | Double           | 64   | 2.22507e-308         | 1.79769e+308         |
| double         | float   | float\_       |           |                  |      |                      |                      |
| float complex  |         | complex64     |           |                  |      |                      |                      |
| double complex | complex | complex128    |           |                  |      |                      |                      |
|                | complex | complex\_     |           |                  |      |                      |                      |

## [NetCDF](NetCDF.md)

