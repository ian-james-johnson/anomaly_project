Project Scenario

Hello,

I have some questions for you that I need to be answered before the board meeting Friday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?



Project Answers

Question 1
Which lesson appears to attract the most traffic consistently across cohorts (per program)?
Highest traffic lesson for each cohort
'PHP Full Srack Web Dev'  : javascript-i 
'Java Full Stack Web Dev' : javascript-i 
'Data Science'            : classification/overview 
'Front End Web Dev'       : introduction.html (I am assuming the others are not lessons but were accessed for technical reasons)


Question 2
Which lessons are least accessed? 
The lists of pages with the least amount of accessions are given in the section work
- Out of 710 pages, 141 of those pages were only accessed once by 'PHP Full Srack Web Dev'
- Out of 1913 pages, 420 of those pages were only accessed once by 'Java Full Stack Web Dev'
- Out of 683 pages, 104 of those pages were only accessed once by 'Data Science'
- For front end web dev, all were low. Content/html-css had two accesses and the other three pages only had one access.
- Many of the least commonly accessed pages covered basics like functions or lists. These topics are reinforced throught the course, and a google search would probably give better answers to specific questions than a broad introduction page. When students encounter a bug, they will probably google the error message instead of returning to the curriculum.


Question 3
What topics are grads continuing to reference after graduation and into their jobs (for each program)?
Alumni are continuing to reference the following topics after graduation:
- 'PHP Full Srack Web Dev' alumni are coming back to javascript-i
- 'Java Full Stack Web Dev' alumni are coming back to javascript-i
- 'Data Science' alumni are coming back to sql/mysql-overview
- 'Front End Web Dev' accessions all seem to be after graduation

Question 4
Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
Users who only accessed the curiculum once had an average enrollment period of less than one month.


Question 5
Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
- There are two anomalous ip addresses, which is defined as activity more than three standard deviations above the mean.
- The likely explanation for the two anomalous ip addresses is that they belong to shared computers being used by multiple students over multiple cohorts.
- I would recommend determining if these two machines belong to the school.



Acquire
- Date and time are separate columns
- Temporal columns are strings
- Program id but no program names
- Some columns do not appear useful (deleted_at is full of nulls, Unnamed: 0 seems to match the index)
- Some null values



repare
- Date and Time columins combined into datetime
- datetime, start_date, end_date converted into datetime type
- Dropped Unnamed: 0 and deleted_at columns
- Added column for program names matching program_id
- Add hour and weekday columns



Explore
- Many numeric columns have lots of big outliers.
- Traffic is heaviest during late afternoon and eary evening.
- Some lessons are frequently accessed, while others are rarely accessed.
- More ip addresses than users, showing that a single user can have multiple computers.
- Front end web dev has a very small amount of records compared to the other programs.



Answers to Questions are given above.



To recreate this work:
The github repository for this notebook is at:
https://github.com/ian-james-johnson/anomaly_detection_project

Clone the repository onto your device.
To access the SQL server you will need to provide your own env.py file with: host, user, and password
Open and run the notebook.
