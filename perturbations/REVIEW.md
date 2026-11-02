# Review: planted errors (blinded)

306 planted errors. Each shows one sentence before and after the change; every
other sentence of the answer is unchanged (checked by code). The generator is hidden.

**Accept an item only if all four hold:**
1. the *after* sentence is **not supported** by the passage(s) it cites, read carefully;
2. it is grammatical and plausible (something a model could have written);
3. the type label is right;
4. for `CITE`: the newly cited passage really does not support the sentence.

Tick `[x] Accept` or `[x] Reject`; write a reason in **Note** for each rejection.
A rejected item gets one replacement of the same type, which you review again.

**Tip:** if you accept everything for a question, you may write `ALL OK` under its
heading instead of ticking each box.

## q01

**Question:** What is the stationary noise limit LpAeq,T for an electric multiple unit (EMU)?

<details><summary>[1] NOI TSI, 4.2.1. Limits for stationary noise</summary>

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

</details>

<details><summary>[2] NOI TSI, 6.2.2.3.2.1. EMU, DMUs, locomotives and coaches</summary>

```
NOI TSI, 6.2.2.3.2.1. EMU, DMUs, locomotives and coaches
For EMU, DMUs, locomotives and coaches three classes of maximum operational speed are distinguished:
(1) If the maximum operational speed of the unit is lower than or equal to 80 km/h, the pass-by noise shall be measured at its maximum speed vmax. That value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3.
(2) If the maximum operational speed vmax of the unit is higher than 80 km/h and lower than 250 km/h, the pass-by noise shall be measured at 80 km/h and at its maximum speed. Both measured pass-by noise values LpAeq,Tp(Vtest) shall be normalised to the reference speed of 80 km/h LpAeq,Tp(80 km/h) using Formula (1). The normalised value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (1): LpAeq,Tp(80 km/h) = LpAeq,Tp(Vtest) – 30 * log (vtest/80 km/h) vtest | = | Actual speed during the measurement
```

</details>

<details><summary>[3] NOI TSI, 4.2.4. Limits for the driver's cab interior noise</summary>

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

</details>

### R001 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].
- **After:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R002 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].
- **After:** For an electric multiple unit (EMU), the stationary noise level LpAeq,T[unit] must be at least 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R003 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].
- **After:** For all rolling stock, the stationary noise limit LpAeq,T[unit] is 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R004 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].
- **Appended:** This limit is measured with the main air compressor running for at least 10 minutes [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R005 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].
- **After:** The stationary noise level LpAeq,T for an EMU must be at least 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R006 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].
- **After:** The stationary noise limit LpAeq,T for an EMU is 65 dB [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R007 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].
- **Appended:** This limit is measured with the main air compressor running for at least 10 minutes [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R008 · `NUM` · in-context

_a number was changed_

- **Before:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].
- **After:** The stationary noise limit LpAeq,T for an EMU is 64 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R009 · `NUM` · in-context

_a number was changed_

- **Before:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 65 dB [1].
- **After:** For an electric multiple unit (EMU), the stationary noise limit LpAeq,T[unit] is 64 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R010 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The stationary noise limit LpAeq,T for an EMU is 65 dB [1].
- **After:** The stationary noise limit LpAeq,T for all rolling stock is 65 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q02

**Question:** What is the pass-by noise limit for freight wagons at 80 km/h?

<details><summary>[1] NOI TSI, 4.2.3. Limits for pass-by noise</summary>

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

</details>

<details><summary>[2] NOI TSI, 6.2.2.3.2.2. Wagons</summary>

```
NOI TSI, 6.2.2.3.2.2. Wagons
For wagons two classes of maximum operational speed are distinguished:
(1) If the maximum operational speed vmax of the unit is lower than or equal to 80 km/h, the pass-by noise shall be measured at its maximum speed. The measured pass-by noise value LpAeq,Tp(Vtest) shall be normalised to a reference APL of 0,225 m-1 LpAeq,Tp (APLref) using Formula (3). That value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (3): LpAeq,Tp (APLref) = LpAeq,Tp(Vtest) – 10 * log(APLwag/0,225 m-1) APLwag | = | Number of axles divided by the length over the buffers [m-1] vtest | = | Actual speed during the measurement
(2) If the maximum operational speed vmax of the unit is higher than 80 km/h, the pass-by noise shall be measured at 80 km/h and at its maximum speed. Both measured pass-by noise values LpAeq,Tp(Vtest) shall be normalised to the reference speed of 80 km/h and to a reference APL of 0,225 m-1 LpAeq,Tp(APL ref, 80 km/h) using Formula (4). The normalised value shall not exceed the limit value LpAeq,Tp(80 km/h) as set out in point 4.2.3. Formula (4): LpAeq,Tp (APLref, 80 km/h) = LpAeq,Tp(Vtest) – 10 * log(APLwag/0,225 m-1) — 30 * log(vtest/80 km/h) APLwag | = | Number of axles divided by the length over the buffers [m-1] vtest | = | Actual speed during the measurement
```

</details>

<details><summary>[3] NOI TSI, (b) Specific case Sweden</summary>

```
NOI TSI, (b) Specific case Sweden
(‘T’) For locomotives with total tractive power of more than 6 000 kW and a maximum axle load of more than 25 t the limit values for pass-by noise LpAeq,Tp (80 km/h) in Table 4 may be raised up to 85 dB.
```

</details>

### R011 · `NUM` · in-context

_a number was changed_

- **Before:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB [1].
- **After:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 81 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R012 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB [1].
- **After:** The pass-by noise level of wagons (normalised to APL = 0,225) at 80 km/h must be at least 83 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R013 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB [1].
- **Appended:** The limit is relaxed for wagons that entered service before 2005 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R014 · `NUM` · in-context

_a number was changed_

- **Before:** The pass-by noise limit for wagons at 80 km/h is 83 dB(A) [1].
- **After:** The pass-by noise limit for wagons at 80 km/h is 81 dB(A) [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R015 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The pass-by noise limit for wagons at 80 km/h is 83 dB(A) [1].
- **Appended:** The limit is relaxed for wagons that entered service before 2005 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R016 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The pass-by noise limit for wagons at 80 km/h is 83 dB(A) [1].
- **After:** The pass-by noise limit for wagons at all speeds is 83 dB(A) [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R017 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The pass-by noise limit for wagons at 80 km/h is 83 dB(A) [1].
- **After:** The pass-by noise level of wagons at 80 km/h must be at least 83 dB(A) [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R018 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB [1].
- **After:** The pass-by noise limit for wagons (normalised to APL = 0,225) at all speeds is 83 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q03

**Question:** How wide must an escape walkway in a railway tunnel be, and how much headroom must it have?

<details><summary>[1] SRT TSI, 4.2.1.6. Escape walkways</summary>

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

</details>

<details><summary>[2] SRT TSI, 4.2.1.5.2 Access to the safe area</summary>

```
SRT TSI, 4.2.1.5.2 Access to the safe area
This specification applies to all tunnels of more than 1 km in length.
(a) Safe areas shall be accessible for people who commence self-evacuation from the train as well as for the emergency response services.
(b) One of the following solutions shall be selected for access points from a train to the safe area: (1) Lateral and/or vertical emergency exits to the surface. These exits shall be provided at least every 1 000 m. (2) Cross-passages between adjacent independent tunnel tubes, which enable the adjacent tunnel tube to be employed as a safe area. Cross-passages shall be provided at least every 500 m. —————
(c) Doors giving access from the escape walkway to the safe area shall have a minimum clear opening of 1,4 m wide and 2,0 m high. Alternatively it is permitted to use multiple doors next to each other which are less wide as long as the flow capacity of people is demonstrated to be equivalent or higher.
(d) After passing the doors, the clear width shall continue to be at least 1,5 m wide and 2,25 m high.
(e) The way in which the emergency response services access the safe area shall be described in the emergency plan.
```

</details>

<details><summary>[3] PRM TSI, 4.2.1.2.2. Vertical circulation</summary>

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

</details>

### R019 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].
- **After:** The escape walkway should be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R020 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].
- **After:** The width of the escape walkway must be at most 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R021 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].
- **Appended:** Walkways must be at least 1,2 m wide in tunnels used by trains running faster than 200 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R022 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1]. The minimum vertical clearance above the walkway must be 2.25 m [1].
- **Appended:** Walkways must be at least 1,2 m wide in tunnels used by trains running faster than 200 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R023 · `NUM` · in-context

_a number was changed_

- **Before:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].
- **After:** The width of the escape walkway must be at least 1.1 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R024 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].
- **After:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R025 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The width of the escape walkway must be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].
- **After:** The width of the escape walkway should be at least 0.8 m, though local constrictions caused by obstacles shall not reduce the minimum width to less than 0,7 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R026 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].
- **After:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R027 · `NUM` · in-context

_a number was changed_

- **Before:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].
- **After:** The escape walkway must be at least 1.1 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R028 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The escape walkway must be at least 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].
- **After:** The escape walkway must be at most 0.8 m wide and have a minimum vertical clearance (headroom) of 2.25 m above it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q05

**Question:** What is the maximum distance between evacuation and rescue points in a tunnel for Category A and for Category B passenger rolling stock, and what is the difference between the two categories?

<details><summary>[1] SRT TSI, 4.2.1.7. Evacuation and rescue points</summary>

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
This specification applies to all tunnels of more than 1 km in length.
(a) For the purpose of this clause, two or more consecutive tunnels will be considered as a single tunnel unless both of the following conditions are met: (1) The separation between tunnels in open air is longer than the maximum length of the passenger train intended to be operated on the line + 100 m and (2) The open air area and track situation around the separation between tunnels allow passengers to move away from the train along a a safe space . The open air area shall contain all passengers of the maximum capacity of the train intended to be operated on the line.
(b) Evacuation and rescue points shall be created (1) Outside both portals of every tunnel of > 1 km and (2) Inside the tunnel, according to the category of rolling stock that is planned to be operated, as summarized in the table below: Rolling stock category according to paragraph 4.2.3 | Maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points Category A | 5 km Category B | 20 km
```

</details>

<details><summary>[2] SRT TSI, 4.4.6. Operational rules related to trains running in tunnels</summary>

```
SRT TSI, 4.4.6. Operational rules related to trains running in tunnels
(b) Operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points , or the length of tunnels exceeds 5 km, in the case where there are no passengers on board.
(c) Operational rules shall be put in place to avoid panic and spontaneous, uncontrolled evacuation in the case of a prolonged stop of a train in a tunnel without the occurrence of a hot or cold incident.
```

</details>

<details><summary>[3] SRT TSI, 4.2.1.7. Evacuation and rescue points</summary>

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
(e) Requirements for evacuation and rescue points inside the tunnel In addition to the requirements in 4.2.1.7 (c), evacuation and rescue points inside the tunnel shall comply with the following requirements (1) A safe area shall be accessible from the stopping position of the train. Dimensions of the evacuation route to the safe area shall consider the evacuation time (as specified in clause 4.2.3.4.1) and the planned capacity of the trains (referred to in clause 4.2.1.5.1) intended to be operated in the tunnel. The adequacy of the sizing of the evacuation route shall be demonstrated. (2) The safe area that is paired with the evacuation and rescue point shall offer a sufficient standing surface relative to the time passengers are expected to wait until they are evacuated to a final place of safety. (3) There shall be an access to the affected train for emergency response services without going through the occupied safe area. (4) The lay-out of the evacuation and rescue point and its equipment shall take into account the control of smoke, in particular to protect people who use the self-evacuation facilities to access the safe area.
```

</details>

<details><summary>[4] SRT TSI, 4.2.3. Subsystem rolling stock</summary>

```
SRT TSI, 4.2.3. Subsystem rolling stock
(a) In the context of this TSI the subsystem rolling stock is subdivided into the following categories. (1) Category A passenger rolling stock (including passenger locomotives) for operation on lines within the scope of this TSI, where the distance between evacuation and rescue points or the length of tunnels does not exceed 5 km. (2) Category B passenger rolling stock (including passenger locomotives) for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels. (3) Freight locomotives and self-propelling units designed to carry payload other than passengers, such as mail and freight for example, for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels. Locomotives designed to haul freight trains as well as passenger trains fall under both categories and shall respect the requirements of both categories. (4) Self-powered on-track machines, when in transport mode, for operation in all tunnels on lines within the scope of this TSI, irrespective of the length of the tunnels.
(b) The rolling stock category shall be recorded in the technical file and will remain valid regardless of future revisions of this TSI.
```

</details>

### R029 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1].
- **After:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R030 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The maximum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 20 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].
- **After:** The minimum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 20 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R031 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1].
- **After:** The minimum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R032 · `NUM` · in-context

_a number was changed_

