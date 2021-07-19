
#these are the answers to our blog no 4 Conversions in python. we strongly recommend you to first try yourself and then consult to these answers. Practice is the key to every skill!
#Happy learning

#easy conversions
#length conversions

#convert 59.5 inches to cm
def inch_cm(inch,cm):
	print(f'59.5 inches is equal to {inch*cm} cm') # 1 inch = 2.54 cm
inch_cm(59.5,2.54)

print('\n')

#convert 59.5 cm to inches
cm = 59.5
inches = cm * 0.3937
print(f'59.5 cm = to {inches} inches')

print('\n')

#convert 5.9 miles to km
miles = 5.9
km = miles * 1.609 # 1 mile = 1.609 km
print(f'5.9 miles is equal to {km} km')

print('\n')

#convert 5.9 km to miles
km = 5.9
miles = km / 1.609 # as 1 mile = 1.609 km
print(f'5.9 km is equal to {miles} miles')

print('\n')

#convert 45 meters to feet
meters = 45
feet = 3.28084 * meters # 1 meters = 3.28084 feet
print(f'45 meters is equal to {feet} feet')

print('\n')

#convert 45 feet to meters 
feet = 45
meters = feet / 3.28084 # as 1 meter = 3.28084 feet
print(f'45 feet is equal to {meters} meters')

print('\n')

#convert 1277 milimeters to inches
mm = 1277
inches = mm / 25.4 # 1 inch = 25.4mm
print(f'1277 millimeters is equal to {inches} inches')

print('\n')

#convert 127 inches to milimeters
inches = 127
mm = inches * 25.4 # 1 inch = 25.4 mm
print(f'127 inches is equal to {mm} mm')

print('\n')

#convert 13 yards to meters 
yards = 13
meters = yards / 1.094 # as 1 meter = 1.094 yards
print(f'13 yards is equal to {meters} meters')

print('\n')

#convert 23 meters to yards
meters = 23
yards = meters * 1.094 # as 1 meter = 1.094 yards
print(f'23 meters is equal to {yards} yards')

print('\n')

#temperature conversions
#convert 44 degrees celsius to fehrenheit
celsius = 44
fehrenheit = (celsius * 9/5) + 32
print(f'44 degrees celsius is equal to {fehrenheit} degrees in fehrenheit scale')

print('\n')

# convert 250 degrees kelvin to celsius
kelvin = 250
celsius = kelvin - 273.15
print(f'250 degrees kelvin is equals to {celsius} degrees celsius')

print('\n')

#convert 130 fehrenheit to celsius
fehrenheit = 130
celsius = (fehrenheit - 32) * 5/9
print(f'130 degrees fehrenheit is equals to {celsius} degrees in celsius')

print('\n')

#convert 120 fehrenheit to kelvin
fehrenheit = 120
kelvin = (fehrenheit - 32) * 5/9 - 273.15
print(f'120 degrees fehrenheit is equals to {kelvin} degrees in kelvin scale')

print('\n')

#convert 30 celsius to kelvin
celsius = 30
kelvin = celsius + 273.15
print(f'30 degrees celsius is equals to {kelvin} degrees in kelvin')

print('\n')

#weight conversions
#convert 260 pounds to kilograms
pounds = 260 
kilograms = pounds / 2.205 # 1kg = 2.205lb
print(f'{pounds} pounds is equals to {kilograms} kilograms')

print('\n')

#convert 121 kilograms to pounds 
kg = 121
pounds = lb = 2.205 * kg # 1 kg = 2.205 lb
print(f'{kg} kg is equals to {lb} pounds')

print('\n')

#convert 45 ounces to kg and lbs
ounces = 45
kg = ounces / 35.274 # 1kg = 35.274 ounces
lb = ounces / 16 # 1 lb = 16 ounces
print(f'{ounces} ounces is equals to {kg} kg and {lb} pounds)')

print('\n')

