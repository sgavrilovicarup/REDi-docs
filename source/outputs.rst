
The outputs of PyREDi are provided in .json format. Each key in the dictionary is an output. 

A summary of REDi outputs is as follows:

- **building_total_downtime** - array of downtime quantities for each of the 3 repair goals. Namely, the time in days for full recovery, functional recovery, and re-occupancy:

  - The first item in the array is full recovery, whcih includes restoring the building back to its pre-damage functionality and aesthetic condition. For example, repairing cracked partitions and facades 
  - The second item in the array is represents functional recovery, or the time required to establish re-occupancy and regain the facility’s primary function. Although non-functional aesthetic elements may still be damaged, the building should be operational according to its original intent, which involves reinstating power, water, fire sprinklers, lighting, elevators, and HVAC systems.
  - The third item in the array is re-occupancy, or the time required to repair major structural damage so that the building is safe enough to be used for shelter.

  Note that re-occupancy can occur before functionality is restored. In this case lighting, heating/air-conditioning, and water may not be available.

- **component_qty** - a dictionary containing the sum of all components quantities where the key is the **NISTR** component tag and the corresponding values are the quantity of that component.
- **consequence_by_component_by_floor** - a dictionary containing lists of the consequences arranged by floor. The key is the **NISTR** component tag and the values are a list of a list. The highest-level list corresponds to the number of consequences, while the inner list corresponds to each floor. The number of consquences is always 4 (1. repair cost [dollars]; 2. repair time [worker days]; 3. occupant injuries; and 4. occupant fatalities), while the number of floors is equal to the number of stories plus the roof (**nFloor** + 1)
- **damage_by_component_all_DS** - a dictionary containing a list of the quantity of damaged components arranged by the damage state. The key is the **NISTR** component tag and the values are a list
- **impeding_delays** - a dictionary containing the delay quantities from each impeding factor. Specifically, the engineering mobilization delay, financing delay, inspection delay, structural and non-structural contractor mobilization delays, and permit delay.
- **max_delay** - the maximum delay in days of all impeding factors.
- **repair_class** - a dictionary containing the repair class of each component. The key is the **NISTR** component tag and the value is the repair class. 
- **repair_schedule** - a list of size 3 containing dictionaries of the repair schedules for the 3 repair goals, i.e., full recovery, functional recovery, and re-occupancy (explained in further detail below).

Repair schedule
---------------

The **repair_schedule** output is a list of size 3 containing dictionaries of the repair schedules for the 3 downtime states, i.e., full recovery, functional recovery, and re-occupancy. The first dictionary in the list corresponds to full recovery, the second to functional recovery, and the third to re-occupancy. 

Each dictionary contains the following information:

- **struct_repairs** - number of days to complete the structural repairs. 
- **total_span** - total span of the repair schedule in days. Note that this value will be the same as the corresponding value in the **building_total_downtime** array. 