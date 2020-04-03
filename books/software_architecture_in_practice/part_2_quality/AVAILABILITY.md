# Availability

| Portion of Scenario | Possible Values |
| - | - |
| Source | Internal/external: people, hardware, software, physical infrastructure, physical environment |
| Stimulus | Fault: omission, crash, incorrect timing, incorrect reponse |
| Artifact | Processors, communication channels, persistent storage, process |
| Environment | Normal operation, startup, shutdown, repair mode, degraded operation, overloaded operation |
| Response | Prevent the fault from becoming a failure. Detecting the fault: Log the fault, notify appropriate entities (people or systems). Recover from the fault: Disable source of events causing the fault, be temporarily unavailable while the repair is being effected, fix or mask the fault/failure or contain the damage it causes, operate in a degraded mode while repair is being effected |
| Response Measure | Time or time interval when the system must be available. Availability percentage (99.999%). Time to detect the fault. Time to repair the fault. Time or time interval in which system can be in degraded mode. Proportion (99%) or rate (up to 100 per second) of a certain class of faults that the system prevents, or handles without failing |