#convert 217 pounds to grams
pounds = 217
grams = pounds * 454 # 1 pound = 454 grams
print(f'{pounds} pounds is equals to {grams} grams')

print('\n')

#convert 27 ounces to carats
ounces = 27
carats = ounces * 142 # 1 ounce = 142 carat
print(f'{ounces} ounces is equals to {carats} carats')

print('\n')

# convert 7 kg to carats
kg = 7
carats = 5000 * kg # 1kg = 5000 carats
print(f'{kg} kg is equals to {carats} carats')

print('\n')

#convert 2701 carats to grams
carats = 2701
grams = carats / 5 # 1 gram = 5 carats
print(f'{carats} is equals to {grams} grams')

print('\n')

#area conversions
#convert 33 square meters to square feet
sq_m = 33
sq_ft = sq_m * 10.764 # 1 sq_m = 10.764 sq_ft
print(f'{sq_m} square meters is equals to {sq_ft} square feet')

print('\n')

#convert 112.5 square feet to square meters
sq_ft = 112.5
sq_m = sq_ft / 10.764 # 1 sq_m = 10.764 sq_ft
print(f'{sq_ft} square feet is equals to {sq_m} square meters')

print('\n')

#convert 3 sq_km to sq_ft
sq_km = 3
sq_ft = sq_km * 1076e+7 # 1 sq_km + 10763910.4 sq_ft & 1076e+7 is the scientific notation used for it.
print(f'{sq_km} square kilometers is equals to {sq_ft} square feet')

print('\n')

#volume conversions
#convert 73 gallons to microlitres
gallons = 73
mic_litres = 3.785e+6 * gallons #1 microlitres = 3785411.78 gallons and 3.785e+6 is the scientific notation used for it.
print(f'{gallons} gallons is equals to {mic_litres} micro litres')

print('\n')

#convert 110.4 micro yards to Uk pints
mic_yrd = 110.4
uk_pin = mic_yrd / 6.458299660028 # 1 uk pint = 1/6.458299660028 micro yards
print(f'{mic_yrd} micro yards is equals to {uk_pin} UK pints')

print('\n')

#convert 1281 mili litres to mili yards
mil_lit = 1281
mil_yrd = mil_lit * 1.307950613786E-6 #1 mili yard = 1.307E-6 mili litres
print(f'{mil_lit} milli litres is equals to {mil_yrd} milli yards')

print('\n')

#speed conversions
#convert 64 kilometers per hour (kph) to miles per hour (mph)
kph = 64
mph = kph / 1.609344 #as 1 mile = 1.609344 kilometers
print(f'{kph} kilometers per hour is equal to speed {mph} in miles per hour')

print('\n')

#13.4 meter per second (mps) to kilometer per hours (kph)
mps = 13.4
kph = mps * 3.6 #as 1 mps = 3.6 kph
print(f'{mps} meter per second is equals to {kph} kilometers per hour')

print('\n')

#convert 98 inches per second (ips) to kilometer per hour (kph)
ips = 98
kph = ips * 10.936 # 1 kph = 10.936 ips
print(f'{ips} inches per second is equals to {kph} kilometers per hour')

print('\n')

#time conversions
#convert 4 years 11 months 27 days 19 hours to seconds
min = 60 # 1 min = 60 sec
hrs = 60 * 60 # 1 hour = 60 min
hrs_19 = hrs * 19 #converting 19 hrs to seconds
day = 24 * hrs # converting 1 day to seconds
day_27 = day * 27 # converting 27 days to seconds
mon = 30 * day # converting 1 month to seconds
mon_11 = mon * 11 # converting 11 months to seconds
year = 12 * mon #converting 1 year to seconds
year_4 = year * 4 #converting 4 years to seconds
con_to_sec = hrs_19 + day_27 + mon_11 + year_4 #adding all the seconds
print(f'4 years, 11 months, 27 days, 19 hours is equals to {con_to_sec} in seconds') #displaying the result on the console

print('\n')

