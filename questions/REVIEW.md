# Review: 24 new questions

Drafted by Claude Opus 5.5 on 2026-11-02 from `rail-regulation-rag` at commit `96ccee4`. Each question below shows its gold passage exactly as the generators will see it.

**For each one, tick a box and add a note if needed:**
1. Is the question answerable from the passage alone?
2. Is the reference answer correct and complete, with numbers exactly as in the passage?
3. Is the gold passage id right?

The 16 existing questions (`q01`–`q16`) were already reviewed in the rail repo (`eval/GOLDEN_SET_REVIEW.md`) and are not repeated here.

Edit this file directly: change `[ ]` to `[x]`, and write in **Note** anything to fix. About 1 minute per question, so roughly 25–30 minutes in total.

## n01 · `tsi-ccs`

**Question:** How far in advance must a Member State notify a national rule that allows only ETCS-equipped vehicles on ETCS-equipped lines, and can that period be shorter?

**Reference answer:** At least 5 years before the decommissioning. A shorter period is allowed if it is agreed between the infrastructure manager and the railway undertakings that run or intend to run services on these lines. The notification is made within the RINF and listed in the Network Statement. The 5-year period does not apply to such requirements announced in the Network Statement before the Regulation entered into force.

**Gold passage:** `tsi-ccs:Annex I §7.4.3#1`

```
CCS TSI, 7.4.3. National requirements
7.4.3.1. Member States may introduce additional requirements at national level, in particular with a view to allowing only ETCS-equipped vehicles to access ETCS-equipped lines, so that existing national systems can be decommissioned; This shall be notified a minimum 5 years before the decommissioning. A shorter period is allowed if this is agreed between the IM and the RUs who run or intend to run (at the time of establishing the agreement) services on these lines. This notification shall be done within the RINF and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU ( 36 ). The 5-year notification period does not apply to those requirements allowing only ETCS-equipped vehicles to access ETCS-equipped lines, which were announced in the Network Statement before the entry into force of this Regulation.
7.4.3.2. Member States may decide to exclude special vehicles as defined in point 2.2.2 (C) of the LOC&PAS TSI, including road-rail vehicles, from the obligation to equip them with ETCS, RMR or ATO on a specific area of use if the operation of these vehicles does not prevent the Class B decommissioning. This shall be registered in RINF ( 37 ).
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n02 · `tsi-ccs`

**Question:** Which track gauges does the CCS TSI apply to, and which lines are excluded?

**Reference answer:** Networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges. It does not apply to short border crossing lines with 1 520 mm track gauge that are connected to the network of third countries.

**Gold passage:** `tsi-ccs:Annex I §1.2#1`

```
CCS TSI, 1.2. Geographical Scope
The geographical scope of this TSI is the network of the whole rail system, as described in point 1 of Annex I to Directive (EU) 2016/797 and excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797.
The TSI shall apply to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges. However, it shall not apply to short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n03 · `tsi-ccs`

**Question:** In a national implementation plan, how much advance notice must railway undertakings get of new mandatory on-board CCS requirements?

**Reference answer:** At least 5 years. Notifications to railway undertakings must be provided at least 5 years in advance, and the date of application of a new on-board requirement requires, at the earliest, a 5-year period.

**Gold passage:** `tsi-ccs:Appendix H §6#1`

