# Bluegrass Bourboneering

<img src="https://drive.google.com/uc?id=1oQuheRkFOL64rvbM9qzdP56SvoMj8LRU" width="300" height="300" />

---

#### Contents

---

- [Contents](#contents)
- [Outline](#outline)
- [HMI](#hmi)
- [Formula](#formula)
- [References](#references)

---

#### Outline

---

In this repository you will find the following five (5) folders:

- Code
  - Contains the `Formula.py` file.
- Ignition
  - Contains the `HMI_Project_File.zip` and `HMI_Tags_File.json` files.
- PLC
  - Contains the `Ladder_Logic.RSS` and `PLC_Manual.pdf` files.
- Tables
  - Contains the `Table.xlsx` file.
- Report
  - Contains the `Preliminary Design Report` file.

---

#### HMI

---

Below you can see an the user interface for the HMI that we designed:

<img src="https://drive.google.com/uc?id=1Ufp0NE1xe6AiPzD1Nsf4SmHjdJsPIKwD"/>

---

#### Formula

---

Below you can see how we derived the formula:

<img src="https://drive.google.com/uc?id=1sPxHn8uyZLDgfVH-GAzdiXTOVsM-KTft"/>

The first three steps show how volume can be modified into weight, which is one of the knowns of the algorithm.

<img src="https://drive.google.com/uc?id=1KepbXnmoloDk5zB4mjkPwMxA_wIYJ5p1"/>

Step four is an equation that was found to represent how the desired Alcohol by Volume (Proof/2) can be found mathematically, with a diluent. ABVf is the alcohol by volume desired, VB is the volume of bourbon, ABV0 is the out-of-barrel proof of the bourbon, VRO is the volume of the RO water to be added.

<img src="https://drive.google.com/uc?id=1OXTr-YY7GgWt-qj1eUvyszUmTlsMPHr8"/>

 In step five, the respective volumes are replaced by equation 3, with similar naming usage.  For this case, since weight is in lbs, g must be 32.2 ft/s^2, and the densities (ρ) are given in lbs/gal.

<img src="https://drive.google.com/uc?id=1_7sTAn5MnKVqoppDp7BEMeki5Z3Zyl3-"/>

Steps 6-9 are algebraic manipulations to equation 5 that result in a RO water weight that can be added to the bourbon to reach the desired proof.


---

#### References

---

1) “Bourbon Facts - Kentucky Distillers Association”,  Kentucky Distillers Association. [Online]. Available: https://kybourbon.com/bourbon_culture-2/key_bourbon_facts/. [Accessed 27 September 2020].

2) M. Fort, “How to calculate percentage of alcohol content in cocktails?,” Conscious Mixology, 19-Mar-2017. [Online]. Available: http://www.consciousmixology.com/how-to-calculate-percentage-of-alcohol-content-in-cocktails/. [Accessed: 04-Nov-2020]. 

3) T. Bugher, “TTB: Gauging Manual,” TTBGov - Distilled Spirits. [Online]. Available: https://www.ttb.gov/foia/distilled-spirits-gauging-manual. [Accessed: 04-Nov-2020].

4) Literature.rockwellautomation.com. 2020. [online] Available at: <https://literature.rockwellautomation.com/idc/groups/literature/documents/td/520-td001_-en-e.pdf> [Accessed 4 November 2020].

5) PRM Filtration. 2020. Solenoid Valve, 2 Inch Cast Iron, 24 VDC, Normally Closed, Flanged Connection With Viton Seals. [online] Available at: <https://shop.prmfiltration.com/collections/cast-iron-solenoid-valves/products/cast-iron-solenoid-valves-24vdc-normally-closed-flanged-with-viton-seals> [Accessed 4 November 2020].

6) “Ladder Logic Basics”, Ladder Logic World. [Online]. Available: “https://ladderlogicworld.com/ladder-logic-basics/. [Accessed 11 November 2020].

7) “OMEGA Engineering,” Omega Engineering. [Online]. Available: https://www.omega.co.uk/prodinfo/load-cells.html. [Accessed: 04-Nov-2020]. 

8) P. by John, “Search for ‘load cell’ - Instrumentation-Electronics,” Instrumentation. [Online]. Available: http://www.instrumentationtoday.com/?s=load+cell. [Accessed: 04-Nov-2020]. 

