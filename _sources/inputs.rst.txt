More information about the following inputs can be found in Section A4.3 “Downtime Assessment Methodology” in the `REDi guidelines <https://www.redi.arup.com>`_. As a reference, an example building input file is provided in the examples folder of the repository: ``REDi/examples/example_building.json``. Note that the building input file is required to be in the json format. 

A high-level summary of REDi inputs is: 

- **_id** - a unique name that can be employed to identify the building
- **nFloor** - number of floors or stories in the building (excluding the roof), e.g., 4
- **replacement_cost** - building replacement cost in millions of dollars, e.g, 5.25
- **replacement_time** - building replacement time in days, e.g., 1240
- **risk_parameters** - dictionary of various input parameters that define repair resources and scheduling (explained in further detail below)
- **components** - list of building components that identify the component type and quantity (explained in further detail below)
- **floor_areas** - list of the floor areas, including the roof, e.g., if **nFloor** = 5, the **floor_areas** list should have 6 items when the roof area is included. Each item in the list is the area for that floor in square feet.
- **component_damage** - dictionary of components where each key is a component id and the corresponding value provides quantities of the damaged components (explained in further detail here)
- **total_consequences** - dictionary of components where each key is a component id and the corresponding value provides quantities of the consequences, e.g., repair time and cost (explained in further detail below)


Risk parameters
---------------

This section highlights the various "risk parameters" that are employed as inputs into the REDi engine. Note that some of the risk parameters are defined as random variables while some are constants. Broadly speaking, the risk parameters are grouped into 3 types: 1) repair; 2) impeding_factors; and 3) business. 

1. Repair risk parameters

   The "repair" risk parameters are related to the physical repair processes. Examples include the number of repair workers, the severity of the repair, and possible repair sequences. 

   The required repair risk parameters include: 
   
   - **repair_class_fragility** - dictionary containing the random variable distribution parameters for the repair class fragility function. “Repair Classes” describe how the extent and severity of damage to types of building components may hinder specific recovery states. 
   
   .. figure:: _static/A4.3-Table3.png
      :alt: Table 3 in Section A4.3 from REDi Downtime Assessment Methodology
      :scale: 60%
      :align: center
      :class: image-caption

      Table 3 in Section A4.3 from REDi Downtime Assessment Methodology.

   - **nwork_perfloor_divider** - list containing the number of workers per floor, for each non-structural repair sequence. The **nwork_perfloor_divider** will always contain 7 items (the number of non-structural repair sequences).
   - **nworkers_recommended_mean** - list that describes the mean number of recommended workers, for each non-structural repair sequence. The **nworkers_recommended_mean** will always contain 7 items (the number of non-structural repair sequences).
   - **nworkers_recommended_mean_struct** - mean number of recommended workers for the structural repair sequence. Since there is only one structural repair sequences, the **nworkers_recommended_mean_struct** will be a single number.
   - **max_workers_per_building** - a dictionary containing parameters that define a function to calculate the mean and sigma of a probability distribution as follows in the function ``get_max_workers`` from the file ``go_redi.py``
   
   .. code-block:: python

   	def get_max_workers(building : Building):
   	
   	    totalArea = building.total_floor_area
   	
   	    # Extract relevant risk parameters
   	    max_workers_minimum = building.max_workers_minimum
   	    max_workers_slope = building.max_workers_slope
   	    max_workers_x_cutoff = building.max_workers_x_cutoff
   	    max_workers_sigma = building.max_workers_sigma
   	
   	    # Calculate mean
   	    mean = max_workers_minimum + max(0, totalArea - max_workers_x_cutoff) * max_workers_slope
   	
   	    # Sample max workers
   	    return sample_dist("Normal", mean, max_workers_sigma)

   - **max_workers_per_struct_divider** - number of workers per floor for the structural repair sequence.
   - **workers_capacity** - dictionary containing the random variable distribution parameters for the worker capacity. The worker capacity is a constraint on the number of workers that can work on the same type of component, floor, etc. 
   - **max_workers_by_sequence** - list of a list that describes the maximum workers per repair goal, per repair sequence. The highest-level list of length 3 corresponds to the 3 repair goals: 1) full recovery; 2) functional recovery; and 3) re-occupancy. The second-level list corresponds to the 7 non-structural repair sequences. A repair sequence defines the order of repairs that are to be conducted. For example, partitions can be replaced only once pipes and HVAC ducts have been repaired. Some repairs can occur simultaneously. Component repairs at a particular floor level need to be ordered in a manner that reflects the sequence of repairs that are likely to be undertaken by the contractor. The suggested repair sequences at a particular floor are presented in Figure 8 below.

   .. figure:: _static/A4.3-Figure8.png
      :alt: Figure 8 in Section A4.3 from REDi Downtime Assessment Methodology
      :scale: 50%
      :align: center
      :class: image-caption

      Figure 8 in Section A4.3 from REDi Downtime Assessment Methodology.
   
