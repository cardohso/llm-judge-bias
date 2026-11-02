# Bound direction: a lower bound (minimum, at least) only moves up and an upper bound (maximum,
# limit, within) only moves down, so the new claim is never implied by the old one.
# Hand-written planted errors (Claude Opus 5.5, 2026-11-02). Emits perturbations/handwritten.jsonl.
# E(q, gen, type, sentence, find, replace[, subtype]); ADD(q, sentence) applies to both generators.
import json
import sys

rows = []


def E(q, g, t, i, find, repl, sub=""):
    if t == "NUM":
        sub = sub or "in-context"
    rows.append(
        {
            "question": q,
            "generator": g,
            "type": t,
            "subtype": sub,
            "sentence": i,
            "find": find,
            "replace": repl,
        }
    )


def ADD(q, text):
    rows.append({"question": q, "generator": "AB", "type": "ADD", "subtype": "", "text": text})


# q01
ADD("q01", "This limit is measured with the main air compressor running for at least 10 minutes")
E("q01", "A", "NUM", 1, "65 dB", "64 dB")
E("q01", "B", "NUM", 1, "65 dB", "64 dB")
E(
    "q01",
    "A",
    "NEG",
    1,
    "the stationary noise limit LpAeq,T[unit] is 65 dB",
    "the stationary noise level LpAeq,T[unit] must be at least 65 dB",
)
E(
    "q01",
    "B",
    "NEG",
    1,
    "The stationary noise limit LpAeq,T for an EMU is 65 dB",
    "The stationary noise level LpAeq,T for an EMU must be at least 65 dB",
)
E("q01", "A", "QUAL", 1, "For an electric multiple unit (EMU), the", "For all rolling stock, the")
E("q01", "B", "QUAL", 1, "for an EMU", "for all rolling stock")
# q02
ADD("q02", "The limit is relaxed for wagons that entered service before 2005")
E("q02", "A", "NUM", 1, "83 dB", "81 dB")
E("q02", "B", "NUM", 1, "83 dB(A)", "81 dB(A)")
E(
    "q02",
    "A",
    "NEG",
    1,
    "The pass-by noise limit for wagons (normalised to APL = 0,225) at 80 km/h is 83 dB",
    "The pass-by noise level of wagons (normalised to APL = 0,225) at 80 km/h must be at least 83 dB",
)
E(
    "q02",
    "B",
    "NEG",
    1,
    "The pass-by noise limit for wagons at 80 km/h is 83 dB(A)",
    "The pass-by noise level of wagons at 80 km/h must be at least 83 dB(A)",
)
E("q02", "A", "QUAL", 1, "at 80 km/h is", "at all speeds is")
E("q02", "B", "QUAL", 1, "at 80 km/h is", "at all speeds is")
# q03
ADD(
    "q03",
    "Walkways must be at least 1,2 m wide in tunnels used by trains running faster than 200 km/h",
)
E("q03", "A", "NUM", 1, "at least 0.8 m", "at least 1.1 m")
E("q03", "B", "NUM", 1, "at least 0.8 m wide", "at least 1.1 m wide")
E("q03", "A", "NEG", 1, "must be at least 0.8 m", "must be at most 0.8 m")
E("q03", "B", "NEG", 1, "must be at least 0.8 m wide", "must be at most 0.8 m wide")
E("q03", "A", "QUAL", 1, "must be at least 0.8 m", "should be at least 0.8 m")
E("q03", "B", "QUAL", 1, "must be at least 0.8 m wide", "should be at least 0.8 m wide")
# q05
ADD(
    "q05",
    "Category B rolling stock must keep running for 15 minutes at 80 km/h after a fire is detected",
)
E("q05", "A", "NUM", 1, "and 20 km for Category B", "and 5 km for Category B")
E("q05", "B", "NUM", 1, "and 20 km for Category B", "and 5 km for Category B")
E("q05", "A", "NEG", 1, "The maximum distance", "The minimum distance")
E("q05", "B", "NEG", 1, "The maximum distance", "The minimum distance")
E("q05", "A", "QUAL", 3, " only when there are no passengers on board", "")
# q06
ADD("q06", "Each wheelchair space must have its own power socket for electric wheelchairs")
E("q06", "A", "NUM", 1, "not less than 3 wheelchair spaces", "not less than 4 wheelchair spaces")
E("q06", "B", "NUM", 1, "must have 3 wheelchair spaces", "must have 4 wheelchair spaces")
E("q06", "A", "NEG", 1, "not less than 3", "not more than 3")
E("q06", "B", "NEG", 1, "must have 3 wheelchair spaces", "may have at most 3 wheelchair spaces")
E("q06", "A", "QUAL", 1, "with a length of more than 205 to 300 metres", "of any length")
E("q06", "B", "QUAL", 1, "that is 250 m long", "of any length")
# q07
ADD("q07", "Doors used for wheelchair access must also have a minimum clear height of 1 900 mm")
E("q07", "A", "NUM", 2, "of 1 000 mm when open", "of 1 050 mm when open", "out-of-context")
E("q07", "B", "NUM", 2, "of 1 000 mm when open", "of 1 050 mm when open", "out-of-context")
E("q07", "A", "NEG", 1, "a minimum clear useable width", "a maximum clear useable width")
E("q07", "B", "NEG", 1, "The minimum clear usable width", "The maximum clear usable width")
E("q07", "A", "QUAL", 1, "shall have", "should have")
E("q07", "B", "QUAL", 2, "must have", "should have")
# q08
ADD("q08", "The DC 1,5 kV system may only be used on lines with speeds below 160 km/h")
E("q08", "A", "NUM", 1, "AC 15 kV, 16,7 Hz;", "AC 15 kV, 50 Hz;")
E("q08", "B", "NUM", 1, "AC 15 kV 16,7 Hz, DC 3 kV", "AC 15 kV 50 Hz, DC 3 kV")
E("q08", "A", "NEG", 2, "must be supplied with one of", "must not be supplied with one of")
E("q08", "B", "NEG", 2, "only the two AC systems", "neither of the two AC systems")
E("q08", "A", "QUAL", 2, "New lines with a speed greater than 250 km/h must", "New lines must")
E(
    "q08",
    "B",
    "QUAL",
    2,
    "For new lines with speeds greater than 250 km/h, only",
    "For new lines, only",
)
# q09 (no in-context number, no requirement to reverse, no qualifier)
ADD("q09", "ETCS must be fitted on all new high-speed lines from the date of their opening")
# q10
ADD("q10", "The lights must be visible from at least 200 m in daylight")
E("q10", "A", "NEG", 2, "shall also be considered to comply", "shall not be considered to comply")
E(
    "q10",
    "B",
    "NEG",
    2,
    "also complies with the requirement",
    "does not comply with the requirement",
)
E("q10", "A", "QUAL", 1, "shall consist", "should consist")
E("q10", "B", "QUAL", 1, "shall consist", "should consist")
# q11
ADD(
    "q11",
    "Wagons not yet fitted with the plates may still run until their next scheduled maintenance",
)
E("q11", "A", "NUM", 1, "1 January 2025", "1 January 2022")
E("q11", "B", "NUM", 1, "1 January 2025", "1 January 2022")
E("q11", "A", "NEG", 1, "from 1 January 2026", "until 1 January 2026")
E("q11", "B", "NEG", 1, "from 1 January 2026", "until 1 January 2026")
E("q11", "A", "QUAL", 1, "must be accepted", "may be accepted")
E("q11", "B", "QUAL", 1, "must be accepted", "may be accepted")
# q12
ADD("q12", "The deadline can be extended once if the applicant agrees")
E("q12", "A", "NUM", 1, "within four months", "within three months")
E("q12", "B", "NUM", 1, "within four months", "within three months")
E("q12", "A", "NEG", 1, "in any case within four months", "in any case not before four months")
E("q12", "B", "NEG", 1, "in any case within four months", "in any case not before four months")
E("q12", "A", "QUAL", 1, "The Agency shall issue", "The Agency should issue")
E("q12", "B", "QUAL", 1, "The Agency must issue", "The Agency should issue")
# q14
ADD("q14", "The doors must open with a force of no more than 150 N")
E("q14", "A", "NUM", 1, "1,4 m wide", "1,5 m wide")
E("q14", "B", "NUM", 1, "1,4 m wide", "1,5 m wide")
E("q14", "A", "NEG", 1, "a minimum clear opening", "a maximum clear opening")
E("q14", "B", "NEG", 1, "a minimum clear opening", "a maximum clear opening")
E("q14", "A", "QUAL", 1, "must have", "should have")
E("q14", "B", "QUAL", 1, "must have", "should have")
# q15
ADD("q15", "Software updates that do not change any parameter never require a new authorisation")
E("q15", "A", "NUM", 1, "point (b) of paragraph 10", "point (b) of paragraph 12")
E("q15", "B", "NUM", 1, "point (b) of paragraph 10", "point (b) of paragraph 12")
E("q15", "A", "NEG", 1, "which are outside the range", "which are within the range")
E("q15", "B", "NEG", 1, "that fall outside the range", "that fall within the range")
E("q15", "A", "QUAL", 1, "is required for", "may be required for")
E("q15", "B", "QUAL", 1, "is required when", "may be required when")
# q16
ADD("q16", "Communication in English is always permitted as an alternative")
E("q16", "A", "NEG", 1, "is the operating language(s)", "is not the operating language(s)")
E("q16", "B", "NEG", 1, "must use", "must not use")
E("q16", "B", "QUAL", 1, "must use", "may use")
# n01
ADD("n01", "The notification must also be sent to the Agency")
E("n01", "A", "NEG", 2, "A shorter period is allowed if", "A shorter period is not allowed even if")
E(
    "n01",
    "B",
    "NEG",
    2,
    "A shorter notification period is permitted if",
    "A shorter notification period is not permitted even if",
)
E(
    "n01",
    "A",
    "QUAL",
    2,
    "agreed between the IM and the RUs who run or intend to run services on these lines at the time of establishing the agreement",
    "agreed by the IM",
)
E(
    "n01",
    "B",
    "QUAL",
    2,
    "agreed between the Infrastructure Manager and the railway undertakings that run or intend to run services on those lines",
    "agreed by the Infrastructure Manager",
)
# n02
ADD("n02", "It also applies to 1 000 mm metre-gauge networks")
E("n02", "A", "NUM", 2, "with 1 520 mm track gauges", "with 1 435 mm track gauges")
E("n02", "B", "NUM", 2, "with 1 520 mm track gauge", "with 1 435 mm track gauge")
E("n02", "A", "NEG", 1, "The CCS TSI applies to", "The CCS TSI does not apply to")
E("n02", "B", "NEG", 1, "The CCS TSI applies to", "The CCS TSI does not apply to")
E("n02", "A", "QUAL", 2, " that are connected to the network of third countries", "")
E("n02", "B", "QUAL", 2, " that are connected to the network of third countries", "")
# n03
ADD("n03", "Shorter notice is allowed for requirements that only concern automatic train operation")
E("n03", "A", "NUM", 1, "at least 5 years", "at least 20 years")
E("n03", "B", "NUM", 1, "at least 5 years", "at least 20 years")
E("n03", "A", "NEG", 1, "at least 5 years", "at most 5 years")
E("n03", "B", "NEG", 1, "at least 5 years", "at most 5 years")
E("n03", "A", "QUAL", 1, "must be provided", "should be provided")
E("n03", "B", "QUAL", 1, "must be notified", "should be notified")
# n04
ADD("n04", "It must then notify the Commission of this decision")
E("n04", "A", "NUM", 1, "in the next 20 years", "in the next 10 years", "out-of-context")
E("n04", "B", "NUM", 1, "in the next 20 years", "in the next 10 years", "out-of-context")
E("n04", "A", "NEG", 1, "if it does not foresee", "if it foresees")
E("n04", "B", "NEG", 1, "if it does not foresee", "if it foresees")
E("n04", "A", "QUAL", 1, "may leave out", "must leave out")
E("n04", "B", "QUAL", 1, "may omit", "must omit")
# n05
ADD("n05", "The table must be updated every year")
# n05 NUM: no alternative value in the cited passage, so the code out-of-context rule applies
E(
    "n05",
    "A",
    "NEG",
    1,
    "must provide complete information",
    "need not provide complete information",
)
E("n05", "B", "NEG", 1, "must cover", "need not cover")
E("n05", "A", "QUAL", 1, "must provide", "should provide")
E("n05", "B", "QUAL", 1, "must cover", "should cover")
# n06
ADD("n06", "On lines below 250 km/h the nominal height may be as low as 4 800 mm")
E(
    "n06",
    "A",
    "NUM",
    1,
    "maximum design contact wire height is 5 300 mm",
    "maximum design contact wire height is 5 000 mm",
)
E("n06", "B", "NUM", 1, "the maximum design height 5 300 mm", "the maximum design height 5 000 mm")
E(
    "n06",
    "A",
    "NEG",
    1,
    "the minimum design contact wire height is 5 080 mm",
    "the maximum design contact wire height is 5 080 mm",
)
E("n06", "B", "NEG", 1, "the minimum design height 5 080 mm", "the maximum design height 5 080 mm")
E(
    "n06",
    "A",
    "QUAL",
    1,
    "For lines with speeds of $v \\ge 250$ [km/h], the nominal",
    "For all lines, the nominal",
)
E(
    "n06",
    "B",
    "QUAL",
    1,
    "For lines with speeds v ≥ 250 km/h the nominal",
    "For all lines the nominal",
)
# n07
ADD("n07", "On curves with a radius below 1 000 m the limit is reduced by 50 mm")
E("n07", "A", "NUM", 1, "it is 550 mm", "it is 500 mm")
E("n07", "B", "NUM", 1, "550 mm for a 1 950 mm", "500 mm for a 1 950 mm")
E("n07", "A", "NEG", 1, "the maximum lateral deviation", "the minimum lateral deviation")
E("n07", "B", "NEG", 1, "The maximum lateral deviation", "The minimum lateral deviation")
E("n07", "A", "QUAL", 2, "shall be adjusted", "may be adjusted")
# n08
ADD("n08", "Above 320 km/h the mean contact force must be measured on every new line")
E("n08", "A", "NUM", 1, "up to 360 km/h", "up to 400 km/h", "out-of-context")
E("n08", "B", "NUM", 1, "up to 360 km/h", "up to 400 km/h", "out-of-context")
E("n08", "A", "NEG", 2, "For speeds above 360 km/h", "For speeds below 360 km/h")
E("n08", "B", "NEG", 2, "For speeds above 360 km/h", "For speeds below 360 km/h")
E("n08", "A", "QUAL", 2, "shall apply", "may apply")
E("n08", "B", "QUAL", 2, "shall apply", "may apply")
# n09
ADD("n09", "The neutral section must be located on level track")
E("n09", "A", "NUM", 1, "at least 402 m", "at least 420 m", "out-of-context")
E("n09", "B", "NUM", 1, "at least 402 m", "at least 420 m", "out-of-context")
E("n09", "A", "NEG", 1, "at least 402 m", "at most 402 m")
E("n09", "B", "NEG", 1, "at least 402 m", "at most 402 m")
E(
    "n09",
    "A",
    "QUAL",
    1,
    "where all the pantographs of the longest TSI compliant trains are within the neutral section, the",
    "the",
)
E("n09", "B", "QUAL", 1, " when all pantographs of the longest train are inside it", "")
# n10
ADD("n10", "Insulators may also enter it on lines with speeds below 160 km/h")
E(
    "n10",
    "A",
    "NEG",
    1,
    "except for the contact wire and steady arm",
    "including the contact wire and steady arm",
)
E(
    "n10",
    "B",
    "NEG",
    1,
    "Only the contact wire and the steady arm may enter",
    "The contact wire and the steady arm may not enter",
)
E("n10", "A", "QUAL", 1, "shall enter", "should enter")
E("n10", "B", "QUAL", 1, "may enter", "must enter")
# n11
ADD("n11", "Benches count as large obstacles regardless of their length")
E("n11", "A", "NUM", 1, "is 80 cm", "is 160 cm")
E("n11", "B", "NUM", 1, "is 80 cm", "is 160 cm")
E("n11", "A", "NEG", 1, "the minimum distance", "the maximum distance")
E("n11", "B", "NEG", 1, "the minimum distance", "the maximum distance")
E("n11", "A", "QUAL", 2, "with a length from 1 m to less than 10 m", "with a length of 1 m or more")
E("n11", "B", "QUAL", 1, "(length 1 m to < 10 m)", "(length 1 m or more)")
# n12
ADD("n12", "Each step must be lit by a light at floor level")
E("n12", "A", "NUM", 1, "minimum depth of 280 mm", "minimum depth of 300 mm", "out-of-context")
E("n12", "B", "NUM", 1, "minimum depth of 280 mm", "minimum depth of 300 mm", "out-of-context")
E("n12", "A", "NEG", 1, "a maximum height of 200 mm", "a minimum height of 200 mm")
E("n12", "B", "NEG", 1, "a maximum height of 200 mm", "a minimum height of 200 mm")
E("n12", "A", "QUAL", 1, "shall have", "should have")
E("n12", "B", "QUAL", 1, "shall have", "should have")
# n13
ADD("n13", "It must be fitted with a safety strap")
E("n13", "A", "NUM", 2, "80 kg", "100 kg", "out-of-context")
E("n13", "B", "NUM", 1, "80 kg", "100 kg", "out-of-context")
E("n13", "A", "NEG", 1, "a minimum of 500 mm wide", "a maximum of 500 mm wide")
E("n13", "B", "NEG", 1, "at least 500 mm wide", "at most 500 mm wide")
E("n13", "A", "QUAL", 2, "must be able", "should be able")
E("n13", "B", "QUAL", 1, "it must be able", "it should be able")
# n14
ADD("n14", "Handrails must be made of a non-conductive material")
E("n14", "A", "NUM", 2, "of 45 mm", "of 50 mm")
E("n14", "B", "NUM", 1, "of 45 mm", "of 50 mm")
E("n14", "A", "NEG", 2, "a minimum clear distance", "a maximum clear distance")
E("n14", "B", "NEG", 1, "a minimum clear distance", "a maximum clear distance")
E("n14", "A", "QUAL", 1, "must be round", "should be round")
E("n14", "B", "QUAL", 1, "shall be round", "should be round")
# n15
ADD("n15", "The measurement must be repeated with the cab windows open")
E("n15", "A", "NUM", 2, "78 dB", "75 dB", "out-of-context")
E("n15", "B", "NUM", 1, "78 dB", "75 dB", "out-of-context")
E(
    "n15",
    "A",
    "NEG",
    1,
    "The noise limit for the driver's cab",
    "The minimum noise level for the driver's cab",
)
E("n15", "B", "NEG", 1, "the limit is 95 dB", "the minimum level is 95 dB")
E("n15", "A", "QUAL", 2, "At maximum speed vmax if vmax < 250 km/h, the", "At maximum speed, the")
E("n15", "B", "QUAL", 1, "at maximum speed when vmax < 250 km/h the", "at maximum speed the")
# n16
ADD("n16", "The test must be carried out at night")
E("n16", "A", "NUM", 1, "up to 30 km/h", "up to 40 km/h")
E("n16", "B", "NUM", 1, "up to 30 km/h", "up to 40 km/h")
E("n16", "A", "QUAL", 1, "the train shall accelerate", "the train may accelerate")
E("n16", "B", "QUAL", 1, "The train must accelerate", "The train may accelerate")
# n18
ADD("n18", "The examination results must be kept for at least ten years")
E("n18", "A", "NUM", 1, "every 3 years for staff", "every year for staff")
E("n18", "B", "NUM", 1, "every 3 years if", "every year if")
E("n18", "A", "QUAL", 1, "must be performed", "should be performed")
E("n18", "B", "QUAL", 1, "must undergo", "should undergo")
# n19
ADD("n19", "Sand must not be applied in tunnels longer than 1 km")
E("n19", "A", "NUM", 1, "less than 20 km/h", "less than 25 km/h", "out-of-context")
E("n19", "B", "NUM", 1, "less than 20 km/h", "less than 25 km/h", "out-of-context")
E("n19", "A", "NEG", 1, "shall avoid using it", "shall use it")
E("n19", "B", "NEG", 1, "shall avoid using", "shall use")
E("n19", "A", "QUAL", 1, "during braking at speeds less than 20 km/h", "during braking")
E("n19", "B", "QUAL", 1, "during braking at speeds less than 20 km/h", "during braking")
# n20
ADD("n20", "This information must be updated every time the timetable changes")
E("n20", "A", "NEG", 1, "may provide", "may not provide")
E("n20", "B", "NEG", 1, "may provide", "may not provide")
E("n20", "A", "QUAL", 1, "may provide", "must provide")
E("n20", "B", "QUAL", 1, "may provide", "must provide")
# n21
ADD("n21", "The consultation must be completed within 60 days")
E("n21", "A", "QUAL", 1, "must start", "should start")
E("n21", "B", "QUAL", 1, "must begin", "should begin")
# n22
ADD("n22", "Lines in both categories must be fully equipped with ETCS")
E("n22", "A", "NUM", 2, "of the order of 200 km/h", "of the order of 250 km/h")
E("n22", "B", "NUM", 1, "of the order of 200 km/h", "of the order of 250 km/h")
E("n22", "A", "NEG", 1, "equal to or greater than", "equal to or less than")
E("n22", "B", "NEG", 1, "equal to or greater than", "equal to or less than")
E("n22", "A", "QUAL", 1, "generally equal", "equal")
E("n22", "B", "QUAL", 1, "generally equal", "equal")
# n23
ADD("n23", "The exercise must then be repeated every two years")
E("n23", "A", "NEG", 1, "Prior to the opening", "After the opening")
E("n23", "B", "NEG", 1, "Before opening", "After opening")
E("n23", "A", "QUAL", 1, "must take place", "should take place")
E("n23", "B", "QUAL", 1, "must be carried out", "should be carried out")
# n24
ADD("n24", "Each section must be no longer than 5 km")
E("n24", "A", "QUAL", 1, "either locally or remotely", "remotely")
E("n24", "B", "QUAL", 1, "either locally or remotely", "remotely")

with open(sys.argv[1], "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows), "rows")
