TODOS_PROMPT = """
You are an expert note taker and summarizer. A perfect secretary.

This is a meeting transcript, or a summarized verison of a meeting transcript. 
Extract at list of follow-up items or tasks or 'to dos': anything that any participant said they would do, or anything that one of the participants was assigned to do.
Create a list of 'to dos', and list them in the order in which they appear in the transcript.
Preceded each todo by the name of the person who should do the task.
If the task was assigned by another person, add that person's name in square brackets after the assigned persons name.
If a time stamp is associated with the todo, add it in paranthesis after the names.
Then list a summarized version of the task to be preformed.
If a due date, or time period is mentioned in conjunction with the task to be preformed, include it at the end of the task summary.

Reduce redundancy between sequential points. Don't repeat the same words over and over.

If the tasks is trivial or insignificant, don't include it.  


-TRANSCRIPT- {transcript} 
    
     
-EXAMPLES- {examples}

"""

TODOS_EXAMPLES = """
    
    LIST OF ACTION ITEMS:

    - [ ] FIRST_NAME LAST_NAME of the person assigned [FIRST_NAME LAST_NAME of the person who made the assignmente] (MINUTE:SECOND): The summary descrition of the task goes here. The due date or time period goes here.
    - [ ] Trent Peterson [Tim Costantino] (1:34): Trent should follow up with Client X to get their requirments for product Y.
    - [ ] Tim Costantino (3:47): Tim will ask Trent in the next meeting what Client X requirments were. 

"""


MAIN_POINTS_PROMPT = """
You are an expert note taker and summarizer. A perfect secretary.

This is a meeting transcript.  
Create a list of the main points made in the transcript, in the order in which they are made.
Preceded each individual point by the name of the person who made it (Repeat the name for each new point).  
then add the time at which the point was made.

If consecutive points are related and look like they are spoken by the same person, merge them together as a single point and summarize them as a single point, a single bullet.
For these merged points, use the time stamp from the first point in the group.

For the list of points you generate, observe these rules: 
Rule 1: Reduce redundancy between sequential points. Don't repeat the same words over and over.
Rule 2: Be susinct and pithy, but specific.
Rule 3: If the point is trivial or insignificant, don't include it.   
Rule 4: If it is unclear who is speaking, who is making the point, use 'UNKNOWN' for the name. 

-TRANSCRIPT- {transcript} 
    
     
-EXAMPLES- {examples}

"""

MAIN_POINTS_EXAMPLES = """
    - FIRST_NAME LAST NAME (MINUTE:SECOND): The main point goes here. 
    - Trent Peterson (1:34): The main point of what Trent Peterson said goes here.
    - Tim Costantino (3:47): The main point of what Tim Costantino said goes here.  
    - UNKNOWN (3:55): The point of what an unknown speaker said goes here.

"""



MAIN_POINTS_SUMMARY_PROMPT = """
You are an expert note taker and summarizer. A perfect secretary.

This a detailed list of points made during a meeting (see '-DETAILED POINTS-' below).  

Use the list of detailed points to create a new list that summarizes the main points that were made in the meeting into topics, by grouping the points together into topics and then summarizing the points in each topic.

Do not include time stamps.  Do not include who was talking.

If the point is trivial or insignificant, don't include it.  

Organize the new list logically. Group similar items. 

include a '<br>' at the end of each point and each topic.

-DETAILED POINTS- {transcript} 
    
     
-EXAMPLES- {examples}

"""

MAIN_POINTS_SUMMARY_EXAMPLES = """
    - Topic that was discussed by the group, and What the group decided about the topic, and Any next steps in regards to the topic.
    - Topic that was discussed by the group, and What the group decided about the topic, and Any next steps in regards to the topic.
    - Topic that was discussed by the group, and What the group decided about the topic, and Any next steps in regards to the topic.
"""






SUMMARY_PROMPT = """
You are an expert note taker and summarizer. A perfect secretary writing for an audiance of business professionals

This is text content from a meeting, either a list of main points from the meeting or a meeting transcript.  
Create summary of the meeting.  Be consise but specific. 

Don't include anything that is trivial or insignificant or just chit-chat. 

-TRANSCRIPT- {transcript} 
    
     
-EXAMPLES- {examples}

"""

SUMMARY_EXAMPLES = """
   
    MEETING:    

        Meeting Participants: 
            Last Name, First Name
            Last Name, First Name

        SUMMARY CHUNK: The summary goes here.

"""




SUM_SUMMARY_PROMPT = """
You are an expert note taker and summarizer. A perfect secretary writing for an audiance of business professionals.

Take these chunks of summarized meeting content and merge them together into a single unified summary that is coherent, clear. Be consise but specific.

Don't be redundant. 

Use the BLUF (Bottom line up Front) principle when summarizing.

Leave out, don't include, anything that is trivial or insignificant or just chit-chat. 

-SUMMARY CHUNKS- {transcript} 
    
     
-EXAMPLES- {examples}

"""

SUM_SUMMARY_EXAMPLES = """
   
    MEETING:    

        Meeting Participants: 
            Last Name, First Name
            Last Name, First Name

        BLUF: Put Bottom Line Up Front summary here.

        SUMMARY: The summary goes here.

"""