#pressure conversion
#convert 12 bars to pascal
bars = 12
pascal = 100000 * bars # 1 bar = 100000 pascals
print(f'{bars} bars pressure is equals to {pascal} pascals')

print('\n')

#convert 23 pascal to bars 
pascal = 23
bars = pascal / 100000 #1 bar = 100000 pascals
print(f'{pascal} pascals is equals to {bars} bars')

print('\n')

#convert 33 bars to inches per square feet (ipsf)
bars = 33
bar_1 = 144 * 2088.545633 # 1 bar = 2088 psf approx
ipsf = bars * bar_1
print(f'{bars} bars is equals to {ipsf} inches per square feet')

print('\n')

#convert 88 pascals to newton per square meter (nsm)
pascal = 88
nsm = pascal # 1 pascal = 1 newton per square meter
print(f'{pascal} pascal is equal to {nsm} newton per square meter')

print('\n')

#intermediate conversions
#angle conversion
#convert 187 degrees to radians
deg = 187
pi = 3.1415
rad = deg * pi/180
print(f'{deg} degrees is equals to {rad} radians')

print('\n')

#convert 2 radians to degrees, minutes, seconds
rad = 2
deg = rad * 180/pi # getting the value of pi from line no 281
print(f'{rad} radians is equals to {deg} degrees')

print('\n')

#temperature conversions
#convert 33 celsius to rankine
cel = 33
ran = cel * (9/5) + 491.67 #as 0 degrees celsius = 491.67 rankine
print(f'{cel} celsius is equals to {ran} degrees on ranline scale')

print('\n')

#convert 33 celsius to delisle
cel = 33
deli = (100 - cel) * 3/2 #this is the formula for converting
print(f'{cel} celsius is equals to {deli} degrees in delisle sclae')

print('\n')

#convert 33 celsius newton
cel = 33
newtn = (cel) * 33/100 # 1 celsius = 0.33 deg newton
print(f'{cel} celsius is equals to {newtn} newtons')

print('\n')

#convert 33 celsius réaumur
cel = 33
reamr = cel/1.25 # this is the formula for converting
print(f'{cel} celsius is equals to {reamr} réaumur')

print('\n')

#convert 33 celsius to rømer
cel = 33
rom = cel * (21/40) + 7.5
print(f'{cel} celsius is equals to {rom} rømer')

print('\n')

#weight conversions
#convert 140 pounds to stones
lbs = 140
ston = lbs / 14 # 1 stone = 14 lbs
print(f'{lbs} pounds is equals to {ston} stones')

print('\n')

#convert 200 kilograms to long underweights
#i didn't found the formula for this comversion, i will update this blog, once i found the correct formula for this conversion

#convert 25 stones to long under weights
#i didn't found the formula for this comversion, i will update this blog, once i found the correct formula for this conversion

#convert 27.4 ounces to troy ounces
ounc = 27.4
troy_ounc = ounc / 1.097 #1 ounce = 0.911 troy ounce
print(f'{ounc} ounces is equals to {troy_ounc} troy ounces')

print('\n')

#convert 11372.1 tones to metric tones
tones = 11372.1
met_tones = tones * 1.1023113109246 # as this is the formula
print(f'{tones} tons is equals to {met_tones} metric tons')

print('\n')

#convert 97.4 kilograms to troy pounds
kgs = 97.4
troy_lbs = kgs * 2.68 # 1 kg = 2.68 troy pounds
print(f'{kgs} kilograms is equals to {troy_lbs} troy pounds')

print('\n')

#convert 112 troy pounds to troy ounces
troy_lbs = 112
troy_ounces = troy_lbs * 12 # 1 troy pound = 12 troy ounces
print(f'{troy_lbs} troy pounds is equals to {troy_ounces} troy ounces')

print('\n')

#convert 34 ounces to pennyweights
ounces = 34
penny_w = ounces * 18.224 #as 1 ounce = 18.224 pennhweights
print(f'{ounces} ounces is equals to {penny_w} pennyweights')