```
CCS TSI, 6. NEW MANDATORY ON-BOARD REQUIREMENTS
[This section shall include information of new mandatory onboard requirements that will be required for operating on the network, ensuring that notifications to RUs are provided at least 5 years in advance.
The template to be filled in to provide the information in this section is given below]
[If relevant, include here an explanatory text in relation to new mandatory onboard requirements that will be required for operating on the network.]
Table 16
New mandatory on-board requirements
Geographical scope | New CCS on-board requirements | Date of application
[Include here the geographical scope in which the specific requirements will be applicable. For example: Complete network or specific lines. | [Include here the legal reference to the new CCS on-board requirements or specify here the new CCS onboard requirements | [Include here date of application of the new CCS on-board requirement. At the earliest, a 5-year period is required.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n04 · `tsi-ccs`

**Question:** When may a Member State leave out the GSM-R decommissioning section of its national implementation plan?

**Reference answer:** When it does not foresee GSM-R decommissioning in the next 20 years. Otherwise the section must include a network map with the dates when GSM-R radio operation is no longer allowed and, if different, the dates when the GSM-R system is taken out of service.

**Gold passage:** `tsi-ccs:Appendix H §5.2.4#1`

```
CCS TSI, 5.2.4. Decommissioning of GSM-R
[This section shall include a network map providing an overview with dates when GSM-R radio operation is not allowed anymore. If not similar, this section shall also include a network map providing an overview with dates where GSM-R system is taken out of service.
This section is not mandatory for those Member States which do not foresee GSM-R decommissioning in the next 20 years.
The template to be filled in to provide the information in this section is given below]
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n05 · `tsi-ccs`

**Question:** How many years ahead must the train detection planning table in a national implementation plan cover?

**Reference answer:** 20 years. For each line, the table gives the planning dates of TSI-compliant train detection deployment and must provide the complete information on changes in the following 20 years. The section must also describe the deployment strategy.

**Gold passage:** `tsi-ccs:Appendix H §3.4#1`

```
CCS TSI, 3.4. Technical migration strategy for Train Detection part
[This section shall include information and planning of the technical migration strategy of TSI compliant train detection part.
For completeness at least the following information shall be included:
— Deployment strategy. Information on the migration to the TSI compliant train detection system.
— Table which includes for each line the planning dates of TSI compliant train detection system deployment and other relevant information. The table shall provide the complete information of changes in the following 20 years.
The template to be filled in to provide the information in this section is given below]
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n06 · `tsi-ene`

**Question:** What contact wire heights does the ENE TSI set for lines with speeds of 250 km/h or more?

**Reference answer:** A nominal contact wire height between 5 080 and 5 300 mm, a minimum design contact wire height of 5 080 mm and a maximum design contact wire height of 5 300 mm.

**Gold passage:** `tsi-ene:Annex §4.2.9.1#1`

```
ENE TSI, 4.2.9.1. Contact wire height
(1) The permissible data for contact wire height is given in Table 4.2.9.1. Table 4.2.9.1 Contact wire height Description | v ≥ 250 [km/h] | v < 250 [km/h] Nominal contact wire height [mm] | Between 5 080 and 5 300 | Between 5 000 and 5 750 Minimum design contact wire height [mm] | 5 080 | In accordance with the specification referenced in Appendix E, Index [3] depending on the chosen gauge Maximum design contact wire height [mm] | 5 300 | 6 200 (1) (1) Taking into account tolerances and uplift in accordance with the specification referenced in Appendix E, Index [3], the maximum contact wire height shall not be greater than 6 500 mm.
(2) For the relation between the contact wire heights and pantograph working heights see the specification referenced in Appendix E, Index [3].
(3) At level crossings, the contact wire height shall be specified by national rules or in the absence of national rules, in accordance with the specification referenced in Appendix E, Index [4].
(4) For the track gauge system 1 520 and 1 524 mm the values for contact wire height are as follows: (a) Nominal contact wire height: between 6 000 mm and 6 300 mm; (b) Minimum design contact wire height: 5 550 mm; (c) Maximum design contact wire height: 6 800 mm.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n07 · `tsi-ene`

**Question:** What is the maximum lateral deviation of the contact wire under crosswind for a 1 600 mm pantograph and for a 1 950 mm pantograph?

**Reference answer:** 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph, measured in relation to the track centre line. The values must be adjusted for pantograph movement and track tolerances according to Appendix D.1.4.

**Gold passage:** `tsi-ene:Annex §4.2.9.2#1`

