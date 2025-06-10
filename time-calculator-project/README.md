# Time Calculator project

## Description
In this project, we coded a time calculator that takes in a 12-hour time string and a duration in **HH:MM** format, then outputs the new time after adding the duration to the input time.
The most challenging part in this project was managing the conversion between 12-hour time and 24-hour time, as there were many unforeseen edge cases such as having to add an extra hour
after calculating the new hours and minutes, having to prepend a `0` for single-digit minutes, having to convert 0 hours in 24-hour time etc., but everything works now.

## Example Input
```
add_time('3:00 PM', '3:10')
add_time('11:30 AM', '2:32', 'Monday')
add_time('11:43 AM', '00:20')
add_time('10:10 PM', '3:30')
add_time('11:30 AM', '2:32', 'Monday')
```

## Output
![image](https://github.com/user-attachments/assets/ad25e567-dc87-4c18-a9d9-5e122ebc8363)
