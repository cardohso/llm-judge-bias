# Review: base answers (blinded)

You see two answers per question, X and Y, in random order. You are not told which
model wrote which. Judge each answer **against the passages shown**, as rendered below.

**Accept an answer only if all three hold:**
1. every sentence is correct and supported by the passage(s) it cites;
2. every sentence that states a fact ends with a citation marker `[n]` that exists above;
3. the sentences are split correctly (S1, S2, … as shown).

Tick `[x] Accept` or `[x] Reject` and write the reason in **Note** for each rejection.
If either answer to a question is rejected, the question is dropped for both generators
(pre-registration, section 4.4). Answers are never edited. About 40 minutes in total.

## q01

**Question:** What is the stationary noise limit LpAeq,T for an electric multiple unit (EMU)?

**[1]**

```
NOI TSI, 4.2.1. Limits for stationary noise
The limit values for the following sound pressure levels under normal vehicle conditions concerning the stationary noise allocated to the categories of the rolling stock subsystem are set out in Table 2:
(a) the A-weighted equivalent continuous sound pressure level of the unit (LpAeq,T[unit]);
(b) the A-weighted equivalent continuous sound pressure level at the nearest measuring position i considering the main air compressor (Li pAeq,T);
(c) the AF-weighted sound pressure level at the nearest measuring position i considering impulsive noise of the exhaust valve of the air dryer (Li pAFmax).
The limit values are set at a distance of 7,5 m from the centre of the track and 1,2 m above top of rail.
Table 2
Limit values for stationary noise
Category of the rolling stock subsystem | LpAeq,T[unit] [dB] | Li pAeq,T [dB] | Li pAFmax [dB]
Electric locomotives and special vehicles with electric traction | 70 | 75 | 85
Diesel locomotives and special vehicles with diesel traction | 71 | 78
EMUs | 65 | 68
DMUs | 72 | 76
Coaches | 64 | 68
Wagons | 65 | n.a. | n.a.
The demonstration of conformity is described in point 6.2.2.1.
```

**[2]**

```
NOI TSI, 6.2.2.3.2.1. EMU, DMUs, locomotives and coaches
For EMU, DMUs, locomotives and coaches three classes of maximum operational speed are distinguished:
(1) If the maximum operational speed of the unit is lower than or equal to 80 km/h, the pass-by noise shall be measured at its maximum speed vmax. That value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3.
(2) If the maximum operational speed vmax of the unit is higher than 80 km/h and lower than 250 km/h, the pass-by noise shall be measured at 80 km/h and at its maximum speed. Both measured pass-by noise values LpAeq,Tp(Vtest) shall be normalised to the reference speed of 80 km/h LpAeq,Tp(80 km/h) using Formula (1). The normalised value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (1): LpAeq,Tp(80 km/h) = LpAeq,Tp(Vtest) – 30 * log (vtest/80 km/h) vtest | = | Actual speed during the measurement
```

**[3]**

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

### q01 · answer X

- **S1:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q01 · answer Y

- **S1:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q02

**Question:** What is the pass-by noise limit for freight wagons at 80 km/h?

**[1]**

```
NOI TSI, 4.2.3. Limits for pass-by noise
The limit values for the A-weighted equivalent continuous sound pressure level at a speed of 80 km/h (LpAeq,Tp,(80 km/h)) and, if applicable, at 250 km/h (LpAeq,Tp,(250 km/h)) concerning the pass-by noise allocated to the categories of the rolling stock subsystem are set out in Table 4. The limit values are set at a distance of 7,5 m from the centre of the track and 1,2 m above top of rail.
Measurements at speeds higher than or equal to 250 km/h shall also be made at the ‘additional measurement position’ with a height of 3,5 m above top of rail in accordance with the specification referenced in Appendix B, Index [1] and assessed against the applicable limit values of Table 4.
Table 4
Limit values for pass-by noise
Category of the rolling stock subsystem | LpAeq,Tp (80 km/h) [dB] | LpAeq,Tp (250 km/h) [dB]
Electric locomotives and special vehicles with electric traction | 84 | 99
Diesel locomotives and special vehicles with diesel traction | 85 | n.a.
EMUs | 80 | 95
DMUs | 81 | 96
Coaches | 79 | n.a.
Wagons (normalised to APL = 0,225) (1) | 83 | n.a.
(1) APL: the number of axles divided by the length over the buffers (m-1)
The demonstration of conformity is described in point 6.2.2.3.
```

**[2]**

```
NOI TSI, 6.2.2.3.2.2. Wagons
For wagons two classes of maximum operational speed are distinguished:
(1) If the maximum operational speed vmax of the unit is lower than or equal to 80 km/h, the pass-by noise shall be measured at its maximum speed. The measured pass-by noise value LpAeq,Tp(Vtest) shall be normalised to a reference APL of 0,225 m-1 LpAeq,Tp (APLref) using Formula (3). That value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (3): LpAeq,Tp (APLref) = LpAeq,Tp(Vtest) – 10 * log(APLwag/0,225 m-1) APLwag | = | Number of axles divided by the length over the buffers [m-1] vtest | = | Actual speed during the measurement
(2) If the maximum operational speed vmax of the unit is higher than 80 km/h, the pass-by noise shall be measured at 80 km/h and at its maximum speed. Both measured pass-by noise values LpAeq,Tp(Vtest) shall be normalised to the reference speed of 80 km/h and to a reference APL of 0,225 m-1 LpAeq,Tp(APL ref, 80 km/h) using Formula (4). The normalised value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (4): LpAeq,Tp (APLref, 80 km/h) = LpAeq,Tp(Vtest) – 10 * log(APLwag/0,225 m-1) — 30 * log(vtest/80 km/h) APLwag | = | Number of axles divided by the length over the buffers [m-1] vtest | = | Actual speed during the measurement
```

**[3]**

```
NOI TSI, (b) Specific case Sweden
(‘T’) For locomotives with total tractive power of more than 6 000 kW and a maximum axle load of more than 25 t the limit values for pass-by noise LpAeq,Tp (80 km/h) in Table 4 may be raised up to 85 dB.
```

### q02 · answer X

- **S1:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q02 · answer Y

- **S1:** The pass-by noise limit for wagons at 80 km/h is 83 dB(A) [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q03

**Question:** How wide must an escape walkway in a railway tunnel be, and how much headroom must it have?

**[1]**

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

**[2]**

```
SRT TSI, 4.2.1.5.2 Access to the safe area
This specification applies to all tunnels of more than 1 km in length.
(a) Safe areas shall be accessible for people who commence self-evacuation from the train as well as for the emergency response services.
(b) One of the following solutions shall be selected for access points from a train to the safe area: (1) Lateral and/or vertical emergency exits to the surface. These exits shall be provided at least every 1 000 m. (2) Cross-passages between adjacent independent tunnel tubes, which enable the adjacent tunnel tube to be employed as a safe area. Cross-passages shall be provided at least every 500 m. —————
(c) Doors giving access from the escape walkway to the safe area shall have a minimum clear opening of 1,4 m wide and 2,0 m high. Alternatively it is permitted to use multiple doors next to each other which are less wide as long as the flow capacity of people is demonstrated to be equivalent or higher.
(d) After passing the doors, the clear width shall continue to be at least 1,5 m wide and 2,25 m high.
(e) The way in which the emergency response services access the safe area shall be described in the emergency plan.
```

**[3]**

```
PRM TSI, 4.2.1.2.2. Vertical circulation
(1) Where an obstacle-free route includes a change in level, there shall be a step-free route providing an alternative to stairs for mobility impaired people.
(2) Steps and stairs on the obstacle-free routes shall have a minimum width of 160 cm measured between the handrails
(2a) As a minimum, the first and last steps of a flight of stairs shall be indicated by a contrasting band. This requirement shall apply from a single step.
(2b) As a minimum, tactile warning surface indicators shall be installed before the first descending step of staircases of three steps or more.
(3) Ramps shall be installed for persons with disabilities and persons with reduced mobility unable to use stairs where lifts are not provided. They shall have a moderate gradient. A steep gradient is allowed for ramps on short distances only.
(3a) When they are used as a complement to stairs, ramps may have a width of 120 cm measured at floor surface.
(4) Stairs of three steps or more and ramps shall be provided with handrails on both sides and at two levels.
(5) Lifts shall be provided where ramps are not available and shall be at least of type 2 in accordance with the specification referenced in Appendix A, Index [1]. Type 1 lifts are allowed in the case of stations being renewed or upgraded only.
(6) Escalators and moving walks shall be designed in accordance with the specification referenced in Appendix A, Index [2].
```

### q03 · answer X

- **S1:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q03 · answer Y

- **S1:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].
- **S2:** The minimum vertical clearance above the walkway must be 2.25 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q04

**Question:** For how long must the emergency lighting on tunnel escape routes keep working after the main power supply fails?

**[1]**

```
SRT TSI, 4.2.1.5.4 Emergency lighting on escape routes
This specification applies to all tunnels of more than 0,5 km in length.
(a) Emergency lighting shall be provided to guide passengers and staff to a safe area in the event of an emergency.
(b) Illumination shall comply with the following requirements: (1) Single-track tube: on the side of the walkway (2) Multiple-track tube: on both sides of the tube (3) Position of lights: — above the walkway, as low as possible, so as not to interfere with the free space for the passage of persons, or — built into the handrails. (4) The maintained illuminance shall be at least 1 lux at a horizontal plane at walkway level.
(c) Autonomy and reliability: an alternative electricity supply shall be available for an appropriate period of time after failure of the main supply. The time required shall be consistent with the evacuation scenarios and reported in the Emergency Plan.
(d) If the emergency light is switched off under normal operating conditions, it shall be possible to switch it on by both of the following means: (1) manually from inside the tunnel at intervals of 250 m (2) by the tunnel operator using remote control
```

**[2]**

```
SRT TSI, 4.2.1.10. Reliability of electrical systems
This specification applies to all tunnels of more than 1 km length.
(a) Electrical systems identified by the Infrastructure Manager as vital to the safety of passengers in the tunnel shall be kept in use as long as necessary according to the evacuation scenarios considered in the emergency plan.
(b) Autonomy and reliability: an alternative electricity supply shall be available for an appropriate period of time after failure of the main supply. The time required shall be consistent with the evacuation scenarios considered and included in the emergency plan.
```

**[3]**

```
SRT TSI, 4.2.1.9. Electricity supply for emergency response services
This specification applies to all tunnels of more than 1 km length.
The electricity supply system in the tunnel shall be suitable for the emergency response services equipment in accordance with the emergency plan for the tunnel. Some national emergency response services groups may be self-sufficient in relation to electricity supply. In this case, the option of not providing electricity supply facilities for the use of such groups may be appropriate. Such a decision, however, must be described in the emergency plan.
```

### q04 · answer X

_(no answer given)_


- [ ] Accept  - [ ] Reject

**Note:** 

### q04 · answer Y