```
ENE TSI, 4.2.9.2. Maximum lateral deviation
(1) The maximum lateral deviation of the contact wire in relation to the track centre line under action of crosswind shall be in accordance with the specification referenced in Appendix E, Index [2]. Table 4.2.9.2 Maximum lateral deviation depending on the pantograph length Pantograph length [mm] | Maximum lateral deviation [mm] 1 600 | 400 (1) 1 950 | 550 (1) (1) The values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4.
(2) In the case of the multi-rail track, the requirement for lateral deviation shall be fulfilled for each pair of rails (designed, to be operated as a separated track) that is intended to be assessed against TSI.
(3) Track gauge system 1 520 mm: For Member States applying the pantograph profile in accordance with point 4.2.8.2.9.2.3 of the LOC&PAS TSI the maximum lateral deviation of the contact wire in relation to the pantograph centre under action of a crosswind shall be 500 mm.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n08 · `tsi-ene`

**Question:** Up to what speed do the mean contact force curves of the ENE TSI apply, and what applies above it?

**Reference answer:** Up to 360 km/h. For speeds above 360 km/h the procedures in point 6.1.3 apply. Overhead contact lines must be designed to sustain the upper design limit of the mean contact force Fm.

**Gold passage:** `tsi-ene:Annex §4.2.11#1`

```
ENE TSI, 4.2.11. Mean contact force
(1) The mean contact force Fm is the statistical mean value of the contact force. Fm is formed by the static, dynamic and aerodynamic components of the pantograph contact force.
(2) The ranges of Fm for each of the traction power supply systems are defined in the specification referenced in Appendix E, Index [2].
(3) The overhead contact lines shall be designed to be capable to sustain the upper design limit of Fm given in the specification referenced in Appendix E, Index [2].
(4) The curves apply to speed up to 360 km/h. For speeds above 360 km/h procedures set out in point 6.1.3 shall apply.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n09 · `tsi-ene`

**Question:** On lines for 250 km/h or more, how long must a phase separation neutral section be when all pantographs of the longest train are inside it?

**Reference answer:** At least 402 m. The alternative design, a shorter phase separation with three insulated overlaps, has a neutral section of less than 142 m including clearances and tolerances.

**Gold passage:** `tsi-ene:Annex §4.2.15.2#1`

```
ENE TSI, 4.2.15.2. Lines with speed v ≥ 250 km/h
Two types of design of phase separation sections may be adopted:
(a) a phase separation design where all the pantographs of the longest TSI compliant trains are within the neutral section. The overall length of the neutral section shall be at least 402 m. For detailed requirements see the specification referenced in Appendix E, Index [2];
(b) a shorter phase separation with three insulated overlaps as shown in the specification referenced in Appendix E, Index [2]. The overall length of the neutral section is less than 142 m including clearances and tolerances.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n10 · `tsi-ene`

**Question:** Which parts of the energy subsystem may enter the pantograph gauge?

**Reference answer:** Only the contact wire and the steady arm. No other part of the energy subsystem shall enter the pantograph gauge.

**Gold passage:** `tsi-ene:Annex §4.2.10#1`

```
ENE TSI, 4.2.10. Pantograph gauge
(1) Track gauge system other than 1 520 mm:
The mechanical kinematic pantograph gauge shall be specified using the method given in the specification referenced in Appendix E, Index [2] to this TSI and the pantograph profiles defined in LOC&PAS TSI, clauses 4.2.8.2.9.2.1 and 4.2.8.2.9.2.2.
(2) Track gauge system 1 520 mm:
For Member States applying the pantograph profile in accordance with LOC&PAS TSI, clause 4.2.8.2.9.2.3, the static gauge available for pantograph is defined in Appendix D to this TSI.
(3) No part of the energy sub-system shall enter the pantograph gauge as stated in points (1) and (2), except for the contact wire and steady arm.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n11 · `tsi-prm`

**Question:** On a platform, what is the minimum distance from an obstacle to the danger area, for small and for large obstacles?

**Reference answer:** 80 cm for a small obstacle (less than 1 m long, measured parallel to the platform edge) and 120 cm for a large obstacle (1 m to less than 10 m). Two small obstacles less than 2,4 m apart count as one large obstacle. Signalling and safety equipment is not considered an obstacle.

**Gold passage:** `tsi-prm:Annex §4.2.1.12#2`

