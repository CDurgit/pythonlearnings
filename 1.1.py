usertime = int(input('Enter time in seconds: '))
minutes = usertime // 60
seconds = usertime % 60
hours = minutes // 60
minutes -= 60 * hours
days = hours // 24
hours -= 24 * days
weeks = days // 7
days -= 7 * weeks
months = weeks // 4
weeks -= 4 * months
years = months // 12
months -= 12 * years
print(years, 'years', months, 'months', weeks, 'weeks', days, 'days', hours, 'hours', minutes, 'minutes', seconds,
      'seconds')