- **Before:** The maximum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 20 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].
- **After:** The maximum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 5 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R033 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Additionally, operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points or the length of tunnels exceeds 5 km only when there are no passengers on board [2].
- **After:** Additionally, operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points or the length of tunnels exceeds 5 km [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R034 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1]. Category A passenger rolling stock is for operation on lines where the distance between evacuation and rescue points or the length of tunnels does not exceed 5 km, whereas Category B passenger rolling stock is for operation in all tunnels on lines within the scope of the TSI, irrespective of the length of the tunnels [4]. Additionally, operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points or the length of tunnels exceeds 5 km only when there are no passengers on board [2].
- **Appended:** Category B rolling stock must keep running for 15 minutes at 80 km/h after a fire is detected [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R035 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The maximum distance between evacuation and rescue points in a tunnel is 5 km for Category A passenger rolling stock and 20 km for Category B passenger rolling stock, giving a difference of 15 km between the two categories [1].
- **Appended:** Category B rolling stock must keep running for 15 minutes at 80 km/h after a fire is detected [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R036 · `NUM` · in-context

_a number was changed_

- **Before:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 20 km for Category B [1].
- **After:** The maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points is 5 km for Category A and 5 km for Category B [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q06

**Question:** How many wheelchair spaces must a 250 m long passenger unit have?

<details><summary>[1] PRM TSI, 4.2.2.2. Wheelchair spaces</summary>

```
PRM TSI, 4.2.2.2. Wheelchair spaces
(1) According to the length of the unit, excluding the locomotive or power head, there shall be in that unit not less than the number of accessible wheelchair spaces shown in the following table: Table 5 Minimum number of wheelchair spaces per unit length Unit length | Number of wheelchair spaces by unit Less than 30 m | 1 wheelchair space 30 to 205 metres | 2 wheelchair spaces More than 205 to 300 metres | 3 wheelchair spaces More than 300 metres | 4 wheelchair spaces
(2) To ensure stability, the wheelchair space shall be designed for the wheelchair to be positioned either facing or back to the direction of travel.
(3) Over the full length of the wheelchair space the width shall be 700 mm from floor level to a minimum height of 1 450 mm with an additional 50 mm width to give clearance for hands on each side that is adjacent to any obstacle that will inhibit clearance for the wheelchair users hands (e.g. wall or structure) from a height of 400 mm to 800 mm above floor level (if one side of the wheelchair is adjacent to the aisle there is no additional 50 mm requirement for that side of the wheelchair as it is already free space).
(4) The minimum distance in the longitudinal plane between the back of the wheelchair space and the next surface shall be in accordance with the specification referenced in Appendix A, Index [16].
```

</details>

<details><summary>[2] PRM TSI, 4.2.2.2. Wheelchair spaces</summary>

```
PRM TSI, 4.2.2.2. Wheelchair spaces
(10) On trains with a design speed higher than 250 km/h excepting double deck trains, it shall be possible for a wheelchair user occupying a wheelchair space to transfer onto a passenger seat that shall be equipped with a movable armrest. Such transfer is made by the wheelchair user in autonomy. In that case, it is allowed that the companion seat is shifted to another row. This requirement is applicable up to the number of wheelchair spaces per unit specified in table 5.
(11) The wheelchair space shall be fitted with a call for aid device that shall, in the event of danger, provide to a wheelchair user the possibility to inform a person who can take appropriate action.
(12) The call for aid device shall be placed within the comfortable reach range of the person using the wheelchair as shown in the specification referenced in Appendix A, Index [9].
(13) The call for aid device shall not be placed within a narrow recess which prevents immediate intentional palm operation but can be protected from unintentional use.
(14) The interface of the call for aid device shall be as set out in point 5.3.2.6.
(15) A sign conforming to appendix N shall be placed immediately next to, or in the wheelchair space so as to identify the space as the wheelchair space.
```

</details>

<details><summary>[3] PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network</summary>

```
PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network
The number of wheelchair spaces is limited to two for any unit intended to be used on Ile de France Express network lines A B C D and E independently of its length.
```

</details>

### R037 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].
- **After:** A passenger unit that is 250 m long must have 3 wheelchair spaces [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R038 · `NUM` · in-context

_a number was changed_

- **Before:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].
- **After:** A passenger unit that is 250 m long must have 4 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R039 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].
- **After:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R040 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].
- **Appended:** Each wheelchair space must have its own power socket for electric wheelchairs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R041 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].
- **After:** A passenger unit of any length must have not less than 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R042 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].
- **After:** A passenger unit of any length must have 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R043 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].
- **After:** A passenger unit with a length of more than 205 to 300 metres must have not more than 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R044 · `NUM` · in-context

_a number was changed_