```
PRM TSI, 4.2.1.12. Platform width and edge of platform
(4) It is permitted to have obstacles inside this freeway of 160 cm. Equipment required for the signalling system and safety equipment shall not be considered as obstacles in this point. The minimum distance from obstacles to the danger area shall be according to the following table: Table 4 Minimum distance from obstacles to the danger area Length of obstacles (measured parallel to the platform edge) | Minimum distance to the danger area < 1 m (note 1) — small obstacle | 80 cm 1 m to < 10 m — large obstacle | 120 cm Note 1: if the distance between two small obstacles is less than 2,4 m measured parallel to the platform edge they shall be considered as one large obstacle. Note 2: Within this minimum distance from a large obstacle to the danger area it is permitted to have additional small obstacles as long as the requirements for small obstacles (minimum distance to danger area and minimum distance to next small obstacle) are met.
(6) The boundary of the danger area, furthest from the rail side edge of the platform, shall have a visual marking and tactile walking surface indicators.
(7) The visual marking shall be a contrasting, slip resistant, warning line with a minimum width of 10 cm.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n12 · `tsi-prm`

**Question:** What maximum height and minimum depth must internal steps in a passenger vehicle have?

**Reference answer:** A maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs. For double-deck trains the depth may be reduced to 270 mm for the stairs accessing the upper and lower deck.

**Gold passage:** `tsi-prm:Annex §4.2.2.8#1`

```
PRM TSI, 4.2.2.8. Height changes
(1) Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs. For double deck trains it is permitted to reduce this value to 270 mm for the stairs accessing the upper deck and the lower deck.
(2) As a minimum, the first and the last steps shall be indicated by a contrasting band extending the full width of the steps on both the front and the top surfaces of the step nosing with a depth of: — 45 mm to 55 mm on the front surface, — 45 mm to 75 mm on the top surface.
(3) Stairs constituted of more than three steps shall be provided with handrails on both sides and at two levels. The higher handrail shall be positioned at a height of 850 mm to 1 000 mm above floor level. The lower handrail shall be positioned at a height of 500 mm to 750 mm above floor level.
(4) Stairs constituted of one, two or three steps shall be provided on both sides with a minimum of one handrail or other item that can be used for personal stability.
(5) Handrails shall be compliant with point 4.2.2.9
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n13 · `tsi-prm`

**Question:** What minimum size and load must a baby nappy changing table on a train have?

**Reference answer:** A usable surface at least 500 mm wide and 700 mm long, and a minimum load of 80 kg. It must be possible to stow it with one hand using a force not exceeding 25 N.

**Gold passage:** `tsi-prm:Annex §5.3.2.5#1`

```
PRM TSI, 5.3.2.5. Baby nappy changing table
(1) The usable surface of the baby nappy changing table shall be a minimum of 500 mm wide and 700 mm long.
(2) It shall be designed to prevent a baby from inadvertently sliding off, shall have no sharp edges and shall be able to take a minimum load of 80 kg.
(3) It shall be possible to put it into the stowed position with only one hand, using a force not exceeding 25 N.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n14 · `tsi-prm`

**Question:** What diameter must handrails in a passenger vehicle have, and how much clearance from adjacent surfaces?

**Reference answer:** Round in section with an outside diameter of 30 mm to 40 mm, and a minimum clear distance of 45 mm to any adjacent surface other than its mountings. A curved handrail needs an inside radius of at least 50 mm.

**Gold passage:** `tsi-prm:Annex §4.2.2.9#1`

