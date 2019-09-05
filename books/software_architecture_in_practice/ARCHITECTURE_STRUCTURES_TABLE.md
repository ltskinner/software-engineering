# Useful Architecture Structures

| | **Software Structure** | **Element Types** | **Relations** | **Useful For** | **Quality Attributes Affected** |
| - | - | - | - | - | - |
| **Module Structures** | Decomposition | Module | Is a submodule of | Resource allocation and project structuring and planning; imformation hiding; encapsulation; configuration control | Modifiability |
|  | Uses | Module | Uses (to use) | Engineering subsets, engineering extensions | "Subsetability", extensilibity |
|  | Layers | Layer | Requires the correct presence of, uses the services of, provides abstraction to | Incremental development, implementing systems on top of "virtual machines" | Portability |
|  | Class | Class, object | Is an instance of, shares access methods of | In object oriented design systems, factoring out commonality, planning extensions of functionality | Modifiability, extensibility |
|  | Data Model | Data entitiy | [one, many]-to-[one, many], generalizes, specializes | Engineering global data structures for consistency and performance | Modifiability, performance |
| **C&C Structures** | Service | Service, ESB, registry, others | Runs concurrently with, may run concurrently with, excludes, precedes, etc. | Scheduling analysis, performance analysis | Interoperability, modifiability |
|  | Concurrency | Process, threads | Can run in parallel | Identifying locations where resource connection exists, or where threads may form, join, be created, or be killed | Performance, availability |
| **Allocation Structures** | Deployment | Components, hardware elements | Allocated to, migrates to | Performance, availability, security analysis | Performance, security, availability |
|  | Implementation | Modules, file structure | Stored in | Configuration control, integration, test activities | Development efficiency |
|  | Work assignment | Modules, organizational units | Assigned to | Project management, best use of expertise and available resources, management of commonality | Developer efficiency |