- **Before:** A passenger unit with a length of more than 205 to 300 metres must have not less than 3 wheelchair spaces [1].
- **After:** A passenger unit with a length of more than 205 to 300 metres must have not less than 4 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R045 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].
- **After:** A passenger unit that is 250 m long may have at most 3 wheelchair spaces [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R046 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A passenger unit that is 250 m long must have 3 wheelchair spaces [1].
- **Appended:** Each wheelchair space must have its own power socket for electric wheelchairs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q07

**Question:** What is the minimum clear usable width of exterior passenger doors, and of wheelchair access doors with level access?

<details><summary>[1] PRM TSI, 4.2.2.3.2. Exterior doors</summary>

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

</details>

<details><summary>[2] PRM TSI, 4.2.1.3. Doors and entrances</summary>

```
PRM TSI, 4.2.1.3. Doors and entrances
(1) This point applies to all doors and entrances that are on obstacle-free routes, with the exception of doors giving access to the toilets which are not dedicated to persons with disabilities and persons with reduced mobility.
(2) Doors shall have a minimum clear useable width of 90 cm and shall be operable by persons with disabilities and persons with reduced mobility.
(3) It is permitted to use manual, semi-automatic or automatic doors.
(4) Door operating devices shall be available at a height of between 80 cm and 110 cm.
```

</details>

<details><summary>[3] PRM TSI, 4.2.2.3.3. Interior doors</summary>

```
PRM TSI, 4.2.2.3.3. Interior doors
(1) Internal automatic and semi-automatic doors shall incorporate devices that prevent passengers becoming trapped during operation of the doors.
(2) Interior doors that are made available for wheelchair users shall have a minimum clear useable width of 800 mm.
(3) The force required to open or close a manual door shall not exceed 60 N.
(4) The centre of interior door controls shall be not less than 800 mm and not more than 1 100 mm measured vertically above the vehicle floor level.
(5) Automatic inter-vehicle connecting doors shall operate either synchronously as a pair, or the second door shall automatically detect the person moving towards it and open.
(6) If more than 75 % of a door's surface is made of a transparent material, it shall be clearly marked with visual indicators.
```

</details>

### R047 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [1].
- **After:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R048 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Wheelchair access doors offering level access must have a minimum clear usable width of 1 000 mm when open[1].
- **After:** Wheelchair access doors offering level access should have a minimum clear usable width of 1 000 mm when open[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R049 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [1]. On trains with a design speed lower than 250 km/h, wheelchair access doors offering a level access shall have a minimum clear useable width of 1 000 mm when open [1].
- **Appended:** Doors used for wheelchair access must also have a minimum clear height of 1 900 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R050 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [1].
- **After:** All exterior passenger doorways shall have a maximum clear useable width of 800 mm when open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R051 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The minimum clear usable width of exterior passenger doors is 800 mm when open[1]. Wheelchair access doors offering level access must have a minimum clear usable width of 1 000 mm when open[1].
- **Appended:** Doors used for wheelchair access must also have a minimum clear height of 1 900 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R052 · `NUM` · out-of-context

_a number was changed_

- **Before:** Wheelchair access doors offering level access must have a minimum clear usable width of 1 000 mm when open[1].
- **After:** Wheelchair access doors offering level access must have a minimum clear usable width of 1 050 mm when open[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R053 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The minimum clear usable width of exterior passenger doors is 800 mm when open[1].
- **After:** The minimum clear usable width of exterior passenger doors is 800 mm when open [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R054 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** All exterior passenger doorways shall have a minimum clear useable width of 800 mm when open [1].
- **After:** All exterior passenger doorways should have a minimum clear useable width of 800 mm when open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R055 · `NUM` · out-of-context

_a number was changed_

- **Before:** On trains with a design speed lower than 250 km/h, wheelchair access doors offering a level access shall have a minimum clear useable width of 1 000 mm when open [1].
- **After:** On trains with a design speed lower than 250 km/h, wheelchair access doors offering a level access shall have a minimum clear useable width of 1 050 mm when open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R056 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The minimum clear usable width of exterior passenger doors is 800 mm when open[1].
- **After:** The maximum clear usable width of exterior passenger doors is 800 mm when open[1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q08

**Question:** Which traction power supply systems does the Energy TSI allow, and which may be used on new lines faster than 250 km/h?

<details><summary>[1] ENE TSI, 2.1.1. Traction power supply</summary>

```
ENE TSI, 2.1.1. Traction power supply
(1) The objective of the traction power supply system is to supply every train with power in order to meet the planned timetable.
(2) Basic parameters for traction power supply system are set out in point 4.2.
```

</details>

<details><summary>[2] ENE TSI, 7.1.1. Implementation rules for voltage and frequency</summary>

```
ENE TSI, 7.1.1. Implementation rules for voltage and frequency
New lines with speed greater than 250 km/h shall be supplied with one of the AC systems listed in point 4.2.3 (a) and (b).
```

</details>

<details><summary>[3] ENE TSI, 7.2. Application of this TSI to a new energy subsystem</summary>

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

</details>

<details><summary>[4] ENE TSI, 4.2.3. Voltage and frequency</summary>

```
ENE TSI, 4.2.3. Voltage and frequency
The nominal voltage and nominal frequency of the traction power supply system shall be one of the four systems:
(a) AC 25 kV, 50 Hz;
(b) AC 15 kV, 16,7 Hz;
(c) DC 3 kV;
(d) DC 1,5 kV.
For new lines with speed greater than 250 km/h, implementation rules are specified in point 7.1.1.
```

</details>

### R057 · `NUM` · in-context

_a number was changed_

- **Before:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 16,7 Hz, DC 3 kV and DC 1,5 kV [4].
- **After:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 50 Hz, DC 3 kV and DC 1,5 kV [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R058 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 16,7 Hz, DC 3 kV and DC 1,5 kV [4].
- **After:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 16,7 Hz, DC 3 kV and DC 1,5 kV [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R059 · `NUM` · in-context

_a number was changed_

- **Before:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 16,7 Hz; DC 3 kV; and DC 1,5 kV [4].
- **After:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 50 Hz; DC 3 kV; and DC 1,5 kV [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R060 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Energy TSI permits four traction power supply systems: AC 25 kV 50 Hz, AC 15 kV 16,7 Hz, DC 3 kV and DC 1,5 kV [4]. For new lines with speeds greater than 250 km/h, only the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].
- **Appended:** The DC 1,5 kV system may only be used on lines with speeds below 160 km/h [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R061 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** New lines with a speed greater than 250 km/h must be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].
- **After:** New lines with a speed greater than 250 km/h must not be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R062 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 16,7 Hz; DC 3 kV; and DC 1,5 kV [4]. New lines with a speed greater than 250 km/h must be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].
- **Appended:** The DC 1,5 kV system may only be used on lines with speeds below 160 km/h [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R063 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For new lines with speeds greater than 250 km/h, only the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].
- **After:** For new lines with speeds greater than 250 km/h, neither of the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R064 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** New lines with a speed greater than 250 km/h must be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].
- **After:** New lines must be supplied with one of the AC systems listed in point 4.2.3 (a) and (b), which are AC 25 kV, 50 Hz and AC 15 kV, 16,7 Hz [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R065 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 16,7 Hz; DC 3 kV; and DC 1,5 kV [4].
- **After:** The Energy TSI allows four traction power supply systems: AC 25 kV, 50 Hz; AC 15 kV, 16,7 Hz; DC 3 kV; and DC 1,5 kV [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R066 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For new lines with speeds greater than 250 km/h, only the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].
- **After:** For new lines, only the two AC systems (AC 25 kV 50 Hz and AC 15 kV 16,7 Hz) may be used [2][4].

- [ ] Accept  - [ ] Reject

**Note:** 

## q09

**Question:** What are the Class A train protection and radio systems under the CCS TSI?

<details><summary>[1] CCS TSI, — Current status of deployment for Class A train protection system</summary>

```
CCS TSI, — Current status of deployment for Class A train protection system
[If relevant, include here an explanatory text in relation to the current status of ETCS deployment.]
```

</details>

<details><summary>[2] CCS TSI, 2.2. Scope</summary>

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

</details>

<details><summary>[3] CCS TSI, — Current status of deployment for Class A radio system</summary>

```
CCS TSI, — Current status of deployment for Class A radio system
[If relevant, include here an explanatory text in relation to the current status of Class A radio system.]
```

</details>

### R067 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Class A train protection system is ETCS (European Train Control System), and the Class A radio system is RMR (Railway Mobile Radio system) [2]. RMR comprises two radio class A systems, which are GSM-R and FRMCS (Future Railway Mobile Communication System) [2].
- **Appended:** ETCS must be fitted on all new high-speed lines from the date of their opening [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R068 · `NUM` · out-of-context

_a number was changed_

- **Before:** RMR comprises two radio class A systems, which are GSM-R and FRMCS (Future Railway Mobile Communication System) [2].
- **After:** RMR comprises six radio class A systems, which are GSM-R and FRMCS (Future Railway Mobile Communication System) [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R069 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Class A train protection system is ETCS (European Train Control System) and the Class A radio system is RMR (Railway Mobile Radio), which includes GSM-R and FRMCS (Future Railway Mobile Communication System)[2].
- **Appended:** ETCS must be fitted on all new high-speed lines from the date of their opening [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R070 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Class A train protection system is ETCS (European Train Control System) and the Class A radio system is RMR (Railway Mobile Radio), which includes GSM-R and FRMCS (Future Railway Mobile Communication System)[2].
- **After:** The Class A train protection system is ETCS (European Train Control System) and the Class A radio system is RMR (Railway Mobile Radio), which includes GSM-R and FRMCS (Future Railway Mobile Communication System) [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R071 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Class A train protection system is ETCS (European Train Control System), and the Class A radio system is RMR (Railway Mobile Radio system) [2].
- **After:** The Class A train protection system is ETCS (European Train Control System), and the Class A radio system is RMR (Railway Mobile Radio system) [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## q10

**Question:** How must the rear end of a passenger train and of a freight train be signalled?

<details><summary>[1] OPE TSI, 4.2.2.1.3. Rear end</summary>

```
OPE TSI, 4.2.2.1.3. Rear end
The railway undertaking shall provide the required means of indicating the rear of a train. The rear end signal shall only be exhibited on the rear of the last vehicle of the train. It shall be displayed as shown below.
```

</details>

<details><summary>[2] OPE TSI, 4.2.2.1.3.1. Passenger trains</summary>

```
OPE TSI, 4.2.2.1.3.1. Passenger trains
The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis.
```

</details>

<details><summary>[3] OPE TSI, 5. COMPLETE FAILURE OF A REAR END SIGNAL</summary>

```
OPE TSI, 5. COMPLETE FAILURE OF A REAR END SIGNAL
(1) If the signaller becomes aware of the complete failure of the train rear end signal, the signaller shall make arrangements to stop the train in an appropriate location and inform the driver.
(2) The driver shall then check the completeness of the train and if necessary repair/replace the train rear end signal.
(3) The driver shall report to the signaller that the train is ready to proceed. Otherwise, if the repair is not possible, the train may not proceed, unless special arrangements are made between signaller and driver.
```

</details>

<details><summary>[4] OPE TSI, 4.2.2.1.3.2. Freight trains</summary>

```
OPE TSI, 4.2.2.1.3.2. Freight trains
The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis. Any train equipped with 2 steady red lights shall also be considered to comply with this obligation.
Reflective plates shall comply with Appendix E to Wagon TSI and have the following shape with white side triangles and red top and bottom triangle:
The plates shall be on the same height above buffer on the transversal axis
```

</details>

<details><summary>[5] OPE TSI, 7.2.2.4. Permanent specific case (P) Finland</summary>

```
OPE TSI, 7.2.2.4. Permanent specific case (P) Finland
For the implementation of point 4.2.2.1.3.2 and the implementation of common operational rule 5 of Appendix B, Finland is not using any rear end signal device for freight trains. The means to indicate the train rear end signal for freight trains as stated in point 4.2.2.1.3.2 are also accepted in Finland.
```

</details>

### R072 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train should consist of 2 steady red lights at the same height above buffer on the transversal axis [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R073 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [2]. The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis, though any train equipped with 2 steady red lights shall also be considered to comply with this obligation [4].
- **Appended:** The lights must be visible from at least 200 m in daylight [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R074 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above the buffer on the transversal axis, although a freight train equipped with 2 steady red lights also complies with the requirement [4].
- **After:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above the buffer on the transversal axis, although a freight train equipped with 2 steady red lights does not comply with the requirement [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R075 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train should consist of 2 steady red lights at the same height above the buffer on the transversal axis [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R076 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [2]. The rear end signal of a freight train shall consist of 2 reflective plates at the same height above the buffer on the transversal axis, although a freight train equipped with 2 steady red lights also complies with the requirement [4].
- **Appended:** The lights must be visible from at least 200 m in daylight [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R077 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis, though any train equipped with 2 steady red lights shall also be considered to comply with this obligation [4].
- **After:** The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis, though any train equipped with 2 steady red lights shall not be considered to comply with this obligation [4].

- [ ] Accept  - [ ] Reject

**Note:** 

### R078 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [5].

- [ ] Accept  - [ ] Reject

**Note:** 

### R079 · `NUM` · out-of-context

_a number was changed_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train shall consist of 4 steady red lights at the same height above buffer on the transversal axis [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R080 · `NUM` · out-of-context

_a number was changed_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above the buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train shall consist of 4 steady red lights at the same height above the buffer on the transversal axis [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R081 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [2].
- **After:** The rear end signal of a passenger train shall consist of 2 steady red lights at the same height above buffer on the transversal axis [5].

- [ ] Accept  - [ ] Reject

**Note:** 

## q11

**Question:** From when must freight trains with reflective plates as the rear-end signal be accepted in Portugal, and across the whole EU network?

<details><summary>[1] OPE TSI, Phasing out:</summary>

```
OPE TSI, Phasing out:
The following deadlines shall apply for accepting freight trains equipped with two reflective plates:
(1) From 1 January 2022, along the rail freight corridors specified in accordance with Regulation (EU) No 913/2010, with the following exceptions on the lines where steady red lights are an operational requirement for ensuring safety: (a) 1 January 2026 for Belgium and France; (b) 1 January 2025 for Portugal and Spain.
(2) From 1 January 2026, in the whole European Union rail network.
Member States concerned by the exceptions under (1) (a) and (b) shall provide, by 1 March 2022 at the latest, the Commission with a detailed action plan and precise targets ensuring the elimination of the requirement for red lights as rear end signals. Every 6 months thereafter, those Member States shall provide the Commission with a report on progress made on the use of reflective plates on their network with the aim of Union-level harmonisation of rear end signals by 1 January 2026. Stakeholders shall provide all necessary input to allow Member States to fulfil their reporting duty.
The Commission shall report to the committee referred to in Article 51 of Directive (EU) 2016/797 on the implementation progress of section 4.2.2.1.
```

</details>

<details><summary>[2] OPE TSI, 7.2.2.1. Permanent specific case (P) Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia</summary>

```
OPE TSI, 7.2.2.1. Permanent specific case (P) Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia
For the implementation of point 4.2.2.1.3.2, freight trains which are operated solely on the 1 520 mm gauge network of Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia may use the following train rear end signal.
The reflective disc shall have a diameter of 185 mm with a red circle diameter of 140 mm. Where justified by operating practices, the reflective disc may be replaced with one reflective plate in compliance with Appendix E to TSI WAG.
For the implementation of point 4.2.2.1.3.1, passenger trains which are operated solely on the 1 520 mm gauge network of Estonia, Latvia, Lithuania, Poland, Hungary and Slovakia may use 3 steady red lights as train rear end signal following the scheme:
This specific case does not prevent the access of TSI compliant rolling stock to their network.
```

</details>

<details><summary>[3] OPE TSI, 4.2.2.1.3.2. Freight trains</summary>

```
OPE TSI, 4.2.2.1.3.2. Freight trains
The rear end signal of a freight train shall consist of 2 reflective plates at the same height above buffer on the transversal axis. Any train equipped with 2 steady red lights shall also be considered to comply with this obligation.
Reflective plates shall comply with Appendix E to Wagon TSI and have the following shape with white side triangles and red top and bottom triangle:
The plates shall be on the same height above buffer on the transversal axis
```

</details>

### R082 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].
- **After:** Freight trains equipped with two reflective plates may be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R083 · `NUM` · in-context

_a number was changed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].
- **After:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2022, and across the whole European Union rail network from 1 January 2026[1][1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R084 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].
- **After:** Freight trains equipped with two reflective plates may be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R085 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].
- **After:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network until 1 January 2026[1][1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R086 · `NUM` · in-context

_a number was changed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].
- **After:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2022 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R087 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].
- **Appended:** Wagons not yet fitted with the plates may still run until their next scheduled maintenance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R088 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network from 1 January 2026 [1].
- **After:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025 along specified rail freight corridors, and across the whole European Union rail network until 1 January 2026 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R089 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Freight trains equipped with two reflective plates must be accepted in Portugal from 1 January 2025, and across the whole European Union rail network from 1 January 2026[1][1].
- **Appended:** Wagons not yet fitted with the plates may still run until their next scheduled maintenance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q12

**Question:** How quickly must the Agency handle an application for a vehicle authorisation for placing on the market?

<details><summary>[1] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
Whenever tests are necessary in order to obtain documentary evidence of the technical compatibility referred to in points (b) and (d) of the first subparagraph, the national safety authorities involved may issue temporary authorisations to the applicant to use the vehicle for practical verifications on the network. The infrastructure manager, in consultation with the applicant, shall make every effort to ensure that any tests take place within three months of receipt of the applicant's request. Where appropriate, the national safety authority shall take measures to ensure that the tests take place.
4. The Agency or, in the case of paragraph 8, the national safety authority shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information from the applicant. The Agency, or, in the cases provided for in paragraph 8, the national safety authority, shall apply the practical arrangements on the authorisation procedure to be established in an implementing act, as referred to in paragraph 9. Those authorisations shall allow vehicles to be placed on the Union market.
```

</details>

<details><summary>[2] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
6. Within one month of receipt of the applicant's request, the Agency shall inform the applicant that the file is complete or ask for relevant supplementary information, setting a reasonable deadline for the provision thereof. With regard to the completeness, relevance and consistency of the file, the Agency may also assess the elements specified in point (d) of paragraph 3.
The Agency shall take full account of the assessments under paragraph 5 before taking its decision on the issuance of the vehicle authorisation for placing on the market. The Agency shall issue the authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information.
In the event of non-application of one or more TSIs or parts of them as referred to in Article 7, the Agency shall issue the vehicle authorisation only after application of the procedure laid down in that Article.
The Agency shall take full responsibility for the authorisations it issues.
```

</details>

<details><summary>[3] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
1. The applicant shall place a vehicle on the market only after having received the vehicle authorisation for placing on the market issued by the Agency in accordance with paragraphs 5 to 7 or by the national safety authority in accordance with paragraph 8.
2. In its application for a vehicle authorisation for placing on the market, the applicant shall specify the area of use of the vehicle. The application shall include evidence that the technical compatibility between the vehicle and the network of the area of use has been checked.
```

</details>

<details><summary>[4] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
5. The Agency shall issue vehicle authorisations for placing on the market in respect of vehicles having an area of use in one or more Member States. In order to issue such authorisations, the Agency shall: (a) assess the elements of the file specified in points (b), (c) and (d) of the first subparagraph of paragraph 3 in order to verify the completeness, relevance and consistency of the file in relation to the relevant TSIs; and (b) refer the applicant's file to the national safety authorities concerned by the intended area of use for assessment of the file in order to verify its completeness, relevance and consistency in relation to point (d) of the first subparagraph of paragraph 3 and to the elements specified in points (a), (b) and (c) of the first subparagraph of paragraph 3 in relation to the relevant national rules.
As part of the assessments pursuant to points (a) and (b) and in the case of justified doubts, the Agency or the national safety authorities may request that tests be conducted on the network. In order to facilitate those tests, the national safety authorities involved may issue temporary authorisations to the applicant to use the vehicle for tests on the network. The infrastructure manager shall make every effort to ensure that any such test takes place within three months of the request of the Agency or the national safety authority.
```

</details>

### R090 · `NUM` · in-context

_a number was changed_

- **Before:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].
- **After:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within three months of receipt of all relevant information [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R091 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].
- **After:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R092 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].
- **Appended:** The deadline can be extended once if the applicant agrees [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R093 · `NUM` · in-context

_a number was changed_

- **Before:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].
- **After:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within three months of receipt of all relevant information from the applicant [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R094 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2]. Additionally, within one month of receipt of the applicant's request, the Agency shall inform the applicant that the file is complete or ask for relevant supplementary information, setting a reasonable deadline for the provision thereof [2].
- **Appended:** The deadline can be extended once if the applicant agrees [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R095 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].
- **After:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case not before four months of receipt of all relevant information [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R096 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].
- **After:** The Agency should issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R097 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].
- **After:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case not before four months of receipt of all relevant information from the applicant [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R098 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [1][2].
- **After:** The Agency must issue the vehicle authorisation for placing on the market, or inform the applicant of its negative decision, within a predetermined reasonable time and in any case within four months of receipt of all relevant information from the applicant [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R099 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The Agency shall issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].
- **After:** The Agency should issue vehicle authorisations for placing on the market or inform the applicant of its negative decision within a predetermined, reasonable time, and in any case within four months of receipt of all relevant information [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

## q14

**Question:** What minimum clear opening must the doors between a tunnel escape walkway and the safe area have?

<details><summary>[1] SRT TSI, 4.2.1.5.2 Access to the safe area</summary>

```
SRT TSI, 4.2.1.5.2 Access to the safe area
This specification applies to all tunnels of more than 1 km in length.
(a) Safe areas shall be accessible for people who commence self-evacuation from the train as well as for the emergency response services.
(b) One of the following solutions shall be selected for access points from a train to the safe area: (1) Lateral and/or vertical emergency exits to the surface. These exits shall be provided at least every 1 000 m. (2) Cross-passages between adjacent independent tunnel tubes, which enable the adjacent tunnel tube to be employed as a safe area. Cross-passages shall be provided at least every 500 m. —————
(c) Doors giving access from the escape walkway to the safe area shall have a minimum clear opening of 1,4 m wide and 2,0 m high. Alternatively it is permitted to use multiple doors next to each other which are less wide as long as the flow capacity of people is demonstrated to be equivalent or higher.
(d) After passing the doors, the clear width shall continue to be at least 1,5 m wide and 2,25 m high.
(e) The way in which the emergency response services access the safe area shall be described in the emergency plan.
```

</details>

<details><summary>[2] SRT TSI, 4.2.1.7. Evacuation and rescue points</summary>

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
(e) Requirements for evacuation and rescue points inside the tunnel In addition to the requirements in 4.2.1.7 (c), evacuation and rescue points inside the tunnel shall comply with the following requirements (1) A safe area shall be accessible from the stopping position of the train. Dimensions of the evacuation route to the safe area shall consider the evacuation time (as specified in clause 4.2.3.4.1) and the planned capacity of the trains (referred to in clause 4.2.1.5.1) intended to be operated in the tunnel. The adequacy of the sizing of the evacuation route shall be demonstrated. (2) The safe area that is paired with the evacuation and rescue point shall offer a sufficient standing surface relative to the time passengers are expected to wait until they are evacuated to a final place of safety. (3) There shall be an access to the affected train for emergency response services without going through the occupied safe area. (4) The lay-out of the evacuation and rescue point and its equipment shall take into account the control of smoke, in particular to protect people who use the self-evacuation facilities to access the safe area.
```

</details>

<details><summary>[3] SRT TSI, 4.2.1.6. Escape walkways</summary>

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

</details>

### R100 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The doors must have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]
- **Appended:** The doors must open with a force of no more than 150 N [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R101 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The doors must have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]
- **After:** The doors should have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

### R102 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,4 m wide and 2,0 m high [1].
- **Appended:** The doors must open with a force of no more than 150 N [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R103 · `NUM` · in-context

_a number was changed_

- **Before:** The doors must have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]
- **After:** The doors must have a minimum clear opening of 1,5 m wide and 2,0 m high.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

### R104 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,4 m wide and 2,0 m high [1].
- **After:** Doors giving access from the escape walkway to the safe area must have a maximum clear opening of 1,4 m wide and 2,0 m high [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R105 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The doors must have a minimum clear opening of 1,4 m wide and 2,0 m high.[1]
- **After:** The doors must have a maximum clear opening of 1,4 m wide and 2,0 m high.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

### R106 · `NUM` · in-context

_a number was changed_

- **Before:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,4 m wide and 2,0 m high [1].
- **After:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,5 m wide and 2,0 m high [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R107 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Doors giving access from the escape walkway to the safe area must have a minimum clear opening of 1,4 m wide and 2,0 m high [1].
- **After:** Doors giving access from the escape walkway to the safe area should have a minimum clear opening of 1,4 m wide and 2,0 m high [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q15

**Question:** When does an upgraded or renewed vehicle that is already authorised need a new vehicle authorisation for placing on the market?

<details><summary>[1] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
12. In the event of renewal or upgrading of existing vehicles which already have a vehicle authorisation for placing on the market, a new vehicle authorisation for placing on the market shall be required if: (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs; (b) the overall safety level of the vehicle concerned may be adversely affected by the works envisaged; or (c) it is required by the relevant TSIs.
13. Where the applicant wishes to extend the area of use of a vehicle which has already been authorised, it shall supplement the file with the relevant documents referred to in paragraph 3 concerning the additional area of use. The applicant shall submit the file to the Agency, which shall, after following the procedures laid down in paragraphs 4 to 7, issue an updated authorisation covering the extended area of use.
If the applicant has received a vehicle authorisation in accordance with paragraph 8 and wishes to extend the area of use within that Member State, it shall supplement the file with the relevant documents referred to in paragraph 3 concerning the additional area of use. It shall submit the file to the national safety authority which shall, after following the procedures laid down in paragraph 8, issue an updated authorisation covering the extended area of use.
```

</details>

<details><summary>[2] Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market</summary>

```
Interoperability Directive, Article 21 — Vehicle authorisation for placing on the market
1. The applicant shall place a vehicle on the market only after having received the vehicle authorisation for placing on the market issued by the Agency in accordance with paragraphs 5 to 7 or by the national safety authority in accordance with paragraph 8.
2. In its application for a vehicle authorisation for placing on the market, the applicant shall specify the area of use of the vehicle. The application shall include evidence that the technical compatibility between the vehicle and the network of the area of use has been checked.
```

</details>

<details><summary>[3] Interoperability Directive, Article 54 — Transitional regime for using vehicles</summary>

```
Interoperability Directive, Article 54 — Transitional regime for using vehicles
1. Without prejudice to paragraph 4 of this Article, vehicles which need to be authorised between 15 June 2016 and 16 June 2019 shall be subject to the provisions set out in Chapter V of Directive 2008/57/EC.
2. Authorisations for the placing in service of vehicles which have been granted pursuant to paragraph 1 and all other authorisations granted prior to 15 June 2016, including authorisations delivered under international agreements, in particular RIC (Regolamento Internazionale Carrozze) and RIV (Regolamento Internazionale Veicoli), shall remain valid in accordance with the conditions under which the authorisations have been granted.
3. Vehicles authorised for placing in service pursuant to paragraphs 1 and 2 shall receive a new vehicle authorisation for placing on the market in order to operate on one or more networks which are not yet covered by their authorisation. The placing on the market on those additional networks shall be subject to Article 21.
```

</details>

### R108 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].
- **After:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall within the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R109 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].
- **After:** A new vehicle authorisation for placing on the market may be required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R110 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].
- **After:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are within the range of acceptable parameters as defined in the TSIs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R111 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].
- **After:** A new vehicle authorisation for placing on the market may be required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R112 · `NUM` · in-context

_a number was changed_

- **Before:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].
- **After:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 12 which are outside the range of acceptable parameters as defined in the TSIs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R113 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].
- **After:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R114 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1].
- **After:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R115 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].
- **Appended:** Software updates that do not change any parameter never require a new authorisation [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R116 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A new vehicle authorisation for placing on the market is required for renewed or upgraded existing vehicles if changes are made to the values of the parameters referred to in point (b) of paragraph 10 which are outside the range of acceptable parameters as defined in the TSIs [1]. It is also required if the overall safety level of the vehicle concerned may be adversely affected by the envisaged works, or if it is required by the relevant TSIs [1].
- **Appended:** Software updates that do not change any parameter never require a new authorisation [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R117 · `NUM` · in-context

_a number was changed_

- **Before:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 10 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].
- **After:** A new vehicle authorisation for placing on the market is required when, after renewal or upgrading of an already-authorised vehicle, (a) changes are made to the values of the parameters referred to in point (b) of paragraph 12 that fall outside the range of acceptable parameters defined in the TSIs, (b) the overall safety level of the vehicle may be adversely affected by the works envisaged, or (c) the relevant TSIs require it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## q16

**Question:** Which language must train crew use for safety-related communication with the staff authorising train movements?

<details><summary>[1] OPE TSI, 4.2.1.5. Safety-related communications between train crew, other railway undertaking staff and staff authorising train movements</summary>

```
OPE TSI, 4.2.1.5. Safety-related communications between train crew, other railway undertaking staff and staff authorising train movements
The language used for safety-related communication between train crew, other railway undertaking staff (as defined in Appendix G) and the staff authorising train movements is the operating language(s) (as defined in Appendix J) used by the infrastructure manager on the route concerned.
The principles for safety-related communication between train crew and staff responsible for authorising the movement of trains are to be found in Appendix C.
In accordance with Directive 2012/34/EU, the infrastructure manager is responsible for publishing the ‘operating’ language(s) used by its personnel in daily operational use.
Where, however, local practice requires that a second language is also provided for, it is the responsibility of the infrastructure manager to determine the geographic boundaries for its use.
```

</details>

<details><summary>[2] OPE TSI, 4.6.2.1. Principles</summary>

```
OPE TSI, 4.6.2.1. Principles
The infrastructure manager and the railway undertaking are required to ensure that their relevant staff are competent in the use of the communication protocols and principles set out in Appendix C.
Where the operating language used by the infrastructure manager differs from that habitually used by the railway undertaking's staff, such linguistic and communications training shall form a critical part of the railway undertaking's overall competence management system.
Railway undertaking staff whose duties require them to communicate with staff of the infrastructure manager in connection with safety-critical matters, whether in normal, degraded or emergency situations, shall have a sufficient level of knowledge in the operating language of the infrastructure manager.
```

</details>

<details><summary>[3] SRT TSI, 4.4.5. Provision of on-train safety and emergency information to passengers</summary>

```
SRT TSI, 4.4.5. Provision of on-train safety and emergency information to passengers
(a) Railway undertakings shall inform passengers of on board emergency and safety procedures related to tunnels.
(b) When such information is in written or spoken form, it shall be presented in the language of the country the train is running in as a minimum, plus English.
(c) An operating rule shall be in place describing how the train crew ensures the complete evacuation of the train when this is necessary, including those people with hearing impairments that may be in closed areas.
```

</details>

### R118 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The language used for safety-related communication between the train crew and the staff authorising train movements is the operating language(s) used by the infrastructure manager on the route concerned [1].
- **Appended:** Communication in English is always permitted as an alternative [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R119 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].
- **After:** The train crew must not use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R120 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The language used for safety-related communication between the train crew and the staff authorising train movements is the operating language(s) used by the infrastructure manager on the route concerned [1].
- **After:** The language used for safety-related communication between the train crew and the staff authorising train movements is the operating language(s) used by the infrastructure manager on the route concerned [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R121 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].
- **After:** The train crew may use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R122 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].
- **Appended:** Communication in English is always permitted as an alternative [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R123 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The language used for safety-related communication between the train crew and the staff authorising train movements is the operating language(s) used by the infrastructure manager on the route concerned [1].
- **After:** The language used for safety-related communication between the train crew and the staff authorising train movements is not the operating language(s) used by the infrastructure manager on the route concerned [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R124 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [1].
- **After:** The train crew must use the operating language(s) used by the infrastructure manager on the route concerned for safety-related communication with the staff authorising train movements [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n02

**Question:** Which track gauges does the CCS TSI apply to, and which lines are excluded?

<details><summary>[1] CCS TSI, 1.2. Geographical Scope</summary>

```
CCS TSI, 1.2. Geographical Scope
The geographical scope of this TSI is the network of the whole rail system, as described in point 1 of Annex I to Directive (EU) 2016/797 and excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797.
The TSI shall apply to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges. However, it shall not apply to short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries.
```

</details>

<details><summary>[2] CCS TSI, 1.1. Technical scope</summary>

```
CCS TSI, 1.1. Technical scope
This TSI concerns the Control Command and Signalling On-Board Subsystem and the Control-Command and Signalling Trackside Subsystem.
This TSI is applicable to control-command and signalling trackside Subsystems of the rail network defined in the point 1.2 (Geographical Scope) of this TSI and to the control-command and signalling on-board subsystems of vehicles which are (or are intended to be) operated on it. These vehicles are of one of the following types (as defined in point 2 of Annex I to Directive (EU) 2016/797):
(1) locomotives and passenger rolling stock, including thermal or electric traction units, self-propelling thermal or electric passenger trains, and passenger coach, if equipped with a driving cab;
(2) special vehicles, such as on-track machines, if equipped with a driving cab intended to be used in running mode on its own wheels.
This list of vehicles shall include those which are specially designed to operate on the different types of high-speed lines described in point 1.2 (Geographical Scope).
```

</details>

<details><summary>[3] CCS TSI, Article 2 — Scope</summary>

```
CCS TSI, Article 2 — Scope
1. The TSI shall apply to new trackside CCS and on-board CCS subsystems of the rail system as defined in points 2.3 and 2.4 of Annex II to Directive (EU) 2016/797. —————
2. The TSI shall not apply to existing trackside CCS and on-board CCS subsystems of the rail system already placed on the market and in service on all or part of any Member State’s railway network by 28 September 2023, except when: (a) the subsystem is subject to renewal or upgrading in accordance with point 7 of Annex I to this Regulation; (b) the area of use of a vehicle is extended in accordance with Article 54(3) of Directive (EU) 2016/797 to at least three Member States, or the installation of ETCS is indicated in RINF for the subsequent five years in the new area of use. In that case point 7.4.2.3 of Annex I to this Regulation shall apply; (c) the subsystem is subject to the specification maintenance requirements set out in point 7.2.10 of Annex I to this Regulation.
3. The technical and geographical scope of the TSI is set out in points 1.1 and 1.2 of Annex I.
```

</details>

### R125 · `NUM` · in-context

_a number was changed_

- **Before:** It does not apply to short border-crossing lines with 1 520 mm track gauge that are connected to the network of third countries[1].
- **After:** It does not apply to short border-crossing lines with 1 435 mm track gauge that are connected to the network of third countries[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R126 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [1].
- **After:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R127 · `NUM` · in-context

_a number was changed_

- **Before:** It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries [1].
- **After:** It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 435 mm track gauges that are connected to the network of third countries [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R128 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges[1]. It does not apply to short border-crossing lines with 1 520 mm track gauge that are connected to the network of third countries[1].
- **Appended:** It also applies to 1 000 mm metre-gauge networks [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R129 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries [1].
- **After:** It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 520 mm track gauges [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R130 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [1]. It excludes the infrastructure cases referred to in Article 1(3) and (4) of Directive (EU) 2016/797, as well as short border crossing lines with 1 520 mm track gauges that are connected to the network of third countries [1].
- **Appended:** It also applies to 1 000 mm metre-gauge networks [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R131 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [1].
- **After:** The CCS TSI does not apply to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R132 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** It does not apply to short border-crossing lines with 1 520 mm track gauge that are connected to the network of third countries[1].
- **After:** It does not apply to short border-crossing lines with 1 520 mm track gauge[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R133 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges[1].
- **After:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R134 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The CCS TSI applies to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges[1].
- **After:** The CCS TSI does not apply to networks with 1 435 mm, 1 520 mm, 1 524 mm, 1 600 mm and 1 668 mm track gauges[1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n03

**Question:** In a national implementation plan, how much advance notice must railway undertakings get of new mandatory on-board CCS requirements?

<details><summary>[1] CCS TSI, 7.4.4. National Implementation Plans</summary>

```
CCS TSI, 7.4.4. National Implementation Plans
The national implementation plan shall provide information on all new, renewed and upgraded lines in relation to mandatory and optional functions listed in 7.2.9 ensuring that notifications to RUs are provided at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network. This shall be notified within the RINF ( 38 ) and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU. The 5-year notification period does not apply to any requirements, which were announced in the Network Statement before the entry into force of this CCS TSI.
The national implementation plans shall cover a period of at least 20 years and shall be updated regularly, at least every five years. The plans shall follow the template provided in the in Appendix H to this Annex for the first five years of the period covered. For the subsequent period of fifteen years, the plan shall follow this template to the extent possible with a less detailed approach.
The Commission shall publish the national implementation plans on its website and inform Member States about them through the Committee referred to in Article 51(1) of Directive (EU) 2016/797.
The Commission shall draw up an analysis of the national implementation plans that shall encompass among others comparison of the plans and identification of needs for additional coordination measures.
The national implementation plan shall at least include the following information ( 39 ):
```

</details>

<details><summary>[2] CCS TSI, 6. NEW MANDATORY ON-BOARD REQUIREMENTS</summary>

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

</details>

<details><summary>[3] CCS TSI, 7.4.4. National Implementation Plans</summary>

```
CCS TSI, 7.4.4. National Implementation Plans
Member States shall develop a national plan for the implementation of this TSI in coordination with the Infrastructure Managers and Railway Undertakings concerned, considering the coherence of the entire rail system of the European Union taking into account the economic viability, interoperability and safety of the rail system. Member States shall consult the neighbouring countries for a coherent planning of the railway cross-border sections. This plan shall include all lines in scope of the TSI including TEN-T lines and the nodes and last mile connections.
Member States shall coordinate the process between all stakeholders concerned to set up the technical and indicative financial migration strategy required for the overall ERTMS deployment of this national implementation plan.
Member States shall include the assessment of the needs expressed by the railway undertakings and the infrastructure managers for the CCS subsystem related to the conditions for mandatory and optional functions listed in 7.2.9 in the National Implementation Plan.
Member States shall decide on the migration strategy describing the expected overall impact for the railway system (taking a Union perspective) and how the impact is balanced in a non-discriminatory way between the stakeholders concerned based on the above assessment. The output of this coordination process shall be the definition of the technical and the financial migration strategy being implemented.
```

</details>

### R135 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].
- **After:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R136 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].
- **Appended:** Shorter notice is allowed for requirements that only concern automatic train operation [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R137 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].
- **After:** Railway undertakings should be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R138 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].
- **After:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R139 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].
- **After:** Railway undertakings must be notified of new mandatory on-board CCS requirements at most 5 years in advance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R140 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].
- **After:** Railway undertakings must be provided with notifications at most 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R141 · `NUM` · in-context

_a number was changed_

- **Before:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].
- **After:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 20 years in advance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R142 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].
- **Appended:** Shorter notice is allowed for requirements that only concern automatic train operation [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R143 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Railway undertakings must be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].
- **After:** Railway undertakings should be notified of new mandatory on-board CCS requirements at least 5 years in advance [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R144 · `NUM` · in-context

_a number was changed_

- **Before:** Railway undertakings must be provided with notifications at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].
- **After:** Railway undertakings must be provided with notifications at least 20 years in advance in case there will be new mandatory on-board requirements for operating on the network [1][2].

- [ ] Accept  - [ ] Reject

**Note:** 

## n04

**Question:** When may a Member State leave out the GSM-R decommissioning section of its national implementation plan?

<details><summary>[1] CCS TSI, 5.2.4. Decommissioning of GSM-R</summary>

```
CCS TSI, 5.2.4. Decommissioning of GSM-R
[This section shall include a network map providing an overview with dates when GSM-R radio operation is not allowed anymore. If not similar, this section shall also include a network map providing an overview with dates where GSM-R system is taken out of service.
This section is not mandatory for those Member States which do not foresee GSM-R decommissioning in the next 20 years.
The template to be filled in to provide the information in this section is given below]
```

</details>

<details><summary>[2] CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning</summary>

```
CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning
[Include here the line identification number] | [Include here the name of the line] | [Include here the current status of the GSM-R deployment on the line. Under construction/ not yet under construction] | [Include here the date when the construction started or is expected to start.] | [Include here the date when GSM-R will be placed in service.] | [If the line is equipped with a Class B radio system, include here the date when Class B operation is not allowed anymore.] | [If not similar to the previous column, include here the date when Class B system is taken out of service] | [Include here the total length of the line] | [Specify here whether GSM-R voice or data is installed] | [Include here the baseline of the GSM-R to be implemented] | [Include here if radio circuit switching is implemented or only packet switching] | [Include here the type of Radio part action. New/ renew/ upgrade] | [If relevant, include here additional comments]
```

</details>

<details><summary>[3] CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning</summary>

```
CCS TSI, — Planning for GSM-R deployment and Class B radio system decommissioning
[If relevant, include here an explanatory text in relation to planning of GSM-R deployment and Class B radio part decommissioning.]
Table 12
Planning for GSM-R deployment and Class B radio part decommissioning
ID | Line | Planning for GSM-R deployment | Planning for Class B radio decommissioning | Additional information | Note
Current status | Realization | Date when GSM-R is placed in service | Dates when Class B operation is not allowed any more | Dates when Class B is taken out of service | Length | GSM-R voice/ GSM-R data | Baseline | Circuit switching/ Packet switching | Type of action
```

</details>

### R145 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R146 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R147 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it foresees GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R148 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State must leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R149 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **Appended:** It must then notify the Commission of this decision [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R150 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State must omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R151 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **Appended:** It must then notify the Commission of this decision [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R152 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it foresees GSM-R decommissioning in the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R153 · `NUM` · out-of-context

_a number was changed_

- **Before:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may omit the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 10 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R154 · `NUM` · out-of-context

_a number was changed_

- **Before:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 20 years [1].
- **After:** A Member State may leave out the GSM-R decommissioning section of its national implementation plan if it does not foresee GSM-R decommissioning in the next 10 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n05

**Question:** How many years ahead must the train detection planning table in a national implementation plan cover?

<details><summary>[1] PRM TSI, Article 8 — National Implementation Plans</summary>

```
PRM TSI, Article 8 — National Implementation Plans
1. Member States shall adopt national implementation plans, including at least the information listed in Appendix C of the Annex, with a view to progressively eliminating all identified barriers to accessibility.
2. The national implementation plans shall be based on existing national plans and, subject to availability, on the inventory of assets referred to in Article 7, or on any other relevant and reliable source of information.
The scope and speed of implementing national plans shall be decided by Member States.
3. The national implementation plans shall run over a period of at least 10 years and shall be updated regularly, at least every five years.
4. The national implementation plans shall contain a strategy, including a prioritisation rule laying down the criteria and priorities for stations and units of rolling stock to be designated for renewal or upgrading. This strategy shall be formulated in cooperation with infrastructure manager(s), station manager(s), railway undertaking(s) and, if needed, other local authorities (including local transport authorities). Representative associations of users including disabled persons and persons with reduced mobility shall be consulted.
5. In each Member State, the prioritisation rule referred to in paragraph 4 shall replace the rule set out in Appendix B of the Annex which shall apply until the adoption of the national implementation plan in that Member State.
```

</details>

<details><summary>[2] CCS TSI, 7.4.4. National Implementation Plans</summary>

```
CCS TSI, 7.4.4. National Implementation Plans
The national implementation plan shall provide information on all new, renewed and upgraded lines in relation to mandatory and optional functions listed in 7.2.9 ensuring that notifications to RUs are provided at least 5 years in advance in case there will be new mandatory on-board requirements for operating on the network. This shall be notified within the RINF ( 38 ) and these changes in RINF shall be listed in the Network Statement as part of Article 27 of Directive 2012/34/EU. The 5-year notification period does not apply to any requirements, which were announced in the Network Statement before the entry into force of this CCS TSI.
The national implementation plans shall cover a period of at least 20 years and shall be updated regularly, at least every five years. The plans shall follow the template provided in the in Appendix H to this Annex for the first five years of the period covered. For the subsequent period of fifteen years, the plan shall follow this template to the extent possible with a less detailed approach.
The Commission shall publish the national implementation plans on its website and inform Member States about them through the Committee referred to in Article 51(1) of Directive (EU) 2016/797.
The Commission shall draw up an analysis of the national implementation plans that shall encompass among others comparison of the plans and identification of needs for additional coordination measures.
The national implementation plan shall at least include the following information ( 39 ):
```

</details>

<details><summary>[3] CCS TSI, 3.4. Technical migration strategy for Train Detection part</summary>

```
CCS TSI, 3.4. Technical migration strategy for Train Detection part
[This section shall include information and planning of the technical migration strategy of TSI compliant train detection part.
For completeness at least the following information shall be included:
— Deployment strategy. Information on the migration to the TSI compliant train detection system.
— Table which includes for each line the planning dates of TSI compliant train detection system deployment and other relevant information. The table shall provide the complete information of changes in the following 20 years.
The template to be filled in to provide the information in this section is given below]
```

</details>

### R155 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The train detection planning table must provide complete information of changes in the following 20 years [3].
- **Appended:** The table must be updated every year [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R156 · `NUM` · out-of-context

_a number was changed_

- **Before:** The train detection planning table must cover the next 20 years[3].
- **After:** The train detection planning table must cover the next 30 years[3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R157 · `NUM` · out-of-context

_a number was changed_

- **Before:** The train detection planning table must provide complete information of changes in the following 20 years [3].
- **After:** The train detection planning table must provide complete information of changes in the following 30 years [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R158 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The train detection planning table must provide complete information of changes in the following 20 years [3].
- **After:** The train detection planning table must provide complete information of changes in the following 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R159 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The train detection planning table must provide complete information of changes in the following 20 years [3].
- **After:** The train detection planning table need not provide complete information of changes in the following 20 years [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R160 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The train detection planning table must cover the next 20 years[3].
- **After:** The train detection planning table must cover the next 20 years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R161 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The train detection planning table must provide complete information of changes in the following 20 years [3].
- **After:** The train detection planning table should provide complete information of changes in the following 20 years [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R162 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The train detection planning table must cover the next 20 years[3].
- **After:** The train detection planning table need not cover the next 20 years[3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R163 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The train detection planning table must cover the next 20 years[3].
- **Appended:** The table must be updated every year [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R164 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The train detection planning table must cover the next 20 years[3].
- **After:** The train detection planning table should cover the next 20 years[3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n07

**Question:** What is the maximum lateral deviation of the contact wire under crosswind for a 1 600 mm pantograph and for a 1 950 mm pantograph?

<details><summary>[1] ENE TSI, 4.2.9.2. Maximum lateral deviation</summary>

```
ENE TSI, 4.2.9.2. Maximum lateral deviation
(1) The maximum lateral deviation of the contact wire in relation to the track centre line under action of crosswind shall be in accordance with the specification referenced in Appendix E, Index [2]. Table 4.2.9.2 Maximum lateral deviation depending on the pantograph length Pantograph length [mm] | Maximum lateral deviation [mm] 1 600 | 400 (1) 1 950 | 550 (1) (1) The values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4.
(2) In the case of the multi-rail track, the requirement for lateral deviation shall be fulfilled for each pair of rails (designed, to be operated as a separated track) that is intended to be assessed against TSI.
(3) Track gauge system 1 520 mm: For Member States applying the pantograph profile in accordance with point 4.2.8.2.9.2.3 of the LOC&PAS TSI the maximum lateral deviation of the contact wire in relation to the pantograph centre under action of a crosswind shall be 500 mm.
```

</details>

<details><summary>[2] ENE TSI, 4.2.9. Geometry of the overhead contact line</summary>

```
ENE TSI, 4.2.9. Geometry of the overhead contact line
(1) The overhead contact line shall be designed for pantographs with the head geometry specified in the LOC & PAS TSI, point 4.2.8.2.9.2 taking into account the rules set out in point 7.1.2 of this TSI.
(2) The contact wire height and the lateral deviation of the contact wire under the action of a crosswind are factors which govern the interoperability of the rail network.
```

</details>

<details><summary>[3] ENE TSI, Static pantograph gauge for 1 520 mm track gauge system</summary>

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

</details>

### R165 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** These values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4 [1].
- **After:** These values may be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R166 · `NUM` · in-context

_a number was changed_

- **Before:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1].
- **After:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 500 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R167 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1]. These values shall be adjusted taking into account the movement of the pantograph and track tolerances according to Appendix D.1.4 [1].
- **Appended:** On curves with a radius below 1 000 m the limit is reduced by 50 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R168 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].
- **After:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R169 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1].
- **After:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R170 · `NUM` · in-context

_a number was changed_

- **Before:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].
- **After:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 500 mm for a 1 950 mm pantograph [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R171 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].
- **Appended:** On curves with a radius below 1 000 m the limit is reduced by 50 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R172 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For a 1 600 mm pantograph, the maximum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1].
- **After:** For a 1 600 mm pantograph, the minimum lateral deviation of the contact wire is 400 mm, and for a 1 950 mm pantograph, it is 550 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R173 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The maximum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].
- **After:** The minimum lateral deviation of the contact wire under cross-wind is 400 mm for a 1 600 mm pantograph and 550 mm for a 1 950 mm pantograph [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n09

**Question:** On lines for 250 km/h or more, how long must a phase separation neutral section be when all pantographs of the longest train are inside it?

<details><summary>[1] ENE TSI, 4.2.15.2. Lines with speed v ≥ 250 km/h</summary>

```
ENE TSI, 4.2.15.2. Lines with speed v ≥ 250 km/h
Two types of design of phase separation sections may be adopted:
(a) a phase separation design where all the pantographs of the longest TSI compliant trains are within the neutral section. The overall length of the neutral section shall be at least 402 m. For detailed requirements see the specification referenced in Appendix E, Index [2];
(b) a shorter phase separation with three insulated overlaps as shown in the specification referenced in Appendix E, Index [2]. The overall length of the neutral section is less than 142 m including clearances and tolerances.
```

</details>

<details><summary>[2] ENE TSI, Appendix E — List of referenced standards</summary>

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

</details>

<details><summary>[3] ENE TSI, 4.2.15.1. General</summary>

```
ENE TSI, 4.2.15.1. General
(1) The design of phase separation sections shall ensure that trains can move from one section to an adjacent one without bridging the two phases. Power exchange between the OCL and the unit shall be brought to zero, by switching off the on-board circuit breaker or other equivalent means, before entering the phase separation section. Adequate means (except for the short separation section) shall be provided to allow a train that is stopped within the phase separation section to be restarted.
(2) The overall length D of neutral sections is defined in the specification referenced in Appendix E, Index [2]. For the calculation of D clearances, the specification referenced in Appendix E, Index [3] and an uplift of S0 shall be taken into account.
```

</details>

### R174 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].
- **Appended:** The neutral section must be located on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R175 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].
- **Appended:** The neutral section must be located on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R176 · `NUM` · out-of-context

_a number was changed_

- **Before:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].
- **After:** The neutral section must be at least 420 m long when all pantographs of the longest train are inside it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R177 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].
- **After:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R178 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].
- **After:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R179 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].
- **After:** The neutral section must be at least 402 m long [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R180 · `NUM` · out-of-context

_a number was changed_

- **Before:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].
- **After:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 420 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R181 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].
- **After:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at most 402 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R182 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** On lines for 250 km/h or more, where all the pantographs of the longest TSI compliant trains are within the neutral section, the overall length of the neutral section shall be at least 402 m [1].
- **After:** On lines for 250 km/h or more, the overall length of the neutral section shall be at least 402 m [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R183 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The neutral section must be at least 402 m long when all pantographs of the longest train are inside it [1].
- **After:** The neutral section must be at most 402 m long when all pantographs of the longest train are inside it [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n10

**Question:** Which parts of the energy subsystem may enter the pantograph gauge?

<details><summary>[1] ENE TSI, 4.2.10. Pantograph gauge</summary>

```
ENE TSI, 4.2.10. Pantograph gauge
(1) Track gauge system other than 1 520 mm:
The mechanical kinematic pantograph gauge shall be specified using the method given in the specification referenced in Appendix E, Index [2] to this TSI and the pantograph profiles defined in LOC&PAS TSI, clauses 4.2.8.2.9.2.1 and 4.2.8.2.9.2.2.
(2) Track gauge system 1 520 mm:
For Member States applying the pantograph profile in accordance with LOC&PAS TSI, clause 4.2.8.2.9.2.3, the static gauge available for pantograph is defined in Appendix D to this TSI.
(3) No part of the energy sub-system shall enter the pantograph gauge as stated in points (1) and (2), except for the contact wire and steady arm.
```

</details>

<details><summary>[2] ENE TSI, Static pantograph gauge for 1 520 mm track gauge system</summary>

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

</details>

<details><summary>[3] ENE TSI, Annex</summary>

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

</details>

### R184 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Only the contact wire and the steady arm may enter the pantograph gauge [1][3].
- **After:** Only the contact wire and the steady arm may enter the pantograph gauge [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R185 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [1].
- **After:** No part of the energy sub-system should enter the pantograph gauge, except for the contact wire and steady arm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R186 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Only the contact wire and the steady arm may enter the pantograph gauge [1][3].
- **After:** Only the contact wire and the steady arm must enter the pantograph gauge [1][3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R187 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [1].
- **After:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R188 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [1].
- **After:** No part of the energy sub-system shall enter the pantograph gauge, including the contact wire and steady arm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R189 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** No part of the energy sub-system shall enter the pantograph gauge, except for the contact wire and steady arm [1].
- **Appended:** Insulators may also enter it on lines with speeds below 160 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R190 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Only the contact wire and the steady arm may enter the pantograph gauge [1][3].
- **After:** The contact wire and the steady arm may not enter the pantograph gauge [1][3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R191 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Only the contact wire and the steady arm may enter the pantograph gauge [1][3].
- **Appended:** Insulators may also enter it on lines with speeds below 160 km/h [3].

- [ ] Accept  - [ ] Reject

**Note:** 

## n11

**Question:** On a platform, what is the minimum distance from an obstacle to the danger area, for small and for large obstacles?

<details><summary>[1] PRM TSI, 4.2.1.12. Platform width and edge of platform</summary>

```
PRM TSI, 4.2.1.12. Platform width and edge of platform
(4) It is permitted to have obstacles inside this freeway of 160 cm. Equipment required for the signalling system and safety equipment shall not be considered as obstacles in this point. The minimum distance from obstacles to the danger area shall be according to the following table: Table 4 Minimum distance from obstacles to the danger area Length of obstacles (measured parallel to the platform edge) | Minimum distance to the danger area < 1 m (note 1) — small obstacle | 80 cm 1 m to < 10 m — large obstacle | 120 cm Note 1: if the distance between two small obstacles is less than 2,4 m measured parallel to the platform edge they shall be considered as one large obstacle. Note 2: Within this minimum distance from a large obstacle to the danger area it is permitted to have additional small obstacles as long as the requirements for small obstacles (minimum distance to danger area and minimum distance to next small obstacle) are met.
(6) The boundary of the danger area, furthest from the rail side edge of the platform, shall have a visual marking and tactile walking surface indicators.
(7) The visual marking shall be a contrasting, slip resistant, warning line with a minimum width of 10 cm.
```

</details>

<details><summary>[2] PRM TSI, 4.2.1.12. Platform width and edge of platform</summary>

```
PRM TSI, 4.2.1.12. Platform width and edge of platform
(1) The danger area of a platform commences at the rail side edge of the platform and is defined as the area where passengers are not allowed to stand when trains are passing or arriving.
(2) It is permitted for the width of the platform to be variable on the whole length of the platform.
(3) The minimum width of the platform without obstacles shall be the width of the danger area plus the width of two opposing freeways of 80 cm (160 cm). This dimension may taper to 90 cm at the platform ends.
```

</details>

<details><summary>[3] PRM TSI, 4.4.3. Provision of boarding aids and provision of assistance</summary>

```
PRM TSI, 4.4.3. Provision of boarding aids and provision of assistance
(e) for boarding aids located on the platforms, the location where they are most likely to be used, taking into account that a free space (no obstacles) of 150 cm is available from the edge of the boarding aid towards the direction where the wheelchair boards/lands at/to the platform level;
(f) the conditions for the provision of alternative transport where: — the platform cannot be reached through an obstacle-free route, or — assistance cannot be provided to deploy a boarding aid between the platform and the rolling stock.
```

</details>

### R192 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For large obstacles with a length from 1 m to less than 10 m, the minimum distance to the danger area is 120 cm [1].
- **After:** For large obstacles with a length of 1 m or more, the minimum distance to the danger area is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R193 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].
- **Appended:** Benches count as large obstacles regardless of their length [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R194 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [1].
- **After:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R195 · `NUM` · in-context

_a number was changed_

- **Before:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].
- **After:** For small obstacles (length < 1 m) the minimum distance to the danger area is 160 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R196 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [1]. For large obstacles with a length from 1 m to less than 10 m, the minimum distance to the danger area is 120 cm [1].
- **Appended:** Benches count as large obstacles regardless of their length [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R197 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].
- **After:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R198 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].
- **After:** For small obstacles (length < 1 m) the maximum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R199 · `NUM` · in-context

_a number was changed_

- **Before:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [1].
- **After:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 160 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R200 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m to < 10 m) it is 120 cm [1].
- **After:** For small obstacles (length < 1 m) the minimum distance to the danger area is 80 cm, and for large obstacles (length 1 m or more) it is 120 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R201 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For small obstacles with a length of less than 1 m, the minimum distance to the danger area is 80 cm [1].
- **After:** For small obstacles with a length of less than 1 m, the maximum distance to the danger area is 80 cm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n12

**Question:** What maximum height and minimum depth must internal steps in a passenger vehicle have?

<details><summary>[1] PRM TSI, 4.2.2.8. Height changes</summary>

```
PRM TSI, 4.2.2.8. Height changes
(1) Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs. For double deck trains it is permitted to reduce this value to 270 mm for the stairs accessing the upper deck and the lower deck.
(2) As a minimum, the first and the last steps shall be indicated by a contrasting band extending the full width of the steps on both the front and the top surfaces of the step nosing with a depth of: — 45 mm to 55 mm on the front surface, — 45 mm to 75 mm on the top surface.
(3) Stairs constituted of more than three steps shall be provided with handrails on both sides and at two levels. The higher handrail shall be positioned at a height of 850 mm to 1 000 mm above floor level. The lower handrail shall be positioned at a height of 500 mm to 750 mm above floor level.
(4) Stairs constituted of one, two or three steps shall be provided on both sides with a minimum of one handrail or other item that can be used for personal stability.
(5) Handrails shall be compliant with point 4.2.2.9
```

</details>

<details><summary>[2] PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network</summary>

```
PRM TSI, Specific Case France ‘P’ for the ‘Ile de France’ network
For double deck trains, internal steps (other than those for external access) shall have a maximum height of 208 mm and a minimum depth of 215 mm, measured at the central axis of the stairs.
```

</details>

<details><summary>[3] PRM TSI, 4.2.2.11.2. Access/egress steps</summary>

```
PRM TSI, 4.2.2.11.2. Access/egress steps
(6) If a step board is fitted and it is an extension of a door sill outside the vehicle, and there is no change in level between the step board and the floor of the vehicle, this shall not be considered to be a step for the purposes of this specification. A minimal drop in level, with a maximum of 60 mm, between the floor surface at door sill and that of the exterior of the vehicle, used to guide and seal the door is also permissible and shall not be considered as a step.
(7) Access to the vestibule shall be achieved with a maximum of 4 steps of which one may be external.
(8) Rolling stock intended to stop, in normal operation, at existing platforms below 380 mm height and having their passenger access doors above bogies need not comply with points (2) and (5) above if it can be demonstrated that this achieves a more even distribution of the steps height.
```

</details>

### R202 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].
- **After:** Internal steps (other than those for external access) should have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R203 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].
- **After:** Internal steps in a passenger vehicle shall have a minimum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R204 · `NUM` · out-of-context

_a number was changed_

- **Before:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].
- **After:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 300 mm, measured at the central axis of the stairs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R205 · `NUM` · out-of-context

_a number was changed_

- **Before:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].
- **After:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 300 mm, measured at the central axis of the stairs[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R206 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].
- **After:** Internal steps in a passenger vehicle should have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R207 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].
- **After:** Internal steps (other than those for external access) shall have a minimum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R208 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1].
- **After:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R209 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].
- **After:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R210 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Internal steps (other than those for external access) shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs[1].
- **Appended:** Each step must be lit by a light at floor level [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R211 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Internal steps in a passenger vehicle shall have a maximum height of 200 mm and a minimum depth of 280 mm, measured at the central axis of the stairs [1]. For double deck trains, it is permitted to reduce this depth value to 270 mm for the stairs accessing the upper deck and the lower deck [1].
- **Appended:** Each step must be lit by a light at floor level [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n13

**Question:** What minimum size and load must a baby nappy changing table on a train have?

<details><summary>[1] PRM TSI, 5.3.2.5. Baby nappy changing table</summary>

```
PRM TSI, 5.3.2.5. Baby nappy changing table
(1) The usable surface of the baby nappy changing table shall be a minimum of 500 mm wide and 700 mm long.
(2) It shall be designed to prevent a baby from inadvertently sliding off, shall have no sharp edges and shall be able to take a minimum load of 80 kg.
(3) It shall be possible to put it into the stowed position with only one hand, using a force not exceeding 25 N.
```

</details>

<details><summary>[2] PRM TSI, 5.3.2.4. Universal toilet</summary>

```
PRM TSI, 5.3.2.4. Universal toilet
(17) If a baby nappy changing table is provided, in the lowered position its usable surface shall be between 800 mm and 1 000 mm above floor level.
```

</details>

<details><summary>[3] PRM TSI, 4.2.1.6. Toilets and baby nappy changing facilities</summary>

```
PRM TSI, 4.2.1.6. Toilets and baby nappy changing facilities
(1) If toilets are provided at a station, then a minimum of one unisex cubicle shall be wheelchair accessible.
(2) If baby nappy changing facilities are provided at a station, then a minimum of one baby nappy changing facility shall be accessible to both men and women wheelchair users.
```

</details>

### R212 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].
- **Appended:** It must be fitted with a safety strap [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R213 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The usable surface of a baby nappy changing table on a train must be a minimum of 500 mm wide and 700 mm long [1].
- **After:** The usable surface of a baby nappy changing table on a train must be a maximum of 500 mm wide and 700 mm long [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R214 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].
- **After:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R215 · `NUM` · out-of-context

_a number was changed_

- **Before:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].
- **After:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 100 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R216 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].
- **After:** The usable surface of the baby nappy changing table must be at most 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R217 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The usable surface of a baby nappy changing table on a train must be a minimum of 500 mm wide and 700 mm long [1].
- **After:** The usable surface of a baby nappy changing table on a train must be a minimum of 500 mm wide and 700 mm long [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R218 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Additionally, it must be able to take a minimum load of 80 kg [1].
- **After:** Additionally, it should be able to take a minimum load of 80 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R219 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it must be able to take a minimum load of 80 kg [1].
- **After:** The usable surface of the baby nappy changing table must be at least 500 mm wide and 700 mm long, and it should be able to take a minimum load of 80 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R220 · `NUM` · out-of-context

_a number was changed_

- **Before:** Additionally, it must be able to take a minimum load of 80 kg [1].
- **After:** Additionally, it must be able to take a minimum load of 100 kg [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R221 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The usable surface of a baby nappy changing table on a train must be a minimum of 500 mm wide and 700 mm long [1]. Additionally, it must be able to take a minimum load of 80 kg [1].
- **Appended:** It must be fitted with a safety strap [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n14

**Question:** What diameter must handrails in a passenger vehicle have, and how much clearance from adjacent surfaces?

<details><summary>[1] PRM TSI, 4.2.2.9. Handrails</summary>

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

</details>

<details><summary>[2] PRM TSI, 4.2.2.1.1. General</summary>

```
PRM TSI, 4.2.2.1.1. General
(1) Handholds or vertical handrails or other items that can be used for personal stability, whilst using the aisle, shall be provided on all aisle-side seats unless the seat, when in the upright position, is within 200 mm of: — the back of another seat facing in the opposite direction which is fitted at its aisle side with a handhold or a vertical handrail or other items that can be used for personal stability, — a handrail or a partition provided at the aisle side of the seat.
(2) Handholds or other items that can be used for personal stability shall be positioned at a height of between 800 mm and 1 200 mm above the floor, measured from the centre of the usable part of the handhold, shall not protrude into the clearway and shall contrast with the seat.
(3) In seating areas with fixed longitudinal seats, handrails shall be used for personal stability. These handrails shall be at a maximum distance of 2 000 mm apart, shall be positioned at a height of between 800 mm and 1 200 mm above the floor and shall contrast with the vehicle interior surroundings.
(4) The handholds or other items shall not have sharp edges.
```

</details>

<details><summary>[3] SRT TSI, 4.2.1.6. Escape walkways</summary>

```
SRT TSI, 4.2.1.6. Escape walkways
This specification applies to all tunnels of more than 0,5 km in length.
(a) Walkways shall be constructed in a single track tunnel tube on at least one side of the track and in a multiple track tunnel tube on both sides of the tunnel tube. In tunnel tubes with more than two tracks, access to a walkway shall be possible from each track. (1) The width of the walkway shall be at least 0.8 m. (2) The minimum vertical clearance above the walkway shall be 2.25 m. (3) The height of the walkway shall be at bottom -of-rail level or higher. (4) Local constrictions caused by obstacles in the escape area shall be avoided. The presence of obstacles shall not reduce the minimum width to less than 0,7 m, and the length of the obstacle shall not exceed 2 m.
(b) Continuous handrails shall be installed between 0.8 m and 1.1 m above the walkway providing a route to a safe area. (1) Handrails shall be placed outside the required minimum clearance of the walkway. (2) Handrails shall be angled at 30° to 40° to the longitudinal axis of the tunnel at the entrance to and exit from an obstacle.
```

</details>

### R222 · `NUM` · in-context

_a number was changed_

- **Before:** Additionally, they must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Additionally, they must have a minimum clear distance of 50 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R223 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** All handrails fitted to a vehicle must be round in section with an outside diameter of 30 mm to 40 mm [1]. Additionally, they must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **Appended:** Handrails must be made of a non-conductive material [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R224 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Handrails should be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R225 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** All handrails fitted to a vehicle must be round in section with an outside diameter of 30 mm to 40 mm [1].
- **After:** All handrails fitted to a vehicle should be round in section with an outside diameter of 30 mm to 40 mm [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R226 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Additionally, they must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Additionally, they must have a maximum clear distance of 45 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R227 · `NUM` · in-context

_a number was changed_

- **Before:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 50 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R228 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a maximum clear distance of 45 mm to any adjacent surface other than its mountings [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R229 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** All handrails fitted to a vehicle must be round in section with an outside diameter of 30 mm to 40 mm [1].
- **After:** All handrails fitted to a vehicle must be round in section with an outside diameter of 30 mm to 40 mm [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R230 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **After:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R231 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Handrails shall be round in section with an outside diameter of 30 mm to 40 mm and must have a minimum clear distance of 45 mm to any adjacent surface other than its mountings [1].
- **Appended:** Handrails must be made of a non-conductive material [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n15

**Question:** What are the noise limits in the driver's cab at standstill with horns sounding, and at maximum speed below 250 km/h?

<details><summary>[1] NOI TSI, 4.2.4. Limits for the driver's cab interior noise</summary>

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

</details>

<details><summary>[2] NOI TSI, 4.2.3. Limits for pass-by noise</summary>

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

</details>

<details><summary>[3] NOI TSI, 4.2.2. Limits for starting noise</summary>

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

</details>

### R232 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The noise limit for the driver's cab at standstill with horns sounding is 95 dB [1].
- **After:** The noise limit for the driver's cab at standstill with horns sounding is 95 dB [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R233 · `NUM` · out-of-context

_a number was changed_

- **Before:** At maximum speed vmax if vmax < 250 km/h, the noise limit is 78 dB [1].
- **After:** At maximum speed vmax if vmax < 250 km/h, the noise limit is 75 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R234 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The noise limit for the driver's cab at standstill with horns sounding is 95 dB [1]. At maximum speed vmax if vmax < 250 km/h, the noise limit is 78 dB [1].
- **Appended:** The measurement must be repeated with the cab windows open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R235 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** At maximum speed vmax if vmax < 250 km/h, the noise limit is 78 dB [1].
- **After:** At maximum speed, the noise limit is 78 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R236 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The noise limit for the driver's cab at standstill with horns sounding is 95 dB [1].
- **After:** The minimum noise level for the driver's cab at standstill with horns sounding is 95 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R237 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].
- **After:** At standstill with horns sounding the minimum level is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R238 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].
- **Appended:** The measurement must be repeated with the cab windows open [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R239 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].
- **After:** At standstill with horns sounding the limit is 95 dB, and at maximum speed the limit is 78 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R240 · `NUM` · out-of-context

_a number was changed_

- **Before:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 78 dB [1].
- **After:** At standstill with horns sounding the limit is 95 dB, and at maximum speed when vmax < 250 km/h the limit is 75 dB [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n16

**Question:** In the starting noise conformity test, up to what speed must the train accelerate?

<details><summary>[1] NOI TSI, 6.2.2.2. Starting noise</summary>

```
NOI TSI, 6.2.2.2. Starting noise
The demonstration of conformity with the limit values on starting noise as set out in point 4.2.2 shall be carried out in accordance with the specification referenced in Appendix B, Index [1]. The maximum level method shall apply. Deviating from the test procedure of the specification, the train shall accelerate from standstill up to 30 km/h and then maintain the speed.
In addition the noise shall be measured at the same distance from the centre of the track and the same height above top of rail as set out in point 4.2.2. The ‘averaged level method’ and the ‘maximum level method’ in accordance with the specification referenced in Appendix B, Index [1] shall apply and the train shall accelerate from standstill up to 40 km/h and then maintain the speed. The measured values are not assessed against any limit value and shall be recorded in the technical file and communicated to the Agency.
For special vehicles the starting procedure shall be performed without additional trailer loads.
```

</details>

<details><summary>[2] NOI TSI, 4.2.2. Limits for starting noise</summary>

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

</details>

<details><summary>[3] NOI TSI, 6.2.2.3.1. Test track conditions</summary>

```
NOI TSI, 6.2.2.3.1. Test track conditions
Confirmation shall be provided in the technical file that the track data related to the type's pass-by noise measurement were valid during the day(s) of testing, e.g. by providing the date of last maintenance having an impact on noise.
Furthermore, it is permitted to carry out tests at speeds equal to or higher than 250 km/h on slab tracks. In that case the limit values shall be 2 dB higher than those set out in point 4.2.3.
```

</details>

### R241 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [1].
- **Appended:** The test must be carried out at night [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R242 · `NUM` · in-context

_a number was changed_

- **Before:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [1].
- **After:** The train must accelerate from standstill up to 40 km/h before maintaining the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R243 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [1].
- **After:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R244 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [1]. Additionally, for the averaged level method and the maximum level method, the train shall accelerate from standstill up to 40 km/h and then maintain the speed [1].
- **Appended:** The test must be carried out at night [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R245 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [1].
- **After:** In the starting noise conformity test using the maximum level method, the train may accelerate from standstill up to 30 km/h and then maintain the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R246 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The train must accelerate from standstill up to 30 km/h before maintaining the speed [1].
- **After:** The train may accelerate from standstill up to 30 km/h before maintaining the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R247 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [1].
- **After:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R248 · `NUM` · in-context

_a number was changed_

- **Before:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 30 km/h and then maintain the speed [1].
- **After:** In the starting noise conformity test using the maximum level method, the train shall accelerate from standstill up to 40 km/h and then maintain the speed [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n18

**Question:** How often must staff doing safety-critical tasks have a periodic medical examination under the OPE TSI?

<details><summary>[1] OPE TSI, 4.7.2.2.1. Frequency of periodic medical examinations</summary>

```
OPE TSI, 4.7.2.2.1. Frequency of periodic medical examinations
At least one systematic medical examination shall be performed:
— Every 5 years for staff aged up to 40;
— Every 3 years for staff aged between 41 and 62;
— Every year for staff aged over 62.
Increased frequency of examination shall be set by the medical doctor if the state of health of the member of the staff requires so.
```

</details>

<details><summary>[2] OPE TSI, 4.7.2.2.2. Content of the periodic medical examination</summary>

```
OPE TSI, 4.7.2.2.2. Content of the periodic medical examination
If the worker complies with the criteria required at the examination, which is carried out before practising an occupation, the periodic specialised examinations shall include ————— :
— General medical examination;
— Examination of sensory functions (vision, hearing, colour perception);
— Urine or blood analysis for the detection of diabetes mellitus and other conditions as indicated by the clinical examination;
— Screening for abuse of drugs where clinically indicated.
```

</details>

<details><summary>[3] OPE TSI, 4.7.2.2.3. Additional medical examinations and/or psychological assessments</summary>

```
OPE TSI, 4.7.2.2.3. Additional medical examinations and/or psychological assessments
Besides the periodic medical examination, an additional specific medical examination and/or psychological assessment shall be performed where there is reasonable ground for doubting the medical or psychological fitness of a member of staff or reasonable suspicion of use of drugs or use of alcohol over the limits allowed. This would be the case especially after an incident or accident caused by human error on the part of the individual.
The railway undertaking and the infrastructure manager shall put systems in place to ensure that such additional examinations and assessments are undertaken as appropriate.
```

</details>

### R249 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].
- **After:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R250 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].
- **Appended:** The examination results must be kept for at least ten years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R251 · `NUM` · in-context

_a number was changed_

- **Before:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].
- **After:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every year if they are aged between 41 and 62, and every year if they are aged over 62 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R252 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Staff performing safety-critical tasks must undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].
- **After:** Staff performing safety-critical tasks should undergo a systematic medical examination at least every 5 years if they are aged up to 40, every 3 years if they are aged between 41 and 62, and every year if they are aged over 62 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R253 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1].
- **After:** Under the OPE TSI, systematic periodic medical examinations for staff should be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R254 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1]. Additionally, an increased frequency must be set by the medical doctor if the staff member's state of health requires it [1].
- **Appended:** The examination results must be kept for at least ten years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R255 · `NUM` · in-context

_a number was changed_

- **Before:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1].
- **After:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every year for staff aged between 41 and 62, and every year for staff aged over 62 [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R256 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [1].
- **After:** Under the OPE TSI, systematic periodic medical examinations for staff must be performed at least every 5 years for staff aged up to 40, every 3 years for staff aged between 41 and 62, and every year for staff aged over 62 [2].

- [ ] Accept  - [ ] Reject

**Note:** 

## n19

**Question:** When should a driver avoid using manually activated sanding equipment, and when is sanding still appropriate there?

<details><summary>[1] OPE TSI, 1. SANDING</summary>

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

</details>

<details><summary>[2] CCS TSI, 7.7.2.9. Italy</summary>

```
CCS TSI, 7.7.2.9. Italy
Specific case | Category | Notes
4.2.10 Trackside Train Detection Systems Index 77, point 3.1.4.1 In addition to the TSI requirements, following criteria shall be respected. The allowed maximum amount of sand per sanding device within 30 s is: (1) For speed v ≤ 140 km/h; 400 g + 100 g (2) For speed v > 140 km/h; 650 g + 150 g | T | The national values for dispensing sand will remain valid until harmonized test specifications (currently non-existent) are available for demonstrating that different modes for dispensing sand are safety-acceptable for train detection systems operating in Italy.
```

</details>

<details><summary>[3] CCS TSI, 7.7.2.7. Luxembourg</summary>

```
CCS TSI, 7.7.2.7. Luxembourg
Specific case | Category | Notes
4.2.10 Trackside Train Detection Systems Index 77, point 3.1.4.1: (1) The output of the sanding devices fitted to the vehicle shall not exceed 0,3 l per minute per rail. (2) The sanding in the stations identified in the infrastructure register is prohibited. (3) The Sanding in the area of switches is prohibited. (4) For emergency braking, no restrictions shall apply. | T | 
4.2.11 Electromagnetic Compatibility between Rolling Stock and Control-Command and Signalling trackside equipment Index 77, point 3.2.2.3: The measurement and evaluation of rolling stock with individual track circuits shall be done according to the document GI.II.STC-VF (parameters A1, A4, V2 and D1). | T | Applicable on vehicles This specific case is needed as long as track circuits (operating frequency 83,3 Hz) are used. Document GI.II.STC.VF is available on the website of the NSA LU (1).
4.2.11 Electromagnetic Compatibility between Rolling Stock and Control-Command and Signalling trackside equipment Index 77, point 3.2.2.3: The measurement and evaluation of rolling stock with individual track circuits shall be done according to the document GI.II.STC-VF (parameters A5, V2 and D2). | T | Applicable on vehicles This specific case is needed as long as track circuits (operating frequency 125 Hz) are used. Document GI.II.STC.VF is available on the website of the NSA LU.
(1) ‘NSA LU’ stands for ‘National Safety Authority of Luxembourg’: Administration des Chemins de Fer (ACF), www.railinfra.lu (website).
```

</details>

### R257 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1]. However, sanding is still appropriate if there is a risk of SPAD (Signal Passed At Danger) or another serious incident and applying sand assists adhesion, when starting away, or when required to test the sanding equipment on the traction unit [1].
- **Appended:** Sand must not be applied in tunnels longer than 1 km [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R258 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].
- **After:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R259 · `NUM` · out-of-context

_a number was changed_

- **Before:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].
- **After:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 25 km/h, and when at standstill[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R260 · `NUM` · out-of-context

_a number was changed_

- **Before:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].
- **After:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 25 km/h, and when at standstill [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R261 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].
- **After:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking, and when at standstill[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R262 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].
- **After:** Drivers equipped with manually activated sanding equipment shall use it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R263 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].
- **After:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R264 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].
- **After:** The driver shall use manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R265 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill [1].
- **After:** Drivers equipped with manually activated sanding equipment shall avoid using it in the area of points and crossings, during braking, and when at standstill [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R266 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The driver shall avoid using manually activated sanding equipment wherever possible: in the area of points and crossings, during braking at speeds less than 20 km/h, and when at standstill[1]. Sanding is still appropriate if there is a risk of SPAD or another serious incident and sand would improve adhesion, when starting away, or when required to test the sanding equipment on the traction unit[1].
- **Appended:** Sand must not be applied in tunnels longer than 1 km [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n20

**Question:** For trains able to run faster than 200 km/h, what braking information may the infrastructure manager provide?

<details><summary>[1] OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed</summary>

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(2) The infrastructure manager may provide the following information: (i) For trains able to run at a maximum speed higher than 200 km/h, deceleration profile and equivalent response time on level track; (ii) For trainsets or for fixed train compositions, unable to run at a maximum speed higher than 200 km/h, deceleration (as above in (i)) or brake weight percentage; (iii) For other trains (variable compositions of trains unable to run at a maximum speed higher than 200 km/h): brake weight percentage. If the infrastructure manager provides the above mentioned information, it shall be made available to all railway undertakings who intend to operate trains on its network in a non-discriminatory way. The braking tables already in use and accepted for the existing non TSI conform lines at the date of entry into force of the present Regulation shall also be made available.
```

</details>

<details><summary>[2] OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed</summary>

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(1) The infrastructure manager shall provide the railway undertaking with all relevant line characteristics for each route through RINF: (i) signalling distances (warning, stopping) containing their inherent safety margins, that are provided via the respective locations of ‘Stopping signal’ and ‘Warning signal’, requested in Appendix D2 via the parameter 1.1.1.3.14.3; (ii) gradients; (iii) maximum permitted speeds; (iv) conditions of use of braking systems possibly affecting the infrastructure such as magnetic, regenerative and eddy current brake. The infrastructure manager shall ensure that the information provided to the railway undertaking(s) is complete and accurate, and shall inform the railway undertaking of the changes on the line characteristics through RINF whenever such information becomes available and affects trains operation.
```

</details>

<details><summary>[3] OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed</summary>

```
OPE TSI, 4.2.2.6.2. Braking performance and maximum speed allowed
(3) The railway undertaking shall, in the planning stage, determine the braking regime, the braking capability and corresponding maximum speed of the train taking into account: (i) the relevant line characteristics as expressed in point (1) and, if available, the information provided by the infrastructure manager in accordance to point (2); and (ii) the rolling stock-related margins derived from reliability and availability of the braking system. Furthermore, the railway undertaking shall ensure that during operation each train achieves at least the necessary braking performance. In particular the railway undertaking has to set up rules to be used if a train does not reach the necessary braking performance during operation. In this case, the railway undertaking shall immediately inform the infrastructure manager. The infrastructure manager may take appropriate measures to reduce the impact on the overall traffic on its network.
```

</details>

### R267 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [1].
- **Appended:** This information must be updated every time the timetable changes [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R268 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may not provide the deceleration profile and the equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R269 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager must provide the deceleration profile and the equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R270 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may not provide the deceleration profile and equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R271 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [1].
- **Appended:** This information must be updated every time the timetable changes [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R272 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R273 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and the equivalent response time on level track [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R274 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager may provide the deceleration profile and equivalent response time on level track [1].
- **After:** For trains able to run at a maximum speed higher than 200 km/h, the infrastructure manager must provide the deceleration profile and equivalent response time on level track [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n21

**Question:** After the Commission mandates it, how quickly must the Agency start consulting the parties about a Member State's measure against a non-compliant interoperability constituent?

<details><summary>[1] Interoperability Directive, Article 11 — Non-compliance of interoperability constituents with essential requirements</summary>

```
Interoperability Directive, Article 11 — Non-compliance of interoperability constituents with essential requirements
1. Where a Member State finds that an interoperability constituent covered by the ‘EC’ declaration of conformity or suitability for use and placed on the market is, when used as intended, unlikely to meet the essential requirements, that Member State shall take all necessary steps to restrict its field of application, prohibit its use, withdraw it from the market or recall it. The Member State shall forthwith inform the Commission, the Agency and the other Member States of the measures taken and give reasons for its decision, stating in particular whether the failure to conform is due to: (a) failure to meet the essential requirements; (b) incorrect application of European specifications where application of such specifications is relied upon; (c) inadequacy of European specifications.
2. The Agency, on a mandate from the Commission, shall start the consultation process with the parties concerned without delay and in any case within 20 days of the date of receipt of that mandate. Where, following that consultation, the Agency establishes that the measure is unjustified, it shall forthwith inform the Commission, the Member State that has taken the initiative as well as other Member States, and the manufacturer or his authorised representative. Where the Agency establishes that the measure is justified, it shall forthwith inform the Member States.
```

</details>

<details><summary>[2] Interoperability Directive, Article 53 — Reports and information</summary>

```
Interoperability Directive, Article 53 — Reports and information
1. By 16 June 2018, the Commission shall report on the progress made in preparing for the Agency's enhanced role under this Directive. Additionally, every three years and for the first time three years after the end of the transitional period provided for by Article 54, the Commission shall report to the European Parliament and to the Council on the progress made towards achieving interoperability of the Union rail system and the functioning of the Agency in this context. That report shall also include an evaluation of the implementation and use of the registers under Chapter VII and an analysis of the cases set out in Article 7 and of the application of Chapter V, assessing in particular the functioning of the cooperation agreements concluded between the Agency and national safety authorities. For the purposes of the first report, after the end of the transitional period the Commission shall carry out extensive consultations with the relevant stakeholders and shall establish a programme to allow for the assessment of progress. The Commission shall, if appropriate in the light of the above analysis, propose legislative measures including measures for the future role of the Agency in enhancing interoperability.
2. The Agency shall develop and periodically update a tool capable of providing, at the request of a Member State, the European Parliament or of the Commission, an overview of the interoperability level of the Union rail system. That tool shall use the information included in the registers provided for in Chapter VII.
```

</details>

<details><summary>[3] Interoperability Directive, Article 50 — Exercise of delegation</summary>

```
Interoperability Directive, Article 50 — Exercise of delegation
1. The power to adopt delegated acts is conferred on the Commission subject to the conditions laid down in this Article.
2. The power to adopt delegated acts referred to in Article 5(1) shall be conferred on the Commission for a period of five years from 15 June 2016. The Commission shall draw up a report in respect of the delegation of power not later than nine months before the end of the five-year period. The delegation of power shall be tacitly extended for periods of an identical duration, unless the European Parliament or the Council opposes such extension not later than three months before the end of each period.
3. It is of particular importance that the Commission follow its usual practice and carry out consultations with experts, including Member States' experts, before adopting those delegated acts.
4. The delegation of power referred to in Article 5(1) may be revoked at any time by the European Parliament or by the Council. A decision of revocation shall put an end to the delegation of the power specified in that decision. It shall take effect the day following the publication of the decision in the Official Journal of the European Union or at a later date specified therein. It shall not affect the validity of any delegated acts already in force.
5. As soon as it adopts a delegated act, the Commission shall notify it simultaneously to the European Parliament and to the Council.
```

</details>

### R275 · `NUM` · out-of-context

_a number was changed_

- **Before:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]
- **After:** The Agency must begin the consultation process without delay and, in any case, within 10 days of receiving the Commission’s mandate.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

### R276 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]
- **After:** The Agency should begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]

- [ ] Accept  - [ ] Reject

**Note:** 

### R277 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]
- **After:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R278 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].
- **After:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R279 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** The Agency must begin the consultation process without delay and, in any case, within 20 days of receiving the Commission’s mandate.[1]
- **Appended:** The consultation must be completed within 60 days [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R280 · `NUM` · out-of-context

_a number was changed_

- **Before:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].
- **After:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 10 days of the date of receipt of that mandate [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R281 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].
- **Appended:** The consultation must be completed within 60 days [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R282 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** After receiving a mandate from the Commission, the Agency must start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].
- **After:** After receiving a mandate from the Commission, the Agency should start the consultation process with the concerned parties without delay and in any case within 20 days of the date of receipt of that mandate [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n22

**Question:** What speeds characterise specially built and specially upgraded high-speed lines in the Union's network?

<details><summary>[1] Interoperability Directive, 1. Network</summary>

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

</details>

<details><summary>[2] ENE TSI, 7.3.1. Performance criteria of the subsystem</summary>

```
ENE TSI, 7.3.1. Performance criteria of the subsystem
In addition to the cases referred to in point 7.2.(3), ‘upgrading’ is a major modification work of an existing energy subsystem resulting in an increase of the line speed of more than 30km/h.
```

</details>

<details><summary>[3] Interoperability Directive, 2. Vehicles</summary>

```
Interoperability Directive, 2. Vehicles
For the purposes of this Directive, Union vehicles shall comprise all vehicles likely to travel on all or part of the Union's network:
— locomotives and passenger rolling stock, including thermal or electric traction units, self-propelling thermal or electric passenger trains, and passenger coaches;
— freight wagons, including low-deck vehicles designed for the entire network and vehicles designed to carry lorries;
— special vehicles, such as on-track machines.
This list of vehicles shall include those which are specially designed to operate on the different types of high-speed lines described in point 1.
```

</details>

### R283 · `NUM` · in-context

_a number was changed_

- **Before:** Specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h [1].
- **After:** Specially upgraded high-speed lines are equipped for speeds of the order of 250 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R284 · `NUM` · in-context

_a number was changed_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].
- **After:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 250 km/h[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R285 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].
- **Appended:** Lines in both categories must be fully equipped with ETCS [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R286 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].
- **After:** Specially built high-speed lines are equipped for speeds equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R287 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [1].
- **After:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R288 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [1].
- **After:** Specially built high-speed lines are equipped for speeds equal to or greater than 250 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R289 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].
- **After:** Specially built high-speed lines are equipped for speeds generally equal to or less than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R290 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [1].
- **After:** Specially built high-speed lines are equipped for speeds generally equal to or less than 250 km/h [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R291 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h[1], while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h[1].
- **After:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h, while specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R292 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Specially built high-speed lines are equipped for speeds generally equal to or greater than 250 km/h [1]. Specially upgraded high-speed lines are equipped for speeds of the order of 200 km/h [1].
- **Appended:** Lines in both categories must be fully equipped with ETCS [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n23

**Question:** What exercise is required before a railway tunnel longer than 1 km opens?

<details><summary>[1] SRT TSI, 4.4.3. Exercises</summary>

```
SRT TSI, 4.4.3. Exercises
These rules apply to tunnels of > 1 km.
(a) Prior to the opening of a single tunnel or a series of tunnels, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, shall take place.
(b) The emergency plan shall define how all organisations involved can be familiarised with the infrastructure and how often visits to the tunnel and table top or other exercises have to take place.
```

</details>

<details><summary>[2] SRT TSI, 4.4.6. Operational rules related to trains running in tunnels</summary>

```
SRT TSI, 4.4.6. Operational rules related to trains running in tunnels
(b) Operation of Category A rolling stock is permitted on lines where the distance between evacuation and rescue points , or the length of tunnels exceeds 5 km, in the case where there are no passengers on board.
(c) Operational rules shall be put in place to avoid panic and spontaneous, uncontrolled evacuation in the case of a prolonged stop of a train in a tunnel without the occurrence of a hot or cold incident.
```

</details>

<details><summary>[3] SRT TSI, 4.2.1.7. Evacuation and rescue points</summary>

```
SRT TSI, 4.2.1.7. Evacuation and rescue points
This specification applies to all tunnels of more than 1 km in length.
(a) For the purpose of this clause, two or more consecutive tunnels will be considered as a single tunnel unless both of the following conditions are met: (1) The separation between tunnels in open air is longer than the maximum length of the passenger train intended to be operated on the line + 100 m and (2) The open air area and track situation around the separation between tunnels allow passengers to move away from the train along a a safe space . The open air area shall contain all passengers of the maximum capacity of the train intended to be operated on the line.
(b) Evacuation and rescue points shall be created (1) Outside both portals of every tunnel of > 1 km and (2) Inside the tunnel, according to the category of rolling stock that is planned to be operated, as summarized in the table below: Rolling stock category according to paragraph 4.2.3 | Maximum distance from the portals to an evacuation and rescue point and between evacuation and rescue points Category A | 5 km Category B | 20 km
```

</details>

### R293 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].
- **After:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R294 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].
- **After:** After the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R295 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].
- **After:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, should be carried out [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R296 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].
- **Appended:** The exercise must then be repeated every two years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R297 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].
- **After:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [2].

- [ ] Accept  - [ ] Reject

**Note:** 

### R298 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].
- **After:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures should take place, involving all categories of personnel defined within the emergency plan [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R299 · `NEG`

_a requirement was negated or its direction reversed_

- **Before:** Before opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].
- **After:** After opening a tunnel longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures, involving all categories of personnel defined within the emergency plan, must be carried out [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R300 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** Prior to the opening of a single tunnel or a series of tunnels longer than 1 km, a full-scale exercise comprising evacuation and rescue procedures must take place, involving all categories of personnel defined within the emergency plan [1].
- **Appended:** The exercise must then be repeated every two years [1].

- [ ] Accept  - [ ] Reject

**Note:** 

## n24

**Question:** In a tunnel longer than 1 km where the traction power supply is divided into sections, what must be possible?

<details><summary>[1] SRT TSI, 4.2.2.1. Sectioning of contact line</summary>

```
SRT TSI, 4.2.2.1. Sectioning of contact line
This specification applies to all tunnels of more than 1 km length.
(a) The traction power supply system in tunnels may be divided into sections.
(b) In such case, it shall be possible to switch off each section of the contact line, either locally or remotely.
```

</details>

<details><summary>[2] ENE TSI, 4.2.16.1. General</summary>

```
ENE TSI, 4.2.16.1. General
(1) The design of system separation sections shall ensure that trains can move from one traction power supply system to an adjacent different traction power supply system without bridging the two systems. There are two methods for traversing system separation sections: (a) with pantograph raised and touching the contact wire; (b) with pantograph lowered and not touching the contact wire.
(2) The neighbouring Infrastructure Managers shall agree either (a) or (b) according to the prevailing circumstances.
(3) The overall length D of neutral sections is defined in the specification referenced in Appendix E, Index [2]. For the calculation of D clearances, the specification referenced in Appendix E, Index [3] and an uplift of S0 shall be taken into account.
```

</details>

<details><summary>[3] SRT TSI, 4.4.4. Switching off and Earthing procedures</summary>

```
SRT TSI, 4.4.4. Switching off and Earthing procedures
These rules apply to all tunnels.
(a) In the case it is required to switch off the traction power supply system the infrastructure manager shall make sure that relevant sections of the contact line have been switched off, and inform the emergency response services before they enter the tunnel or a section of the tunnel.
(b) It is the responsibility of the infrastructure manager to switch off the traction power supply.
(c) Procedures and responsibilities for earthing of the contact line shall be defined between the Infrastructure Manager and the emergency response services, and reported in the emergency plan. Provision shall be made for switching off the section in which the incident has taken place.
```

</details>

### R301 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** It must be possible to switch off each section of the contact line, either locally or remotely [1].
- **Appended:** Each section must be no longer than 5 km [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R302 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, either locally or remotely [1].
- **After:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, remotely [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R303 · `ADD`

_a sentence was appended that no passage supports_

- **Answer:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, either locally or remotely [1].
- **Appended:** Each section must be no longer than 5 km [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R304 · `QUAL`

_an obligation was weakened/strengthened, or a condition/exception was removed_

- **Before:** It must be possible to switch off each section of the contact line, either locally or remotely [1].
- **After:** It must be possible to switch off each section of the contact line, remotely [1].

- [ ] Accept  - [ ] Reject

**Note:** 

### R305 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, either locally or remotely [1].
- **After:** In tunnels of more than 1 km length where the traction power supply is divided into sections, it must be possible to switch off each section of the contact line, either locally or remotely [3].

- [ ] Accept  - [ ] Reject

**Note:** 

### R306 · `CITE`

_the citation now points to a passage that does not support the sentence_

- **Before:** It must be possible to switch off each section of the contact line, either locally or remotely [1].
- **After:** It must be possible to switch off each section of the contact line, either locally or remotely [2].

- [ ] Accept  - [ ] Reject

**Note:** 