```
PRM TSI, 4.2.2.9. Handrails
(1) All handrails fitted to a vehicle shall be round in section with an outside diameter of 30 mm to 40 mm, and shall have a minimum clear distance of 45 mm to any adjacent surface other than its mountings.
(2) If a handrail is curved, the radius to the inside face of the curve shall be a minimum of 50 mm.
(3) All handrails shall contrast with their background.
(4) External doorways shall be provided with handrails on both sides, fitted internally as close as practicable to the vehicle outer wall. Exception can be made for one side of the doorway if it is fitted with a device such as an on-board lift.
(5) The handrails referred to in point (4) shall be: — vertical handrails that shall extend from 700 mm to 1 200 mm above the threshold of the first step for all external doorways; — additional handrails at a height of between 800 mm and 900 mm above the first useable step and parallel with the line of the step nosing for doorways with more than two entrance steps.
(6) Where the clearway of the gangway is narrower than 1 000 mm and longer than 2 000 mm there shall be handrails or handholds provided in, or adjacent to, inter-vehicle gangways that are provided for passenger use.
(7) Where the clearway of the gangway is wider than or equal to 1 000 mm handrails or handholds shall be provided in the gangway.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n15 · `tsi-noi`

**Question:** What are the noise limits in the driver's cab at standstill with horns sounding, and at maximum speed below 250 km/h?

**Reference answer:** 95 dB at standstill with horns sounding and 78 dB at maximum speed when vmax < 250 km/h (LpAeq,T, near the driver's ear). The limits are not mandatory for special vehicles, but the conformity test must still be performed and the values recorded in the technical file.

**Gold passage:** `tsi-noi:Annex §4.2.4#1`

```
NOI TSI, 4.2.4. Limits for the driver's cab interior noise
The limit values for the A-weighted equivalent continuous sound pressure level (LpAeq,T) concerning the noise within the driver's cab of electric and diesel locomotives, EMUs, DMUs and coaches fitted with a cab are set out in Table 5. The limit values are set in the vicinity of the driver's ear.
These limit values are not mandatory for special vehicles. However, the demonstration of conformity referred to in point 6.2.2.4 shall be performed and the resulting values shall be recorded in the technical file.
Table 5
Limit values for driver's cab interior noise
Noise within the driver's cab | LpAeq,T [dB]
At standstill with horns sounding | 95
At maximum speed vmax if vmax < 250 km/h | 78
At maximum speed vmax if 250 km/h ≤ vmax < 350 km/h | 80
The demonstration of conformity is described in point 6.2.2.4.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n16 · `tsi-noi`

**Question:** In the starting noise conformity test, up to what speed must the train accelerate?

**Reference answer:** From standstill up to 30 km/h, then maintain that speed, using the maximum level method. An additional measurement accelerating up to 40 km/h is recorded and sent to the Agency but not assessed against a limit.

**Gold passage:** `tsi-noi:Annex §6.2.2.2#1`

```
NOI TSI, 6.2.2.2. Starting noise
The demonstration of conformity with the limit values on starting noise as set out in point 4.2.2 shall be carried out in accordance with the specification referenced in Appendix B, Index [1]. The maximum level method shall apply. Deviating from the test procedure of the specification, the train shall accelerate from standstill up to 30 km/h and then maintain the speed.
In addition the noise shall be measured at the same distance from the centre of the track and the same height above top of rail as set out in point 4.2.2. The ‘averaged level method’ and the ‘maximum level method’ in accordance with the specification referenced in Appendix B, Index [1] shall apply and the train shall accelerate from standstill up to 40 km/h and then maintain the speed. The measured values are not assessed against any limit value and shall be recorded in the technical file and communicated to the Agency.
For special vehicles the starting procedure shall be performed without additional trailer loads.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n17 · `tsi-noi`

**Question:** What counts as a 'quieter route' under the NOI TSI?

**Reference answer:** A part of the railway infrastructure at least 20 km long on which the average number of daily freight trains at night was higher than 12, based on freight traffic in 2015, 2016 and 2017. If exceptional circumstances made one year diverge by more than 25 %, the Member State can use the remaining two years.

**Gold passage:** `tsi-noi:Article 5b#1`