2. Impeding factors risk parameters

   The "impeding factors" risk parameters are related to potential delays in scheduling inspections, workers, and materials to site. Other impeding factors include the time that it takes to get financing for the repairs. Example values for the impeding factors can be found in A4.3 in the `REDi guidelines <https://www.redi.arup.com>`_.

   The required impeding factors parameters include:
 
   - **inspection_delay** - dictionary containing the random variable distribution parameters for the inspection delay, i.e., the delay in days of getting a municipal building inspector to inspect the repair work
   - **financing_delay** - dictionary containing the random variable distribution parameters for the delay in financing of the repair. Note that there are different parameters for delays in issuing insurance funds (default) and for private loans in the case where the repair cost is more than the insurance limit.
   - **longlead** - dictionary containing the random variable distribution parameters for the long-lead times of acquiring repair materials. There are some building components which require long procurement lead times – they are not readily available even in normal circumstances. These components include elevators, mechanical equipment, and non-standard and custom made components including structural elements, facades, mission-critical contents, etc. The long-lead times should be quantified from information provided by manufacturers, maintenance professionals, contractors, and/or cost estimators.
   - **permit_delay_seismic** - dictionary containing the random variable distribution parameters for the repair permit delays. The repair permit delays account for the time it takes to procure the required building permits from the local municipality. Note that there are different permit delay parameters for the different repair classes.
   - **contractor_mobilization_delay_seismic** - dictionary containing the random variable distribution parameters for the contractor mobilization delay. The contractor mobilization delay is the time it takes for a repair contractor to start the repair, i.e., schedule workers and account for potential shortage of workers, bidding phase for contract procurement, etc. Note that there are different contractor mobilization delay parameters for the different repair classes.
   - **engineer_mobilization_delay_seismic** - dictionary containing the random variable distribution parameters for the engineer mobilization delay. The engineer mobilization delay is the time it takes for an engineer to arrive at the site and assess the damage. An engineer would need to be consulted if there is structural damage to the building and the repair of minor structural damage (Repair Class 1) would likely require an engineer to stamp and approve the proposed repair strategy. Note that there are different engineer mobilization delay parameters for the different repair classes. Contractors and engineers will likely be in scarce supply after a major earthquake and retaining them on an annual basis to perform post-earthquake repairs could save weeks of downtime.

3. Business risk parameters

   The "business" risk parameters include stake-holder specific information that can impact the repair. Examples include whether there are sufficient funds available for repair, the fraction of the total repair cost that is insured and at what deductible, and whether any private financing will be needed to cover the difference between the total repair cost and the insured amount. The required business parameters include: 
   
   - **finance_method** - string that describes the financing method for funding the recovery and repair. The two options are ``insurance`` or ``other``.
   - **insur_limit_ratio** - fraction of the building replacement cost that is insured, e.g., 0.5
   - **loss_thresh_ratio** - fraction of the building replacement cost after which total loss occurs, e.g., 0.7. Total loss means that the total repair cost exceeds the loss threshold and no repairs occur (``sum(repair_costs)>replacement_cost*loss_thresh_ratio``). Instead, a complete redesign, reconstruction, and replacement of the entire building takes place. 
   - **available_fund_ratio** - fraction of the building replacement cost that is available for funding building repairs, e.g., 0.5
   - **deductible_ratio** - fraction of the building replacement cost that is equal to the insurance deductible, e.g., 0.2

