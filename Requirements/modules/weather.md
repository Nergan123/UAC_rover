# Weather module requirements

| **REQ-id** | **Target**     | **Description**                                                                        |
|:-----------|:---------------|:---------------------------------------------------------------------------------------|
| 1          | Weather module | On request Module should provide measurements                                          |
| 2          | Weather module | Module should not make a new measurement if previous was done less than 30 seconds ago |
| 3          | Weather module | Module should output measurement in form of bytes                                      |
| 4          | Weather module | The temperature should affect the efficiency of the solar panels                       |
| 5          | Weather module | Max efficiency loss due to temperature is 0.6                                          |