```
NOI TSI, Article 5b
A ‘quieter route’ means a part of the railway infrastructure with a minimum length of 20 km on which the average number of daily operated freight trains during the night-time as defined in national legislation transposing Directive 2002/49/EC of the European Parliament and of the Council ( 5 ) was higher than 12. The freight traffic in the years 2015, 2016 and 2017 shall be the basis for the calculation of that average number. In case the freight traffic due to exceptional circumstances diverges in a given year from that average number by more than 25 %, the Member State concerned can calculate the average number on the basis of the remaining two years.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n18 · `tsi-ope`

**Question:** How often must staff doing safety-critical tasks have a periodic medical examination under the OPE TSI?

**Reference answer:** At least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62. The medical doctor sets a higher frequency if the person's state of health requires it.

**Gold passage:** `tsi-ope:Annex §4.7.2.2.1#1`

```
OPE TSI, 4.7.2.2.1. Frequency of periodic medical examinations
At least one systematic medical examination shall be performed:
— Every 5 years for staff aged up to 40;
— Every 3 years for staff aged between 41 and 62;
— Every year for staff aged over 62.
Increased frequency of examination shall be set by the medical doctor if the state of health of the member of the staff requires so.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n19 · `tsi-ope`

**Question:** When should a driver avoid using manually activated sanding equipment, and when is sanding still appropriate there?

**Reference answer:** The driver is always allowed to apply sand but should avoid it in the area of points and crossings, during braking at speeds less than 20 km/h, and at standstill. The exceptions are a risk of SPAD or another serious incident where sand would help adhesion, starting away, and testing the sanding equipment.

**Gold passage:** `tsi-ope:Appendix B §1#1`

```
OPE TSI, 1. SANDING
If the train is equipped with manually activated sanding equipment, the driver shall always be allowed to apply sand but shall avoid it wherever possible:
— in the area of points and crossings,
— during braking at speeds less than 20 km/h,
— when at standstill.
The exceptions to this are:
— if there is a risk of SPAD (Signal Passed At Danger), or other serious incident and the application of sand would assist adhesion,
— when starting away,
— when required to test the sanding equipment on the traction unit.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n20 · `tsi-ope`

**Question:** For trains able to run faster than 200 km/h, what braking information may the infrastructure manager provide?

**Reference answer:** The deceleration profile and the equivalent response time on level track. If the infrastructure manager provides it, the information must be made available in a non-discriminatory way to all railway undertakings that intend to operate trains on its network.

**Gold passage:** `tsi-ope:Annex §4.2.2.6.2#2`

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(2) The infrastructure manager may provide the following information: (i) For trains able to run at a maximum speed higher than 200 km/h, deceleration profile and equivalent response time on level track; (ii) For trainsets or for fixed train compositions, unable to run at a maximum speed higher than 200 km/h, deceleration (as above in (i)) or brake weight percentage; (iii) For other trains (variable compositions of trains unable to run at a maximum speed higher than 200 km/h): brake weight percentage. If the infrastructure manager provides the above mentioned information, it shall be made available to all railway undertakings who intend to operate trains on its network in a non-discriminatory way. The braking tables already in use and accepted for the existing non TSI conform lines at the date of entry into force of the present Regulation shall also be made available.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n21 · `iop-directive`

**Question:** After the Commission mandates it, how quickly must the Agency start consulting the parties about a Member State's measure against a non-compliant interoperability constituent?