Components
----------

The **components** object is a list of lists. The highest-level, outer list contains **nFloor** + 1 lists, where each sub-list contains all components on a particular floor (including any components on the roof). Note that index 0 corresponds to the first story, index 1 to the second story, and so on until the last index which corresponds to the roof. 

Each component in the sub-list for each floor is a dictionary containing the component tag **NISTR** and an array of quantities **Qty** in each direction, i.e., ``[dir_1, dir_2]``. The **NISTR** id corresponds to the FEMA P-58 component id in the supplied component dictionary. 
		
.. code-block:: text

	# the length of the "components" list is equal to nFloor + 1, or the number of stories plus the roof
	"components" :[floor_1, floor_2, ..., floor_n]
	
	where 
	
	# the length of the "floor_n" list is equal to the number of different components on that floor
	floor_n = [
		     {'NISTR' : nistr_id_1, # NISTR id, e.g., B1033.061b
		     'Qty' : [dir_1, dir_2]}, # component quantity in each direction, e.g.,  [11.5, 11.5]
		     ...,
		     {'NISTR' : nistr_id_n,
		     'Qty' : [dir_1, dir_2]}
		  ]

Component damage
----------------

The **component_damage** object is a dictionary where each key is a component tag **NISTR** and the values is a list of a list. The highest level, outer list is associated with the number of damage states while the inner list corresponds to the number of floors.
		
.. code-block:: text

	# the length of the "component_damage" dictionary will be equal to the number of different types of damaged components in the building
	"component_damage": {
		# the length of the "NISTR" list below is equal to the number of damage states for that particular component
		"NISTR": [
			ds_1,
			...,
			ds_n
		],
		...,
		}
		
        where 
		
		# the length of the "ds_n" list is equal to the number of floors, or **nFloor** + 1
		ds_n = [
		   num_dmg_units_floor_1, # the quantity of damaged components of the type NISTR, in damage state ds_n, on floor_n
		   num_dmg_units_floor_2, 
		   ..., 
		   num_dmg_units_floor_n
		]
		

Total consequences
------------------

The **total_consequences** object is a dictionary where each key is a component tag **NISTR** and the values are a list of lists of lists. The highest-level list (always length 4) corresponds to the 4 types of consequences at the component level: 1) repair cost [dollars]; 2) repair time [worker days]; 3) occupant injuries; and 4) occupant fatalities. The second-level list contains the number of floors, or **nFloor** + 1, so a list with length 5 will be a 4-story building with a roof. The third-level list is based on the number of damage states (not including Damage State 0, i.e., undamaged). 
		
.. code-block:: text

	# the length of the "total_consequences" dictionary will be equal to the number of the different types of damaged components in the building
	"total_consequences": {
		# the length of the "NISTR" list below is equal to the number of damage states for that particular component
		"NISTR": [
			repair_cost_list,
			repair_time_list,
			injury_list,
			fatalities_list
		],
		...,
		}
		
        where 
		
		# the length of the "repair_cost_list" list is equal to the number of floors, or **nFloor** + 1
		repair_cost_list = [
		   floor_1_list, 
		   floor_1_list, 
		   ..., 
		   floor_n_list
		]
		
		# the length of the "floor_n_list" is equal to the number of damage states in the component (not including damage state 0)
		floor_n_list = [
		   ds_1_qty, # Quantity of the consequence "repair cost", at floor_n, for ds_1 
		   ds_2_qty, 
		   ..., 
		   ds_n_qty
		]
		
