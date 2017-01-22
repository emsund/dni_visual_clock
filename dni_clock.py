# 12/26/2015
# emasundin@gmail.com

'''
D'ni Unit	Surface Equivalent	Subunits 		| Calc. equiv
----------------------------------------------------------------|--------------
1 hahr 		~1 year			10 vai-lee-tee 		| 365.319444... days
1 vai-lee	~1 month		29 yahr-tee		| 36.5319444... days
1 yahr		30 hr 14 min		5 gahr-tah-vo-tee	| using this as base
1 gahr-tah-vo	6 hr 3 min		25 tah-vo-tee		| 6 hr 2.8 min (close)
1 tah-vo	14.5 min		25 gor-ahn-tee		| 14.512 min (close)
1 gor-ahn	36 sec			25 pro-rahn-tee		| 34.8288 sec (36???)
1 pro-rahn	1.5 sec			(none)			| 1.393... sec

Source: myst5.com, tabulated by me (first 3 cols). I believe it is a transcript of the page 
found in the Uru neighborhood classroom.

I have added another column (Calculated equivalent) showing the results obtained by dividing
the subunits. This is interesting to compare to the given equivalents.

By these equivalences, the D'ni year is suspiciously similar in length to the "surface" year:
1 hahr ~= 365.32 "surface days", vs. 1 year = 365.25 "surface days". I wonder if this was the
original standard conversion set? Any in-game explanation seems unlikely.

-----------------------------
Found my old screencap of the "DRC-approved" D'ni time information sheet from Uru.
It seems a bit different from what I've got above. ?:/

D'ni Unit	Surface Equivalent	Subunits 		| 
----------------------------------------------------------------|-
1 hahr 		~1 year			10 vai-lee-tee 		| 
1 vai-lee	~1 month		29 yahr-tee		| 
1 yahr		30 hr 14 min (1.26 d)	5 gahr-tah-vo-tee	| 
1 gahr-tah-vo	6 hr 3 min		5 pahr-tah-vo		| 
1 pahr-tah-vo	1 hr 13 min		5 tah-vo-tee		|	
1 tah-vo	14.5 min		25 gor-ahn-tee		| 
1 gor-ahn	36 sec			25 pro-rahn-tee		| 
1 pro-rahn	1.5 sec			(none)			| 

There is a note indicating that D'ni clocks typically have 25 pahrtahvotee on
them (= 1 day).

Plan to put on clockface:
1 hand indicating pahrtahvotee (25 discrete positions; whole face = 1 D'ni day).
No hand needed for gahr-tah-vo-tee: current gahr-tah-vo is indicated by the 
colored region the pahrtahvo hand is in. (This seems sort of like 
our fuzzy evening/afternoon/morning "cultural" divisions of the day, but with
more precision). At a guess, perhaps they are somewhat like:
Pahrtahvo 1-5: "early morning"
Pahrtahvo 6-10: "morning day"
Pahrtahvo 11-15: "mid-day and afternoon"
Pahrtahvo 16-20: "evening"
Pahrtahvo 21-25: "late night"

I'll bet you they had special names (in-universe; if RAWA never invented any, he should.)
The D'ni day-cycle was based on the algae, IIRC. I always assumed these divs were, too.

On Aitrus's watch drawing on the BoT map, there are dragee-like dots in the middle of
every gahrtahvo (or what I assume to be). It seems odd to have these centered: with an
odd-numbered division, the middle is not the beginning of a particular integer. 
However, when considered in terms of the algae, another possibility appears:
if (pure speculation) the algae go through five distinct color/luminosity changes
(3 bright, 2 dim), it's unlikely, as a huge number of bioluminescent living critters, 
that they switch on and off instantly like an array of lightbulbs. They would probably
transition slowly from one state to another. Therefore, perhaps these dots on the
watch demark the peak intensity of each algal state.
  

'''

# The "yahr" is the largest time unit given with a reasonably precise conversion 
# (the "year" and "month" equivalents seem to be more "cultural", and are wildly approximate)
# Therefore, the "yahr" should give the most accurate conversion value for the smallest unit,
# the pro-rahn (better than the 1.5 given):
# 1 yahr = 30 hr 14 min
#earth_seconds_in_a_yahr = (30*60+14)*60
#print(earth_seconds_in_a_yahr)

import sys
import time
import math

def dni_timer():
	''' Count up from zero in prorahntee (D'ni seconds). Prints to standard output. 
	Updated with RAWA-confirmed conversion ("D'ni timekeeping conversion algorithms", MYSTlore)'''

	prorahntee = 0
	sys.stdout.write(str(prorahntee)+"\r")
	while 1:
		#time.sleep(1.392887)
		time.sleep(1.392857388844137931)
		prorahntee += 1
		sys.stdout.write(str(prorahntee)+"\r")
		#sys.stdout.write(time.asctime()+"\r")