**Reference answer:** Without delay and in any case within 20 days of receiving the mandate. If the Agency finds the measure unjustified, it informs the Commission, the Member States and the manufacturer; if justified, it informs the Member States.

**Gold passage:** `iop-directive:Article 11#1`

```
Interoperability Directive, Article 11 — Non-compliance of interoperability constituents with essential requirements
1. Where a Member State finds that an interoperability constituent covered by the ‘EC’ declaration of conformity or suitability for use and placed on the market is, when used as intended, unlikely to meet the essential requirements, that Member State shall take all necessary steps to restrict its field of application, prohibit its use, withdraw it from the market or recall it. The Member State shall forthwith inform the Commission, the Agency and the other Member States of the measures taken and give reasons for its decision, stating in particular whether the failure to conform is due to: (a) failure to meet the essential requirements; (b) incorrect application of European specifications where application of such specifications is relied upon; (c) inadequacy of European specifications.
2. The Agency, on a mandate from the Commission, shall start the consultation process with the parties concerned without delay and in any case within 20 days of the date of receipt of that mandate. Where, following that consultation, the Agency establishes that the measure is unjustified, it shall forthwith inform the Commission, the Member State that has taken the initiative as well as other Member States, and the manufacturer or his authorised representative. Where the Agency establishes that the measure is justified, it shall forthwith inform the Member States.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n22 · `iop-directive`

**Question:** What speeds characterise specially built and specially upgraded high-speed lines in the Union's network?

**Reference answer:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h. Specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h.

**Gold passage:** `iop-directive:Annex I §1#1`

```
Interoperability Directive, 1. Network
For the purposes of this Directive, the Union's network shall include the following elements:
(a) specially built high-speed lines equipped for speeds generally equal to or greater than 250 km/h;
(b) specially upgraded high-speed lines equipped for speeds of the order of 200 km/h;
(c) specially upgraded high-speed lines which have special features as a result of topographical, relief or town-planning constraints, to which the speed must be adapted in each case. This category includes interconnecting lines between high-speed and conventional networks, lines through stations, accesses to terminals, depots, etc. travelled at conventional speed by ‘high-speed’ rolling stock;
(d) conventional lines intended for passenger services;
(e) conventional lines intended for mixed traffic (passengers and freight);
(f) conventional lines intended for freight services;
(g) passenger hubs;
(h) freight hubs, including intermodal terminals;
(i) lines connecting the abovementioned elements.
This network includes traffic management, tracking and navigation systems, technical installations for data processing and telecommunications intended for long-distance passenger services and freight services on the network in order to guarantee the safe and harmonious operation of the network and efficient traffic management.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n23 · `tsi-srt`

**Question:** What exercise is required before a railway tunnel longer than 1 km opens?

**Reference answer:** A full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined in the emergency plan. The emergency plan must also define how often tunnel visits and table top or other exercises take place.

**Gold passage:** `tsi-srt:Annex §4.4.3#1`

```
SRT TSI, 4.4.3. Exercises
These rules apply to tunnels of > 1 km.
(a) Prior to the opening of a single tunnel or a series of tunnels, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, shall take place.
(b) The emergency plan shall define how all organisations involved can be familiarised with the infrastructure and how often visits to the tunnel and table top or other exercises have to take place.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 

## n24 · `tsi-srt`

**Question:** In a tunnel longer than 1 km where the traction power supply is divided into sections, what must be possible?

**Reference answer:** It must be possible to switch off each section of the contact line, either locally or remotely.

**Gold passage:** `tsi-srt:Annex §4.2.2.1#1`

```
SRT TSI, 4.2.2.1. Sectioning of contact line
This specification applies to all tunnels of more than 1 km length.
(a) The traction power supply system in tunnels may be divided into sections.
(b) In such case, it shall be possible to switch off each section of the contact line, either locally or remotely.
```

- [ ] Accept  - [ ] Fix (see note)  - [ ] Drop

**Note:** 