9) D. Trent and With Load Cell Central since 2017, “Strain Gauge Load Cell Basics,” How Does a Strain Gauge Load Cell Work? | Load Cell Central. [Online]. Available: https://www.800loadcel.com/load-cell-and-strain-gauge-basics.html. [Accessed: 04-Nov-2020]. 

10) “What is a Pancake Load Cell?,” ATO. [Online]. Available: https://www.ato.com/what-is-a-pancake-load-cell. [Accessed: 04-Nov-2020]. 

11) “Load Cells - Canister,” Canister Load Cells | Compression, Tension, High Capacity. [Online]. Available: https://www.centralcarolinascale.com/Compression-Canister.htm. [Accessed: 04-Nov-2020]. 

12) “Tension/Compression Load Cell, Low Profile, 500kg/30 ton to 100 ton,” ATO.com. [Online]. Available: https://www.ato.com/compression-load-cell-low-profile-200kg-to-100-ton. [Accessed: 04-Nov-2020]. 

13) “Model SPWE: Low-Profile Vessel Weighing Load Cell,” Low-Profile Vessel Weighing Load Cell | Tank and Hopper Scales | Load Cell Central. [Online]. Available: https://www.800loadcel.com/load-cells/pancake-shear-web-load-cells/spwe.html. [Accessed: 04-Nov-2020]. 

14) “CG-21,” Coti Global. [Online]. Available: https://www.cotiglobal.com/cg-21/. [Accessed: 04-Nov-2020]. 

15) “Universal Pancake Load Cell,” Universal Pancake Load Cell LCF500 : QSH01956. [Online]. Available: https://www.futek.com/store/load-cells/universal-pancake-load-cells/universal-pancake-LCF500/QSH01956. [Accessed: 18-Nov-2020]. 

16) “Omega Engineering,” Ultra Low Profile, Tension and Compression Load Cells. [Online]. Available: https://www.omega.com/en-us/force-strain-measurement/load-cells/lchd/p/LCHD-20K. [Accessed: 18-Nov-2020].

17) “Load Cell Junction Box Signal Trim,” Load Cell Junction Box Signal Trim | Load Cell Central. [Online]. Available: https://www.800loadcel.com/load-cell-hardware/j-boxes.html. [Accessed: 18-Nov-2020]. 

18) “Model TLM8 Load Cell Transmitter,” Load cell transmitter with analog, digital, and relay outputs. Ethernet & fieldbus options available. | Load Cell Central. [Online]. Available: https://www.800loadcel.com/electronics/signal-conditioners/tlm8.html. [Accessed: 18-Nov-2020].

19) D. Kalyanaraman, “Industrial flow meters/flow transmitters,” Analog Applications Journal, no. 2Q, pp. 28–32, 2012.

20) Bronkhorst. [Online]. Available: https://www.bronkhorst.com/en-us/products-en/liquid-flow/mini-cori-flow/m14/. [Accessed: 03-Nov-2020]. 

21) Endress+Hauser. [Online]. Available: https://portal.endress.com/wa001/dla/5001121/0154/000/06/TI01287DEN_0719.pdf. [Accessed: 03-Nov-2020].

22) Emerson. [Online]. Available: https://www.emerson.com/en-us/catalog/micro-motion-sku-cmf200m?fetchFacets=true#facet:&partsFacet:&facetLimit:&productBeginIndex:0&partsBeginIndex:0&orderBy:&partsOrderBy:&pageView:list&minPrice:&maxPrice:&pageSize:&. [Accessed: 03-Nov-2020].

23) “Inline density meter: L‑Dens 7000 series,” Anton Paar. [Online]. Available:     https://www.anton-paar.com/us-en/products/details/l-dens-7000-density-sensor-series/?ref=adwords. [Accessed: 17-Nov-2020]. 

24) Software, E. and 5, D., 2020. Data Recording Software: DAVIS 5 :: Anton-Paar.Com. [online] Anton Paar. Available at: <https://www.anton-paar.com/us-en/products/details/davis-5-software-for-the-recording-storing-visualization-and-analysis-of-measured-data/> [Accessed 4 November 2020].

---

[*back to top*](#bluegrass-bourboneering)