def dni_time_since_epoch(give_float=False):
	''' Returns a list with the time in D'ni units since the Epoch.
	Format is [hahr, vailee, yahr, gahrtahvo, tahvo, gorahn, prorahn].
	Updated with RAWA-confirmed conversion ("D'ni timekeeping conversion algorithms", MYSTlore)

	This function does not give "true" D'ni time, as the D'ni time system does
	not coincide with the beginning of the Unix Epoch. For conversion to true 
	D'ni time, use the function dni_time().'''

	sec_since_epoch = time.time()
	sec_in_hahr = 365.25*24*60*60 #1 hahr = 1 year = 365.25 days
	#sec_in_hahr = 31556925.216  # Exactly
	sec_in_vailee = sec_in_hahr/10
	sec_in_yahr = sec_in_vailee/29
	sec_in_gahrtahvo = sec_in_yahr/5
	sec_in_tahvo = sec_in_gahrtahvo/25
	sec_in_gorahn = sec_in_tahvo/25
	sec_in_prorahn = sec_in_gorahn/25

	times = []
	conversions = [sec_in_hahr, sec_in_vailee, sec_in_yahr, 
		sec_in_gahrtahvo, sec_in_tahvo, sec_in_gorahn, sec_in_prorahn] 

	t = sec_since_epoch

	for n in range(7):
		if give_float:
			times.append(t/conversions[n])
			t -= math.trunc(times[n])*conversions[n]
		else:
			times.append(t//conversions[n])
			t -= times[n]*conversions[n]

	#print(times)
	return times

def dni_time(give_float=False):
	''' Returns a list with the current D'ni time.

	Time is calculated from convergence point given by RAWA ("D'ni 
	timekeeping conversion algorithms", MYSTlore): beginning of D'ni hahr 
	9647 = create timestamp of original HyperCard stack for Myst
	(April 21st, 1991, 16:54:00 UTC, or 672249240 Unix time)

	Format is [hahr, vailee, yahr, gahrtahvo, pahrtahvo, tahvo, gorahn, prorahn].
'''
	sec_since_epoch = time.time()
	sec_since_hahr_9647 = sec_since_epoch - 672249240 

	sec_in_hahr = 31556925.216  # Exactly
	sec_in_vailee = sec_in_hahr/10
	sec_in_yahr = sec_in_vailee/29
	sec_in_gahrtahvo = sec_in_yahr/5
	sec_in_pahrtahvo = sec_in_gahrtahvo/5
	sec_in_tahvo = sec_in_pahrtahvo/5
	sec_in_gorahn = sec_in_tahvo/25
	sec_in_prorahn = sec_in_gorahn/25

	times = []
	conversions = [sec_in_hahr, sec_in_vailee, sec_in_yahr, sec_in_gahrtahvo, 
		sec_in_pahrtahvo, sec_in_tahvo, sec_in_gorahn, sec_in_prorahn] 

	t = sec_since_hahr_9647

	for n in range(8):
		if give_float:
			times.append(t/conversions[n])
			t -= math.trunc(times[n])*conversions[n]
		else:
			times.append(math.trunc(t/conversions[n]))
			t -= times[n]*conversions[n]

	# Tack on preceeding hahr
	times[0] += 9647
	#print(times)
	return times

def print_dni_time():
	''' Uses dni_time_since_epoch function output to print pretty, labeled output. '''
	labels = ['hahrtee', 'vaileetee', 'yahrtee', 'gahrtahvotee', 'tahvotee', 'gorahntee', 'prorahntee']
	times = dni_time_since_epoch()
	print("Time since the Epoch:")
	for n in range(7):	
		print(labels[n]+":\t"+str(times[n]))

def ticking_dni_clock():
	'''A digital-style clock that refreshes in place to the console to show the current time,
	in D'ni units, since the Epoch'''
	while 1:
		t = dni_time_since_epoch()
		sys.stdout.write(str(t[0])+":"+str(t[1])+":"+str(t[2])+":"+str(t[3])+":"+str(t[4])+":"+str(t[5])+":"+str(t[6])+"       \r")
		time.sleep(1.392887)


if __name__ == '__main__':
	#dni_timer()
	#print_dni_time()
	#ticking_dni_clock()
	dni_time_since_epoch(give_float=True)
	print(dni_time_since_epoch())
	print(dni_time())