print('\n')

#area conversions
#convert 34 hectares to acres
hect = 34
acres = hect * 2.471 # 1 hect = 2.471 acres
print(f'{hect} hectares is equals to {acres} acres')

print('\n')

#convert 12 acres to square yards
acre = 12
sq_yards = acre * 4840 # 1 acre to 4840 square yards
print(f'{acre} acres is equals to {sq_yards} square yards')

print('\n')

#volume conversions
#convert 75.3 cubic meters to litres, cubic feet, kilolitre, microlitre and cubic yards
cub_met = 75.3
lit = cub_met * 1000 # 1 cubic meters = 1000 litres
cub_ft = 35.315 * cub_met # 1 cubic meter = 35.315 cubic feet
k_lit = cub_met #as these are equal
mic_lit = cub_met * 1000000000 # 1 cubic meter = 1e+9 micro litres
cub_yrd = cub_met * 1.308 # 1 cubic meter = 1.308 cubic yards
print(f' {cub_met} cubic meters is equals to {lit} litres, {cub_ft} cubic feet, {k_lit} kilo litres, {mic_lit} micro litres, and {cub_yrd} cubic yards')

print('\n')

#speed conversions
#convert 1223 milimeters per minute to kilometers per hour, miles per second, nanometer per hour, meters per minute, inches per minute and yards per hour
mmpm = 1223
kmph = mmpm * 16666.667 # 1 millimeter per minute = 16666.667 kilometers per hour
mps = mmpm / 9.656e+7 #this is the formula for converting
nmph = mmpm / 6e+7  #this is the formula for converting
mpm = mmpm * 1000 # 1 meter per minute = 1000 millimeters per minute
ipm = mmpm/25.4 #this is the formula for converting
yph = mmpm / 15.24 #this is the formula for converting

print(f'{mmpm} millimeters per minute is equals to {kmph} kilometers per hour, {mps} miles per second, {nmph} nanometer per hour, {mpm} meters per minute, {ipm} inches per minute and {yph} yards per hour')

print('\n')

#pressure conversions
#convert 12 newton per meter square to inches per square foot
#we failed to find the formula for this conversion

#convert 87 inches per square meter to newton per square feet
#we failed to find the formula for this conversion

#difficult conversions
#angle conversions
#convert 274 degrees, 12 minutes, 36 seconds to centrad, gradians and milliradians
pi = 3.1415
deg = 274
min = 12
sec = 36
cent = deg / 0.57296 #this is the formula
grad = deg * 1.111111 #1 deg = 1.111111 gradians
milli_rad = deg * ((1000*pi)/180)
print(f'{deg} degrees is equals to {cent} centrad, {grad} gradians and {milli_rad} milli radians but remember we could not convert the minutes and seconds due to not knowing of the conversion formula')
# remember that we couldn't convert the minutes and seconds, becuase we didn't know the formula

print('\n')

#pressure conversions
#convert 66 bars to torr
bars = 66
torr = bars * 750.062 # because 1 bar = 750.062 torr
print(f'{bars} bars is equals to {torr} torr')

print('\n')

#convert 12 torr to newton per square meter
torr = 12
npsm = 133.322 * torr #because 1 torr = 133.322 newton per square meter
print(f'{torr} torr is equals to {npsm} newton per square meter')

print('\n')

#convert 13 pascal to pounds per square foot
pascal = 13
lb_p_sqft = 0.02029 # 1 pascal = 0.02029 pounds per square foot
print(f'{pascal} pascal is equals to {lb_p_sqft} pounds oer square feet')

print('\n')