- **S1:** An alternative electricity supply must be available for an appropriate period of time after the main supply fails, with the required time being consistent with the evacuation scenarios and reported in the Emergency Plan [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q05

**Question:** What is the maximum distance between evacuation and rescue points in a tunnel for Category A and for Category B passenger rolling stock, and what is the difference between the two categories?

**[1]**

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
This specification applies to all tunnels of more than 1 km in length.
(a) For the purpose of this clause, two or more consecutive tunnels will be considered as a single tunnel unless both of the following conditions are met: (1) The separation between tunnels in open air is longer than the maximum length of the passenger train intended to be operated on the line + 100 m and (2) The open air area and track situation around the separation between tunnels allow passengers to move away from the train along a a safe space . The open air area shall contain all passengers of the maximum capacity of the train intended to be operated on the line.
(b) Evacuation and rescue points shall be created (1) Outside both portals of every tunnel of > 1 km and (2) Inside the tunnel, according to the category of rolling stock that is planned to be operated, as summarized in the table below: Rolling stock category according to paragraph 4.2.3 | Maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points Category A | 5 km Category B | 20 km
```

**[2]**

```
SRT TSI, 4.4.6. Operational rules related to trains running in tunnels
(b) Operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points , or the length of tunnels exceeds 5 km, in the case where there are no passengers on board.
(c) Operational rules shall be put in place to avoid panic and spontaneous, uncontrolled evacuation in the case of a prolonged stop of a train in a tunnel without the occurrence of a hot or cold incident.
```

**[3]**

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
(e) Requirements for evacuation and rescue points inside the tunnel In addition to the requirements in 4.2.1.7 (c), evacuation and rescue points inside the tunnel shall comply with the following requirements (1) A safe area shall be accessible from the stopping position of the train. Dimensions of the evacuation route to the safe area shall consider the evacuation time (as specified in clause 4.2.3.4.1) and the planned capacity of the trains (referred to in clause 4.2.1.5.1) intended to be operated in the tunnel. The adequacy of the sizing of the evacuation route shall be demonstrated. (2) The safe area that is paired with the evacuation and rescue point shall offer a sufficient standing surface relative to the time passengers are expected to wait until they are evacuated to a final place of safety. (3) There shall be an access to the affected train for emergency response services without going through the occupied safe area. (4) The lay-out of the evacuation and rescue point and its equipment shall take into account the control of smoke, in particular to protect people who use the self-evacuation facilities to access the safe area.
```

**[4]**

```
SRT TSI, 4.2.3. Subsystem rolling stock
(a) In the context of this TSI the subsystem rolling stock is subdivided into the following categories. (1) Category A passenger rolling stock (including passenger locomotives) for operation on lines within the scope of this TSI, where the distance between evacuation and rescue points or the length of tunnels does not exceed 5 km. (2) Category B passenger rolling stock (including passenger locomotives) for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels. (3) Freight locomotives and self-propelling units designed to carry payload other than passengers, such as mail and freight for example, for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels. Locomotives designed to haul freight trains as well as passenger trains fall under both categories and shall respect the requirements of both categories. (4) Self-powered on-track machines, when in transport mode, for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels.
(b) The rolling stock category shall be recorded in the technical file and will remain valid regardless of future revisions of this TSI.
```

### q05 · answer X

- **S1:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1].
- **S2:** Category A passenger rolling stock is for operation on lines where the distance between evacuation and rescue points or the length of tunnels does not exceed 5 km, whereas Category B passenger rolling stock is for operation in all tunnels on lines within the scope of the TSI, irrespective of the length of the tunnels [4].
- **S3:** Additionally, operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points or the length of tunnels exceeds 5 km only when there are no passengers on board [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### q05 · answer Y

- **S1:** The maximum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 20 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q06

**Question:** How many wheelchair spaces must a 250 m long passenger unit have?

**[1]**

```
PRM TSI, 4.2.2.2. Wheelchair spaces
(1) According to the length of the unit, excluding the locomotive or power head, there shall be in that unit not less than the number of accessible wheelchair spaces shown in the following table: Table 5 Minimum number of wheelchair spaces per unit length Unit length | Number of wheelchair spaces by unit Less than 30 m | 1 wheelchair space 30 to 205 metres | 2 wheelchair spaces More than 205 to 300 metres | 3 wheelchair spaces More than 300 metres | 4 wheelchair spaces
(2) To ensure stability, the wheelchair space shall be designed for the wheelchair to be positioned either facing or back to the direction of travel.
(3) Over the full length of the wheelchair space the width shall be 700 mm from floor level to a minimum height of 1 450 mm with an additional 50 mm width to give clearance for hands on each side that is adjacent to any obstacle that will inhibit clearance for the wheelchair users hands (e.g. wall or structure) from a height of 400 mm to 800 mm above floor level (if one side of the wheelchair is adjacent to the aisle there is no additional 50 mm requirement for that side of the wheelchair as it is already free space).
(4) The minimum distance in the longitudinal plane between the back of the wheelchair space and the next surface shall be in accordance with the specification referenced in Appendix A, Index [16].
```

**[2]**

```
PRM TSI, 4.2.2.2. Wheelchair spaces
(10) On trains with a design speed higher than 250 km/h excepting double deck trains, it shall be possible for a wheelchair user occupying a wheelchair space to transfer onto a passenger seat that shall be equipped with a movable armrest. Such transfer is made by the wheelchair user in autonomy. In that case, it is allowed that the companion seat is shifted to another row. This requirement is applicable up to the number of wheelchair spaces per unit specified in table 5.
(11) The wheelchair space shall be fitted with a call for aid device that shall, in the event of danger, provide to a wheelchair user the possibility to inform a person who can take appropriate action.
(12) The call for aid device shall be placed within the comfortable reach range of the person using the wheelchair as shown in the specification referenced in Appendix A, Index [9].
(13) The call for aid device shall not be placed within a narrow recess which prevents immediate intentional palm operation but can be protected from unintentional use.
(14) The interface of the call for aid device shall be as set out in point 5.3.2.6.
(15) A sign conforming to appendix N shall be placed immediately next to, or in the wheelchair space so as to identify the space as the wheelchair space.
```

**[3]**

```
PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network
The number of wheelchair spaces is limited to two for any unit intended to be used on Ile de France Express network lines A B C D and E independently of its length.
```

### q06 · answer X

- **S1:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q06 · answer Y

- **S1:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q07

**Question:** What is the minimum clear usable width of exterior passenger doors, and of wheelchair access doors with level access?

**[1]**

```
PRM TSI, 4.2.2.3.2. Exterior doors
(1) All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open.
(2) On trains with a design speed lower than 250 km/h, wheelchair access doors offering a level access as defined in point 2.3 shall have a minimum clear useable width of 1 000 mm when open.
(3) All exterior passenger doorways shall be marked on the outside in a way that gives a contrast to the vehicle body-side surrounding them.
(4) The designated wheelchair exterior accessible doorways shall be the closest doorways to the designated wheelchair spaces.
(5) The doors to be used for wheelchair access shall be clearly labelled with a sign in accordance with Appendix N.
(6) From the inside of the vehicle the position of external doorways shall clearly be marked by use of contrasted adjacent flooring.
(7) Audible and visible signals shall be given to persons inside and outside the train when doors are operated or about to operate.
(8) The door operating signals are the following:
(a) when a door is released for opening, a door opening signal shall be given; it shall last a minimum of 5 seconds unless the door is operated, in which case it may cease after 3 seconds;
(b) when a door is automatically or remotely opened by the driver or other member of the train crew, a door opening signal shall be given; it shall last a minimum of 3 seconds from the moment that the door starts to open;
```

**[2]**

```
PRM TSI, 4.2.1.3. Doors and entrances
(1) This point applies to all doors and entrances that are on obstacle-free routes, with the exception of doors giving access to the toilets which are not dedicated to persons with disabilities and persons with reduced mobility.
(2) Doors shall have a minimum clear useable width of 90 cm and shall be operable by persons with disabilities and persons with reduced mobility.
(3) It is permitted to use manual, semi-automatic or automatic doors.
(4) Door operating devices shall be available at a height of between 80 cm and 110 cm.
```

**[3]**

```
PRM TSI, 4.2.2.3.3. Interior doors
(1) Internal automatic and semi-automatic doors shall incorporate devices that prevent passengers becoming trapped during operation of the doors.
(2) Interior doors that are made available for wheelchair users shall have a minimum clear useable width of 800 mm.
(3) The force required to open or close a manual door shall not exceed 60 N.
(4) The centre of interior door controls shall be not less than 800 mm and not more than 1 100 mm measured vertically above the vehicle floor level.
(5) Automatic inter-vehicle connecting doors shall operate either synchronously as a pair, or the second door shall automatically detect the person moving towards it and open.
(6) If more than 75 % of a door's surface is made of a transparent material, it shall be clearly marked with visual indicators.
```

### q07 · answer X

- **S1:** The minimum clear usable width of exterior passenger doors is 800 mm when open[1].
- **S2:** Wheelchair access doors offering level access must have a minimum clear usable width of 1 000 mm when open[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q07 · answer Y

- **S1:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [1].
- **S2:** On trains with a design speed lower than 250 km/h, wheelchair access doors offering a level access shall have a minimum clear useable width of 1 000 mm when open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q08

**Question:** Which traction power supply systems does the Energy TSI allow, and which may be used on new lines faster than 250 km/h?

**[1]**

```
ENE TSI, 2.1.1. Traction power supply
(1) The objective of the traction power supply system is to supply every train with power in order to meet the planned timetable.
(2) Basic parameters for traction power supply system are set out in point 4.2.
```

**[2]**

```
ENE TSI, 7.1.1. Implementation rules for voltage and frequency
New lines with speed greater than 250 km/h shall be supplied with one of the AC systems listed in point 4.2.3 (a) and (b).
```

**[3]**

```
ENE TSI, 7.2. Application of this TSI to a new energy subsystem
(1) For a new energy subsystem, the application of this TSI shall be compulsory.
(2) A ‘new energy subsystem’ means an energy subsystem placed into service after 28 September 2023, which is created where no traction power supply and OCL previously existed.
Any other energy subsystem shall be considered as an ‘existing energy subsystem’.
(3) The following cases are considered as upgrading and not as the placing into service of new energy subsystems:
(a) the realignment of part of an existing route;
(b) the creation of a bypass;
(c) the addition of one or more tracks on an existing route, regardless of the distance between the original tracks and the additional tracks.
```

**[4]**

```
ENE TSI, 4.2.3. Voltage and frequency
The nominal voltage and nominal frequency of the traction power supply system shall be one of the four systems:
(a) AC 25 kV, 50 Hz;
(b) AC 15 kV, 16,7 Hz;
(c) DC 3 kV;
(d) DC 1,5 kV.
For new lines with speed greater than 250 km/h, implementation rules are specified in point 7.1.1.
```

### q08 · answer X

- **S1:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 16,7 Hz; DC 3 kV; and DC 1,5 kV [4].
- **S2:** New lines with a speed greater than 250 km/h must be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

### q08 · answer Y

- **S1:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 16,7 Hz, DC 3 kV and DC 1,5 kV [4].
- **S2:** For new lines with speeds greater than 250 km/h, only the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

## q09

**Question:** What are the Class A train protection and radio systems under the CCS TSI?

**[1]**

```
CCS TSI, — Current status of deployment for Class A train protection system
[If relevant, include here an explanatory text in relation to the current status of ETCS deployment.]
```

**[2]**

```
CCS TSI, 2.2. Scope
The Control-Command and Signalling Subsystem TSI specifies only those requirements which are necessary to assure the interoperability of the Union rail system and the compliance with the essential requirements ( 2 ).
The Control-Command and Signalling Subsystems include the following parts:
(1) train protection;
(2) voice radio communication;
(3) data radio communication;
(4) train detection;
(5) automated train operation ( 3 ).
ERTMS (European Rail Traffic Management System) is composed of train protection (ETCS), radio communication (RMR) and automated train operation (ATO).
The Class A train protection system is ETCS (European Train Control System) ( 4 ) whilst the Class A radio system is RMR (Railway Mobile Radio system). In this TSI, RMR comprises two radio class A systems: GSM-R and FRMCS (Future Railway Mobile Communication System) that may be implemented both at the same time or each of them independently ( 5 ).
For train detection, this TSI specifies only the requirements for the interface with other subsystems.
The list of Class B systems is established in the Annex II to this regulation.
The requirements for the Control-Command and Signalling On-board Subsystem are specified in relation to Class A radio mobiles, train protection and automatic train operation.
The requirements for the Control-Command and Signalling Trackside Subsystem are specified in relation to:
(1) the Class A radio network;
(2) the Class A train protection;
(3) the Class A automated train operation;
(4) the interface requirements for train detection systems, to ensure their compatibility with rolling stock.
```

**[3]**

```
CCS TSI, — Current status of deployment for Class A radio system
[If relevant, include here an explanatory text in relation to the current status of Class A radio system.]
```

### q09 · answer X

- **S1:** The Class A train protection system is ETCS (European Train Control System), and the Class A radio system is RMR (Railway Mobile Radio system) [2].
- **S2:** RMR comprises two radio class A systems, which are GSM-R and FRMCS (Future Railway Mobile Communication System) [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### q09 · answer Y

- **S1:** The Class A train protection system is ETCS (European Train Control System) and the Class A radio system is RMR (Railway Mobile Radio), which includes GSM-R and FRMCS (Future Railway Mobile Communication System)[2].

- [ ] Accept  - [ ] Reject

**Note:** 

## q10

**Question:** How must the rear end of a passenger train and of a freight train be signalled?

**[1]**

```
OPE TSI, 4.2.2.1.3. Rear end
The railway undertaking shall provide the required means of indicating the rear of a train. The rear end signal shall only be exhibited on the rear of the last vehicle of the train. It shall be displayed as shown below.
```

**[2]**

```
OPE TSI, 4.2.2.1.3.1. Passenger trains
The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis.
```

**[3]**

```
OPE TSI, 5. COMPLETE FAILURE OF A REAR END SIGNAL
(1) If the signaller becomes aware of the complete failure of the train rear end signal, the signaller shall make arrangements to stop the train in an appropriate location and inform the driver.
(2) The driver shall then check the completeness of the train and if necessary repair/replace the train rear end signal.
(3) The driver shall report to the signaller that the train is ready to proceed. Otherwise, if the repair is not possible, the train may not proceed, unless special arrangements are made between signaller and driver.
```

**[4]**

```
OPE TSI, 4.2.2.1.3.2. Freight trains
The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis. Any train equipped with 2 steady red lights shall also be considered to comply with this obligation.
Reflective plates shall comply with Appendix E to Wagon TSI and have the following shape with white side triangles and red top and bottom triangle:
The plates shall be on the same height above buffer on the transversal axis
```

**[5]**

```
OPE TSI, 7.2.2.4. Permanent specific case (P) Finland
For the implementation of point 4.2.2.1.3.2 and the implementation of common operational rule 5 of Appendix B, Finland is not using any rear end signal device for freight trains. The means to indicate the train rear end signal for freight trains as stated in point 4.2.2.1.3.2 are also accepted in Finland.
```

### q10 · answer X

- **S1:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [2].
- **S2:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above the buffer on the transversal axis, although a freight train equipped with 2 steady red lights also complies with the requirement [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### q10 · answer Y

- **S1:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [2].
- **S2:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis, though any train equipped with 2 steady red lights shall also be considered to comply with this obligation [4].

- [ ] Accept  - [ ] Reject

**Note:** 

## q11

**Question:** From when must freight trains with reflective plates as the rear-end signal be accepted in Portugal, and across the whole EU network?

**[1]**

```
OPE TSI, Phasing out:
The following deadlines shall apply for accepting freight trains equipped with two reflective plates:
(1) From 1 January 2022, along the rail freight corridors specified in accordance with Regulation (EU) No 913/2010, with the following exceptions on the lines where steady red lights are an operational requirement for ensuring safety: (a) 1 January 2026 for Belgium and France; (b) 1 January 2025 for Portugal and Spain.
(2) From 1 January 2026, in the whole European Union rail network.
Member States concerned by the exceptions under (1) (a) and (b) shall provide, by 1 March 2022 at the latest, the Commission with a detailed action plan and precise targets ensuring the elimination of the requirement for red lights as rear end signals. Every 6 months thereafter, those Member States shall provide the Commission with a report on progress made on the use of reflective plates on their network with the aim of Union-level harmonisation of rear end signals by 1 January 2026. Stakeholders shall provide all necessary input to allow Member States to fulfil their reporting duty.
The Commission shall report to the committee referred to in Article 51 of Directive (EU) 2016/797 on the implementation progress of section 4.2.2.1.
```

**[2]**

```
OPE TSI, 7.2.2.1. Permanent specific case (P) Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia
For the implementation of point 4.2.2.1.3.2, freight trains which are operated solely on the 1 520 mm gauge network of Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia may use the following train rear end signal.
The reflective disc shall have a diameter of 185 mm with a red circle diameter of 140 mm. Where justified by operating practices, the reflective disc may be replaced with one reflective plate in compliance with Appendix E to TSI WAG.
For the implementation of point 4.2.2.1.3.1, passenger trains which are operated solely on the 1 520 mm gauge network of Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia may use 3 steady red lights as train rear end signal following the scheme:
This specific case does not prevent the access of TSI compliant rolling stock to their network.
```

**[3]**

```
OPE TSI, 4.2.2.1.3.2. Freight trains
The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis. Any train equipped with 2 steady red lights shall also be considered to comply with this obligation.
Reflective plates shall comply with Appendix E to Wagon TSI and have the following shape with white side triangles and red top and bottom triangle:
The plates shall be on the same height above buffer on the transversal axis
```

### q11 · answer X

- **S1:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q11 · answer Y

- **S1:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q12

**Question:** How quickly must the Agency handle an application for a vehicle authorisation for placing on the market?

**[1]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
Whenever tests are necessary in order to obtain documentary evidence of the technical compatibility referred to in points (b) and (d) of the first subparagraph, the national safety authorities involved may issue temporary authorisations to the applicant to use the vehicle for practical verifications on the network. The infrastructure manager, in consultation with the applicant, shall make every effort to ensure that any tests take place within three months of receipt of the applicant's request. Where appropriate, the national safety authority shall take measures to ensure that the tests take place.
4. The Agency or, in the case of paragraph 8, the national safety authority shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information from the applicant. The Agency, or, in the cases provided for in paragraph 8, the national safety authority, shall apply the practical arrangements on the authorisation procedure to be established in an implementing act, as referred to in paragraph 9. Those authorisations shall allow vehicles to be placed on the Union market.
```

**[2]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
6. Within one month of receipt of the applicant's request, the Agency shall inform the applicant that the file is complete or ask for relevant supplementary information, setting a reasonable deadline for the provision thereof. With regard to the completeness, relevance and consistency of the file, the Agency may also assess the elements specified in point (d) of paragraph 3.
The Agency shall take full account of the assessments under paragraph 5 before taking its decision on the issuance of the vehicle authorisation for placing on the market. The Agency shall issue the authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information.
In the event of non-application of one or more TSIs or parts of them as referred to in Article 7, the Agency shall issue the vehicle authorisation only after application of the procedure laid down in that Article.
The Agency shall take full responsibility for the authorisations it issues.
```

**[3]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
1. The applicant shall place a vehicle on the market only after having received the vehicle authorisation for placing on the market issued by the Agency in accordance with paragraphs 5 to 7 or by the national safety authority in accordance with paragraph 8.
2. In its application for a vehicle authorisation for placing on the market, the applicant shall specify the area of use of the vehicle. The application shall include evidence that the technical compatibility between the vehicle and the network of the area of use has been checked.
```

**[4]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
5. The Agency shall issue vehicle authorisations for placing on the market in respect of vehicles having an area of use in one or more Member States. In order to issue such authorisations, the Agency shall: (a) assess the elements of the file specified in points (b), (c) and (d) of the first subparagraph of paragraph 3 in order to verify the completeness, relevance and consistency of the file in relation to the relevant TSIs; and (b) refer the applicant's file to the national safety authorities concerned by the intended area of use for assessment of the file in order to verify its completeness, relevance and consistency in relation to point (d) of the first subparagraph of paragraph 3 and to the elements specified in points (a), (b) and (c) of the first subparagraph of paragraph 3 in relation to the relevant national rules.
As part of the assessments pursuant to points (a) and (b) and in the case of justified doubts, the Agency or the national safety authorities may request that tests be conducted on the network. In order to facilitate those tests, the national safety authorities involved may issue temporary authorisations to the applicant to use the vehicle for tests on the network. The infrastructure manager shall make every effort to ensure that any such test takes place within three months of the request of the Agency or the national safety authority.
```

### q12 · answer X

- **S1:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].
- **S2:** Additionally, within one month of receipt of the applicant's request, the Agency shall inform the applicant that the file is complete or ask for relevant supplementary information, setting a reasonable deadline for the provision thereof [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### q12 · answer Y

- **S1:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

## q13

**Question:** How long does the Commission have to decide on a Member State's request not to apply a TSI, and what happens if it does not decide in time?

**[1]**

```
OPE TSI, Article 5a
By 28 March 2024, each Member State shall notify to the Commission and the Agency any national rules made redundant by the entry into force of Commission Implementing Regulation (EU) 2023/1693 ( 4 ), together with a timetable for their withdrawal if not yet done.
```

**[2]**

```
Interoperability Directive, Article 6 — Deficiencies in TSIs
1. If, after its adoption, it appears that a TSI has a deficiency, that TSI shall be amended in accordance with Article 5(11). If appropriate, the Commission shall apply this procedure without delay. Such deficiencies shall include cases which could result in unsafe operations within a Member State.
2. Pending the review of a TSI, the Commission may request an opinion from the Agency. The Commission shall analyse the Agency's opinion and inform the committee of its conclusions.
3. At the request of the Commission, the Agency's opinion referred to in paragraph 2 shall constitute acceptable means of compliance and may therefore be used for the assessment of projects, pending the adoption of a revised TSI.
4. Any member of the network of representative bodies referred to in Article 38(4) of Regulation (EU) 2016/796 may make the Commission aware of possible TSI deficiencies.
```

**[3]**

```
Interoperability Directive, Article 7 — Non-application of TSIs
5. The Commission shall, by means of an implementing act, establish the information to be included in the file referred to in paragraph 4, the required format of that file and the method to be used for its transmission. That implementing act shall be adopted in accordance with the examination procedure referred to in Article 51(3).
6. Pending the decision of the Commission, the Member State may apply the alternative provisions referred to in paragraph 4 without delay.
7. The Commission shall give its decision within four months of submission of the request supported by the complete file. In the absence of such a decision, the request shall be deemed to have been accepted.
8. Member States shall be informed of the results of the analyses and of the outcome of the procedure set out in paragraph 4.
```

### q13 · answer X

- **S1:** The Commission must give its decision within four months of submission of the request supported by the complete file [3].
- **S2:** If the Commission does not decide in time, the request is deemed to have been accepted [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### q13 · answer Y

- **S1:** The Commission must decide within four months of the Member State’s submission of the complete file; if it does not decide within that period, the request is deemed to have been accepted [3][7][8].

- [ ] Accept  - [ ] Reject

**Note:** 

## q14

**Question:** What minimum clear opening must the doors between a tunnel escape walkway and the safe area have?

**[1]**

```
SRT TSI, 4.2.1.5.2 Access to the safe area
This specification applies to all tunnels of more than 1 km in length.
(a) Safe areas shall be accessible for people who commence self-evacuation from the train as well as for the emergency response services.
(b) One of the following solutions shall be selected for access points from a train to the safe area: (1) Lateral and/or vertical emergency exits to the surface. These exits shall be provided at least every 1 000 m. (2) Cross-passages between adjacent independent tunnel tubes, which enable the adjacent tunnel tube to be employed as a safe area. Cross-passages shall be provided at least every 500 m. —————
(c) Doors giving access from the escape walkway to the safe area shall have a minimum clear opening of 1,4 m wide and 2,0 m high. Alternatively it is permitted to use multiple doors next to each other which are less wide as long as the flow capacity of people is demonstrated to be equivalent or higher.
(d) After passing the doors, the clear width shall continue to be at least 1,5 m wide and 2,25 m high.
(e) The way in which the emergency response services access the safe area shall be described in the emergency plan.
```

**[2]**

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
(e) Requirements for evacuation and rescue points inside the tunnel In addition to the requirements in 4.2.1.7 (c), evacuation and rescue points inside the tunnel shall comply with the following requirements (1) A safe area shall be accessible from the stopping position of the train. Dimensions of the evacuation route to the safe area shall consider the evacuation time (as specified in clause 4.2.3.4.1) and the planned capacity of the trains (referred to in clause 4.2.1.5.1) intended to be operated in the tunnel. The adequacy of the sizing of the evacuation route shall be demonstrated. (2) The safe area that is paired with the evacuation and rescue point shall offer a sufficient standing surface relative to the time passengers are expected to wait until they are evacuated to a final place of safety. (3) There shall be an access to the affected train for emergency response services without going through the occupied safe area. (4) The lay-out of the evacuation and rescue point and its equipment shall take into account the control of smoke, in particular to protect people who use the self-evacuation facilities to access the safe area.
```

**[3]**

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

### q14 · answer X

- **S1:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,4 m wide and 2,0 m high [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q14 · answer Y

- **S1:** The doors must have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

## q15

**Question:** When does an upgraded or renewed vehicle that is already authorised need a new vehicle authorisation for placing on the market?

**[1]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
12. In the event of renewal or upgrading of existing vehicles which already have a vehicle authorisation for placing on the market, a new vehicle authorisation for placing on the market shall be required if: (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs; (b) the overall safety level of the vehicle concerned may be adversely affected by the works envisaged; or (c) it is required by the relevant TSIs.
13. Where the applicant wishes to extend the area of use of a vehicle which has already been authorised, it shall supplement the file with the relevant documents referred to in paragraph 3 concerning the additional area of use. The applicant shall submit the file to the Agency, which shall, after following the procedures laid down in paragraphs 4 to 7, issue an updated authorisation covering the extended area of use.
If the applicant has received a vehicle authorisation in accordance with paragraph 8 and wishes to extend the area of use within that Member State, it shall supplement the file with the relevant documents referred to in paragraph 3 concerning the additional area of use. It shall submit the file to the national safety authority which shall, after following the procedures laid down in paragraph 8, issue an updated authorisation covering the extended area of use.
```

**[2]**

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
1. The applicant shall place a vehicle on the market only after having received the vehicle authorisation for placing on the market issued by the Agency in accordance with paragraphs 5 to 7 or by the national safety authority in accordance with paragraph 8.
2. In its application for a vehicle authorisation for placing on the market, the applicant shall specify the area of use of the vehicle. The application shall include evidence that the technical compatibility between the vehicle and the network of the area of use has been checked.
```

**[3]**

```
Interoperability Directive, Article 54 — Transitional regime for using vehicles
1. Without prejudice to paragraph 4 of this Article, vehicles which need to be authorised between 15 June 2016 and 16 June 2019 shall be subject to the provisions set out in Chapter V of Directive 2008/57/EC.
2. Authorisations for the placing in service of vehicles which have been granted pursuant to paragraph 1 and all other authorisations granted prior to 15 June 2016, including authorisations delivered under international agreements, in particular RIC (Regolamento Internazionale Carrozze) and RIV (Regolamento Internazionale Veicoli), shall remain valid in accordance with the conditions under which the authorisations have been granted.
3. Vehicles authorised for placing in service pursuant to paragraphs 1 and 2 shall receive a new vehicle authorisation for placing on the market in order to operate on one or more networks which are not yet covered by their authorisation. The placing on the market on those additional networks shall be subject to Article 21.
```

### q15 · answer X

- **S1:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q15 · answer Y

- **S1:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].
- **S2:** It is also required if the overall safety level of the vehicle concerned may be adversely affected by the envisaged works, or if it is required by the relevant TSIs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q16

**Question:** Which language must train crew use for safety-related communication with the staff authorising train movements?

**[1]**

```
OPE TSI, 4.2.1.5. Safety-related communications between train crew, other railway undertaking staff and staff authorising train movements
The language used for safety-related communication between train crew, other railway undertaking staff (as defined in Appendix G) and the staff authorising train movements is the operating language(s) (as defined in Appendix J) used by the infrastructure manager on the route concerned.
The principles for safety-related communication between train crew and staff responsible for authorising the movement of trains are to be found in Appendix C.
In accordance with Directive 2012/34/EU, the infrastructure manager is responsible for publishing the ‘operating’ language(s) used by its personnel in daily operational use.
Where, however, local practice requires that a second language is also provided for, it is the responsibility of the infrastructure manager to determine the geographic boundaries for its use.
```

**[2]**

```
OPE TSI, 4.6.2.1. Principles
The infrastructure manager and the railway undertaking are required to ensure that their relevant staff are competent in the use of the communication protocols and principles set out in Appendix C.
Where the operating language used by the infrastructure manager differs from that habitually used by the railway undertaking's staff, such linguistic and communications training shall form a critical part of the railway undertaking's overall competence management system.
Railway undertaking staff whose duties require them to communicate with staff of the infrastructure manager in connection with safety-critical matters, whether in normal, degraded or emergency situations, shall have a sufficient level of knowledge in the operating language of the infrastructure manager.
```

**[3]**

```
SRT TSI, 4.4.5. Provision of on-train safety and emergency information to passengers
(a) Railway undertakings shall inform passengers of on board emergency and safety procedures related to tunnels.
(b) When such information is in written or spoken form, it shall be presented in the language of the country the train is running in as a minimum, plus English.
(c) An operating rule shall be in place describing how the train crew ensures the complete evacuation of the train when this is necessary, including those people with hearing impairments that may be in closed areas.
```

### q16 · answer X

- **S1:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### q16 · answer Y

- **S1:** The language used for safety-related communication between the train crew and the staff authorising train movements is the operating language(s) used by the infrastructure manager on the route concerned [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n01

**Question:** How far in advance must a Member State notify a national rule that allows only ETCS-equipped vehicles on ETCS-equipped lines, and can that period be shorter?

**[1]**

```
CCS TSI, 7.4.3. National requirements
7.4.3.1. Member States may introduce additional requirements at national level, in particular with a view to allowing only ETCS-equipped vehicles to access ETCS-equipped lines, so that existing national systems can be decommissioned; This shall be notified a minimum 5 years before the decommissioning. A shorter period is allowed if this is agreed between the IM and the RUs who run or intend to run (at the time of establishing the agreement) services on these lines. This notification shall be done within the RINF and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU ( 36 ). The 5-year notification period does not apply to those requirements allowing only ETCS-equipped vehicles to access ETCS-equipped lines, which were announced in the Network Statement before the entry into force of this Regulation.
7.4.3.2. Member States may decide to exclude special vehicles as defined in point 2.2.2 (C) of the LOC&PAS TSI, including road-rail vehicles, from the obligation to equip them with ETCS, RMR or ATO on a specific area of use if the operation of these vehicles does not prevent the Class B decommissioning. This shall be registered in RINF ( 37 ).
```

**[2]**

```
CCS TSI, B1. Changes of requirements and transition regimes for On-Board Subsystems
2 | Points 7.4.2.1, and 7.4.3 | 7.4.2.1.2. and 7.4.3(2) grants exemptions for new vehicles to be equipped with ETCS | 7.4.2.1.2. and point 7.4.3(2) deleted. All newly built vehicles shall be equipped with ETCS. | Directly applicable Note: Design phase started after 28 September 2023 here relates to ‘RST design phase’ for any vehicles without ETCS. For special vehicles applicable from 1 January 2026 unless Member States have issued decisions in accordance with 7.4.3.2. | Applicable if design phase ends on or after 1 January 2028 Note: Design phase started before 28 September 2023 here relates to ‘RST design phase’ for any vehicles without ETCS. For special vehicles applicable if design phase ends on or after 1 January 2030 unless Member States have issued decisions in accordance with 7.4.3.2. | Applicable for newly built vehicles placed on the market on or after 1 January 2030 For special vehicles applicable for newly built vehicles placed on the market on or after 1 January 2030 unless Member States have issued decisions in accordance with 7.4.3.2. | Not applicable
```

**[3]**

```
CCS TSI, 7.4.2.2. Existing vehicles
When authorising existing vehicles in accordance with Article 21 of Directive (EU) 2016/797, they shall be equipped and ready for operation with ETCS (Class A train protection system) in accordance with this TSI if installing any new Class B train protection system in a control-command and signalling on-board subsystem.
It is mandatory to fulfil points 7.4.2.4.1 and 7.4.2.4.2 if upgrading the existing ETCS on-board part within a vehicle.
It is not needed to fulfil points 7.4.2.4.1 and 7.4.2.4.2 if correcting the existing ETCS on-board functionality within a vehicle.
```

### n01 · answer X

- **S1:** The Member State must notify the national rule at least 5 years before the de-commissioning of the ETCS-equipped line[1].
- **S2:** A shorter notification period is permitted if it is agreed between the Infrastructure Manager and the railway undertakings that run or intend to run services on those lines[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n01 · answer Y

- **S1:** A Member State must notify the national rule a minimum 5 years before the decommissioning [1].
- **S2:** A shorter period is allowed if this is agreed between the IM and the RUs who run or intend to run services on these lines at the time of establishing the agreement [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n02

**Question:** Which track gauges does the CCS TSI apply to, and which lines are excluded?

**[1]**

```
CCS TSI, 1.2. Geographical Scope
The geographical scope of this TSI is the network of the whole rail system, as described in point 1 of Annex I to Directive (EU) 2016/797 and excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797.
The TSI shall apply to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges. However, it shall not apply to short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries.
```

**[2]**

```
CCS TSI, 1.1. Technical scope
This TSI concerns the Control Command and Signalling On-Board Subsystem and the Control-Command and Signalling Trackside Subsystem.
This TSI is applicable to control-command and signalling trackside Subsystems of the rail network defined in the point 1.2 (Geographical Scope) of this TSI and to the control-command and signalling on-board subsystems of vehicles which are (or are intended to be) operated on it. These vehicles are of one of the following types (as defined in point 2 of Annex I to Directive (EU) 2016/797):
(1) locomotives and passenger rolling stock, including thermal or electric traction units, self-propelling thermal or electric passenger trains, and passenger coach, if equipped with a driving cab;
(2) special vehicles, such as on-track machines, if equipped with a driving cab intended to be used in running mode on its own wheels.
This list of vehicles shall include those which are specially designed to operate on the different types of high-speed lines described in point 1.2 (Geographical Scope).
```

**[3]**

```
CCS TSI, Article 2 — Scope
1. The TSI shall apply to new trackside CCS and on-board CCS subsystems of the rail system as defined in points 2.3 and 2.4 of Annex II to Directive (EU) 2016/797. —————
2. The TSI shall not apply to existing trackside CCS and on-board CCS subsystems of the rail system already placed on the market and in service on all or part of any Member State’s railway network by 28 September 2023, except when: (a) the subsystem is subject to renewal or upgrading in accordance with point 7 of Annex I to this Regulation; (b) the area of use of a vehicle is extended in accordance with Article 54(3) of Directive (EU) 2016/797 to at least three Member States, or the installation of ETCS is indicated in RINF for the subsequent five years in the new area of use. In that case point 7.4.2.3 of Annex I to this Regulation shall apply; (c) the subsystem is subject to the specification maintenance requirements set out in point 7.2.10 of Annex I to this Regulation.
3. The technical and geographical scope of the TSI is set out in points 1.1 and 1.2 of Annex I.
```

### n02 · answer X

- **S1:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges[1].
- **S2:** It does not apply to short border-crossing lines with 1 520 mm track gauge that are connected to the network of third countries[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n02 · answer Y

- **S1:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [1].
- **S2:** It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n03

**Question:** In a national implementation plan, how much advance notice must railway undertakings get of new mandatory on-board CCS requirements?

**[1]**

```
CCS TSI, 7.4.4. National Implementation Plans
The national implementation plan shall provide information on all new, renewed and upgraded lines in relation to mandatory and optional functions listed in 7.2.9 ensuring that notifications to RUs are provided at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network. This shall be notified within the RINF ( 38 ) and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU. The 5-year notification period does not apply to any requirements, which were announced in the Network Statement before the entry into force of this CCS TSI.
The national implementation plans shall cover a period of at least 20 years and shall be updated regularly, at least every five years. The plans shall follow the template provided in the in Appendix H to this Annex for the first five years of the period covered. For the subsequent period of fifteen years, the plan shall follow this template to the extent possible with a less detailed approach.
The Commission shall publish the national implementation plans on its website and inform Member States about them through the Committee referred to in Article 51(1) of Directive (EU) 2016/797.
The Commission shall draw up an analysis of the national implementation plans that shall encompass among others comparison of the plans and identification of needs for additional coordination measures.
The national implementation plan shall at least include the following information ( 39 ):
```

**[2]**

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

**[3]**

```
CCS TSI, 7.4.4. National Implementation Plans
Member States shall develop a national plan for the implementation of this TSI in coordination with the Infrastructure Managers and Railway Undertakings concerned, considering the coherence of the entire rail system of the European Union taking into account the economic viability, interoperability and safety of the rail system. Member States shall consult the neighbouring countries for a coherent planning of the railway cross-border sections. This plan shall include all lines in scope of the TSI including TEN-T lines and the nodes and last mile connections.
Member States shall coordinate the process between all stakeholders concerned to set up the technical and indicative financial migration strategy required for the overall ERTMS deployment of this national implementation plan.
Member States shall include the assessment of the needs expressed by the railway undertakings and the infrastructure managers for the CCS subsystem related to the conditions for mandatory and optional functions listed in 7.2.9 in the National Implementation Plan.
Member States shall decide on the migration strategy describing the expected overall impact for the railway system (taking a Union perspective) and how the impact is balanced in a non-discriminatory way between the stakeholders concerned based on the above assessment. The output of this coordination process shall be the definition of the technical and the financial migration strategy being implemented.
```

### n03 · answer X

- **S1:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n03 · answer Y

- **S1:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

## n04

**Question:** When may a Member State leave out the GSM-R decommissioning section of its national implementation plan?

**[1]**

```
CCS TSI, 5.2.4. Decommissioning of GSM-R
[This section shall include a network map providing an overview with dates when GSM-R radio operation is not allowed anymore. If not similar, this section shall also include a network map providing an overview with dates where GSM-R system is taken out of service.
This section is not mandatory for those Member States which do not foresee GSM-R decommissioning in the next 20 years.
The template to be filled in to provide the information in this section is given below]
```

**[2]**

```
CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning
[Include here the line identification number] | [Include here the name of the line] | [Include here the current status of the GSM-R deployment on the line. Under construction/ not yet under construction] | [Include here the date when the construction started or is expected to start.] | [Include here the date when GSM-R will be placed in service.] | [If the line is equipped with a Class B radio system, include here the date when Class B operation is not allowed anymore.] | [If not similar to the previous column, include here the date when Class B system is taken out of service] | [Include here the total length of the line] | [Specify here whether GSM-R voice or data is installed] | [Include here the baseline of the GSM-R to be implemented] | [Include here if radio circuit switching is implemented or only packet switching] | [Include here the type of Radio part action. New/ renew/ upgrade] | [If relevant, include here additional comments]
```

**[3]**

```
CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning
[If relevant, include here an explanatory text in relation to planning of GSM-R deployment and Class B radio part decommissioning.]
Table 12
Planning for GSM-R deployment and Class B radio part decommissioning
ID | Line | Planning for GSM-R deployment | Planning for Class B radio decommissioning | Additional information | Note
Current status | Realization | Date when GSM-R is placed in service | Dates when Class B operation is not allowed any more | Dates when Class B is taken out of service | Length | GSM-R voice/ GSM-R data | Baseline | Circuit switching/ Packet switching | Type of action
```

### n04 · answer X

- **S1:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n04 · answer Y

- **S1:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n05

**Question:** How many years ahead must the train detection planning table in a national implementation plan cover?

**[1]**

```
PRM TSI, Article 8 — National Implementation Plans
1. Member States shall adopt national implementation plans, including at least the information listed in Appendix C of the Annex, with a view to progressively eliminating all identified barriers to accessibility.
2. The national implementation plans shall be based on existing national plans and, subject to availability, on the inventory of assets referred to in Article 7, or on any other relevant and reliable source of information.
The scope and speed of implementing national plans shall be decided by Member States.
3. The national implementation plans shall run over a period of at least 10 years and shall be updated regularly, at least every five years.
4. The national implementation plans shall contain a strategy, including a prioritisation rule laying down the criteria and priorities for stations and units of rolling stock to be designated for renewal or upgrading. This strategy shall be formulated in cooperation with infrastructure manager(s), station manager(s), railway undertaking(s) and, if needed, other local authorities (including local transport authorities). Representative associations of users including disabled persons and persons with reduced mobility shall be consulted.
5. In each Member State, the prioritisation rule referred to in paragraph 4 shall replace the rule set out in Appendix B of the Annex which shall apply until the adoption of the national implementation plan in that Member State.
```

**[2]**

```
CCS TSI, 7.4.4. National Implementation Plans
The national implementation plan shall provide information on all new, renewed and upgraded lines in relation to mandatory and optional functions listed in 7.2.9 ensuring that notifications to RUs are provided at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network. This shall be notified within the RINF ( 38 ) and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU. The 5-year notification period does not apply to any requirements, which were announced in the Network Statement before the entry into force of this CCS TSI.
The national implementation plans shall cover a period of at least 20 years and shall be updated regularly, at least every five years. The plans shall follow the template provided in the in Appendix H to this Annex for the first five years of the period covered. For the subsequent period of fifteen years, the plan shall follow this template to the extent possible with a less detailed approach.
The Commission shall publish the national implementation plans on its website and inform Member States about them through the Committee referred to in Article 51(1) of Directive (EU) 2016/797.
The Commission shall draw up an analysis of the national implementation plans that shall encompass among others comparison of the plans and identification of needs for additional coordination measures.
The national implementation plan shall at least include the following information ( 39 ):
```

**[3]**

```
CCS TSI, 3.4. Technical migration strategy for Train Detection part
[This section shall include information and planning of the technical migration strategy of TSI compliant train detection part.
For completeness at least the following information shall be included:
— Deployment strategy. Information on the migration to the TSI compliant train detection system.
— Table which includes for each line the planning dates of TSI compliant train detection system deployment and other relevant information. The table shall provide the complete information of changes in the following 20 years.
The template to be filled in to provide the information in this section is given below]
```

### n05 · answer X

- **S1:** The train detection planning table must cover the next 20 years[3].

- [ ] Accept  - [ ] Reject

**Note:** 

### n05 · answer Y

- **S1:** The train detection planning table must provide complete information of changes in the following 20 years [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n06

**Question:** What contact wire heights does the ENE TSI set for lines with speeds of 250 km/h or more?

**[1]**

```
ENE TSI, 4.2.9.1. Contact wire height
(1) The permissible data for contact wire height is given in Table 4.2.9.1. Table 4.2.9.1 Contact wire height Description | v ≥ 250 [km/h] | v < 250 [km/h] Nominal contact wire height [mm] | Between 5 080 and 5 300 | Between 5 000 and 5 750 Minimum design contact wire height [mm] | 5 080 | In accordance with the specification referenced in Appendix E, Index [3] depending on the chosen gauge Maximum design contact wire height [mm] | 5 300 | 6 200 (1) (1) Taking into account tolerances and uplift in accordance with the specification referenced in Appendix E, Index [3], the maximum contact wire height shall not be greater than 6 500 mm.
(2) For the relation between the contact wire heights and pantograph working heights see the specification referenced in Appendix E, Index [3].
(3) At level crossings, the contact wire height shall be specified by national rules or in the absence of national rules, in accordance with the specification referenced in Appendix E, Index [4].
(4) For the track gauge system 1 520 and 1 524 mm the values for contact wire height are as follows: (a) Nominal contact wire height: between 6 000 mm and 6 300 mm; (b) Minimum design contact wire height: 5 550 mm; (c) Maximum design contact wire height: 6 800 mm.
```

**[2]**

```
ENE TSI, 7.1.1. Implementation rules for voltage and frequency
New lines with speed greater than 250 km/h shall be supplied with one of the AC systems listed in point 4.2.3 (a) and (b).
```

**[3]**

```
ENE TSI, P case
For, upgrade or renewal of the existing energy subsystem it is allowed for the overhead contact line wire height to be designed in accordance with the technical rules notified for this purpose.
```

### n06 · answer X

- **S1:** For lines with speeds of $v \ge 250$ [km/h], the nominal contact wire height is between 5 080 and 5 300 mm, the minimum design contact wire height is 5 080 mm, and the maximum design contact wire height is 5 300 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n06 · answer Y

- **S1:** For lines with speeds v ≥ 250 km/h the nominal contact wire height shall be between 5 080 mm and 5 300 mm, the minimum design height 5 080 mm and the maximum design height 5 300 mm (the maximum shall not exceed 6 500 mm) [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n07

**Question:** What is the maximum lateral deviation of the contact wire under crosswind for a 1 600 mm pantograph and for a 1 950 mm pantograph?

**[1]**

```
ENE TSI, 4.2.9.2. Maximum lateral deviation
(1) The maximum lateral deviation of the contact wire in relation to the track centre line under action of crosswind shall be in accordance with the specification referenced in Appendix E, Index [2]. Table 4.2.9.2 Maximum lateral deviation depending on the pantograph length Pantograph length [mm] | Maximum lateral deviation [mm] 1 600 | 400 (1) 1 950 | 550 (1) (1) The values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4.
(2) In the case of the multi-rail track, the requirement for lateral deviation shall be fulfilled for each pair of rails (designed, to be operated as a separated track) that is intended to be assessed against TSI.
(3) Track gauge system 1 520 mm: For Member States applying the pantograph profile in accordance with point 4.2.8.2.9.2.3 of the LOC&PAS TSI the maximum lateral deviation of the contact wire in relation to the pantograph centre under action of a crosswind shall be 500 mm.
```

**[2]**

```
ENE TSI, 4.2.9. Geometry of the overhead contact line
(1) The overhead contact line shall be designed for pantographs with the head geometry specified in the LOC & PAS TSI, point 4.2.8.2.9.2 taking into account the rules set out in point 7.1.2 of this TSI.
(2) The contact wire height and the lateral deviation of the contact wire under the action of a crosswind are factors which govern the interoperability of the rail network.
```

**[3]**

```
ENE TSI, Static pantograph gauge for 1 520 mm track gauge system
Table D.1
Distances between live parts of OCL and pantograph and earthed parts of rolling stock and fixed instalations for 1 520 mm track gauge system
Voltage of the contact system in respect of the ground [kV] | Vertical air clearance A1 between the rolling stock and lowest position of the contact wire [mm] | Vertical air clearance A2 between live parts of OCL and earthed parts [mm] | Lateral air clearance α between live parts of the pantograph and earthed parts [mm] | Vertical space δ for the live parts of the OCL (mm)
Normal | Minimal allowed for plain and main station tracks on which train hoteling is not foreseen | Without catenary wire | With catenary wire
Plain and main station tracks on which train hoteling is not foreseen | Other station tracks | Normal | Minimal allowed | Normal | Minimal allowed | Normal | Minimal allowed | Normal | Minimal allowed
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
1,5-4 | 450 | 950 | 250 | 200 | 150 | 200 | 150 | 150 | 100 | 300 | 250
6-12 | 450 | 950 | 300 | 250 | 200 | 220 | 180 | 150 | 100 | 300 | 250
25 | 450 | 950 | 375 | 350 | 300 | 250 | 200 | 150 | 100 | 300 | 250
```

### n07 · answer X

- **S1:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1].
- **S2:** These values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n07 · answer Y

- **S1:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n08

**Question:** Up to what speed do the mean contact force curves of the ENE TSI apply, and what applies above it?

**[1]**

```
OPE TSI, Note:
Pantograph | Mean contact force curve | 1.1.1.2.5.2 Contact force permitted | X |  | Comparison of mean contact force between the vehicle and the intended route: For TSI-Compliant vehicle intended to operate in Non-TSI conform line(s): comparison of mean contact force between the vehicle and the intended route, for each voltage. For existing non TSI-compliant vehicle: comparison of the mean contact between vehicle and the intended route, for each voltage. Note: A TSI-compliant vehicle is authorised with a mean contact force within limits values defined in EN 50367:2012 Table 6.
```

**[2]**

```
ENE TSI, 5.2.1.2. Mean contact force
The overhead contact line shall be designed by using the mean contact force Fm stipulated in point 4.2.11.
```

**[3]**

```
ENE TSI, 4.2.11. Mean contact force
(1) The mean contact force Fm is the statistical mean value of the contact force. Fm is formed by the static, dynamic and aerodynamic components of the pantograph contact force.
(2) The ranges of Fm for each of the traction power supply systems are defined in the specification referenced in Appendix E, Index [2].
(3) The overhead contact lines shall be designed to be capable to sustain the upper design limit of Fm given in the specification referenced in Appendix E, Index [2].
(4) The curves apply to speed up to 360 km/h. For speeds above 360 km/h procedures set out in point 6.1.3 shall apply.
```

### n08 · answer X

- **S1:** The mean contact force curves apply to speeds up to 360 km/h.
- **S2:** For speeds above 360 km/h, the procedures set out in point 6.1.3 shall apply [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### n08 · answer Y

- **S1:** The curves apply to speed up to 360 km/h [3].
- **S2:** For speeds above 360 km/h procedures set out in point 6.1.3 shall apply [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n09

**Question:** On lines for 250 km/h or more, how long must a phase separation neutral section be when all pantographs of the longest train are inside it?

**[1]**

```
ENE TSI, 4.2.15.2. Lines with speed v ≥ 250 km/h
Two types of design of phase separation sections may be adopted:
(a) a phase separation design where all the pantographs of the longest TSI compliant trains are within the neutral section. The overall length of the neutral section shall be at least 402 m. For detailed requirements see the specification referenced in Appendix E, Index [2];
(b) a shorter phase separation with three insulated overlaps as shown in the specification referenced in Appendix E, Index [2]. The overall length of the neutral section is less than 142 m including clearances and tolerances.
```

**[2]**

```
ENE TSI, Appendix E — List of referenced standards
[2.5] | Pantograph spacing for overhead contact line design | 4.2.13 | 8.2.2, Table 9
[2.6] | Phase separation sections - General - length D of neutral section | 4.2.15.1 (2) | 4
[2.7] | Lines with speed v ≥ 250 km/h | 4.2.15.2 (a) | Annex A.1.2
[2.8] | Lines with speed v ≥ 250 km/h | 4.2.15.2 (b) | Annex A.1.4
[2.9] | Lines with speed v < 250 km/h | 4.2.15.3 | Annex A.1
[2.10] | System separation sections - General - length D of neutral section | 4.2.16.1 (3) | 4
[2.11] | Assessment of current at standstill (DC systems only) | 6.1.4.2 | Annex A.3
[3] | EN 50119:2020 Railway Applications - Fixed installations – Electric traction overhead contact lines
[3.1] | Minimum design contact wire height | 4.2.9.1 (1) | 5.10.4
[3.2] | Maximum design contact wire height | 4.2.9.1 (1) (note (1)) | figure 3
[3.3] | Relation with pantograph working height | 4.2.9.1 (2) | figure 3
[3.4] | Dynamic behaviour and quality of current collection | 4.2.12 (2) | 5.10.2
[3.5] | Dynamic behaviour and quality of current collection | 4.2.12 (3) | 5.2.5.2, Table 4
[3.6] | Phase separation sections - calculation of D, clearances | 4.2.15.1 (2) | 5.1.3
[3.7] | System separation sections – General - calculation of D, clearances | 4.2.16.1 (3) | 5.1.3
[3.8] | System separation sections - pantographs raised | 4.2.16.2 (2) | 5.10.3
```

**[3]**

```
ENE TSI, 4.2.15.1. General
(1) The design of phase separation sections shall ensure that trains can move from one section to an adjacent one without bridging the two phases. Power exchange between the OCL and the unit shall be brought to zero, by switching off the on-board circuit breaker or other equivalent means, before entering the phase separation section. Adequate means (except for the short separation section) shall be provided to allow a train that is stopped within the phase separation section to be restarted.
(2) The overall length D of neutral sections is defined in the specification referenced in Appendix E, Index [2]. For the calculation of D clearances, the specification referenced in Appendix E, Index [3] and an uplift of S0 shall be taken into account.
```

### n09 · answer X

- **S1:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n09 · answer Y

- **S1:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n10

**Question:** Which parts of the energy subsystem may enter the pantograph gauge?

**[1]**

```
ENE TSI, 4.2.10. Pantograph gauge
(1) Track gauge system other than 1 520 mm:
The mechanical kinematic pantograph gauge shall be specified using the method given in the specification referenced in Appendix E, Index [2] to this TSI and the pantograph profiles defined in LOC&PAS TSI, clauses 4.2.8.2.9.2.1 and 4.2.8.2.9.2.2.
(2) Track gauge system 1 520 mm:
For Member States applying the pantograph profile in accordance with LOC&PAS TSI, clause 4.2.8.2.9.2.3, the static gauge available for pantograph is defined in Appendix D to this TSI.
(3) No part of the energy sub-system shall enter the pantograph gauge as stated in points (1) and (2), except for the contact wire and steady arm.
```

**[2]**

```
ENE TSI, Static pantograph gauge for 1 520 mm track gauge system
Table D.1
Distances between live parts of OCL and pantograph and earthed parts of rolling stock and fixed instalations for 1 520 mm track gauge system
Voltage of the contact system in respect of the ground [kV] | Vertical air clearance A1 between the rolling stock and lowest position of the contact wire [mm] | Vertical air clearance A2 between live parts of OCL and earthed parts [mm] | Lateral air clearance α between live parts of the pantograph and earthed parts [mm] | Vertical space δ for the live parts of the OCL (mm)
Normal | Minimal allowed for plain and main station tracks on which train hoteling is not foreseen | Without catenary wire | With catenary wire
Plain and main station tracks on which train hoteling is not foreseen | Other station tracks | Normal | Minimal allowed | Normal | Minimal allowed | Normal | Minimal allowed | Normal | Minimal allowed
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
1,5-4 | 450 | 950 | 250 | 200 | 150 | 200 | 150 | 150 | 100 | 300 | 250
6-12 | 450 | 950 | 300 | 250 | 200 | 220 | 180 | 150 | 100 | 300 | 250
25 | 450 | 950 | 375 | 350 | 300 | 250 | 200 | 150 | 100 | 300 | 250
```

**[3]**

```
ENE TSI, Annex
7.4.1. | General
7.4.2. | List of specific cases
Appendix A — | Conformity assessment of interoperability constituents
Appendix B — | EC verification of the energy subsystem
Appendix C — | (not used)
Appendix D — | Specification of the static pantograph gauge (track gauge system 1 520 mm)
Appendix E — | List of referenced standards
Appendix F — | List of open points
Appendix G — | Glossary
```

### n10 · answer X

- **S1:** Only the contact wire and the steady arm may enter the pantograph gauge [1][3].

- [ ] Accept  - [ ] Reject

**Note:** 

### n10 · answer Y

- **S1:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n11

**Question:** On a platform, what is the minimum distance from an obstacle to the danger area, for small and for large obstacles?

**[1]**

```
PRM TSI, 4.2.1.12. Platform width and edge of platform
(4) It is permitted to have obstacles inside this freeway of 160 cm. Equipment required for the signalling system and safety equipment shall not be considered as obstacles in this point. The minimum distance from obstacles to the danger area shall be according to the following table: Table 4 Minimum distance from obstacles to the danger area Length of obstacles (measured parallel to the platform edge) | Minimum distance to the danger area < 1 m (note 1) — small obstacle | 80 cm 1 m to < 10 m — large obstacle | 120 cm Note 1: if the distance between two small obstacles is less than 2,4 m measured parallel to the platform edge they shall be considered as one large obstacle. Note 2: Within this minimum distance from a large obstacle to the danger area it is permitted to have additional small obstacles as long as the requirements for small obstacles (minimum distance to danger area and minimum distance to next small obstacle) are met.
(6) The boundary of the danger area, furthest from the rail side edge of the platform, shall have a visual marking and tactile walking surface indicators.
(7) The visual marking shall be a contrasting, slip resistant, warning line with a minimum width of 10 cm.
```

**[2]**

```
PRM TSI, 4.2.1.12. Platform width and edge of platform
(1) The danger area of a platform commences at the rail side edge of the platform and is defined as the area where passengers are not allowed to stand when trains are passing or arriving.
(2) It is permitted for the width of the platform to be variable on the whole length of the platform.
(3) The minimum width of the platform without obstacles shall be the width of the danger area plus the width of two opposing freeways of 80 cm (160 cm). This dimension may taper to 90 cm at the platform ends.
```

**[3]**

```
PRM TSI, 4.4.3. Provision of boarding aids and provision of assistance
(e) for boarding aids located on the platforms, the location where they are most likely to be used, taking into account that a free space (no obstacles) of 150 cm is available from the edge of the boarding aid towards the direction where the wheelchair boards/lands at/to the platform level;
(f) the conditions for the provision of alternative transport where: — the platform cannot be reached through an obstacle-free route, or — assistance cannot be provided to deploy a boarding aid between the platform and the rolling stock.
```

### n11 · answer X

- **S1:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n11 · answer Y

- **S1:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [1].
- **S2:** For large obstacles with a length from 1 m to less than 10 m, the minimum distance to the danger area is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n12

**Question:** What maximum height and minimum depth must internal steps in a passenger vehicle have?

**[1]**

```
PRM TSI, 4.2.2.8. Height changes
(1) Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs. For double deck trains it is permitted to reduce this value to 270 mm for the stairs accessing the upper deck and the lower deck.
(2) As a minimum, the first and the last steps shall be indicated by a contrasting band extending the full width of the steps on both the front and the top surfaces of the step nosing with a depth of: — 45 mm to 55 mm on the front surface, — 45 mm to 75 mm on the top surface.
(3) Stairs constituted of more than three steps shall be provided with handrails on both sides and at two levels. The higher handrail shall be positioned at a height of 850 mm to 1 000 mm above floor level. The lower handrail shall be positioned at a height of 500 mm to 750 mm above floor level.
(4) Stairs constituted of one, two or three steps shall be provided on both sides with a minimum of one handrail or other item that can be used for personal stability.
(5) Handrails shall be compliant with point 4.2.2.9
```

**[2]**

```
PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network
For double deck trains, internal steps (other than those for external access) shall have a maximum height of 208 mm and a minimum depth of 215 mm, measured at the central axis of the stairs.
```

**[3]**

```
PRM TSI, 4.2.2.11.2. Access/egress steps
(6) If a step board is fitted and it is an extension of a door sill outside the vehicle, and there is no change in level between the step board and the floor of the vehicle, this shall not be considered to be a step for the purposes of this specification. A minimal drop in level, with a maximum of 60 mm, between the floor surface at door sill and that of the exterior of the vehicle, used to guide and seal the door is also permissible and shall not be considered as a step.
(7) Access to the vestibule shall be achieved with a maximum of 4 steps of which one may be external.
(8) Rolling stock intended to stop, in normal operation, at existing platforms below 380 mm height and having their passenger access doors above bogies need not comply with points (2) and (5) above if it can be demonstrated that this achieves a more even distribution of the steps height.
```

### n12 · answer X

- **S1:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n12 · answer Y

- **S1:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].
- **S2:** For double deck trains, it is permitted to reduce this depth value to 270 mm for the stairs accessing the upper deck and the lower deck [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n13

**Question:** What minimum size and load must a baby nappy changing table on a train have?

**[1]**

```
PRM TSI, 5.3.2.5. Baby nappy changing table
(1) The usable surface of the baby nappy changing table shall be a minimum of 500 mm wide and 700 mm long.
(2) It shall be designed to prevent a baby from inadvertently sliding off, shall have no sharp edges and shall be able to take a minimum load of 80 kg.
(3) It shall be possible to put it into the stowed position with only one hand, using a force not exceeding 25 N.
```

**[2]**

```
PRM TSI, 5.3.2.4. Universal toilet
(17) If a baby nappy changing table is provided, in the lowered position its usable surface shall be between 800 mm and 1 000 mm above floor level.
```

**[3]**

```
PRM TSI, 4.2.1.6. Toilets and baby nappy changing facilities
(1) If toilets are provided at a station, then a minimum of one unisex cubicle shall be wheelchair accessible.
(2) If baby nappy changing facilities are provided at a station, then a minimum of one baby nappy changing facility shall be accessible to both men and women wheelchair users.
```

### n13 · answer X

- **S1:** The usable surface of a baby nappy changing table on a train must be a minimum of 500 mm wide and 700 mm long [1].
- **S2:** Additionally, it must be able to take a minimum load of 80 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n13 · answer Y

- **S1:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n14

**Question:** What diameter must handrails in a passenger vehicle have, and how much clearance from adjacent surfaces?

**[1]**

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

**[2]**

```
PRM TSI, 4.2.2.1.1. General
(1) Handholds or vertical handrails or other items that can be used for personal stability, whilst using the aisle, shall be provided on all aisle-side seats unless the seat, when in the upright position, is within 200 mm of: — the back of another seat facing in the opposite direction which is fitted at its aisle side with a handhold or a vertical handrail or other items that can be used for personal stability, — a handrail or a partition provided at the aisle side of the seat.
(2) Handholds or other items that can be used for personal stability shall be positioned at a height of between 800 mm and 1 200 mm above the floor, measured from the centre of the usable part of the handhold, shall not protrude into the clearway and shall contrast with the seat.
(3) In seating areas with fixed longitudinal seats, handrails shall be used for personal stability. These handrails shall be at a maximum distance of 2 000 mm apart, shall be positioned at a height of between 800 mm and 1 200 mm above the floor and shall contrast with the vehicle interior surroundings.
(4) The handholds or other items shall not have sharp edges.
```

**[3]**

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

### n14 · answer X

- **S1:** All handrails fitted to a vehicle must be round in section with an outside diameter of 30 mm to 40 mm [1].
- **S2:** Additionally, they must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n14 · answer Y

- **S1:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n15

**Question:** What are the noise limits in the driver's cab at standstill with horns sounding, and at maximum speed below 250 km/h?

**[1]**

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

**[2]**

```
NOI TSI, 4.2.3. Limits for pass-by noise
The limit values for the A-weighted equivalent continuous sound pressure level at a speed of 80 km/h (LpAeq,Tp,(80 km/h)) and, if applicable, at 250 km/h (LpAeq,Tp,(250 km/h)) concerning the pass-by noise allocated to the categories of the rolling stock subsystem are set out in Table 4. The limit values are set at a distance of 7,5 m from the centre of the track and 1,2 m above top of rail.
Measurements at speeds higher than or equal to 250 km/h shall also be made at the ‘additional measurement position’ with a height of 3,5 m above top of rail in accordance with the specification referenced in Appendix B, Index [1] and assessed against the applicable limit values of Table 4.
Table 4
Limit values for pass-by noise
Category of the rolling stock subsystem | LpAeq,Tp (80 km/h) [dB] | LpAeq,Tp (250 km/h) [dB]
Electric locomotives and special vehicles with electric traction | 84 | 99
Diesel locomotives and special vehicles with diesel traction | 85 | n.a.
EMUs | 80 | 95
DMUs | 81 | 96
Coaches | 79 | n.a.
Wagons (normalised to APL = 0,225) (1) | 83 | n.a.
(1) APL: the number of axles divided by the length over the buffers (m-1)
The demonstration of conformity is described in point 6.2.2.3.
```

**[3]**

```
NOI TSI, 4.2.2. Limits for starting noise
The limit values for the AF-weighted maximum sound pressure level (LpAF,max) concerning the starting noise allocated to the categories of the rolling stock subsystem are set out in Table 3. The limit values are set at a distance of 7,5 m from the centre of the track and 1,2 m above top of rail.
Table 3
Limit values for starting noise
Category of the rolling stock subsystem | LpAF,max [dB]
Electric locomotives with total tractive power P < 4 500 kW | 81
Electric locomotives with total tractive power P ≥ 4 500 kW Special vehicles with electric traction | 84
Diesel locomotives P < 2 000 kW at the engine output shaft | 85
Diesel locomotives P ≥ 2 000 kW at the engine output shaft Special vehicles with diesel traction | 87
EMUs with a maximum speed vmax < 250 km/h | 80
EMUs with a maximum speed vmax ≥ 250 km/h | 83
DMUs P < 560 kW/engine at the engine output shaft | 82
DMUs P ≥ 560 kW/engine at the engine output shaft | 83
The demonstration of conformity is described in point 6.2.2.2.
```

### n15 · answer X

- **S1:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n15 · answer Y

- **S1:** The noise limit for the driver's cab at standstill with horns sounding is 95 dB [1].
- **S2:** At maximum speed vmax if vmax < 250 km/h, the noise limit is 78 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n16

**Question:** In the starting noise conformity test, up to what speed must the train accelerate?

**[1]**

```
NOI TSI, 6.2.2.2. Starting noise
The demonstration of conformity with the limit values on starting noise as set out in point 4.2.2 shall be carried out in accordance with the specification referenced in Appendix B, Index [1]. The maximum level method shall apply. Deviating from the test procedure of the specification, the train shall accelerate from standstill up to 30 km/h and then maintain the speed.
In addition the noise shall be measured at the same distance from the centre of the track and the same height above top of rail as set out in point 4.2.2. The ‘averaged level method’ and the ‘maximum level method’ in accordance with the specification referenced in Appendix B, Index [1] shall apply and the train shall accelerate from standstill up to 40 km/h and then maintain the speed. The measured values are not assessed against any limit value and shall be recorded in the technical file and communicated to the Agency.
For special vehicles the starting procedure shall be performed without additional trailer loads.
```

**[2]**

```
NOI TSI, 4.2.2. Limits for starting noise
The limit values for the AF-weighted maximum sound pressure level (LpAF,max) concerning the starting noise allocated to the categories of the rolling stock subsystem are set out in Table 3. The limit values are set at a distance of 7,5 m from the centre of the track and 1,2 m above top of rail.
Table 3
Limit values for starting noise
Category of the rolling stock subsystem | LpAF,max [dB]
Electric locomotives with total tractive power P < 4 500 kW | 81
Electric locomotives with total tractive power P ≥ 4 500 kW Special vehicles with electric traction | 84
Diesel locomotives P < 2 000 kW at the engine output shaft | 85
Diesel locomotives P ≥ 2 000 kW at the engine output shaft Special vehicles with diesel traction | 87
EMUs with a maximum speed vmax < 250 km/h | 80
EMUs with a maximum speed vmax ≥ 250 km/h | 83
DMUs P < 560 kW/engine at the engine output shaft | 82
DMUs P ≥ 560 kW/engine at the engine output shaft | 83
The demonstration of conformity is described in point 6.2.2.2.
```

**[3]**

```
NOI TSI, 6.2.2.3.1. Test track conditions
Confirmation shall be provided in the technical file that the track data related to the type's pass-by noise measurement were valid during the day(s) of testing, e.g. by providing the date of last maintenance having an impact on noise.
Furthermore, it is permitted to carry out tests at speeds equal to or higher than 250 km/h on slab tracks. In that case the limit values shall be 2 dB higher than those set out in point 4.2.3.
```

### n16 · answer X

- **S1:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [1].
- **S2:** Additionally, for the averaged level method and the maximum level method, the train shall accelerate from standstill up to 40 km/h and then maintain the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n16 · answer Y

- **S1:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n17

**Question:** What counts as a 'quieter route' under the NOI TSI?

**[1]**

```
NOI TSI, D.1 Identification of quieter routes
By the same date the Agency shall inform the Commission of the lists and maps of quieter routes. The Commission shall inform the Member States accordingly through the committee referred to in Article 51 of Directive (EU) 2016/797.
```

**[2]**

```
NOI TSI, D.1 Identification of quieter routes
In accordance with Article 5c(1), the Member States shall provide the Agency with a list of quieter routes and ensure that the infrastructure managers identify them in the RINF (application) as set out in Commission Implementing Regulation (EU) 2019/777 ( 9 ) (RINF). The list shall contain at least the following information:
— start and end points of the quieter routes and their corresponding sections, using geographical code location in the register set out in RINF. If one of those points is at the border of the Member State, it shall be reflected;
— identification of the sections making up the quieter route
The list shall be provided using the template below:
Quieter route | Sections in the route | Unique section ID | Quieter route starts/finishes at the border of the Member State
Point A — Point E | Point A — Point B | 201 | Yes POINT E (Country Y)
Point B — Point C | 202
Point C — Point D | 203
Point D — Point E | 204
Point F — Point I | Point F — Point G | 501 | No
Point G — Point H | 502
Point H — Point I | 503
In addition, the Member States may provide maps illustrating the quieter routes on a voluntary basis. All lists and maps shall be published on the Agency website (http://www.era.europa.eu) no later than 9 months after 27.5.2019.
```

**[3]**

```
NOI TSI, Article 5b
A ‘quieter route’ means a part of the railway infrastructure with a minimum length of 20 km on which the average number of daily operated freight trains during the night-time as defined in national legislation transposing Directive 2002/49/EC of the European Parliament and of the Council ( 5 ) was higher than 12. The freight traffic in the years 2015, 2016 and 2017 shall be the basis for the calculation of that average number. In case the freight traffic due to exceptional circumstances diverges in a given year from that average number by more than 25 %, the Member State concerned can calculate the average number on the basis of the remaining two years.
```

### n17 · answer X

- **S1:** A ‘quieter route’ is a part of the railway infrastructure with a minimum length of 20 km where the average number of daily operated freight trains during night-time (as defined in national legislation transposing Directive 2002/49/EC) was higher than 12, based on freight traffic data from 2015-2017 (or two years if one year deviates by more than 25 %).

- [ ] Accept  - [ ] Reject

**Note:** 

### n17 · answer Y

- **S1:** A 'quieter route' is a part of the railway infrastructure with a minimum length of 20 km on which the average number of daily operated freight trains during the night-time was higher than 12 [3].
- **S2:** This average is based on freight traffic in the years 2015, 2016, and 2017, using the definition of night-time from national legislation transposing Directive 2002/49/EC [3].
- **S3:** If freight traffic in a given year diverges by more than 25 % due to exceptional circumstances, the average may be calculated using the remaining two years [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n18

**Question:** How often must staff doing safety-critical tasks have a periodic medical examination under the OPE TSI?

**[1]**

```
OPE TSI, 4.7.2.2.1. Frequency of periodic medical examinations
At least one systematic medical examination shall be performed:
— Every 5 years for staff aged up to 40;
— Every 3 years for staff aged between 41 and 62;
— Every year for staff aged over 62.
Increased frequency of examination shall be set by the medical doctor if the state of health of the member of the staff requires so.
```

**[2]**

```
OPE TSI, 4.7.2.2.2. Content of the periodic medical examination
If the worker complies with the criteria required at the examination, which is carried out before practising an occupation, the periodic specialised examinations shall include ————— :
— General medical examination;
— Examination of sensory functions (vision, hearing, colour perception);
— Urine or blood analysis for the detection of diabetes mellitus and other conditions as indicated by the clinical examination;
— Screening for abuse of drugs where clinically indicated.
```

**[3]**

```
OPE TSI, 4.7.2.2.3. Additional medical examinations and/or psychological assessments
Besides the periodic medical examination, an additional specific medical examination and/or psychological assessment shall be performed where there is reasonable ground for doubting the medical or psychological fitness of a member of staff or reasonable suspicion of use of drugs or use of alcohol over the limits allowed. This would be the case especially after an incident or accident caused by human error on the part of the individual.
The railway undertaking and the infrastructure manager shall put systems in place to ensure that such additional examinations and assessments are undertaken as appropriate.
```

### n18 · answer X

- **S1:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1].
- **S2:** Additionally, an increased frequency must be set by the medical doctor if the staff member's state of health requires it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n18 · answer Y

- **S1:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n19

**Question:** When should a driver avoid using manually activated sanding equipment, and when is sanding still appropriate there?

**[1]**

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

**[2]**

```
CCS TSI, 7.7.2.9. Italy
Specific case | Category | Notes
4.2.10 Trackside Train Detection Systems Index 77, point 3.1.4.1 In addition to the TSI requirements, following criteria shall be respected. The allowed maximum amount of sand per sanding device within 30 s is: (1) For speed v ≤ 140 km/h; 400 g + 100 g (2) For speed v > 140 km/h; 650 g + 150 g | T | The national values for dispensing sand will remain valid until harmonized test specifications (currently non-existent) are available for demonstrating that different modes for dispensing sand are safety-acceptable for train detection systems operating in Italy.
```

**[3]**

```
CCS TSI, 7.7.2.7. Luxembourg
Specific case | Category | Notes
4.2.10 Trackside Train Detection Systems Index 77, point 3.1.4.1: (1) The output of the sanding devices fitted to the vehicle shall not exceed 0,3 l per minute per rail. (2) The sanding in the stations identified in the infrastructure register is prohibited. (3) The Sanding in the area of switches is prohibited. (4) For emergency braking, no restrictions shall apply. | T | 
4.2.11 Electromagnetic Compatibility between Rolling Stock and Control-Command and Signalling trackside equipment Index 77, point 3.2.2.3: The measurement and evaluation of rolling stock with individual track circuits shall be done according to the document GI.II.STC-VF (parameters A1, A4, V2 and D1). | T | Applicable on vehicles This specific case is needed as long as track circuits (operating frequency 83,3 Hz) are used. Document GI.II.STC.VF is available on the website of the NSA LU (1).
4.2.11 Electromagnetic Compatibility between Rolling Stock and Control-Command and Signalling trackside equipment Index 77, point 3.2.2.3: The measurement and evaluation of rolling stock with individual track circuits shall be done according to the document GI.II.STC-VF (parameters A5, V2 and D2). | T | Applicable on vehicles This specific case is needed as long as track circuits (operating frequency 125 Hz) are used. Document GI.II.STC.VF is available on the website of the NSA LU.
(1) ‘NSA LU’ stands for ‘National Safety Authority of Luxembourg’: Administration des Chemins de Fer (ACF), www.railinfra.lu (website).
```

### n19 · answer X

- **S1:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].
- **S2:** However, sanding is still appropriate if there is a risk of SPAD (Signal Passed At Danger) or another serious incident and applying sand assists adhesion, when starting away, or when required to test the sanding equipment on the traction unit [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n19 · answer Y

- **S1:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].
- **S2:** Sanding is still appropriate if there is a risk of SPAD or another serious incident and sand would improve adhesion, when starting away, or when required to test the sanding equipment on the traction unit[1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n20

**Question:** For trains able to run faster than 200 km/h, what braking information may the infrastructure manager provide?

**[1]**

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(2) The infrastructure manager may provide the following information: (i) For trains able to run at a maximum speed higher than 200 km/h, deceleration profile and equivalent response time on level track; (ii) For trainsets or for fixed train compositions, unable to run at a maximum speed higher than 200 km/h, deceleration (as above in (i)) or brake weight percentage; (iii) For other trains (variable compositions of trains unable to run at a maximum speed higher than 200 km/h): brake weight percentage. If the infrastructure manager provides the above mentioned information, it shall be made available to all railway undertakings who intend to operate trains on its network in a non-discriminatory way. The braking tables already in use and accepted for the existing non TSI conform lines at the date of entry into force of the present Regulation shall also be made available.
```

**[2]**

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(1) The infrastructure manager shall provide the railway undertaking with all relevant line characteristics for each route through RINF: (i) signalling distances (warning, stopping) containing their inherent safety margins, that are provided via the respective locations of ‘Stopping signal’ and ‘Warning signal’, requested in Appendix D2 via the parameter 1.1.1.3.14.3; (ii) gradients; (iii) maximum permitted speeds; (iv) conditions of use of braking systems possibly affecting the infrastructure such as magnetic, regenerative and eddy current brake. The infrastructure manager shall ensure that the information provided to the railway undertaking(s) is complete and accurate, and shall inform the railway undertaking of the changes on the line characteristics through RINF whenever such information becomes available and affects trains operation.
```

**[3]**

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(3) The railway undertaking shall, in the planning stage, determine the braking regime, the braking capability and corresponding maximum speed of the train taking into account: (i) the relevant line characteristics as expressed in point (1) and, if available, the information provided by the infrastructure manager in accordance to point (2); and (ii) the rolling stock-related margins derived from reliability and availability of the braking system. Furthermore, the railway undertaking shall ensure that during operation each train achieves at least the necessary braking performance. In particular the railway undertaking has to set up rules to be used if a train does not reach the necessary braking performance during operation. In this case, the railway undertaking shall immediately inform the infrastructure manager. The infrastructure manager may take appropriate measures to reduce the impact on the overall traffic on its network.
```

### n20 · answer X

- **S1:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n20 · answer Y

- **S1:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n21

**Question:** After the Commission mandates it, how quickly must the Agency start consulting the parties about a Member State's measure against a non-compliant interoperability constituent?

**[1]**

```
Interoperability Directive, Article 11 — Non-compliance of interoperability constituents with essential requirements
1. Where a Member State finds that an interoperability constituent covered by the ‘EC’ declaration of conformity or suitability for use and placed on the market is, when used as intended, unlikely to meet the essential requirements, that Member State shall take all necessary steps to restrict its field of application, prohibit its use, withdraw it from the market or recall it. The Member State shall forthwith inform the Commission, the Agency and the other Member States of the measures taken and give reasons for its decision, stating in particular whether the failure to conform is due to: (a) failure to meet the essential requirements; (b) incorrect application of European specifications where application of such specifications is relied upon; (c) inadequacy of European specifications.
2. The Agency, on a mandate from the Commission, shall start the consultation process with the parties concerned without delay and in any case within 20 days of the date of receipt of that mandate. Where, following that consultation, the Agency establishes that the measure is unjustified, it shall forthwith inform the Commission, the Member State that has taken the initiative as well as other Member States, and the manufacturer or his authorised representative. Where the Agency establishes that the measure is justified, it shall forthwith inform the Member States.
```

**[2]**

```
Interoperability Directive, Article 53 — Reports and information
1. By 16 June 2018, the Commission shall report on the progress made in preparing for the Agency's enhanced role under this Directive. Additionally, every three years and for the first time three years after the end of the transitional period provided for by Article 54, the Commission shall report to the European Parliament and to the Council on the progress made towards achieving interoperability of the Union rail system and the functioning of the Agency in this context. That report shall also include an evaluation of the implementation and use of the registers under Chapter VII and an analysis of the cases set out in Article 7 and of the application of Chapter V, assessing in particular the functioning of the cooperation agreements concluded between the Agency and national safety authorities. For the purposes of the first report, after the end of the transitional period the Commission shall carry out extensive consultations with the relevant stakeholders and shall establish a programme to allow for the assessment of progress. The Commission shall, if appropriate in the light of the above analysis, propose legislative measures including measures for the future role of the Agency in enhancing interoperability.
2. The Agency shall develop and periodically update a tool capable of providing, at the request of a Member State, the European Parliament or of the Commission, an overview of the interoperability level of the Union rail system. That tool shall use the information included in the registers provided for in Chapter VII.
```

**[3]**

```
Interoperability Directive, Article 50 — Exercise of delegation
1. The power to adopt delegated acts is conferred on the Commission subject to the conditions laid down in this Article.
2. The power to adopt delegated acts referred to in Article 5(1) shall be conferred on the Commission for a period of five years from 15 June 2016. The Commission shall draw up a report in respect of the delegation of power not later than nine months before the end of the five-year period. The delegation of power shall be tacitly extended for periods of an identical duration, unless the European Parliament or the Council opposes such extension not later than three months before the end of each period.
3. It is of particular importance that the Commission follow its usual practice and carry out consultations with experts, including Member States' experts, before adopting those delegated acts.
4. The delegation of power referred to in Article 5(1) may be revoked at any time by the European Parliament or by the Council. A decision of revocation shall put an end to the delegation of the power specified in that decision. It shall take effect the day following the publication of the decision in the Official Journal of the European Union or at a later date specified therein. It shall not affect the validity of any delegated acts already in force.
5. As soon as it adopts a delegated act, the Commission shall notify it simultaneously to the European Parliament and to the Council.
```

### n21 · answer X

- **S1:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n21 · answer Y

- **S1:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

## n22

**Question:** What speeds characterise specially built and specially upgraded high-speed lines in the Union's network?

**[1]**

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

**[2]**

```
ENE TSI, 7.3.1. Performance criteria of the subsystem
In addition to the cases referred to in point 7.2.(3), ‘upgrading’ is a major modification work of an existing energy subsystem resulting in an increase of the line speed of more than 30km/h.
```

**[3]**

```
Interoperability Directive, 2. Vehicles
For the purposes of this Directive, Union vehicles shall comprise all vehicles likely to travel on all or part of the Union's network:
— locomotives and passenger rolling stock, including thermal or electric traction units, self-propelling thermal or electric passenger trains, and passenger coaches;
— freight wagons, including low-deck vehicles designed for the entire network and vehicles designed to carry lorries;
— special vehicles, such as on-track machines.
This list of vehicles shall include those which are specially designed to operate on the different types of high-speed lines described in point 1.
```

### n22 · answer X

- **S1:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n22 · answer Y

- **S1:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [1].
- **S2:** Specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n23

**Question:** What exercise is required before a railway tunnel longer than 1 km opens?

**[1]**

```
SRT TSI, 4.4.3. Exercises
These rules apply to tunnels of > 1 km.
(a) Prior to the opening of a single tunnel or a series of tunnels, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, shall take place.
(b) The emergency plan shall define how all organisations involved can be familiarised with the infrastructure and how often visits to the tunnel and table top or other exercises have to take place.
```

**[2]**

```
SRT TSI, 4.4.6. Operational rules related to trains running in tunnels
(b) Operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points , or the length of tunnels exceeds 5 km, in the case where there are no passengers on board.
(c) Operational rules shall be put in place to avoid panic and spontaneous, uncontrolled evacuation in the case of a prolonged stop of a train in a tunnel without the occurrence of a hot or cold incident.
```

**[3]**

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
This specification applies to all tunnels of more than 1 km in length.
(a) For the purpose of this clause, two or more consecutive tunnels will be considered as a single tunnel unless both of the following conditions are met: (1) The separation between tunnels in open air is longer than the maximum length of the passenger train intended to be operated on the line + 100 m and (2) The open air area and track situation around the separation between tunnels allow passengers to move away from the train along a a safe space . The open air area shall contain all passengers of the maximum capacity of the train intended to be operated on the line.
(b) Evacuation and rescue points shall be created (1) Outside both portals of every tunnel of > 1 km and (2) Inside the tunnel, according to the category of rolling stock that is planned to be operated, as summarized in the table below: Rolling stock category according to paragraph 4.2.3 | Maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points Category A | 5 km Category B | 20 km
```

### n23 · answer X

- **S1:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n23 · answer Y

- **S1:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n24

**Question:** In a tunnel longer than 1 km where the traction power supply is divided into sections, what must be possible?

**[1]**

```
SRT TSI, 4.2.2.1. Sectioning of contact line
This specification applies to all tunnels of more than 1 km length.
(a) The traction power supply system in tunnels may be divided into sections.
(b) In such case, it shall be possible to switch off each section of the contact line, either locally or remotely.
```

**[2]**

```
ENE TSI, 4.2.16.1. General
(1) The design of system separation sections shall ensure that trains can move from one traction power supply system to an adjacent different traction power supply system without bridging the two systems. There are two methods for traversing system separation sections: (a) with pantograph raised and touching the contact wire; (b) with pantograph lowered and not touching the contact wire.
(2) The neighbouring Infrastructure Managers shall agree either (a) or (b) according to the prevailing circumstances.
(3) The overall length D of neutral sections is defined in the specification referenced in Appendix E, Index [2]. For the calculation of D clearances, the specification referenced in Appendix E, Index [3] and an uplift of S0 shall be taken into account.
```

**[3]**

```
SRT TSI, 4.4.4. Switching off and Earthing procedures
These rules apply to all tunnels.
(a) In the case it is required to switch off the traction power supply system the infrastructure manager shall make sure that relevant sections of the contact line have been switched off, and inform the emergency response services before they enter the tunnel or a section of the tunnel.
(b) It is the responsibility of the infrastructure manager to switch off the traction power supply.
(c) Procedures and responsibilities for earthing of the contact line shall be defined between the Infrastructure Manager and the emergency response services, and reported in the emergency plan. Provision shall be made for switching off the section in which the incident has taken place.
```

### n24 · answer X

- **S1:** It must be possible to switch off each section of the contact line, either locally or remotely [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### n24 · answer Y

- **S1:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, either locally or remotely [1].

- [ ] Accept  - [ ] Reject

**Note:** 