#temperature conversions
#recently 54.2 degrees celsius have been recorded in the state of california in USA. we don't how much it is in other scales and we have to use it in different scientific experiments. convert the above recorded temoerarure to kelvin, fehrenheit, delisle, rankine, newton, réaumur and rømer.
celsius = 54.2
kelvin = celsius + 273.15 #as 0 celsius = 273.15 kelvin
fehrenheit = (celsius * 9/5) + 32 #as 0 celsius = 32 fehrenheit
delisle = (100 - celsius) * 3/2 #this is the formula for conversion
rankine = (celsius * 9/7) + 491.67 # 0 celsius = 491.67 rankine
newton = celsius * 33/100 #this is the formula for conversion
reaumur = celsius / 1.25 #this is the formula for conversion
romer = celsius * 21/40 + 7.5 #this is the formula for conversion
print(f'{celsius} degrees celsius is equals to {kelvin} degrees kelvin, {fehrenheit} degrees fehrenheit, {delisle} degrees delisle, {rankine} degrees rankine, {newton} degrees newton, {reaumur} degrees réaumur and {romer} degrees rømer')

print('\n')

#weight conversions
#convert 12 kilogram to hundred weights
kg = 12
hun_wght = kg * 0.019684130552221 #this is the formula for conversion
print(f'{kg} kg is equals to {hun_wght} hundred weights')

print('\n')

#convert 66 tons to short tons and long tons
tons = 66
short_tons = tons * 1.10231 # as 1.10231 tons = 1 short ton
long_tons = tons / 1.12 #this is the formula for conversion
print(f'{tons} tons is equals to {short_tons} short tons and {long_tons} long tons')

print('\n')

#convert 22 pounds to milligrams and micrograms
lbs = 22
milli_gram = lbs * 453592.37 # 1 pound = 453592 milligrams approx
micro_gram = lbs * 4.536e+8 # 1 pound = 453592370 micrograms
print(f'{lbs} pounds is equals to {milli_gram} milli grams and {micro_gram} micro grams')

print('\n')

#area conversions
#convert 1745.3 square millimteres to square microns
sq_mm = 1745.3
sq_microns = sq_mm * 1e+6 # 1 square millimeters = 1000000 sq_microns
print(f'{sq_mm} square millimeters is equals to {sq_microns} square microns')

print('\n')

#convert 334.2 square inches to square microns and square decimeters
sq_inch = 334.2
sq_microns = sq_inch * 6.452e+8 # 1 square inches = 645160000 square microns
sq_deci_m = sq_inch / 15.5 #this is the formula for conversion
print(f'{sq_inch} square inches os equals to {sq_microns} square microns and {sq_deci_m} square deci meters')

print('\n')

#volume conversions
#convert 45.7 litres to UK gallons, US pints, UK quarts, UK tabblespoons, US teaspoons, gills and ounces
litres = 45.7
uk_gal = litres / 4.546 # this is the formula for conversion
us_pint = litres * 2.113 # 1 litre = 2.113 us pints
uk_qrt = litres * 0.88 # 1 litre = 0.88 uk quartz
uk_t_spoons = litres * 56.312 # 1 litre = 56.312 uk table spoons
us_tea_sp = litres * 202.884 # 1 litre = 202.884 us tea spoons
gills = litres * 8.454 #1 litre = 8.454 gills
ounces = litres * 33.814 # 1 litre = 33.814 ounces
print(f'{litres} litres is equal to {uk_gal} UK gallons, {us_pint} US pints, {uk_qrt} UK quartz, {uk_t_spoons} UK table spoons, {us_tea_sp} US tea spoons, {gills} gills and {ounces} ounces')

print('\n')

#speed conversions
#convert 35.70 knots to mach, lightspeed, micron per second, feet per day and miles per year
knots = 350.7
mach = knots / 667 # 1 knit = 0.0015 mach
lightspeed = knots / 5.827e+8 #this is the formula for conversion
micron_p_sec = knots / 514444 # this is the formula for conversion
feet_p_day = knots * 145827 #this is the formula for conversion
miles_p_year = knots * 10081
print(f'{knots} knots is equals to {mach} mach, {lightspeed} lightspeed, {micron_p_sec} micron per second, {feet_p_day} feet per day and {miles_p_year} miles per year')

print('\n')
